#!/usr/bin/env python3
"""
Stage 4f: Investigate Data Precision Issues (Fixed)
Check actual column names first, then precision
"""

import pandas as pd
import os
from pathlib import Path

def investigate_precision():
    """Check data precision in CSV files vs game display"""
    
    # Find the Civ VI logs directory
    logs_dir = Path(os.path.expandvars(r"%LOCALAPPDATA%\Firaxis Games\Sid Meier's Civilization VI\Logs"))
    
    if not logs_dir.exists():
        print(f"❌ Logs directory not found: {logs_dir}")
        return
    
    print(f"🔍 Investigating data precision in: {logs_dir}")
    print("=" * 60)
    
    # Check each CSV file
    csv_files = ["Player_Stats.csv", "Player_Stats_2.csv", "Game_PlayerScores.csv"]
    
    for csv_name in csv_files:
        csv_file = logs_dir / csv_name
        if not csv_file.exists():
            print(f"❌ {csv_name} not found")
            continue
            
        print(f"\n📊 {csv_name.upper()} ANALYSIS")
        print("=" * 50)
        
        try:
            df = pd.read_csv(csv_file)
            print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
            
            # Show column names
            print(f"\nColumns: {list(df.columns)}")
            
            # Show data types
            print(f"\nData types:")
            for col, dtype in df.dtypes.items():
                print(f"  {col}: {dtype}")
            
            # Show sample data from latest records
            print(f"\nSample data (last 3 rows):")
            print(df.tail(3).to_string())
            
            # Check for decimal values
            print(f"\nPRECISION CHECK:")
            print("-" * 30)
            
            numeric_cols = df.select_dtypes(include=['float64', 'int64', 'float32', 'int32']).columns
            
            for col in numeric_cols:
                # Get some sample values
                sample_vals = df[col].dropna().tail(5).tolist()
                
                # Check if any values have decimal parts
                has_decimals = False
                decimal_examples = []
                
                for val in sample_vals:
                    if pd.notna(val) and val != int(val):
                        has_decimals = True
                        decimal_examples.append(val)
                
                precision_status = "HAS DECIMALS" if has_decimals else "INTEGER ONLY"
                print(f"  {col}: {precision_status}")
                
                if decimal_examples:
                    print(f"    Examples: {decimal_examples[:3]}")
                elif sample_vals:
                    print(f"    Examples: {sample_vals[:3]}")
            
        except Exception as e:
            print(f"❌ Error reading {csv_name}: {e}")
    
    # Now let's specifically look for Science and Culture values
    print(f"\n🎯 SCIENCE & CULTURE PRECISION FOCUS")
    print("=" * 50)
    
    for csv_name in csv_files:
        csv_file = logs_dir / csv_name
        if not csv_file.exists():
            continue
            
        try:
            df = pd.read_csv(csv_file)
            
            # Look for Science and Culture columns
            science_cols = [col for col in df.columns if 'science' in col.lower()]
            culture_cols = [col for col in df.columns if 'culture' in col.lower()]
            
            if science_cols or culture_cols:
                print(f"\n📁 {csv_name}:")
                
                for col in science_cols + culture_cols:
                    latest_values = df[col].dropna().tail(10).tolist()
                    has_decimals = any(val != int(val) for val in latest_values if pd.notna(val))
                    
                    print(f"  {col}: {latest_values[-3:]} [{'DECIMAL' if has_decimals else 'INTEGER'}]")
                    
                    # If you mentioned 4.5 in game but we see 4, let's check
                    if not has_decimals and any(val == 4 for val in latest_values):
                        print(f"    ⚠️  Found integer 4 - this might be your 4.5 rounded down!")
                        
        except Exception as e:
            print(f"❌ Error checking {csv_name}: {e}")
    
    print(f"\n💡 FINDINGS & SOLUTIONS:")
    print("=" * 40)
    print("If CSV shows integers but game shows decimals:")
    print("1. CSV files contain ROUNDED/TRUNCATED values")
    print("2. Game UI calculates precise values in real-time")
    print("3. Options:")
    print("   a) Accept CSV precision (still useful for trends)")
    print("   b) Look for save files (.Civ6Save) with full precision")
    print("   c) Parse game memory for exact values (advanced)")
    print("   d) Note precision limitations in dashboard")
if __name__ == "__main__":
    investigate_precision()
