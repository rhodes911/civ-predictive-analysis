#!/usr/bin/env python3
"""
Civ VI Analytics - Main Application
Orchestrates the complete pipeline from Lua.log parsing to ML analysis
"""

import os
import sys
import time
import subprocess
import threading
from pathlib import Path

# Add current directory to path for imports  
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.data.log_parser import LuaLogParser, find_lua_log_path
from src.data.loader import DataLoader
from src.models.predictors import VictoryPredictor

class CivMLPipeline:
    def __init__(self):
        self.log_parser = None
        self.data_loader = None
        self.victory_predictor = None
        self.running = False
        
    def initialize(self):
        """Initialize all components"""
        print("🚀 Initializing Civ VI ML Pipeline...")
        
        # Check if Docker containers are running
        if not self.check_docker_services():
            print("❌ Docker services not running. Please run: stage2.bat start")
            return False
        
        # Initialize components
        self.log_parser = LuaLogParser()
        self.data_loader = DataLoader()
        self.victory_predictor = VictoryPredictor()
        
        print("✅ Pipeline initialized successfully")
        return True
    
    def check_docker_services(self):
        """Check if required Docker services are running"""
        try:
            result = subprocess.run(['docker', 'ps'], capture_output=True, text=True)
            if 'civ6_database' in result.stdout and 'civ6_superset' in result.stdout:
                return True
            return False
        except:
            return False
    
    def start_log_monitoring(self):
        """Start monitoring Lua.log file"""
        lua_log_path = find_lua_log_path()
        if not lua_log_path:
            print("❌ Lua.log file not found. Please:")
            print("   1. Install the Civ VI mod")
            print("   2. Play at least one turn in Civ VI")
            print("   3. Make sure logging is enabled")
            return False
        
        print(f"👀 Monitoring Lua.log: {lua_log_path}")
        
        # Start log parsing in background thread
        def monitor_logs():
            self.log_parser.parse_lua_log(lua_log_path)
            # Set up file watching
            from watchdog.observers import Observer
            observer = Observer()
            observer.schedule(self.log_parser, os.path.dirname(lua_log_path), recursive=False)
            observer.start()
            
            try:
                while self.running:
                    time.sleep(1)
            finally:
                observer.stop()
                observer.join()
        
        self.running = True
        monitor_thread = threading.Thread(target=monitor_logs, daemon=True)
        monitor_thread.start()
        
        return True
    
    def run_analysis(self):
        """Run ML analysis on current data"""
        print("🧠 Running ML analysis...")
        
        # Load recent game data
        games = self.data_loader.get_recent_games(limit=10)
        if not games:
            print("⚠️ No game data found for analysis")
            return
        
        print(f"📊 Analyzing {len(games)} games...")
        
        # Run victory prediction
        for game in games:
            prediction = self.victory_predictor.predict_victory(game)
            print(f"🎯 Game {game['game_id']}: {prediction}")
    
    def run_dashboard(self):
        """Open Superset dashboard"""
        import webbrowser
        dashboard_url = "http://localhost:8088"
        print(f"📊 Opening dashboard: {dashboard_url}")
        webbrowser.open(dashboard_url)
    
    def status(self):
        """Show system status"""
        print("📋 Civ VI ML Pipeline Status")
        print("=" * 40)
        
        # Docker services
        if self.check_docker_services():
            print("✅ Docker services: Running")
        else:
            print("❌ Docker services: Not running")
        
        # Lua.log
        lua_log_path = find_lua_log_path()
        if lua_log_path:
            print(f"✅ Lua.log found: {lua_log_path}")
        else:
            print("❌ Lua.log: Not found")
        
        # Database connection
        if self.log_parser and self.log_parser.db_connection:
            print("✅ Database: Connected")
        else:
            print("❌ Database: Not connected")
        
        # Data count
        if self.data_loader:
            count = self.data_loader.get_total_records()
            print(f"📊 Total records: {count}")
        
        print()
    
    def stop(self):
        """Stop the pipeline"""
        self.running = False
        print("🛑 Pipeline stopped")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Civ VI ML Analytics Pipeline')
    parser.add_argument('command', choices=['start', 'monitor', 'analyze', 'dashboard', 'status', 'stop'], 
                       help='Command to execute')
    
    args = parser.parse_args()
    
    pipeline = CivMLPipeline()
    
    if args.command == 'start':
        print("🎮 Starting Civ VI ML Pipeline...")
        if pipeline.initialize():
            pipeline.start_log_monitoring()
            print("\n✅ Pipeline running! Use 'analyze' to run ML analysis")
            print("🛑 Press Ctrl+C to stop")
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                pipeline.stop()
    
    elif args.command == 'monitor':
        if pipeline.initialize():
            pipeline.start_log_monitoring()
            print("\n👀 Log monitoring active")
            print("🛑 Press Ctrl+C to stop")
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                pipeline.stop()
    
    elif args.command == 'analyze':
        if pipeline.initialize():
            pipeline.run_analysis()
    
    elif args.command == 'dashboard':
        pipeline.run_dashboard()
    
    elif args.command == 'status':
        if pipeline.initialize():
            pipeline.status()
    
    elif args.command == 'stop':
        pipeline.stop()


if __name__ == "__main__":
    main()
