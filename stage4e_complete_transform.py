#!/usr/bin/env python3
"""
Stage 4e: Complete Data Transformation

Create final transformation that combines all CSV data into our database format.
Test with complete turn 39 data.
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

def transform_complete_data():
    """Transform complete CSV data into database format"""
    
    print("🔄 STAGE 4E: COMPLETE DATA TRANSFORMATION")
    print("="*60)
    
    log_dir = find_civ_log_directory()
    if not log_dir:
        print("❌ Could not find Civ VI logs directory!")
        return None
    
    # Load all CSV files
    print("📥 Loading CSV files...")
    
    stats_file = os.path.join(log_dir, "Player_Stats.csv")
    stats2_file = os.path.join(log_dir, "Player_Stats_2.csv")
    scores_file = os.path.join(log_dir, "Game_PlayerScores.csv")
    
    df_stats = pd.read_csv(stats_file)
    df_stats2 = pd.read_csv(stats2_file)
    df_scores = pd.read_csv(scores_file)
    
    print(f"✅ Loaded {len(df_stats)} Player_Stats records")
    print(f"✅ Loaded {len(df_stats2)} Player_Stats_2 records") 
    print(f"✅ Loaded {len(df_scores)} Game_PlayerScores records")
    
    # Use turn 39 for complete data test
    test_turn = 39
    print(f"\n🔄 Transforming data for turn {test_turn}...")
    
    # Get turn data
    turn_stats = df_stats[df_stats['Game Turn'] == test_turn].copy()
    turn_stats2 = df_stats2[df_stats2['Game Turn'] == test_turn].copy()
    turn_scores = df_scores[df_scores['Game Turn'] == test_turn].copy()
    
    # Clean civilization names in stats data
    turn_stats['civilization'] = turn_stats[' Player'].apply(clean_civilization_name)
    turn_stats['is_city_state'] = turn_stats['civilization'].apply(is_city_state)
    
    # Clean stats2 data
    turn_stats2['civilization'] = turn_stats2[' Player'].apply(clean_civilization_name)
    
    # Create player mapping for scores (Player 0-5 = major civs, 6+ = city states)
    major_civs = turn_stats[turn_stats['is_city_state'] == False]['civilization'].tolist()
    player_mapping = {i: civ for i, civ in enumerate(major_civs)}
    
    # Add city-state mappings (player numbers 6+ map to city-states)
    city_state_civs = turn_stats[turn_stats['is_city_state'] == True]['civilization'].tolist()
    for i, civ in enumerate(city_state_civs):
        player_mapping[6 + i] = civ
    
    print(f"\n🗺️ Player mapping created:")
    for player_num in sorted(player_mapping.keys())[:10]:  # Show first 10
        civ_name = player_mapping[player_num]
        print(f"  Player {player_num:2d} → {civ_name}")
    
    # Map scores to civilizations
    turn_scores['civilization'] = turn_scores[' Player'].map(player_mapping)
    turn_scores_mapped = turn_scores.dropna(subset=['civilization'])
    
    print(f"\n📊 Successfully mapped {len(turn_scores_mapped)} score records")
    
    # Merge all data
    print(f"\n🔗 Merging all data sources...")
    
    # Start with stats data as base
    merged_data = turn_stats.copy()
    
    # Merge with stats2 data
    stats2_merge = turn_stats2[['civilization', ' BY TYPE: Tiles', ' Districts', 
                              ' Outgoing Trade Routes', ' TOURISM', ' BALANCE: Favor']].copy()
    merged_data = merged_data.merge(stats2_merge, on='civilization', how='left')
    
    # Merge with scores data  
    scores_merge = turn_scores_mapped[['civilization', ' Score', ' CATEGORY_CIVICS', 
                                     ' CATEGORY_EMPIRE', ' CATEGORY_GREAT_PEOPLE',
                                     ' CATEGORY_RELIGION', ' CATEGORY_TECH', 
                                     ' CATEGORY_WONDER', ' CATEGORY_TRADE']].copy()
    merged_data = merged_data.merge(scores_merge, on='civilization', how='left')
    
    print(f"✅ Merged data: {len(merged_data)} records")
    
    # Create final database format
    print(f"\n📋 Creating final database format...")
    
    db_data = []
    
    for _, row in merged_data.iterrows():
        record = {
            'game_turn': test_turn,
            'civilization': row['civilization'],
            'is_city_state': row['is_city_state'],
            
            # Core stats
            'num_cities': row[' Num Cities'],
            'population': row[' Population'], 
            'techs': row[' Techs'],
            'civics': row[' Civics'],
            'land_units': row[' Land Units'],
            'naval_units': row[' Naval Units'],
            'tiles_owned': row[' TILES: Owned'],
            'tiles_improved': row[' Improved'],
            
            # Economy
            'gold_balance': row[' BALANCE: Gold'],
            'faith_balance': row[' Faith'],
            'science_per_turn': row[' YIELDS: Science'],
            'culture_per_turn': row[' Culture'],
            'gold_per_turn': row[' Gold'],
            'faith_per_turn': row[' Faith.1'],
            'production_per_turn': row[' Production'],
            'food_per_turn': row[' Food'],
            
            # Advanced stats
            'tiles_controlled': row.get(' BY TYPE: Tiles', 0),
            'districts': row.get(' Districts', 0),
            'trade_routes': row.get(' Outgoing Trade Routes', 0),
            'tourism': row.get(' TOURISM', 0),
            'diplomatic_favor': row.get(' BALANCE: Favor', 0),
            
            # Scores
            'total_score': row.get(' Score', 0),
            'score_civics': row.get(' CATEGORY_CIVICS', 0),
            'score_empire': row.get(' CATEGORY_EMPIRE', 0),
            'score_great_people': row.get(' CATEGORY_GREAT_PEOPLE', 0),
            'score_religion': row.get(' CATEGORY_RELIGION', 0),
            'score_tech': row.get(' CATEGORY_TECH', 0),
            'score_wonder': row.get(' CATEGORY_WONDER', 0),
            'score_trade': row.get(' CATEGORY_TRADE', 0),
        }
        db_data.append(record)
    
    # Show sample records
    print(f"\n📋 SAMPLE DATABASE RECORDS (Turn {test_turn}):")
    print("-" * 80)
    
    # Show major civilizations only
    major_records = [r for r in db_data if not r['is_city_state']]
    
    for record in major_records[:3]:  # Show first 3 major civs
        civ = record['civilization']
        print(f"\n🏛️ {civ}:")
        print(f"  🏙️  Cities: {record['num_cities']}")
        print(f"  👥 Population: {record['population']}")
        print(f"  🔬 Science: {record['science_per_turn']}/turn")
        print(f"  🎭 Culture: {record['culture_per_turn']}/turn") 
        print(f"  💰 Gold: {record['gold_per_turn']}/turn")
        print(f"  🏆 Score: {record['total_score']}")
        print(f"  🗺️  Tiles: {record['tiles_controlled']}")
        print(f"  🎭 Tourism: {record['tourism']}")
    
    print(f"\n📊 TRANSFORMATION SUMMARY:")
    print(f"  📁 Total records: {len(db_data)}")
    print(f"  🏛️ Major civilizations: {len([r for r in db_data if not r['is_city_state']])}")
    print(f"  🏛️ City-states: {len([r for r in db_data if r['is_city_state']])}")
    
    print(f"\n✅ TRANSFORMATION COMPLETE")
    print(f"💡 Next: Create actual database table and insert this data")
    
    return db_data

if __name__ == "__main__":
    result = transform_complete_data()
