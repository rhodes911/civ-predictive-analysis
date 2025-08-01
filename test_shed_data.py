#!/usr/bin/env python3
"""
Generate comprehensive test data for the DeepResearch Method
Creates multiple games with realistic progression patterns
"""

import sys
import os
import time
import random
from datetime import datetime

# Add src to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.data.log_parser import LuaLogParser
from src.data.loader import DataLoader

def generate_realistic_game_data(game_id, num_players=6, max_turns=50):
    """Generate realistic Civ VI game progression data"""
    
    # Define civilizations with their typical strengths
    civs = [
        ("Korea", {"science_bonus": 1.3, "culture_bonus": 1.0}),
        ("Rome", {"science_bonus": 1.0, "culture_bonus": 1.1}),
        ("Egypt", {"science_bonus": 1.0, "culture_bonus": 1.2}),
        ("Germany", {"science_bonus": 1.2, "culture_bonus": 0.9}),
        ("Greece", {"science_bonus": 1.0, "culture_bonus": 1.3}),
        ("Japan", {"science_bonus": 1.1, "culture_bonus": 1.1}),
        ("China", {"science_bonus": 1.1, "culture_bonus": 1.0}),
        ("Russia", {"science_bonus": 1.0, "culture_bonus": 0.9})
    ]
    
    # Select civilizations for this game
    selected_civs = random.sample(civs, min(num_players, len(civs)))
    
    game_data = []
    
    for turn in range(1, max_turns + 1):
        for player_id, (civ_name, bonuses) in enumerate(selected_civs):
            
            # Base yields that grow over time
            base_science = 2.0 + (turn * 0.8) + random.uniform(-0.5, 0.5)
            base_culture = 1.5 + (turn * 0.6) + random.uniform(-0.3, 0.3)
            base_gold = 3.0 + (turn * 0.4) + random.uniform(-0.8, 0.8)
            base_faith = 0.0 + (turn * 0.2) + random.uniform(-0.1, 0.2)
            
            # Apply civilization bonuses
            science = base_science * bonuses["science_bonus"]
            culture = base_culture * bonuses["culture_bonus"]
            
            # Add some randomness and player skill differences
            player_skill = random.uniform(0.8, 1.2)  # Some players are better
            science *= player_skill
            culture *= player_skill
            
            # Cities grow over time
            cities = min(1 + (turn // 10) + random.randint(0, 2), 12)
            
            # Ensure positive values
            science = max(0.1, science)
            culture = max(0.1, culture)
            gold = max(0.1, base_gold)
            faith = max(0.0, base_faith)
            
            game_data.append({
                'turn': turn,
                'player_id': player_id,
                'civilization': civ_name,
                'science': round(science, 1),
                'culture': round(culture, 1),
                'gold': round(gold, 1),
                'faith': round(faith, 1),
                'cities': cities
            })
    
    return game_data

def create_test_log_file(filename, games_data):
    """Create a test Lua.log file with multiple games"""
    
    with open(filename, 'w') as f:
        for game_id, game_data in games_data.items():
            # Write game start
            f.write(f"GAME_START: {game_id}\n")
            f.write(f"GAME_INFO: Map=Pangaea, Difficulty=Emperor, Players={len(set(d['player_id'] for d in game_data))}\n")
            
            # Write player info
            players_written = set()
            for data in game_data:
                if data['player_id'] not in players_written:
                    f.write(f"PLAYER: ID={data['player_id']}, Name=Player_{data['player_id']}, Civ={data['civilization']}, Leader=Leader_{data['player_id']}, Human=False\n")
                    players_written.add(data['player_id'])
            
            # Write turn data
            for data in game_data:
                f.write(f"Turn {data['turn']}: Player {data['player_id']} ({data['civilization']}) -> Science={data['science']}, Culture={data['culture']}, Gold={data['gold']}, Faith={data['faith']}, Cities={data['cities']}\n")

def test_with_shed_of_data():
    """Test the system with a comprehensive dataset"""
    
    print("🏗️ Generating a shed of test data...")
    print("=" * 50)
    
    # Generate multiple games with different characteristics
    games_data = {}
    
    # Game 1: Science victory game (Korea dominates)
    print("📊 Generating Game 1: Science Victory Pattern...")
    games_data["science_victory_game"] = generate_realistic_game_data("science_victory_game", 4, 30)
    
    # Game 2: Culture victory game (Greece/Egypt strong)
    print("📊 Generating Game 2: Culture Victory Pattern...")
    games_data["culture_victory_game"] = generate_realistic_game_data("culture_victory_game", 6, 25)
    
    # Game 3: Balanced game
    print("📊 Generating Game 3: Balanced Competition...")
    games_data["balanced_game"] = generate_realistic_game_data("balanced_game", 5, 40)
    
    # Calculate total data points
    total_turns = sum(len(game_data) for game_data in games_data.values())
    print(f"📈 Generated {len(games_data)} games with {total_turns} total data points")
    
    # Create test log file
    test_log_filename = "test_shed_data.log"
    print(f"📝 Creating test log file: {test_log_filename}")
    create_test_log_file(test_log_filename, games_data)
    
    # Parse the data
    print("🔍 Parsing test data through DeepResearch pipeline...")
    parser = LuaLogParser()
    
    if parser.db_connection:
        print("✅ Database connected")
        
        # Parse the test file
        parser.parse_lua_log(test_log_filename)
        
        print("📊 Testing data retrieval...")
        loader = DataLoader()
        
        # Get stats
        total_records = loader.get_total_records()
        recent_games = loader.get_recent_games(limit=5)
        
        print(f"📈 Total records in database: {total_records}")
        print(f"🎮 Recent games: {len(recent_games)}")
        
        for game in recent_games:
            print(f"   🎯 {game['game_id']}: {game['max_turn']} turns, {game['active_players']} players")
        
        # Test ML analysis
        print("\n🧠 Testing ML analysis on generated data...")
        from src.models.predictors import VictoryPredictor
        predictor = VictoryPredictor()
        
        for game in recent_games[-3:]:  # Test last 3 games
            game_analytics = loader.get_turn_analytics(game['game_id'])
            if game_analytics:
                prediction = predictor.predict_victory(game_analytics)
                print(f"🎯 {game['game_id']}: {prediction.get('predicted_victory', 'Unknown')} ({prediction.get('confidence', 0):.2f} confidence)")
        
        # Clean up test file
        os.remove(test_log_filename)
        print(f"🧹 Cleaned up test file: {test_log_filename}")
        
        print("\n✅ Shed of data test completed successfully!")
        
    else:
        print("❌ Database connection failed")

if __name__ == "__main__":
    test_with_shed_of_data()
