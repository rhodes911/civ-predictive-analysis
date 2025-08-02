#!/usr/bin/env python3
"""
Test database filtering to verify current game data isolation
"""

import psycopg2

def test_database_filtering():
    """Test database queries to verify game session filtering works correctly"""
    
    # Connect to database
    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        database='civ6_analytics',
        user='civ6_user',
        password='civ6_password'
    )
    cursor = conn.cursor()

    print('🔍 TESTING DATABASE FILTERING FOR CURRENT GAME')
    print('=' * 60)

    # Test 1: Show timestamp distribution
    print('\n⏰ TIMESTAMP DISTRIBUTION:')
    cursor.execute('''
        SELECT created_at::date as date, 
               MIN(created_at::time) as earliest,
               MAX(created_at::time) as latest,
               COUNT(*) as records
        FROM civ_game_data 
        GROUP BY created_at::date
        ORDER BY date
    ''')
    for date, earliest, latest, count in cursor.fetchall():
        print(f'  {date} | {earliest} - {latest} | {count} records')

    # Test 2: Show sample records with timestamps
    print('\n📊 SAMPLE DATA WITH TIMESTAMPS:')
    cursor.execute('''
        SELECT created_at, game_turn, 
               REPLACE(civilization, 'CIVILIZATION_', '') as civ, 
               total_score 
        FROM civ_game_data 
        ORDER BY created_at, game_turn
        LIMIT 10
    ''')
    for created_at, turn, civ, score in cursor.fetchall():
        print(f'  {created_at} | Turn {turn:2d} | {civ:12s} | Score: {score:4d}')

    # Test 3: Filter for NEW GAME only (07:00:00 and later)
    print('\n🆕 NEW GAME DATA ONLY (TIME >= 07:00:00):')
    cursor.execute('''
        SELECT COUNT(*) as total_records,
               MIN(game_turn) as min_turn,
               MAX(game_turn) as max_turn,
               COUNT(DISTINCT game_turn) as unique_turns,
               COUNT(DISTINCT civilization) as unique_civs
        FROM civ_game_data 
        WHERE created_at::time >= '07:00:00'
    ''')
    result = cursor.fetchone()
    print(f'  Total records: {result[0]}')
    print(f'  Turn range: {result[1]} - {result[2]} ({result[3]} unique turns)')
    print(f'  Unique civilizations: {result[4]}')

    # Test 4: Show civilizations in NEW GAME
    print('\n🏛️ NEW GAME CIVILIZATIONS:')
    cursor.execute('''
        SELECT REPLACE(civilization, 'CIVILIZATION_', '') as civ,
               COUNT(*) as records,
               MIN(game_turn) as first_turn,
               MAX(game_turn) as last_turn
        FROM civ_game_data 
        WHERE created_at::time >= '07:00:00'
        GROUP BY civilization
        ORDER BY civ
    ''')
    for civ, count, first, last in cursor.fetchall():
        print(f'  {civ:12s} | {count:2d} records | Turns {first}-{last}')

    # Test 5: Compare OLD vs NEW game data
    print('\n⚖️ OLD GAME vs NEW GAME COMPARISON:')
    cursor.execute('''
        SELECT 
            CASE WHEN created_at::time >= '07:00:00' THEN 'NEW_GAME' ELSE 'OLD_GAME' END as game_type,
            COUNT(*) as records,
            MIN(game_turn) as min_turn,
            MAX(game_turn) as max_turn,
            COUNT(DISTINCT civilization) as unique_civs
        FROM civ_game_data 
        GROUP BY CASE WHEN created_at::time >= '07:00:00' THEN 'NEW_GAME' ELSE 'OLD_GAME' END
        ORDER BY game_type
    ''')
    for game_type, records, min_turn, max_turn, civs in cursor.fetchall():
        print(f'  {game_type:8s} | {records:3d} records | Turns {min_turn}-{max_turn} | {civs} civs')

    # Test 6: Latest turn data for NEW GAME
    print('\n🎯 LATEST TURN DATA FOR NEW GAME:')
    cursor.execute('''
        SELECT game_turn, REPLACE(civilization, 'CIVILIZATION_', '') as civ, 
               yields_science, yields_culture, total_score
        FROM civ_game_data 
        WHERE created_at::time >= '07:00:00'
        AND game_turn = (
            SELECT MAX(game_turn) 
            FROM civ_game_data 
            WHERE created_at::time >= '07:00:00'
        )
        ORDER BY total_score DESC
    ''')
    latest_results = cursor.fetchall()
    if latest_results:
        latest_turn = latest_results[0][0]
        print(f'  Latest turn: {latest_turn}')
        for turn, civ, science, culture, score in latest_results:
            print(f'    {civ:12s} | Science: {science:3d} | Culture: {culture:3d} | Score: {score:4d}')
    else:
        print('  No new game data found!')

    # Test 7: Verify filter excludes old game data
    print('\n🔒 VERIFICATION - OLD GAME DATA EXCLUDED:')
    cursor.execute('''
        SELECT COUNT(*) as old_records
        FROM civ_game_data 
        WHERE created_at::time < '07:00:00'
    ''')
    old_count = cursor.fetchone()[0]
    print(f'  Old game records (excluded by filter): {old_count}')

    print('\n✅ DATABASE FILTERING TEST COMPLETE!')
    print('📊 Use created_at::time >= \'07:00:00\' in Superset to get current game only')

    conn.close()

if __name__ == "__main__":
    test_database_filtering()
