#!/usr/bin/env python3
"""
Stage 4a: Database Schema Design - Analyze Real Data Structure

This script examines our CSV data to understand exactly what we need 
to store in the database for the dashboard.

Baby Steps Approach:
1. Load the CSV files
2. Examine column names and data types
3. Identify key fields for dashboard
4. Design database schema
5. Test with sample data
"""

import pandas as pd
import os
from pathlib import Path

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

def analyze_data_structure():
    """Analyze the structure of our Civ VI data files"""
    log_dir = find_civ_log_directory()
    if not log_dir:
        print("❌ Could not find Civ VI logs directory!")
        return None
    
    print("🔍 STAGE 4A: DATABASE SCHEMA ANALYSIS")
    print("="*60)
    print(f"📁 Data source: {log_dir}")
    
    # Analyze Player_Stats.csv (main stats)
    print("\n📊 ANALYZING Player_Stats.csv:")
    print("-" * 40)
    
    stats_file = os.path.join(log_dir, "Player_Stats.csv")
    if os.path.exists(stats_file):
        df_stats = pd.read_csv(stats_file)
        print(f"✅ File loaded: {len(df_stats)} records")
        print(f"📅 Turn range: {df_stats['Game Turn'].min()} to {df_stats['Game Turn'].max()}")
        
        print("\n🏛️ Column structure:")
        for i, col in enumerate(df_stats.columns):
            dtype = df_stats[col].dtype
            sample_val = df_stats[col].iloc[0] if len(df_stats) > 0 else "N/A"
            print(f"  {i+1:2d}. '{col}' ({dtype}) - Sample: {sample_val}")
        
        print("\n🌍 Civilizations found:")
        civs = df_stats[' Player'].unique()
        for i, civ in enumerate(civs):
            print(f"  {i:2d}. {civ}")
        
        # Show sample record
        print("\n📋 Sample record (latest turn):")
        latest_turn = df_stats['Game Turn'].max()
        sample = df_stats[df_stats['Game Turn'] == latest_turn].iloc[0]
        for col in df_stats.columns:
            print(f"  {col}: {sample[col]}")
            if col == ' Civics':  # Stop after first few for readability
                break
    
    # Analyze Player_Stats_2.csv (advanced stats)
    print("\n\n📊 ANALYZING Player_Stats_2.csv:")
    print("-" * 40)
    
    stats2_file = os.path.join(log_dir, "Player_Stats_2.csv")
    if os.path.exists(stats2_file):
        df_stats2 = pd.read_csv(stats2_file)
        print(f"✅ File loaded: {len(df_stats2)} records")
        
        print("\n🏛️ Column structure:")
        for i, col in enumerate(df_stats2.columns):
            dtype = df_stats2[col].dtype
            sample_val = df_stats2[col].iloc[0] if len(df_stats2) > 0 else "N/A"
            print(f"  {i+1:2d}. '{col}' ({dtype}) - Sample: {sample_val}")
    
    # Analyze Game_PlayerScores.csv (scores)
    print("\n\n📊 ANALYZING Game_PlayerScores.csv:")
    print("-" * 40)
    
    scores_file = os.path.join(log_dir, "Game_PlayerScores.csv")
    if os.path.exists(scores_file):
        df_scores = pd.read_csv(scores_file)
        print(f"✅ File loaded: {len(df_scores)} records")
        
        print("\n🏛️ Column structure:")
        for i, col in enumerate(df_scores.columns):
            dtype = df_scores[col].dtype
            sample_val = df_scores[col].iloc[0] if len(df_scores) > 0 else "N/A"
            print(f"  {i+1:2d}. '{col}' ({dtype}) - Sample: {sample_val}")
    
    print("\n" + "="*60)
    print("🎯 ANALYSIS COMPLETE")
    print("💡 Next: Design database schema based on this structure")

if __name__ == "__main__":
    analyze_data_structure()
