#!/usr/bin/env python3
"""
Enhanced leader detection - try to find civilization/leader names
by examining all available log sources and making educated guesses.
"""

import os
import re
from find_lua_logs import find_lua_logs

def get_logs_directory():
    """Get the Civ VI logs directory path."""
    log_path = find_lua_logs()
    if not log_path:
        return None
    return os.path.dirname(log_path)

def search_all_logs_for_leaders(logs_dir):
    """Search through all log files for any leader or civilization references."""
    leader_clues = {}
    
    # Common leader names to search for
    known_leaders = [
        'Gandhi', 'Cleopatra', 'Caesar', 'Washington', 'Victoria', 
        'Peter', 'Catherine', 'Frederick', 'Montezuma', 'Gilgamesh',
        'Qin', 'Trajan', 'Pericles', 'Saladin', 'Mvemba', 'Hojo',
        'Philip', 'Chandragupta', 'Alexander', 'Cyrus', 'Dido',
        'Hammurabi', 'Ramesses', 'Lincoln', 'Roosevelt', 'Churchill'
    ]
    
    # Common civilization names
    known_civs = [
        'India', 'Egypt', 'Rome', 'America', 'England', 'Britain',
        'Russia', 'Germany', 'France', 'Aztec', 'Sumeria', 'China',
        'Greece', 'Arabia', 'Kongo', 'Japan', 'Spain', 'Persia',
        'Babylon', 'Phoenicia', 'Scotland', 'Canada', 'Australia'
    ]
    
    # Search patterns that might indicate civilizations
    civ_patterns = [
        r'CIVILIZATION_([A-Z_]+)',
        r'LEADER_([A-Z_]+)', 
        r'CIV_([A-Z_]+)',
        r'LOC_CIVILIZATION_([A-Z_]+)',
        r'LOC_LEADER_([A-Z_]+)'
    ]
    
    search_terms = known_leaders + known_civs
    
    print("🔍 Searching through all log files for civilization clues...")
    
    # Get all files in logs directory
    try:
        for filename in os.listdir(logs_dir):
            if filename.endswith(('.log', '.csv', '.txt')):
                file_path = os.path.join(logs_dir, filename)
                
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                        content = file.read()
                        
                    # Search for known terms
                    found_in_file = []
                    for term in search_terms:
                        if term.lower() in content.lower():
                            found_in_file.append(term)
                    
                    # Search for patterns
                    for pattern in civ_patterns:
                        matches = re.findall(pattern, content, re.IGNORECASE)
                        for match in matches:
                            found_in_file.append(f"Pattern: {match}")
                    
                    if found_in_file:
                        leader_clues[filename] = found_in_file
                        
                except Exception as e:
                    continue  # Skip files we can't read
                    
    except Exception as e:
        print(f"❌ Error searching logs: {e}")
        return {}
    
    return leader_clues

def analyze_player_activity(logs_dir):
    """Analyze which players are most active/likely to be real civilizations."""
    scores_file = os.path.join(logs_dir, "Game_PlayerScores.csv")
    
    if not os.path.exists(scores_file):
        return {}
    
    player_analysis = {}
    
    try:
        with open(scores_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
            for line in lines[1:]:  # Skip header
                if line.strip():
                    parts = [part.strip() for part in line.split(',')]
                    if len(parts) >= 3:
                        try:
                            game_turn = int(parts[0])
                            player = int(parts[1])
                            score = int(parts[2])
                            
                            if player not in player_analysis:
                                player_analysis[player] = {
                                    'max_score': 0,
                                    'total_score': 0,
                                    'turns_active': 0,
                                    'score_progression': []
                                }
                            
                            player_data = player_analysis[player]
                            player_data['max_score'] = max(player_data['max_score'], score)
                            player_data['total_score'] += score
                            if score > 0:
                                player_data['turns_active'] += 1
                            player_data['score_progression'].append((game_turn, score))
                            
                        except ValueError:
                            continue
                            
    except Exception as e:
        print(f"❌ Error analyzing players: {e}")
        return {}
    
    return player_analysis

def guess_civilization_types(player_analysis):
    """Make educated guesses about what type of player each ID represents."""
    player_types = {}
    
    for player_id, data in player_analysis.items():
        max_score = data['max_score']
        turns_active = data['turns_active']
        
        # Categorize players
        if player_id >= 62:
            player_types[player_id] = "Barbarian/City-State"
        elif max_score == 0:
            player_types[player_id] = "Inactive/Empty Slot"
        elif max_score > 10 and turns_active > 5:
            player_types[player_id] = "Major Civilization (Active)"
        elif max_score > 0 and turns_active > 0:
            player_types[player_id] = "Minor/AI Civilization"
        else:
            player_types[player_id] = "Unknown"
    
    return player_types

def main():
    """Search for leader names in all available sources."""
    print("🔍 Advanced Leader Detection - Searching all sources")
    print("=" * 60)
    
    logs_dir = get_logs_directory()
    if not logs_dir:
        print("❌ Could not find logs directory")
        return
    
    # Search all log files for leader clues
    leader_clues = search_all_logs_for_leaders(logs_dir)
    
    # Analyze player activity patterns
    player_analysis = analyze_player_activity(logs_dir)
    
    # Guess civilization types
    player_types = guess_civilization_types(player_analysis)
    
    print("\n🎯 RESULTS:")
    print("=" * 60)
    
    if leader_clues:
        print("📋 CIVILIZATION CLUES FOUND:")
        for filename, clues in leader_clues.items():
            print(f"\n📁 {filename}:")
            for clue in clues[:10]:  # Show first 10 clues
                print(f"   - {clue}")
            if len(clues) > 10:
                print(f"   ... and {len(clues) - 10} more")
    else:
        print("❌ No direct civilization/leader names found in logs")
    
    print(f"\n👥 PLAYER ANALYSIS:")
    active_civs = []
    
    for player_id in sorted(player_analysis.keys()):
        if player_id < 62:  # Skip barbarians
            data = player_analysis[player_id]
            player_type = player_types.get(player_id, "Unknown")
            
            print(f"   🎮 Player {player_id:2d}: {player_type}")
            print(f"       Max Score: {data['max_score']:2d}, Active Turns: {data['turns_active']:2d}")
            
            if "Active" in player_type or data['max_score'] > 7:
                active_civs.append(player_id)
    
    print(f"\n🎯 LIKELY ACTIVE CIVILIZATIONS: {len(active_civs)}")
    for player_id in active_civs:
        score = player_analysis[player_id]['max_score']
        print(f"   👑 Player {player_id}: Max Score {score} (Likely major civilization)")
    
    print(f"\n💡 RECOMMENDATIONS:")
    print(f"   - Found {len(active_civs)} likely active civilizations")
    print(f"   - Civilization names not directly available in logs")
    print(f"   - Could implement civilization guessing based on gameplay patterns")
    print(f"   - Player IDs 0-{max(active_civs)} appear to be the main game")

if __name__ == "__main__":
    main()
