#!/usr/bin/env python3
import pandas as pd
from pathlib import Path

# Use the correct path
logs_dir = Path(r"C:\Users\rhode\AppData\Local\Firaxis Games\Sid Meier's Civilization VI\Logs")
stats_file = logs_dir / "Player_Stats.csv"

print(f"📂 Reading from: {stats_file}")
print(f"File exists: {stats_file.exists()}")

if stats_file.exists():
    df = pd.read_csv(stats_file)
    print(f"\nPlayer_Stats.csv: {df.shape[0]} rows, {df.shape[1]} columns")
    
    if ' Player' in df.columns:
        civs = df[' Player'].unique()
        print(f"\n🏛️ All civilizations in logs ({len(civs)} total):")
        for civ in sorted(civs):
            print(f"  - {repr(civ)}")
        
        # Show latest turn
        latest_turn = max(df['Game Turn'].unique())
        latest_data = df[df['Game Turn'] == latest_turn]
        latest_civs = set(latest_data[' Player'].unique())
        print(f"\n📊 Latest turn ({latest_turn}): {len(latest_civs)} civilizations")
        for civ in sorted(latest_civs):
            print(f"  - {repr(civ)}")
    else:
        print("\nColumn ' Player' not found. Available columns:")
        for col in df.columns:
            print(f"  - {repr(col)}")
else:
    print("❌ Player_Stats.csv not found")
