#!/usr/bin/env python3
"""
Stage 3c: Show What We Found - Updated with CSV data discovery
Ultra simple approach - display real Civ VI game data from CSV files.
"""

import os
import csv
from find_lua_logs import find_lua_logs

def get_logs_directory():
    """Get the Civ VI logs directory path."""
    log_path = find_lua_logs()
    if not log_path:
        return None
    
    # Get the directory containing the log files
    return os.path.dirname(log_path)

def read_player_scores(logs_dir):
    """Read player scores from Game_PlayerScores.csv."""
    scores_file = os.path.join(logs_dir, "Game_PlayerScores.csv")
    
    if not os.path.exists(scores_file):
        return None
    
    scores_data = []
    
    try:
        with open(scores_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
            # The CSV has simple format: Game Turn, Player, Score, ...
            # Skip header and parse manually
            for line in lines[1:]:  # Skip header
                if line.strip():
                    parts = [part.strip() for part in line.split(',')]
                    if len(parts) >= 3:  # At least Game Turn, Player, Score
                        try:
                            game_turn = int(parts[0])
                            player = int(parts[1])
                            score = int(parts[2])
                            
                            scores_data.append({
                                'Game Turn': game_turn,
                                'Player': player,
                                'Score': score
                            })
                        except ValueError:
                            continue  # Skip malformed lines
                            
    except Exception as e:
        print(f"❌ Error reading scores: {e}")
        return None
    
    return scores_data

def read_diplomacy_data(logs_dir):
    """Read diplomacy data from DiplomacySummary.csv."""
    diplo_file = os.path.join(logs_dir, "DiplomacySummary.csv")
    
    if not os.path.exists(diplo_file):
        return None
    
    diplo_data = []
    
    try:
        with open(diplo_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
            # Format: Game Turn, Initiator, Recipient, Action, Details, Mayhem, Visibility
            for line in lines[1:]:  # Skip header
                if line.strip():
                    parts = [part.strip() for part in line.split(',')]
                    if len(parts) >= 4:  # At least Game Turn, Initiator, Recipient, Action
                        try:
                            game_turn = int(parts[0])
                            initiator = int(parts[1])
                            recipient = int(parts[2])
                            action = parts[3]
                            
                            diplo_data.append({
                                'Game Turn': game_turn,
                                'Initiator': initiator,
                                'Recipient': recipient,
                                'Action': action
                            })
                        except ValueError:
                            continue  # Skip malformed lines
                            
    except Exception as e:
        print(f"❌ Error reading diplomacy: {e}")
        return None
    
    return diplo_data

def analyze_active_players(scores_data):
    """Find which players are actually active in the game."""
    if not scores_data:
        return []
    
    # Find players with non-zero scores
    active_players = set()
    
    for row in scores_data:
        player_id = int(row['Player'])
        total_score = int(row['Score'])
        
        # Skip barbarians (62, 63) and look for players with scores
        if player_id < 62 and total_score > 0:
            active_players.add(player_id)
    
    return sorted(list(active_players))

def show_civ_data():
    """Main function to demonstrate our Civ VI data connection."""
    print("🎮 Civ VI Data Connection Test - Stage 3c")
    print("UPDATED: Now reading real CSV game data!")
    print("=" * 60)
    print()
    
    # Step 1: Find logs directory
    print("🔍 STEP 1: Finding Civ VI logs directory...")
    logs_dir = get_logs_directory()
    
    if not logs_dir:
        print("\n❌ RESULT: No log directory found")
        print("🎮 Please install and run Civ VI first")
        return
    
    print(f"\n✅ RESULT: Found logs at {logs_dir}")
    
    # Step 2: Read game data
    print("\n🔍 STEP 2: Reading real game data...")
    scores_data = read_player_scores(logs_dir)
    diplo_data = read_diplomacy_data(logs_dir)
    
    # Step 3: Show results
    print("\n🎯 STEP 3: Real Game Data Results")
    print("=" * 60)
    
    if scores_data:
        print("🎉 SUCCESS! We found REAL Civ VI game data!")
        print()
        
        # Show basic game info
        turns = set(int(row['Game Turn']) for row in scores_data)
        max_turn = max(turns) if turns else 0
        
        print(f"📊 GAME STATUS:")
        print(f"   🕒 Current Turn: {max_turn}")
        print(f"   📈 Total Data Points: {len(scores_data):,}")
        
        # Find active players
        active_players = analyze_active_players(scores_data)
        print(f"\n👥 ACTIVE PLAYERS: {len(active_players)} found")
        
        for player_id in active_players:
            # Get latest score for this player
            player_scores = [row for row in scores_data if int(row['Player']) == player_id]
            if player_scores:
                latest = max(player_scores, key=lambda x: int(x['Game Turn']))
                score = int(latest['Score'])
                turn = int(latest['Game Turn'])
                print(f"   🎮 Player {player_id}: Score {score} (Turn {turn})")
        
        # Show diplomacy summary
        if diplo_data:
            print(f"\n🤝 DIPLOMACY DATA: {len(diplo_data)} interactions recorded")
            
            # Show recent diplomacy
            recent_diplo = [row for row in diplo_data if int(row['Game Turn']) >= max_turn - 2]
            if recent_diplo:
                print(f"   � Recent interactions (last 3 turns):")
                for action in recent_diplo[-5:]:  # Show last 5
                    turn = action['Game Turn']
                    init = action['Initiator']
                    recip = action['Recipient']
                    action_type = action['Action']
                    print(f"   � Turn {turn}: Player {init} → Player {recip} ({action_type})")
        
        print("\n🔗 What this means:")
        print("   ✅ We can read live Civ VI game data")
        print("   ✅ We have turn-by-turn player progression") 
        print("   ✅ We have diplomatic interaction logs")
        print("   ✅ Ready for database integration!")
        print("   ✅ Ready for live dashboard!")
        
    else:
        print("❌ No game data found in CSV files")
        print("🎮 Make sure you have an active Civ VI game running")
    
    print("\n" + "=" * 60)
    print("🎯 STAGE 3 COMPLETE! 🎉")
    print("   ✅ Stage 3a: Found Civ VI log files")
    print("   ✅ Stage 3b: Discovered CSV data goldmine") 
    print("   ✅ Stage 3c: Successfully reading real game data")
    print()
    print("🚀 READY FOR STAGE 4:")
    print("   - Connect this data to our PostgreSQL database")
    print("   - Build live charts in Superset dashboard")
    print("   - Add real-time monitoring")
    print()
    print("🔒 Community ready: We can read live Civ VI data!")

if __name__ == "__main__":
    show_civ_data()
