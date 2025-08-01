#!/usr/bin/env python3
"""
Process existing Civ VI log data and insert into live database
"""
import re
import psycopg2

def process_existing_logs():
    """Process existing log data and insert into database"""
    log_file = r"C:\Users\rhode\AppData\Local\Firaxis Games\Sid Meier's Civilization VI\Logs\Lua.log"
    
    # Database config
    db_config = {
        'host': 'localhost',
        'database': 'civ6_live',
        'user': 'civ6_user',
        'password': 'civ6_password',
        'port': 5432
    }
    
    print("📋 Processing existing log data...")
    
    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"❌ Could not read log file: {e}")
        return
    
    current_game = None
    players_to_insert = []
    
    # Parse log data
    for line in lines:
        if 'GAME_START:' in line:
            match = re.search(r'GAME_START: (game_\d+)', line)
            if match:
                current_game = match.group(1)
                print(f"🎮 Found game: {current_game}")
        
        elif 'PLAYER:' in line and current_game:
            match = re.search(r'PLAYER: ID=(\d+), Name=([^,]+), Civ=([^,]+), Leader=([^,]+), Human=(\w+)', line)
            if match:
                player_data = {
                    'id': int(match.group(1)),
                    'name': match.group(2),
                    'civilization': match.group(3),
                    'leader': match.group(4),
                    'is_human': match.group(5).lower() == 'true',
                    'game_session': current_game
                }
                players_to_insert.append(player_data)
                print(f"👤 Player {player_data['id']}: {player_data['name']} (Human: {player_data['is_human']})")
    
    # Insert into database
    if players_to_insert:
        try:
            conn = psycopg2.connect(**db_config)
            cursor = conn.cursor()
            
            for player in players_to_insert:
                query = """
                INSERT INTO leaders (id, name, civilization, leader, is_human, game_session)
                VALUES (%(id)s, %(name)s, %(civilization)s, %(leader)s, %(is_human)s, %(game_session)s)
                ON CONFLICT (id, game_session) DO UPDATE SET
                    name = EXCLUDED.name,
                    civilization = EXCLUDED.civilization,
                    leader = EXCLUDED.leader,
                    is_human = EXCLUDED.is_human;
                """
                cursor.execute(query, player)
            
            conn.commit()
            cursor.close()
            conn.close()
            
            print(f"✅ Inserted {len(players_to_insert)} players into live database")
            print(f"🎯 Current game session: {current_game}")
            
        except Exception as e:
            print(f"❌ Database error: {e}")
    else:
        print("ℹ️ No player data found in logs")

if __name__ == "__main__":
    process_existing_logs()
