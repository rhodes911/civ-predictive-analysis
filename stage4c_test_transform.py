#!/usr/bin/env python3
"""
Stage 4c: Data Transformation Test

Test our data transformation logic with real CSV data.
This will show exactly what data we'll insert into the database.

Baby Steps:
1. Load all 3 CSV files  
2. Merge them by turn and civilization
3. Transform player numbers to civilization names
4. Show sample transformed records
5. Validate data quality
"""

import pandas as pd
import os

def find_civ_log_directory():
    """Find the Civ VI logs directory"""
    log_paths = [
        os.path.expandvars(r"%LOCALAPPDATA%\Firaxis Games\Sid Meier's Civilization VI\Logs"),
        os.path.expandvars(r"%USERPROFILE%\Documents\My Games\Sid Meier's Civilization VI\Logs"),
        r"C:\Users\rhode\AppData\Local\Firaxis Games\Sid Meier's Civilization VI\Logs"
    ]
    
    for path in log_paths:
        if os.path.exists(path):
            return path
    return None

def clean_civilization_name(civ_name):
    """Convert ' CIVILIZATION_NETHERLANDS' to 'NETHERLANDS'"""
    if isinstance(civ_name, str):
        return civ_name.replace(' CIVILIZATION_', '').replace('CIVILIZATION_', '')
    return civ_name

def is_city_state(civ_name):
    """Determine if a civilization is a city-state"""
    city_states = [
        'FEZ', 'VILNIUS', 'WOLIN', 'NALANDA', 'ZANZIBAR', 
        'TARUGA', 'AKKAD', 'CAGUANA', 'HONG_KONG', 'FREE_CITIES'
    ]
    return civ_name in city_states

def test_data_transformation():
    """Test transforming CSV data into our database format"""
    
    print("🔄 STAGE 4C: DATA TRANSFORMATION TEST")
    print("="*60)
    
    log_dir = find_civ_log_directory()
    if not log_dir:
        print("❌ Could not find Civ VI logs directory!")
        return
    
    # Load all CSV files
    print("📥 Loading CSV files...")
    
    # 1. Load Player_Stats.csv (main stats)
    stats_file = os.path.join(log_dir, "Player_Stats.csv")
    df_stats = pd.read_csv(stats_file)
    print(f"✅ Player_Stats.csv: {len(df_stats)} records")
    
    # 2. Load Player_Stats_2.csv (advanced stats)
    stats2_file = os.path.join(log_dir, "Player_Stats_2.csv")
    df_stats2 = pd.read_csv(stats2_file)
    print(f"✅ Player_Stats_2.csv: {len(df_stats2)} records")
    
    # 3. Load Game_PlayerScores.csv (scores)
    scores_file = os.path.join(log_dir, "Game_PlayerScores.csv") 
    df_scores = pd.read_csv(scores_file)
    print(f"✅ Game_PlayerScores.csv: {len(df_scores)} records")
    
    print("\n🔄 Transforming data...")
    
    # Create player number to civilization mapping
    print("\n📊 Creating player mapping...")
    player_mapping = {}
    
    # Get latest turn data to build mapping
    latest_turn = df_stats['Game Turn'].max()
    latest_stats = df_stats[df_stats['Game Turn'] == latest_turn]
    
    # Major civilizations in order (Player 0, 1, 2, etc.)
    major_civs = []
    for _, row in latest_stats.iterrows():
        civ_name = clean_civilization_name(row[' Player'])
        if not is_city_state(civ_name):
            major_civs.append(civ_name)
    
    # Build mapping: Player 0 = first major civ, etc.
    for i, civ in enumerate(major_civs):
        player_mapping[i] = civ
    
    print("🗺️ Player mapping:")
    for player_num, civ_name in player_mapping.items():
        print(f"  Player {player_num} → {civ_name}")
    
    # Transform main stats data
    print("\n🔄 Transforming Player_Stats data...")
    df_stats_clean = df_stats.copy()
    df_stats_clean['civilization'] = df_stats_clean[' Player'].apply(clean_civilization_name)
    df_stats_clean['is_city_state'] = df_stats_clean['civilization'].apply(is_city_state)
    
    # Transform scores data (map player numbers to civilization names)
    print("🔄 Transforming scores data...")
    df_scores_clean = df_scores.copy()
    df_scores_clean['civilization'] = df_scores_clean[' Player'].map(player_mapping)
    df_scores_clean = df_scores_clean.dropna(subset=['civilization'])  # Remove unmapped players
    
    # Merge all data for latest turn
    print(f"\n🔗 Merging data for turn {latest_turn}...")
    
    # Get data for latest turn
    turn_stats = df_stats_clean[df_stats_clean['Game Turn'] == latest_turn]
    turn_stats2 = df_stats2[df_stats2['Game Turn'] == latest_turn]
    turn_scores = df_scores_clean[df_scores_clean['Game Turn'] == latest_turn]
    
    print(f"📊 Turn {latest_turn} data:")
    print(f"  Stats records: {len(turn_stats)}")
    print(f"  Stats2 records: {len(turn_stats2)}")
    print(f"  Scores records: {len(turn_scores)}")
    
    # Show sample transformed records
    print(f"\n📋 SAMPLE TRANSFORMED RECORDS (Turn {latest_turn}):")
    print("-" * 60)
    
    for _, row in turn_stats.head(3).iterrows():
        civ = row['civilization']
        print(f"\n🏛️ {civ}:")
        print(f"  🏙️  Cities: {row[' Num Cities']}")
        print(f"  👥 Population: {row[' Population']}")
        print(f"  🔬 Science/turn: {row[' YIELDS: Science']}")
        print(f"  🎭 Culture/turn: {row[' Culture']}")
        print(f"  💰 Gold/turn: {row[' Gold']}")
        print(f"  🗺️  Tiles owned: {row[' TILES: Owned']}")
        
        # Find corresponding score
        score_row = turn_scores[turn_scores['civilization'] == civ]
        if not score_row.empty:
            total_score = score_row.iloc[0][' Score']
            print(f"  🏆 Total Score: {total_score}")
        
        print(f"  🏛️ City-state: {row['is_city_state']}")
    
    print("\n✅ DATA TRANSFORMATION TEST COMPLETE")
    print("💡 Next: Create database table and test insertion")

if __name__ == "__main__":
    test_data_transformation()
