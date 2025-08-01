#!/usr/bin/env python3
"""
Civ VI Lua.log Parser
Watches and parses Lua.log file for structured game data from print() statements
This is the core component that bridges Civ VI logging to our database
"""

import re
import os
import time
import json
import psycopg2
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class LuaLogParser(FileSystemEventHandler):
    def __init__(self, db_config=None):
        self.db_config = db_config or {
            'host': 'localhost',
            'port': 5432,
            'database': 'civ6_analytics',
            'user': 'civ6_user',
            'password': 'civ6_password'
        }
        self.db_connection = None
        self.last_position = 0
        self.current_game_id = None
        self.connect_to_database()
        
        # Patterns to match our structured log output from Civ VI
        self.patterns = {
            'turn_data': re.compile(r'Turn (\d+): Player (\d+) \((.+?)\) -> Science=([0-9.]+), Culture=([0-9.]+), Gold=([0-9.]+), Faith=([0-9.]+), Cities=(\d+)'),
            'game_start': re.compile(r'GAME_START: (.+)'),
            'game_info': re.compile(r'GAME_INFO: Map=(.+?), Difficulty=(.+?), Players=(\d+)'),
            'player_info': re.compile(r'PLAYER: ID=(\d+), Name=(.+?), Civ=(.+?), Leader=(.+?), Human=(\w+)')
        }
    
    def connect_to_database(self):
        """Connect to PostgreSQL database"""
        try:
            self.db_connection = psycopg2.connect(**self.db_config)
            print("✅ Connected to database")
            return True
        except Exception as e:
            print(f"❌ Database connection failed: {e}")
            self.db_connection = None
            return False
    
    def parse_lua_log(self, log_file_path):
        """Parse the Lua.log file for new entries"""
        if not os.path.exists(log_file_path):
            print(f"⚠️ Lua.log not found at: {log_file_path}")
            return
        
        try:
            with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as f:
                # Seek to last known position
                f.seek(self.last_position)
                
                # Read new lines
                new_lines = f.readlines()
                if new_lines:
                    print(f"📖 Found {len(new_lines)} new log lines")
                    for line in new_lines:
                        self.process_log_line(line.strip())
                
                # Update position
                self.last_position = f.tell()
                
        except Exception as e:
            print(f"❌ Error reading Lua.log: {e}")
    
    def process_log_line(self, line):
        """Process a single log line and extract data"""
        if not line:
            return
        
        # Check for game start
        match = self.patterns['game_start'].search(line)
        if match:
            self.current_game_id = match.group(1)
            print(f"🎮 New game started: {self.current_game_id}")
            return
        
        # Check for game info
        match = self.patterns['game_info'].search(line)
        if match:
            map_type, difficulty, num_players = match.groups()
            self.insert_game_session(map_type, difficulty, int(num_players))
            return
        
        # Check for player info
        match = self.patterns['player_info'].search(line)
        if match:
            player_id, name, civ, leader, is_human = match.groups()
            print(f"👤 Player {player_id}: {name} ({civ}) - {leader}")
            return
        
        # Check for turn data
        match = self.patterns['turn_data'].search(line)
        if match:
            turn, player_id, civ, science, culture, gold, faith, cities = match.groups()
            self.insert_turn_data(
                int(turn), int(player_id), civ,
                float(science), float(culture), float(gold), float(faith), int(cities)
            )
            return
    
    def insert_game_session(self, map_type, difficulty, num_players):
        """Insert or update game session info"""
        if not self.db_connection or not self.current_game_id:
            return
        
        try:
            cursor = self.db_connection.cursor()
            cursor.execute("""
                INSERT INTO game_sessions (game_id, map_type, difficulty, num_players) 
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (game_id) DO UPDATE SET
                    map_type = EXCLUDED.map_type,
                    difficulty = EXCLUDED.difficulty,
                    num_players = EXCLUDED.num_players
            """, (self.current_game_id, map_type, difficulty, num_players))
            self.db_connection.commit()
            print(f"📊 Game session updated: {map_type}, {difficulty}, {num_players} players")
        except Exception as e:
            print(f"❌ Error inserting game session: {e}")
            if self.db_connection:
                self.db_connection.rollback()
    
    def insert_turn_data(self, turn, player_id, civilization, science, culture, gold, faith, cities):
        """Insert turn data into database"""
        if not self.db_connection or not self.current_game_id:
            return
        
        try:
            cursor = self.db_connection.cursor()
            
            # First ensure game session exists
            cursor.execute("""
                INSERT INTO game_sessions (game_id, map_type, difficulty, num_players) 
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (game_id) DO NOTHING
            """, (self.current_game_id, 'Test Game', 'Unknown', 2))
            
            # Use player_id as player_name if we don't have a name mapping
            player_name = f"Player_{player_id}"
            
            cursor.execute("""
                INSERT INTO game_data (game_id, turn_number, player_name, civilization, 
                                     science_per_turn, culture_per_turn)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (game_id, turn_number, player_name) 
                DO UPDATE SET 
                    civilization = EXCLUDED.civilization,
                    science_per_turn = EXCLUDED.science_per_turn,
                    culture_per_turn = EXCLUDED.culture_per_turn
            """, (self.current_game_id, turn, player_name, civilization, science, culture))
            
            self.db_connection.commit()
            print(f"🎯 Turn {turn}: {player_name} ({civilization}) - Science: {science}, Culture: {culture}")
            
        except Exception as e:
            print(f"❌ Error inserting turn data: {e}")
            if self.db_connection:
                self.db_connection.rollback()
    
    def on_modified(self, event):
        """Handle file modification events from watchdog"""
        if event.is_directory:
            return
        
        if event.src_path.endswith('Lua.log'):
            print(f"📝 Lua.log updated: {event.src_path}")
            self.parse_lua_log(event.src_path)


