#!/usr/bin/env python3
"""
Stage 4h: Insert Real Civ VI Data
Load data from CSV files and insert into PostgreSQL database
"""

import pandas as pd
import psycopg2
import os
from pathlib import Path
import sys
import numpy as np

def insert_civ_data():
    """Insert real Civ VI data from CSV files into database"""
    
    print("💾 STAGE 4H: Inserting Real Civ VI Data")
    print("=" * 50)
    
    # Find the Civ VI logs directory
    # Check if running in Docker container first
    docker_logs_dir = Path("/civ6-logs")
    if docker_logs_dir.exists():
        logs_dir = docker_logs_dir
        print(f"📦 Running in Docker - using mounted logs directory")
    else:
        # Running locally - use Windows path
        logs_dir = Path(os.path.expandvars(r"%LOCALAPPDATA%\Firaxis Games\Sid Meier's Civilization VI\Logs"))
        print(f"💻 Running locally - using Windows logs directory")
    
    if not logs_dir.exists():
        print(f"❌ Logs directory not found: {logs_dir}")
        return False
    
    print(f"📂 Reading data from: {logs_dir}")
    
    # Database connection settings
    # Use Docker service name if running in container, localhost if running locally
    db_host = 'postgres' if docker_logs_dir.exists() else 'localhost'
    db_config = {
        'host': db_host,
        'port': 5432,
        'database': 'civ6_analytics',
        'user': 'civ6_user',
        'password': 'civ6_password'
    }
    
    try:
        # Load CSV files
        print("📊 Loading CSV files...")
        
        csv_files = {
            'stats': logs_dir / "Player_Stats.csv",
            'stats2': logs_dir / "Player_Stats_2.csv", 
            'scores': logs_dir / "Game_PlayerScores.csv"
        }
        
        dataframes = {}
        for name, file_path in csv_files.items():
            if file_path.exists():
                df = pd.read_csv(file_path)
                dataframes[name] = df
                print(f"  ✅ {name}: {df.shape[0]} rows, {df.shape[1]} columns")
            else:
                print(f"  ❌ {name}: File not found")
                return False
        
        # Define the major civilizations (the main players, not city-states)
        # This includes civilizations from all game sessions
        major_civilizations = {
            # First game
            " CIVILIZATION_NETHERLANDS", 
            " CIVILIZATION_ROME", 
            " CIVILIZATION_CHINA",
            " CIVILIZATION_ENGLAND",
            " CIVILIZATION_CANADA",
            " CIVILIZATION_INDONESIA",
            " CIVILIZATION_ETHIOPIA",
            " CIVILIZATION_CREE",        # Appears in multiple games
            " CIVILIZATION_OTTOMAN",
            # Second game
            " CIVILIZATION_GAUL",        
            " CIVILIZATION_MALI",        
            " CIVILIZATION_GRAN_COLOMBIA",
            " CIVILIZATION_JAPAN",       
            " CIVILIZATION_MAORI",       # Appears in multiple games
            " CIVILIZATION_MAYA",
            # Third game
            " CIVILIZATION_AUSTRALIA",
            " CIVILIZATION_BABYLON",
            " CIVILIZATION_MACEDON",
            " CIVILIZATION_POLAND",
            " CIVILIZATION_SCYTHIA"
        }
        
        # Find the latest complete turn (same logic as stage4d/4e)
        stats_df = dataframes['stats']
        
        # Find ALL turns with data (any number of major civilizations)
        print("🔍 Finding all turns with civilization data...")
        
        complete_turns = []
        for turn in sorted(stats_df['Game Turn'].unique()):
            turn_data = stats_df[stats_df['Game Turn'] == turn]
            turn_civs = set(turn_data[' Player'].unique())
            major_civ_count = len(turn_civs.intersection(major_civilizations))
            
            print(f"  Turn {turn}: {major_civ_count} major civilizations, {len(turn_civs)} total")
            
            # Accept turns with ANY number of major civs (flexible for different games)
            if major_civ_count >= 1:  # At least 1 major civ present
                complete_turns.append(turn)
        
        if not complete_turns:
            print("❌ No turn data found with major civilizations")
            return False
        
        print(f"✅ Found {len(complete_turns)} complete turns: {complete_turns}")
        latest_turn = max(complete_turns)
        
        # Process and merge data for ALL complete turns
        print("🔄 Processing and merging data for all complete turns...")
        
        # Connect to database
        print("📡 Connecting to database...")
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()
        
        # Check what historical data we already have and what civs are in current logs
        print("📊 Checking existing historical data...")
        cursor.execute("SELECT DISTINCT game_turn FROM civ_game_data ORDER BY game_turn")
        existing_turns = [row[0] for row in cursor.fetchall()]
        
        cursor.execute("SELECT DISTINCT civilization FROM civ_game_data ORDER BY civilization")
        existing_civs = set([row[0] for row in cursor.fetchall()])
        
        # Get civilizations from current logs
        current_civs = set()
        for turn in complete_turns:
            turn_data = stats_df[stats_df['Game Turn'] == turn]
            turn_civs = set(turn_data[' Player'].str.strip().unique())
            # Add ALL civilizations that appear in the logs, not just major ones
            current_civs.update(turn_civs)
        
        # Filter to only major civilizations for comparison
        current_major_civs = current_civs.intersection(major_civilizations)
        
        print(f"   📈 Existing turns in database: {existing_turns}")
        print(f"   🏛️ Existing civilizations: {sorted(existing_civs)}")
        print(f"   🆕 Current log civilizations (all): {sorted(current_civs)}")
        print(f"   🎯 Current major civilizations: {sorted(current_major_civs)}")
        
        # Check if this is a different game session
        is_different_game = len(current_major_civs.intersection(existing_civs)) == 0
        
        if is_different_game and existing_civs:
            print("🎮 Detected DIFFERENT GAME SESSION!")
            print("   This appears to be a new game with different civilizations.")
            print("   Both games will be preserved in the database.")
        elif existing_civs:
            print("🔄 Detected SAME GAME SESSION (continuing previous game)")
        else:
            print("🆕 First game session in database")
        
        # Determine which turns to process
        turns_to_process = []
        
        if is_different_game:
            # Different game - we can insert all turns regardless of existing turn numbers
            turns_to_process = complete_turns
            print("🎯 Different game detected - will insert all available turns")
            
            # However, we need to handle civilization overlaps (like GAUL appearing in both games)
            print("⚠️  Checking for civilization overlaps between games...")
            overlapping_civs = current_civs.intersection(existing_civs)
            if overlapping_civs:
                print(f"🔄 Found overlapping civilizations: {sorted(overlapping_civs)}")
                print("   Will delete conflicting old data and insert fresh data")
                
                # Delete old data for overlapping civilizations in conflicting turns
                for civ in overlapping_civs:
                    for turn in turns_to_process:
                        if turn in existing_turns:
                            cursor.execute(
                                "DELETE FROM civ_game_data WHERE game_turn = %s AND civilization = %s",
                                (int(turn), civ)
                            )
                            print(f"   🗑️ Removed old data for {civ} turn {turn}")
                conn.commit()
            else:
                print("✅ No civilization overlaps - can insert safely")
        else:
            # Same game - only insert new turns
            for turn in complete_turns:
                if turn not in existing_turns:
                    turns_to_process.append(turn)
        
        if not turns_to_process:
            print("✅ All complete turns already in database!")
            print(f"   Existing: {existing_turns}")
            print(f"   Available: {complete_turns}")
            return True
        
        print(f"🎯 Will process {len(turns_to_process)} new turns: {turns_to_process}")
        
        # Prepare insert statement
        insert_sql = """
        INSERT INTO civ_game_data (
            game_turn, civilization, player_number,
            num_cities, population, techs, civics,
            land_units, corps, armies, naval_units,
            tiles_owned, tiles_improved,
            balance_gold, balance_faith,
            yields_science, yields_culture, yields_gold, yields_faith, yields_production, yields_food,
            buildings, districts, outgoing_trade_routes, tourism,
            diplo_victory, balance_favor, lifetime_favor, co2_per_turn,
            total_score
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        )
        """
        
        total_inserted = 0
        
        # Process each complete turn
        for current_turn in turns_to_process:
            print(f"\n📊 Processing Turn {current_turn}...")
            
            # Filter data for this specific turn and major civs only
            turn_stats = stats_df[stats_df['Game Turn'] == current_turn]
            turn_stats2 = dataframes['stats2'][dataframes['stats2']['Game Turn'] == current_turn]
            turn_scores = dataframes['scores'][dataframes['scores']['Game Turn'] == current_turn]
            
            # Filter for major civilizations only
            major_civs_stats = turn_stats[turn_stats[' Player'].isin(major_civilizations)]
            major_civs_stats2 = turn_stats2[turn_stats2[' Player'].isin(major_civilizations)]
            
            # For scores, we need to map civilization names to player numbers
            # Create a mapping based on the civilizations ACTUALLY IN THIS TURN, not all major civs
            current_turn_civs = sorted(major_civs_stats[' Player'].unique())
            civ_to_player = {}
            for i, civ in enumerate(current_turn_civs):
                civ_to_player[civ] = i
            
            print(f"  🎯 Turn {current_turn} civ-to-player mapping:")
            for civ, player_num in civ_to_player.items():
                print(f"    {civ} → Player {player_num}")
            
            # Filter scores using the actual number of players in this turn
            max_players = len(current_turn_civs)
            major_civs_scores = turn_scores[turn_scores[' Player'].isin(range(max_players))]
            
            print(f"  Stats: {len(major_civs_stats)} records")
            print(f"  Stats2: {len(major_civs_stats2)} records") 
            print(f"  Scores: {len(major_civs_scores)} records")
        
            # Process each major civilization for this turn
            turn_inserted = 0
            for _, stats_row in major_civs_stats.iterrows():
                civilization_name = stats_row[' Player'].strip()  # Remove leading space
                player_num = civ_to_player.get(stats_row[' Player'], 999)  # Get mapped player number
                
                # Find corresponding records in other files
                stats2_row = major_civs_stats2[major_civs_stats2[' Player'] == stats_row[' Player']]
                scores_row = major_civs_scores[major_civs_scores[' Player'] == player_num]
                
                # Helper function to safely convert values
                def safe_int(value, default=0):
                    try:
                        if pd.isna(value):
                            return default
                        return int(float(value))
                    except (ValueError, TypeError):
                        return default
                
                # Extract data with proper column names (handling spaces)
                # Convert all values to Python native types
                data = [
                    safe_int(current_turn),
                    str(civilization_name),
                    safe_int(player_num),
                    safe_int(stats_row.get(' Num Cities', 0)),
                    safe_int(stats_row.get(' Population', 0)),
                    safe_int(stats_row.get(' Techs', 0)),
                    safe_int(stats_row.get(' Civics', 0)),
                    safe_int(stats_row.get(' Land Units', 0)),
                    safe_int(stats_row.get(' corps', 0)),
                    safe_int(stats_row.get(' Armies', 0)),
                    safe_int(stats_row.get(' Naval Units', 0)),
                    safe_int(stats_row.get(' TILES: Owned', 0)),
                    safe_int(stats_row.get(' Improved', 0)),
                    safe_int(stats_row.get(' BALANCE: Gold', 0)),
                    safe_int(stats_row.get(' Faith', 0)),
                    safe_int(stats_row.get(' YIELDS: Science', 0)),
                    safe_int(stats_row.get(' Culture', 0)),
                    safe_int(stats_row.get(' Gold', 0)),
                    safe_int(stats_row.get(' Faith.1', 0)),
                    safe_int(stats_row.get(' Production', 0)),
                    safe_int(stats_row.get(' Food', 0)),
                    safe_int(stats2_row.iloc[0].get(' Buildings', 0)) if len(stats2_row) > 0 else 0,
                    safe_int(stats2_row.iloc[0].get(' Districts', 0)) if len(stats2_row) > 0 else 0,
                    safe_int(stats2_row.iloc[0].get(' Outgoing Trade Routes', 0)) if len(stats2_row) > 0 else 0,
                    safe_int(stats2_row.iloc[0].get(' TOURISM', 0)) if len(stats2_row) > 0 else 0,
                    safe_int(stats2_row.iloc[0].get(' Diplo Victory', 0)) if len(stats2_row) > 0 else 0,
                    safe_int(stats2_row.iloc[0].get(' BALANCE: Favor', 0)) if len(stats2_row) > 0 else 0,
                    safe_int(stats2_row.iloc[0].get(' LIFETIME: Favor', 0)) if len(stats2_row) > 0 else 0,
                    safe_int(stats2_row.iloc[0].get(' CO2 Per Turn', 0)) if len(stats2_row) > 0 else 0,
                    safe_int(scores_row.iloc[0].get(' Score', 0)) if len(scores_row) > 0 else 0
                ]
                
                cursor.execute(insert_sql, data)
                turn_inserted += 1
                total_inserted += 1
                
                print(f"    ✅ {civilization_name}: Science={data[15]}, Culture={data[16]}, Score={data[29]}")
            
            print(f"  ✅ Turn {current_turn}: Inserted {turn_inserted} civilizations")
        
        # Commit the transaction
        conn.commit()
        
        print(f"\n🎉 DATA INSERTION COMPLETE!")
        print("=" * 40)
        print(f"✅ Inserted: {total_inserted} civilizations across {len(turns_to_process)} turns")
        print(f"✅ Turns processed: {turns_to_process}")
        print("⚠️  Note: Science/Culture values are rounded integers from CSV")
        
        # Verify the insertion by showing latest turn
        print(f"\n🔍 Verifying latest turn data (Turn {latest_turn})...")
        cursor.execute("""
            SELECT game_turn, civilization, yields_science, yields_culture, total_score 
            FROM civ_game_data 
            WHERE game_turn = %s 
            ORDER BY total_score DESC
        """, (int(latest_turn),))
        
        results = cursor.fetchall()
        print(f"📊 Database contains {len(results)} records for turn {latest_turn}:")
        
        for turn, civ, science, culture, score in results:
            civ_short = civ.replace('CIVILIZATION_', '')
            print(f"  {civ_short}: Science={science}, Culture={culture}, Score={score}")
        
        # Show total historical data
        print("\n📈 Complete historical data summary:")
        cursor.execute("""
            SELECT game_turn, COUNT(*) as civ_count
            FROM civ_game_data 
            GROUP BY game_turn 
            ORDER BY game_turn
        """)
        
        historical_data = cursor.fetchall()
        print(f"   Total turns in database: {len(historical_data)}")
        for turn, count in historical_data:
            print(f"   Turn {turn}: {count} civilizations")
        
        print(f"\n🎯 PERFECT FOR RACE ANALYSIS!")
        print("📊 Superset can now show progression over time:")
        print("   • Who's rising/falling in rankings")
        print("   • Science/Culture/Score trends by civilization")
        print("   • Turn-by-turn position changes")
        print("🌐 Dashboard URL: http://localhost:8088 (admin/admin)")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
        
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()
    
    return True

if __name__ == "__main__":
    success = insert_civ_data()
    if not success:
        sys.exit(1)
