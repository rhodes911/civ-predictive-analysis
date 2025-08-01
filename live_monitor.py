#!/usr/bin/env python3
"""
Civ VI Live Data Monitor
Watches for live game data from Civ VI mod and feeds it into our PostgreSQL database
"""

import json
import time
import psycopg2
import os
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class LiveDataHandler(FileSystemEventHandler):
    def __init__(self):
        self.db_connection = None
        self.last_processed_turn = -1
        self.connect_to_database()
        
    def connect_to_database(self):
        """Connect to PostgreSQL database"""
        try:
            self.db_connection = psycopg2.connect(
                host="localhost",
                port=5432,
                database="civ6_analytics",
                user="civ6_user",
                password="civ6_password"
            )
            print("✅ Connected to database")
        except Exception as e:
            print(f"❌ Database connection failed: {e}")
            self.db_connection = None
    
    def on_modified(self, event):
        if event.is_directory:
            return
            
        if event.src_path.endswith('current_game.json'):
            print(f"📊 Live data file updated: {event.src_path}")
            self.process_live_data()
        elif event.src_path.endswith('connection_status.json'):
            print(f"🔗 Connection status updated: {event.src_path}")
            self.check_connection_status()
    
    def process_live_data(self):
        """Process live game data and insert into database"""
        try:
            with open('live_data/current_game.json', 'r') as f:
                game_data = json.load(f)
            
            turn_number = game_data.get('turn_number', 0)
            
            # Skip if we've already processed this turn
            if turn_number <= self.last_processed_turn:
                print(f"⏭️ Turn {turn_number} already processed")
                return
                
            print(f"🎯 Processing Turn {turn_number}")
            
            if not self.db_connection:
                self.connect_to_database()
                if not self.db_connection:
                    print("❌ No database connection")
                    return
            
            cursor = self.db_connection.cursor()
            
            # Insert game session if needed
            game_id = game_data.get('game_id', 'live_game')
            cursor.execute("""
                INSERT INTO game_sessions (game_id, map_type, difficulty, num_players) 
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (game_id) DO NOTHING
            """, (game_id, 'Live Game', 'Unknown', len(game_data.get('players', []))))
            
            # Process each player
            for player_data in game_data.get('players', []):
                cursor.execute("""
                    INSERT INTO game_data (game_id, turn_number, player_name, civilization, science_per_turn, culture_per_turn)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (game_id, turn_number, player_name) 
                    DO UPDATE SET 
                        science_per_turn = EXCLUDED.science_per_turn,
                        culture_per_turn = EXCLUDED.culture_per_turn
                """, (
                    game_id,
                    turn_number,
                    player_data.get('player_name', 'Unknown'),
                    player_data.get('civilization', 'Unknown'),
                    player_data.get('science_per_turn', 0),
                    player_data.get('culture_per_turn', 0)
                ))
            
            self.db_connection.commit()
            self.last_processed_turn = turn_number
            print(f"✅ Turn {turn_number} data inserted into database")
            
            # Update connection status in database
            self.update_dashboard_status(True, f"Live data: Turn {turn_number}")
            
        except Exception as e:
            print(f"❌ Error processing live data: {e}")
            if self.db_connection:
                self.db_connection.rollback()
    
    def check_connection_status(self):
        """Check and display connection status"""
        try:
            with open('live_data/connection_status.json', 'r') as f:
                status = json.load(f)
            
            connected = status.get('connected', False)
            message = status.get('message', '')
            timestamp = status.get('timestamp', 0)
            
            if timestamp > 0:
                dt = datetime.fromtimestamp(timestamp)
                print(f"🔗 Connection: {'✅ CONNECTED' if connected else '❌ DISCONNECTED'}")
                print(f"   Message: {message}")
                print(f"   Last Update: {dt.strftime('%H:%M:%S')}")
            
        except Exception as e:
            print(f"⚠️ Error reading connection status: {e}")
    
    def update_dashboard_status(self, connected, message):
        """Update connection status for dashboard"""
        try:
            status_data = {
                'connected': connected,
                'message': message,
                'timestamp': int(time.time()),
                'last_update': datetime.now().isoformat()
            }
            
            with open('live_data/dashboard_status.json', 'w') as f:
                json.dump(status_data, f, indent=2)
                
        except Exception as e:
            print(f"⚠️ Error updating dashboard status: {e}")

def main():
    print("🎮 Civ VI Live Data Monitor - Starting...")
    print("📁 Monitoring: live_data/ directory")
    print("🔗 Database: localhost:5432")
    print()
    
    # Create handler and observer
    event_handler = LiveDataHandler()
    observer = Observer()
    observer.schedule(event_handler, 'live_data', recursive=False)
    
    # Start monitoring
    observer.start()
    print("👀 Watching for live data updates...")
    print("   - current_game.json: Game data from Civ VI")
    print("   - connection_status.json: Connection status")
    print()
    print("🛑 Press Ctrl+C to stop")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Stopping live data monitor...")
        observer.stop()
    
    observer.join()
    print("✅ Live data monitor stopped")

if __name__ == "__main__":
    main()