def find_lua_log_path():
    """Find the Civ VI Lua.log file path"""
    possible_paths = [
        # AppData location (most common for newer Civ VI versions)
        "C:/Users/{}/AppData/Local/Firaxis Games/Sid Meier's Civilization VI/Logs/Lua.log".format(os.getenv('USERNAME', '')),
        # Documents location (older versions or some installations)
        os.path.expanduser("~/Documents/My Games/Sid Meier's Civilization VI/Logs/Lua.log"),
        os.path.expanduser("~/OneDrive/Documents/My Games/Sid Meier's Civilization VI/Logs/Lua.log"),
        # Alternative paths
        "C:/Users/{}/Documents/My Games/Sid Meier's Civilization VI/Logs/Lua.log".format(os.getenv('USERNAME', '')),
        "C:/Users/{}/OneDrive/Documents/My Games/Sid Meier's Civilization VI/Logs/Lua.log".format(os.getenv('USERNAME', ''))
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            return path
    
    return None


def main():
    print("🎮 Civ VI Lua.log Parser - Starting...")
    
    # Find Lua.log file
    lua_log_path = find_lua_log_path()
    if not lua_log_path:
        print("❌ Lua.log file not found!")
        print("📋 Expected locations:")
        for path in [
            "~/Documents/My Games/Sid Meier's Civilization VI/Logs/Lua.log",
            "~/OneDrive/Documents/My Games/Sid Meier's Civilization VI/Logs/Lua.log"
        ]:
            print(f"   {path}")
        print("\n💡 Make sure:")
        print("   1. Civ VI is installed")
        print("   2. You've played at least one game (to create the log)")
        print("   3. Logging is enabled in Civ VI settings")
        return
    
    print(f"✅ Found Lua.log: {lua_log_path}")
    
    # Create parser
    parser = LuaLogParser()
    
    # Parse existing content
    print("📖 Parsing existing log content...")
    parser.parse_lua_log(lua_log_path)
    
    # Set up file watching
    observer = Observer()
    observer.schedule(parser, os.path.dirname(lua_log_path), recursive=False)
    
    print("👀 Watching for new log entries...")
    print(f"📁 Monitoring: {lua_log_path}")
    print("🎯 Database: localhost:5432")
    print("\n🛑 Press Ctrl+C to stop")
    
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Stopping log parser...")
        observer.stop()
    
    observer.join()
    print("✅ Log parser stopped")


if __name__ == "__main__":
    main()
