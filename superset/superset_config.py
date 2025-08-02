# Superset Configuration for Civ VI Analytics
# This configuration sets up Superset to work with our PostgreSQL database
# ENHANCED with custom Civ VI refresh button functionality

import os

# Database Configuration - using environment variables
DATABASE_USER = os.environ.get('DATABASE_USER', 'civ6_user')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', 'civ6_password')
DATABASE_HOST = os.environ.get('DATABASE_HOST', 'postgres')
DATABASE_DB = os.environ.get('DATABASE_DB', 'civ6_analytics')

SQLALCHEMY_DATABASE_URI = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:5432/{DATABASE_DB}'

# Security Configuration
SECRET_KEY = os.environ.get('SUPERSET_SECRET_KEY', 'this_is_a_very_long_jwt_secret_key_for_civ6_local_development_definitely_more_than_32_bytes_long_12345')

# Disable JWT for local development
WTF_CSRF_ENABLED = False
JWT_SECRET_KEY = SECRET_KEY

# 🏆 CIV VI CUSTOM EXTENSIONS
# Enable custom functionality for Civ VI dashboard

# Feature flags for enhanced dashboard functionality
FEATURE_FLAGS = {
    'DASHBOARD_NATIVE_FILTERS': True,
    'DASHBOARD_CROSS_FILTERS': True,
    'ENABLE_TEMPLATE_PROCESSING': True,
    'EMBEDDED_SUPERSET': False,
    'DRILL_TO_DETAIL': True,
    'DRILL_BY': True,
}

