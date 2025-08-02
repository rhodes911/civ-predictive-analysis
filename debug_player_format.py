#!/usr/bin/env python3
"""
Debug the Player column format in CSV files
"""

import pandas as pd
import os
from pathlib import Path

def debug_player_format():
    """Debug the Player column to understand the format"""
    
    logs_dir = Path(os.path.expandvars(r"%LOCALAPPDATA%\Firaxis Games\Sid Meier's Civilization VI\Logs"))
    
    print("🔍 DEBUGGING PLAYER COLUMN FORMAT")
    print("=" * 50)
    
    # Load Player_Stats.csv
    stats_file = logs_dir / "Player_Stats.csv"
    if not stats_file.exists():
        print("❌ Player_Stats.csv not found")
        return
    
    df = pd.read_csv(stats_file)
    print(f"📊 Loaded {df.shape[0]} rows from Player_Stats.csv")
    
    # Check latest turn
    latest_turn = df['Game Turn'].max()
    print(f"🎯 Latest turn: {latest_turn}")
    
    # Get all unique Player values for latest turn
    latest_data = df[df['Game Turn'] == latest_turn]
    unique_players = latest_data[' Player'].unique()
    
    print(f"\n📋 Unique Player values for turn {latest_turn}:")
    for player in sorted(unique_players):
        player_type = type(player).__name__
        print(f"  '{player}' (type: {player_type})")
    
    # Check a few other recent turns
    print(f"\n📊 Player counts by turn (last 5 turns):")
    for turn in sorted(df['Game Turn'].unique(), reverse=True)[:5]:
        turn_data = df[df['Game Turn'] == turn]
        player_count = len(turn_data[' Player'].unique())
        print(f"  Turn {turn}: {player_count} unique players")
        
        # Show first few players for this turn
        sample_players = list(turn_data[' Player'].unique())[:10]
        print(f"    Sample players: {sample_players}")
    
    # Look specifically for civilization names
    print(f"\n🏛️ Looking for civilization names...")
    civ_players = latest_data[latest_data[' Player'].str.contains('CIVILIZATION', na=False)]
    print(f"Found {len(civ_players)} civilization records in latest turn")
    
    if len(civ_players) > 0:
        print("Civilization names found:")
        for civ in civ_players[' Player'].unique():
            print(f"  {civ}")

if __name__ == "__main__":
    debug_player_format()
