from flask import Flask, render_template, redirect, jsonify
import psycopg2
from datetime import datetime
import os

app = Flask(__name__)

# Database connection settings
DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'civ6_analytics',
    'user': 'civ6_user',
    'password': 'civ6_password'
}

def get_latest_turn_data():
    """Get current game status from database"""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        
        # Get latest turn number and count
        cur.execute("""
            SELECT 
                MAX(game_turn) as latest_turn,
                COUNT(DISTINCT civilization) as civilizations,
                COUNT(*) as total_records
            FROM civ_game_data
        """)
        
        result = cur.fetchone()
        latest_turn, civilizations, total_records = result
        
        # Get latest turn rankings
        cur.execute("""
            SELECT 
                civilization,
                total_score,
                yields_science,
                yields_culture
            FROM civ_game_data 
            WHERE game_turn = %s
            ORDER BY total_score DESC
        """, (latest_turn,))
        
        rankings = cur.fetchall()
        
        conn.close()
        
        return {
            'latest_turn': latest_turn,
            'civilizations': civilizations,
            'total_records': total_records,
            'rankings': rankings,
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
    except Exception as e:
        return {'error': str(e)}

@app.route('/')
def index():
    """Main dashboard page"""
    data = get_latest_turn_data()
    return render_template('index.html', data=data)

@app.route('/refresh')
def refresh_data():
    """Show instructions for manual refresh"""
    return jsonify({
        'success': False,
        'message': 'Please run the data loader manually:',
        'instructions': [
            'Open terminal/command prompt',
            'Navigate to project directory',
            'Run: docker-compose --profile data-import up data-loader',
            'Or double-click: load-game-data.bat'
        ]
    })

@app.route('/status')
def status():
    """Get current status as JSON"""
    data = get_latest_turn_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
