#!/usr/bin/env python3
"""
Current Game Parser - Only captures data from the current active Civ VI game
"""
import re
import time
import psycopg2
import os

class CurrentGameParser:
    def __init__(self):
        self.db_config = {
            'host': 'localhost',
            'database': 'civ6_live',
            'user': 'civ6_user',
            'password': 'civ6_password',
            'port': 5432
        }
        self.log_file = r"C:\Users\rhode\AppData\Local\Firaxis Games\Sid Meier's Civilization VI\Logs\Lua.log"
        
    def connect_db(self):
        """Connect to the live database"""
        try:
            conn = psycopg2.connect(**self.db_config)
            return conn
        except Exception as e:
            print(f"❌ Database connection failed: {e}")
            return None
    
    def find_current_game_session(self):
        """Find the most recent/current game session in the log file"""
        try:
            if not os.path.exists(self.log_file):
                print(f"❌ Log file not found: {self.log_file}")
                return None
                
            with open(self.log_file, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
                
            # Look for the last GAME_START entry
            current_session = None
            for line in reversed(lines):
                if 'GAME_START:' in line:
                    match = re.search(r'GAME_START:\s*([a-zA-Z0-9_]+)', line)
                    if match:
                        current_session = match.group(1)
                        break
            
            return current_session
                
        except Exception as e:
            print(f"❌ Error finding current game session: {e}")
            return None
    
    def parse_player_data(self, line):
        """Parse PLAYER line from logs"""
        # TurnDataLogger: PLAYER: ID=0, Name=LOC_LEADER_SALADIN_ALT_NAME, Civ=LOC_CIVILIZATION_ARABIA_NAME, Leader=LOC_LEADER_SALADIN_ALT_NAME, Human=True
        player_pattern = r'TurnDataLogger: PLAYER: ID=(\d+), Name=([^,]+), Civ=([^,]+), Leader=([^,]+), Human=(\w+)'
        match = re.search(player_pattern, line)
        
        if match:
            player_id = int(match.group(1))
            name = match.group(2)
            civ = match.group(3)
            leader = match.group(4)
            is_human = match.group(5).lower() == 'true'
            
            return {
                'id': player_id,
                'name': name,
                'civilization': civ,
                'leader': leader,
                'is_human': is_human
            }
        return None
    
    def load_current_game_data(self):
        """Load only the current game session data"""
        current_session = self.find_current_game_session()
        if not current_session:
            print("⚠️ No active game session found")
            return False
            
        print(f"🎮 Found current game session: {current_session}")
        
        conn = self.connect_db()
        if not conn:
            return False
            
        try:
            cursor = conn.cursor()
            
            # Clear all old data
            cursor.execute("DELETE FROM leaders")
            print(f"🧹 Cleared old data from database")
            
            # Parse the log file and extract ONLY current session data
            with open(self.log_file, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
            
            capturing = False
            players_found = 0
            
            for line in lines:
                line = line.strip()
                
                # Check if this is the start of our current session
                if f'GAME_START: {current_session}' in line:
                    capturing = True
                    print(f"📝 Processing current game: {current_session}")
                    continue
                
                # If we encounter a different game session, stop capturing
                elif 'GAME_START:' in line and capturing:
                    other_session = re.search(r'GAME_START:\s*([a-zA-Z0-9_]+)', line)
                    if other_session and other_session.group(1) != current_session:
                        break
                
                # Capture player data only for current session
                if capturing and 'PLAYER:' in line:
                    player_data = self.parse_player_data(line)
                    if player_data:
                        player_data['game_session'] = current_session
                        
                        # Insert player data
                        query = """
                        INSERT INTO leaders (id, name, civilization, leader, is_human, game_session)
                        VALUES (%(id)s, %(name)s, %(civilization)s, %(leader)s, %(is_human)s, %(game_session)s)
                        ON CONFLICT (id, game_session) DO UPDATE SET
                            name = EXCLUDED.name,
                            civilization = EXCLUDED.civilization,
                            leader = EXCLUDED.leader,
                            is_human = EXCLUDED.is_human;
                        """
                        
                        cursor.execute(query, player_data)
                        players_found += 1
                        print(f"✅ Player {player_data['id']} ({player_data['name']}) - Human: {player_data['is_human']}")
            
            conn.commit()
            cursor.close()
            conn.close()
            
            print(f"🎯 Loaded {players_found} players for current game: {current_session}")
            return True
            
        except Exception as e:
            print(f"❌ Error loading current game data: {e}")
            if conn:
                conn.close()
            return False
    
    def monitor_for_new_games(self):
        """Monitor for new games and update data when needed"""
        last_session = None
        
        while True:
            try:
                current_session = self.find_current_game_session()
                
                if current_session and current_session != last_session:
                    print(f"🆕 New game session detected: {current_session}")
                    if self.load_current_game_data():
                        last_session = current_session
                        print("✅ Current game data updated")
                        
                time.sleep(10)  # Check every 10 seconds
                
            except KeyboardInterrupt:
                print("\n⏹️ Parser stopped by user")
                break
            except Exception as e:
                print(f"❌ Error in monitoring: {e}")
                time.sleep(10)

def main():
    """Main function"""
    print("🎯 Starting Current Game Parser...")
    
    parser = CurrentGameParser()
    
    # Create database table if needed
    conn = parser.connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS leaders (
                id INTEGER,
                name VARCHAR(255),
                civilization VARCHAR(255),
                leader VARCHAR(255),
                is_human BOOLEAN,
                game_session VARCHAR(100),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (id, game_session)
            );
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Database table ready")
    
    # Load current game data once
    print("📊 Loading current game data...")
    if parser.load_current_game_data():
        print("✅ Successfully loaded current game data")
    else:
        print("⚠️ No current game data found")
    
    # Start monitoring for new games
    print("🚀 Starting game session monitoring...")
    parser.monitor_for_new_games()

if __name__ == "__main__":
    main()
