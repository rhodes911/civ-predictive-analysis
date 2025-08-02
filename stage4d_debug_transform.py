#!/usr/bin/env python3
"""
Stage 4d: Fix Data Transformation Issues

Debug why we're only getting 1 civilization in our mapping.
Test with complete turn data.
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

def debug_data_issues():
    """Debug data transformation issues"""
    
    print("🐛 STAGE 4D: DEBUG DATA TRANSFORMATION")
    print("="*60)
    
    log_dir = find_civ_log_directory()
    if not log_dir:
        print("❌ Could not find Civ VI logs directory!")
        return
    
    # Load Player_Stats.csv
    stats_file = os.path.join(log_dir, "Player_Stats.csv")
    df_stats = pd.read_csv(stats_file)
    
    print("🔍 Checking data completeness by turn...")
    
    # Check records per turn
    turn_counts = df_stats['Game Turn'].value_counts().sort_index()
    print("\n📊 Records per turn:")
    for turn in sorted(turn_counts.index)[-10:]:  # Last 10 turns
        count = turn_counts[turn]
        print(f"  Turn {turn:2d}: {count:2d} records")
    
    # Find a complete turn (should have 16 records - 6 major civs + 9 city states + free cities)
    complete_turns = turn_counts[turn_counts >= 15].index
    if len(complete_turns) > 0:
        test_turn = complete_turns[-1]  # Use latest complete turn
        print(f"\n✅ Using turn {test_turn} for testing (complete data)")
    else:
        test_turn = 39  # Fallback
        print(f"\n⚠️  Using turn {test_turn} (may be incomplete)")
    
    # Get data for test turn
    test_data = df_stats[df_stats['Game Turn'] == test_turn]
    print(f"\n🔍 Turn {test_turn} civilizations:")
    
    major_civs = []
    city_states = []
    
    for i, (_, row) in enumerate(test_data.iterrows()):
        civ_raw = row[' Player']
        civ_clean = clean_civilization_name(civ_raw)
        is_cs = is_city_state(civ_clean)
        
        print(f"  {i:2d}. '{civ_raw}' → '{civ_clean}' (City-state: {is_cs})")
        
        if is_cs:
            city_states.append(civ_clean)
        elif civ_clean != 'FREE_CITIES':  # Skip free cities
            major_civs.append(civ_clean)
    
    print(f"\n📊 Summary:")
    print(f"  Major civilizations: {len(major_civs)}")
    print(f"  City-states: {len(city_states)}")
    
    print(f"\n🏛️ Major civilizations found:")
    for i, civ in enumerate(major_civs):
        print(f"  Player {i}: {civ}")
    
    # Now test score mapping
    print(f"\n🔍 Testing score data mapping...")
    scores_file = os.path.join(log_dir, "Game_PlayerScores.csv")
    df_scores = pd.read_csv(scores_file)
    
    test_scores = df_scores[df_scores['Game Turn'] == test_turn]
    print(f"\n📊 Score records for turn {test_turn}:")
    
    # Create proper player mapping
    player_mapping = {}
    for i, civ in enumerate(major_civs):
        player_mapping[i] = civ
    
    for _, row in test_scores.iterrows():
        player_num = row[' Player']
        score = row[' Score']
        mapped_civ = player_mapping.get(player_num, f"Unknown Player {player_num}")
        print(f"  Player {player_num}: {score:3d} points → {mapped_civ}")
    
    print(f"\n✅ DEBUG COMPLETE")
    print(f"💡 Next: Create full transformation with complete turn {test_turn}")

if __name__ == "__main__":
    debug_data_issues()
