#!/usr/bin/env python3
"""
Live Civ VI Log Parser - Watches for CURRENT ACTIVE game data only
"""
import re
import time
import psycopg2
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class LiveCivLogHandler(FileSystemEventHandler):
    def __init__(self):
        self.db_config = {
            'host': 'localhost',
            'database': 'civ6_live',
            'user': 'civ6_user',
            'password': 'civ6_password',
            'port': 5432
        }
        self.last_position = 0
        self.current_game_session = None
        self.capturing_current_game = False
        self.processed_sessions = set()  # Track sessions we've already processed
        
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
                lines = f.readlines()
                
            # Look for the last GAME_START entry
            current_session = None
            for line in reversed(lines):
                if 'GAME_START:' in line:
                    match = re.search(r'GAME_START:\s*([a-zA-Z0-9_]+)', line)
                    if match:
                        current_session = match.group(1)
                        break
            
            if current_session:
                print(f"🎮 Found current game session: {current_session}")
                return current_session
            else:
                print("⚠️ No active game session found in logs")
                return None
                
        except Exception as e:
            print(f"❌ Error finding current game session: {e}")
            return None
    
    def clear_old_data_and_load_current_game(self, log_file_path):
        """Clear database and load only the current game session data"""
        current_session = self.find_current_game_session(log_file_path)
        if not current_session:
            return False
            
        # Skip if we've already processed this session
        if current_session in self.processed_sessions:
            return True
            
        conn = self.connect_db()
        if not conn:
            return False
            
        try:
            cursor = conn.cursor()
            
            # Clear all old data
            cursor.execute("DELETE FROM leaders")
            print(f"🧹 Cleared old data from database")
            
            # Parse the log file and extract ONLY current session data
            with open(log_file_path, 'r', encoding='utf-8') as f:
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
            
            self.current_game_session = current_session
            self.capturing_current_game = True
            self.processed_sessions.add(current_session)
            
            print(f"🎯 Loaded {players_found} players for current game: {current_session}")
            return True
            
        except Exception as e:
            print(f"❌ Error loading current game data: {e}")
            if conn:
                conn.close()
            return False
    
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
                'is_human': is_human,
                'game_session': self.current_game_session
            }
        return None
    
    def parse_game_start(self, line):
        """Parse GAME_START line from logs"""
        # TurnDataLogger: GAME_START: game_1754078751
        game_pattern = r'TurnDataLogger: GAME_START: (game_\d+)'
        match = re.search(game_pattern, line)
        
        if match:
            new_game_session = match.group(1)
            
            # Only capture if this is a NEW game session (different from current)
            if new_game_session != self.current_game_session:
                self.current_game_session = new_game_session
                self.capturing_current_game = True
                
                # Clear existing data for this new game session
                self.clear_game_session_data(new_game_session)
                
                print(f"🎮 NEW game session detected: {self.current_game_session}")
                print(f"📝 Now capturing data for current game only")
                return self.current_game_session
        return None
    
    def clear_game_session_data(self, game_session):
        """Clear data for a specific game session to start fresh"""
        conn = self.connect_db()
        if not conn:
            return False
            
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM leaders WHERE game_session = %s", (game_session,))
            conn.commit()
            cursor.close()
            conn.close()
            print(f"🧹 Cleared old data for game session: {game_session}")
            return True
        except Exception as e:
            print(f"❌ Failed to clear game session data: {e}")
            if conn:
                conn.close()
            return False
    
    def insert_player_data(self, player_data):
        """Insert player data into database - only for current game session"""
        # Only insert if we're capturing the current game
        if not self.capturing_current_game:
            return False
            
        conn = self.connect_db()
        if not conn:
            return False
            
        try:
            cursor = conn.cursor()
            
            # Insert or update player data
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
            conn.commit()
            
            print(f"✅ Player {player_data['id']} ({player_data['name']}) - Human: {player_data['is_human']}")
            
            cursor.close()
            conn.close()
            return True
            
        except Exception as e:
            print(f"❌ Database insert failed: {e}")
            if conn:
                conn.close()
            return False
    
    def process_new_lines(self, log_file_path):
        """Process new lines in the log file"""
        try:
            with open(log_file_path, 'r', encoding='utf-8') as f:
                f.seek(self.last_position)
                new_lines = f.readlines()
                self.last_position = f.tell()
                
                for line in new_lines:
                    line = line.strip()
                    
                    # Check for game start
                    if 'GAME_START:' in line:
                        self.parse_game_start(line)
                    
                    # Check for player data - only process if we're capturing current game
                    elif 'PLAYER:' in line and self.capturing_current_game:
                        player_data = self.parse_player_data(line)
                        if player_data and self.current_game_session:
                            self.insert_player_data(player_data)
                            
        except Exception as e:
            print(f"❌ Error processing log file: {e}")
    
    def on_modified(self, event):
        """Called when log file is modified"""
        if not event.is_directory and event.src_path.endswith('Lua.log'):
            print(f"📝 Log file updated: {event.src_path}")
            self.process_new_lines(event.src_path)

def main():
    """Main function to start log monitoring"""
    log_path = r"C:\Users\rhode\AppData\Local\Firaxis Games\Sid Meier's Civilization VI\Logs"
    log_file = r"C:\Users\rhode\AppData\Local\Firaxis Games\Sid Meier's Civilization VI\Logs\Lua.log"
    
    print("🎯 Starting Live Civ VI Log Parser (CURRENT GAME ONLY)...")
    print(f"📂 Monitoring: {log_path}")
    
    # Create database table if needed
    handler = LiveCivLogHandler()
    conn = handler.connect_db()
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
    
    # Load current game session data immediately
    if handler.clear_old_data_and_load_current_game(log_file):
        print("✅ Current game data loaded successfully")
    else:
        print("⚠️ No current game found - will monitor for new games")
    
    # Set position to end of file for future monitoring
    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            f.seek(0, 2)  # Seek to end of file
            handler.last_position = f.tell()
    except Exception as e:
        print(f"⚠️ Could not set initial position: {e}")
    
    # Start file monitoring for NEW games
    event_handler = handler
    observer = Observer()
    observer.schedule(event_handler, log_path, recursive=False)
    observer.start()
    
    print("🚀 Live parser started! Monitoring for game session changes...")
    print("   Current game data loaded. Will update if new game starts.")
    
    try:
        while True:
            time.sleep(5)  # Check every 5 seconds for new game sessions
            handler.clear_old_data_and_load_current_game(log_file)
    except KeyboardInterrupt:
        observer.stop()
        print("\n⏹️ Live parser stopped")
    
    observer.join()

if __name__ == "__main__":
    main()
