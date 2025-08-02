#!/usr/bin/env python3
import pandas as pd
from pathlib import Path

# Check the actual score mapping
logs_dir = Path(r"C:\Users\rhode\AppData\Local\Firaxis Games\Sid Meier's Civilization VI\Logs")
scores_file = logs_dir / "Game_PlayerScores.csv"
stats_file = logs_dir / "Player_Stats.csv"

print("🔍 INVESTIGATING SCORE MAPPING")
print("=" * 40)

if scores_file.exists() and stats_file.exists():
    # Read both files
    scores_df = pd.read_csv(scores_file)
    stats_df = pd.read_csv(stats_file)
    
    print("📊 Game_PlayerScores.csv structure:")
    print(f"  Columns: {list(scores_df.columns)}")
    print(f"  Shape: {scores_df.shape}")
    
    # Show latest turn scores
    latest_turn = max(scores_df['Game Turn'].unique())
    latest_scores = scores_df[scores_df['Game Turn'] == latest_turn]
    
    print(f"\n🎯 Latest turn ({latest_turn}) scores:")
    for _, row in latest_scores.iterrows():
        player_num = row[' Player']
        score = row[' Score']
        print(f"  Player {player_num}: Score = {score}")
    
    # Show civilizations in stats for same turn
    latest_stats = stats_df[stats_df['Game Turn'] == latest_turn]
    print(f"\n🏛️ Civilizations in turn {latest_turn}:")
    for _, row in latest_stats.iterrows():
        civ = row[' Player']
        print(f"  - {repr(civ)}")
    
    # Show current alphabetical mapping
    major_civs = [' CIVILIZATION_AUSTRALIA', ' CIVILIZATION_BABYLON', ' CIVILIZATION_CREE', 
                  ' CIVILIZATION_MACEDON', ' CIVILIZATION_MAORI', ' CIVILIZATION_POLAND', 
                  ' CIVILIZATION_SCYTHIA']
    
    print(f"\n🔤 Current alphabetical mapping:")
    for i, civ in enumerate(sorted(major_civs)):
        print(f"  Player {i}: {civ}")
        
    print(f"\n❓ Poland is mapped to player {sorted(major_civs).index(' CIVILIZATION_POLAND')}")
    poland_player_num = sorted(major_civs).index(' CIVILIZATION_POLAND')
    poland_score = latest_scores[latest_scores[' Player'] == poland_player_num]
    if not poland_score.empty:
        actual_score = poland_score.iloc[0][' Score']
        print(f"   According to mapping, Poland should have score: {actual_score}")
    else:
        print(f"   No score found for player {poland_player_num}")
        
else:
    print("❌ CSV files not found")
