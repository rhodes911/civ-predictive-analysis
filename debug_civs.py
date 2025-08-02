#!/usr/bin/env python3
"""
Debug script to see why we're only getting one civilization
"""

import pandas as pd
import os

def debug_civ_data():
    log_dir = r"C:\Users\rhode\AppData\Local\Firaxis Games\Sid Meier's Civilization VI\Logs"
    stats_file = os.path.join(log_dir, "Player_Stats.csv")
    
    print("🔍 DEBUGGING CIVILIZATION DATA")
    print("=" * 50)
    
    df = pd.read_csv(stats_file)
    
    print(f"📊 Total records in file: {len(df)}")
    print(f"📅 Turns available: {df['Game Turn'].min()} to {df['Game Turn'].max()}")
    
    print("\n🌍 All civilizations in the data:")
    all_civs = df[' Player'].unique()
    for i, civ in enumerate(all_civs):
        print(f"  {i}: {civ}")
    
    current_turn = df['Game Turn'].max()
    print(f"\n📅 Current turn: {current_turn}")
    
    current_data = df[df['Game Turn'] == current_turn]
    print(f"📊 Records for current turn: {len(current_data)}")
    
    print("\n🎯 Civilizations with data on current turn:")
    current_civs = current_data[' Player'].unique()
    for civ in current_civs:
        print(f"  • {civ}")
    
    # Check our filtering logic
    known_major_civs = [
        'CIVILIZATION_NETHERLANDS', 'CIVILIZATION_ROME', 'CIVILIZATION_CHINA',
        'CIVILIZATION_ENGLAND', 'CIVILIZATION_CANADA', 'CIVILIZATION_GAUL'
    ]
    
    major_civs_found = [civ for civ in current_civs if civ in known_major_civs]
    print(f"\n🏛️ Major civilizations found: {len(major_civs_found)}")
    for civ in major_civs_found:
        print(f"  ✅ {civ}")
    
    missing_civs = [civ for civ in known_major_civs if civ not in current_civs]
    if missing_civs:
        print(f"\n❌ Expected but missing civilizations:")
        for civ in missing_civs:
            print(f"  • {civ}")
    
    # Check if they exist in earlier turns
    print(f"\n🔍 Checking if missing civs exist in ANY turn:")
    for missing_civ in missing_civs:
        civ_data = df[df[' Player'] == missing_civ]
        if len(civ_data) > 0:
            turns = civ_data['Game Turn'].unique()
            print(f"  • {missing_civ}: Found in turns {sorted(turns)}")
        else:
            print(f"  • {missing_civ}: NOT found in any turn")

if __name__ == "__main__":
    debug_civ_data()
