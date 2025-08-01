#!/usr/bin/env python3
"""
Live Civ VI Log Parser - CURRENT GAME ONLY
Finds the most recent game session and loads only that data
"""
import re
import time
import psycopg2

class CurrentGameParser:
    def __init__(self):
        self.db_config = {
            'host': 'localhost',
            'database': 'civ6_live',
            'user': 'civ6_user',
            'password': 'civ6_password',
            'port': 5432
        }
        self.last_processed_session = None
        
    def connect_db(self):
        """Connect to the live database"""
        try:
            conn = psycopg2.connect(**self.db_config)
            return conn
        except Exception as e:
            print(f"❌ Database connection failed: {e}")
            return None
    
    def find_current_game_session(self, log_file_path):
        """Find the most recent/current game session in the log file"""
        try:
            with open(log_file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Find all GAME_START entries and get the last one
            game_starts = re.findall(r'GAME_START:\s*([a-zA-Z0-9_]+)', content)
            
            if game_starts:
                current_session = game_starts[-1]  # Get the most recent one
                return current_session
            else:
                print("⚠️ No game sessions found in logs")
                return None
                
        except Exception as e:
            print(f"❌ Error finding current game session: {e}")
            return None
    
    def parse_player_data(self, line):
        """Parse PLAYER line from logs"""
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
    
    def load_current_game_data(self, log_file_path):
        """Load data for the current game session only"""
        current_session = self.find_current_game_session(log_file_path)
        if not current_session:
            print("❌ No current game session found")
            return False
            
        # Skip if we've already processed this session
        if current_session == self.last_processed_session:
            return True
            
        print(f"🎮 Current game session: {current_session}")
        
        conn = self.connect_db()
        if not conn:
            return False
            
        try:
            cursor = conn.cursor()
            
            # Clear all old data
            cursor.execute("DELETE FROM leaders")
            print(f"🧹 Cleared old game data")
            
            # Read the entire log file
            with open(log_file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # Find the start of the current session and extract only its data
            capturing = False
            players_found = 0
            
            for line in lines:
                line = line.strip()
                
                # Check if this is the start of our current session
                if f'GAME_START: {current_session}' in line:
                    capturing = True
                    print(f"📝 Found current game start: {current_session}")
                    continue
                
                # If we encounter a different/newer game session, stop
                elif 'GAME_START:' in line and capturing:
                    other_session = re.search(r'GAME_START:\s*([a-zA-Z0-9_]+)', line)
                    if other_session and other_session.group(1) != current_session:
                        print(f"📝 Found newer session, stopping at: {other_session.group(1)}")
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
            
            self.last_processed_session = current_session
            print(f"🎯 Loaded {players_found} players for current game: {current_session}")
            return True
            
        except Exception as e:
            print(f"❌ Error loading current game data: {e}")
            if conn:
                conn.close()
            return False

def main():
    """Main function"""
    log_file = r"C:\Users\rhode\AppData\Local\Firaxis Games\Sid Meier's Civilization VI\Logs\Lua.log"
    
    print("🎯 Starting Current Game Parser...")
    
    # Create database table if needed
    parser = CurrentGameParser()
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
    
    print("🚀 Loading current game data...")
    
    try:
        while True:
            parser.load_current_game_data(log_file)
            print("⏱️ Checking for game changes in 10 seconds...")
            time.sleep(10)  # Check every 10 seconds
            
    except KeyboardInterrupt:
        print("\n⏹️ Parser stopped")

if __name__ == "__main__":
    main()