# Custom routes registration
def register_custom_views(app):
    """Register custom views and endpoints for Civ VI functionality"""
    
    # Import and register our custom refresh plugin
    try:
        import sys
        import subprocess
        from flask import Blueprint, jsonify, request, Response
        from superset.extensions import db
        import logging
        
        # Add the app directory to Python path for imports
        sys.path.append('/app')
        
        logger = logging.getLogger(__name__)
        
        # Create blueprint for Civ VI endpoints
        civ6_blueprint = Blueprint('civ6_refresh', __name__, url_prefix='/civ6')
        
        @civ6_blueprint.route('/refresh-data', methods=['POST'])
        def refresh_civ6_data():
            """Endpoint to trigger Civ VI data refresh using Docker"""
            try:
                # Get the project root directory
                project_root = '/app/project'  # Docker mount path
                
                # Run the Docker command to refresh data
                result = subprocess.run([
                    'docker-compose', '--profile', 'data-import', 'up', 'data-loader'
                ], 
                cwd=project_root,
                capture_output=True, 
                text=True, 
                timeout=300
                )
                
                if result.returncode == 0:
                    # Query latest turn data from our Civ VI database
                    from sqlalchemy import create_engine, text
                    import psycopg2
                    
                    # Connect to our Civ VI PostgreSQL database
                    engine = create_engine('postgresql://civ6_user:civ6_password@postgres:5432/civ6_analysis')
                    
                    query = text("""
                        SELECT 
                            MAX(game_turn) as latest_turn,
                            COUNT(DISTINCT civilization) as civilizations,
                            COUNT(*) as total_records
                        FROM civ_game_data
                    """)
                    
                    with engine.connect() as conn:
                        result_data = conn.execute(query).fetchone()
                        
                    return jsonify({
                        'success': True,
                        'message': 'Civ VI data refresh completed successfully!',
                        'data': {
                            'latest_turn': result_data[0] if result_data else 0,
                            'civilizations': result_data[1] if result_data else 0,
                            'total_records': result_data[2] if result_data else 0
                        }
                    })
                else:
                    return jsonify({
                        'success': False,
                        'error': f'Data refresh failed: {result.stderr}'
                    }), 500
                    
            except Exception as e:
                logger.error(f"Error refreshing Civ VI data: {str(e)}")
                return jsonify({
                    'success': False,
                    'error': f'Refresh failed: {str(e)}'
                }), 500
        
        @civ6_blueprint.route('/status', methods=['GET'])
        def get_civ6_status():
            """Get current Civ VI game status"""
            try:
                from sqlalchemy import create_engine, text
                import psycopg2
                
                # Connect to our Civ VI PostgreSQL database
                engine = create_engine('postgresql://civ6_user:civ6_password@postgres:5432/civ6_analysis')
                
                status_query = text("""
                    SELECT 
                        MAX(game_turn) as latest_turn,
                        COUNT(DISTINCT civilization) as civilizations,
                        COUNT(*) as total_records
                    FROM civ_game_data
                """)
                
                rankings_query = text("""
                    SELECT 
                        civilization,
                        total_score,
                        yields_science,
                        yields_culture
                    FROM civ_game_data 
                    WHERE game_turn = (SELECT MAX(game_turn) FROM civ_game_data)
                    ORDER BY total_score DESC
                """)
                
                with engine.connect() as conn:
                    status_result = conn.execute(status_query).fetchone()
                    rankings_result = conn.execute(rankings_query).fetchall()
                    
                return jsonify({
                    'success': True,
                    'status': {
                        'latest_turn': status_result[0] if status_result else 0,
                        'civilizations': status_result[1] if status_result else 0,
                        'total_records': status_result[2] if status_result else 0
                    },
                    'rankings': [
                        {
                            'civilization': row[0].replace('CIVILIZATION_', '') if row[0] else 'Unknown',
                            'total_score': row[1],
                            'yields_science': row[2],
                            'yields_culture': row[3]
                        }
                        for row in rankings_result
                    ] if rankings_result else []
                })
                
            except Exception as e:
                logger.error(f"Error getting Civ VI status: {str(e)}")
                return jsonify({
                    'success': False,
                    'error': f'Status check failed: {str(e)}'
                }), 500
        
        # Register the blueprint
        app.register_blueprint(civ6_blueprint)
        
        # Serve custom JavaScript extension
        @app.route('/static/civ6_dashboard_extension.js')
        def serve_civ6_extension():
            """Serve the Civ VI dashboard extension JavaScript"""
            from flask import Response
            
            # JavaScript code for the dashboard extension
            js_code = '''
/**
 * Civ VI Data Refresh Button - Embedded in Superset Configuration
 */
(function() {
    'use strict';
    
    function createRefreshButton() {
        return `
            <div style="display: inline-flex; align-items: center; margin-left: 12px;">
                <button 
                    id="civ6-refresh-btn" 
                    style="
                        background: linear-gradient(135deg, #ff6b6b, #ee5a52);
                        border: none;
                        border-radius: 6px;
                        padding: 8px 16px;
                        color: white;
                        font-weight: 500;
                        font-size: 13px;
                        cursor: pointer;
                        transition: all 0.3s ease;
                        display: flex;
                        align-items: center;
                        gap: 6px;
                    "
                    title="Load new Civ VI turn data"
                >
                    <span style="font-size: 14px;">🏆</span>
                    <span>Load New Turns</span>
                </button>
                <div id="civ6-status" style="margin-left: 8px; font-size: 12px; color: #666;"></div>
            </div>
        `;
    }
    
    async function handleRefresh() {
        const button = document.getElementById('civ6-refresh-btn');
        if (!button) return;
        
        button.style.background = '#6c757d';
        button.querySelector('span:last-child').textContent = 'Loading...';
        button.disabled = true;
        
        try {
            const response = await fetch('/civ6/refresh-data', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' }
            });
            
            const data = await response.json();
            
            if (data.success) {
                alert(`✅ Success! Data refresh completed. Latest turn: ${data.data?.latest_turn || 'Unknown'}`);
                setTimeout(() => window.location.reload(), 1000);
            } else {
                alert(`❌ Error: ${data.error}`);
            }
        } catch (error) {
            alert(`❌ Network error: ${error.message}`);
        } finally {
            button.style.background = 'linear-gradient(135deg, #ff6b6b, #ee5a52)';
            button.querySelector('span:last-child').textContent = 'Load New Turns';
            button.disabled = false;
        }
    }
    
    function insertButton() {
        const selectors = [
            '.dashboard-header .header-right',
            '.header-container .right-side',
            '[data-test="dashboard-header"]'
        ];
        
        for (const selector of selectors) {
            const element = document.querySelector(selector);
            if (element && !document.getElementById('civ6-refresh-btn')) {
                element.insertAdjacentHTML('beforeend', createRefreshButton());
                document.getElementById('civ6-refresh-btn').addEventListener('click', handleRefresh);
                console.log('🏆 Civ VI refresh button added!');
                return true;
            }
        }
        return false;
    }
    
    // Initialize
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', insertButton);
    } else {
        insertButton();
    }
    
    setTimeout(insertButton, 2000);
})();
            '''
            
            return Response(js_code, mimetype='application/javascript')
        
        print("✅ Civ VI refresh functionality loaded successfully!")
        
    except Exception as e:
        print(f"⚠️ Could not load Civ VI refresh functionality: {e}")

# Register custom views when app starts
CUSTOM_APP_INITIALIZER = register_custom_views

# Feature Flags
FEATURE_FLAGS = {
    'DASHBOARD_NATIVE_FILTERS': True,
    'DASHBOARD_CROSS_FILTERS': True,
    'GLOBAL_ASYNC_QUERIES': False,  # Disable async queries for local development
}

# Cache Configuration (Redis not needed for local setup)
CACHE_CONFIG = {
    'CACHE_TYPE': 'SimpleCache',
    'CACHE_DEFAULT_TIMEOUT': 300
}

# Email Configuration (disabled for local setup)
SMTP_HOST = None
SMTP_STARTTLS = False
SMTP_SSL = False

# CSV Export
CSV_EXPORT = {
    'encoding': 'utf-8',
}

# Webdriver Configuration (for screenshots/alerts - optional)
WEBDRIVER_TYPE = None

# Logging
import logging
LOG_LEVEL = logging.INFO

# Authentication
AUTH_TYPE = 1  # Database authentication
AUTH_ROLE_ADMIN = 'Admin'
AUTH_ROLE_PUBLIC = 'Public'

# Allow embedding (for potential iframe usage)
HTTP_HEADERS = {'X-Frame-Options': 'ALLOWALL'}
