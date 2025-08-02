"""
Custom Superset Dashboard Extension for Civ VI Data Refresh
"""
import subprocess
import os
from flask import Blueprint, jsonify, request
from superset.extensions import db
from superset.views.base import BaseView
from superset import appbuilder
import logging

# Create a blueprint for our custom endpoints
civ6_blueprint = Blueprint(
    'civ6_refresh',
    __name__,
    url_prefix='/civ6'
)

logger = logging.getLogger(__name__)

@civ6_blueprint.route('/refresh-data', methods=['POST'])
def refresh_civ6_data():
    """Endpoint to trigger Civ VI data refresh using Docker"""
    try:
        # Get the project root directory (assuming Superset is running from project dir)
        project_root = os.getcwd()
        
        # Run the Docker command to refresh data
        result = subprocess.run([
            'docker-compose', '--profile', 'data-import', 'up', 'data-loader'
        ], 
        cwd=project_root,
        capture_output=True, 
        text=True, 
        timeout=300  # 5 minute timeout
        )
        
        if result.returncode == 0:
            # Check if data was actually updated by querying the database
            from sqlalchemy import text
            
            # Query latest turn data
            query = text("""
                SELECT 
                    MAX(game_turn) as latest_turn,
                    COUNT(DISTINCT civilization) as civilizations,
                    COUNT(*) as total_records
                FROM civ_game_data
            """)
            
            with db.engine.connect() as conn:
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
            logger.error(f"Docker command failed: {result.stderr}")
            return jsonify({
                'success': False,
                'error': f'Data refresh failed: {result.stderr}'
            }), 500
            
    except subprocess.TimeoutExpired:
        return jsonify({
            'success': False,
            'error': 'Data refresh timed out. Please try again.'
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
        from sqlalchemy import text
        
        # Query latest turn data and rankings
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
        
        with db.engine.connect() as conn:
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
def register_civ6_refresh_blueprint(app):
    """Register the Civ VI refresh blueprint with the Flask app"""
    app.register_blueprint(civ6_blueprint)
