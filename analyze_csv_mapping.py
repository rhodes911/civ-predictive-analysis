#!/usr/bin/env python3
"""
CSV Analysis Tool - Examine Civ VI CSV files to understand player mapping
"""

import pandas as pd
import os
from pathlib import Path

def analyze_csv_files():
    """Analyze the CSV files to understand player ID mapping"""
    
    print("🔍 CSV MAPPING ANALYSIS")
    print("=" * 50)
    
    # Find the Civ VI logs directory
    logs_dir = Path(os.path.expandvars(r"%LOCALAPPDATA%\Firaxis Games\Sid Meier's Civilization VI\Logs"))
    
    if not logs_dir.exists():
        print(f"❌ Logs directory not found: {logs_dir}")
        return False
    
    print(f"📂 Reading data from: {logs_dir}")
    
    # List all CSV files
    print("\n📋 Available CSV files:")
    csv_files = list(logs_dir.glob("*.csv"))
    for csv_file in csv_files:
        print(f"  📄 {csv_file.name}")
    
    # Load the main CSV files we know about
    main_files = {
        'stats': logs_dir / "Player_Stats.csv",
        'stats2': logs_dir / "Player_Stats_2.csv", 
        'scores': logs_dir / "Game_PlayerScores.csv"
    }
    
    dataframes = {}
    for name, file_path in main_files.items():
        if file_path.exists():
            df = pd.read_csv(file_path)
            dataframes[name] = df
            print(f"\n✅ Loaded {name}: {df.shape[0]} rows, {df.shape[1]} columns")
        else:
            print(f"\n❌ {name}: File not found")
    
    if not dataframes:
        print("❌ No CSV files could be loaded")
        return False
    
    # Analyze the first few turns to understand the structure
    print("\n" + "="*60)
    print("📊 ANALYZING TURN 1 DATA")
    print("="*60)
    
    for name, df in dataframes.items():
        print(f"\n🔍 {name.upper()} FILE ANALYSIS:")
        
        # Show columns
        print(f"  📋 Columns: {list(df.columns)}")
        
        # Filter to turn 1 if Game Turn column exists
        if 'Game Turn' in df.columns:
            turn1_data = df[df['Game Turn'] == 1]
            print(f"  📈 Turn 1 records: {len(turn1_data)}")
            
            # Show first few rows of turn 1
            print(f"  📄 Turn 1 sample data:")
            for idx, row in turn1_data.head(10).iterrows():
                if ' Player' in row:
                    player_col = row[' Player'] if pd.notna(row[' Player']) else 'N/A'
                    print(f"    Row {idx}: Player = {player_col}")
                else:
                    print(f"    Row {idx}: {dict(row)}")
        else:
            # Show first few rows if no Game Turn column
            print(f"  📄 Sample data (first 5 rows):")
            for idx, row in df.head(5).iterrows():
                print(f"    Row {idx}: {dict(row)}")
    
    # Look specifically at the score mapping issue
    if 'stats' in dataframes and 'scores' in dataframes:
        print("\n" + "="*60)
        print("🎯 PLAYER ID MAPPING ANALYSIS")
        print("="*60)
        
        stats_df = dataframes['stats']
        scores_df = dataframes['scores']
        
        # Get turn 1 data
        if 'Game Turn' in stats_df.columns and 'Game Turn' in scores_df.columns:
            turn1_stats = stats_df[stats_df['Game Turn'] == 1]
            turn1_scores = scores_df[scores_df['Game Turn'] == 1]
            
            print(f"\n📊 Turn 1 Stats - Civilizations found:")
            if ' Player' in turn1_stats.columns:
                civs = turn1_stats[' Player'].tolist()
                for i, civ in enumerate(civs):
                    print(f"  Stats Row {i}: {civ}")
            
            print(f"\n📊 Turn 1 Scores - Player IDs found:")
            if ' Player' in turn1_scores.columns:
                players = turn1_scores[' Player'].tolist()
                scores = turn1_scores[' Score'].tolist() if ' Score' in turn1_scores.columns else ['N/A'] * len(players)
                for player, score in zip(players, scores):
                    print(f"  Player {player}: Score = {score}")
            
            # Try to correlate them
            print(f"\n🔗 CORRELATION ATTEMPT:")
            print("Current script assumes:")
            if ' Player' in turn1_stats.columns:
                sorted_civs = sorted(turn1_stats[' Player'].unique())
                for i, civ in enumerate(sorted_civs):
                    print(f"  {civ} → Player {i}")
            
            print("\nBut actual Player IDs in scores file might be different!")
    
    # Look for other CSV files that might help with mapping
    print("\n" + "="*60)
    print("🔍 SEARCHING FOR ADDITIONAL MAPPING FILES")
    print("="*60)
    
    other_csvs = [f for f in csv_files if f.name not in ['Player_Stats.csv', 'Player_Stats_2.csv', 'Game_PlayerScores.csv']]
    
    for csv_file in other_csvs:
        print(f"\n📄 Examining {csv_file.name}:")
        try:
            df = pd.read_csv(csv_file)
            print(f"  📏 Shape: {df.shape}")
            print(f"  📋 Columns: {list(df.columns)}")
            
            # Look for player/civilization mapping clues
            if any('player' in col.lower() for col in df.columns):
                print(f"  🎯 Has player-related columns!")
                # Show first few rows
                print(f"  📄 Sample data:")
                for idx, row in df.head(3).iterrows():
                    print(f"    {dict(row)}")
            
        except Exception as e:
            print(f"  ❌ Error reading {csv_file.name}: {e}")
    
    print(f"\n🎯 RECOMMENDATIONS:")
    print("1. Check if there's a separate civilization mapping file")
    print("2. Look at the actual Player IDs in Game_PlayerScores.csv")
    print("3. Compare with victory screen to verify correct mapping")
    print("4. Consider using a different approach to match civilizations to scores")

if __name__ == "__main__":
    analyze_csv_files()
