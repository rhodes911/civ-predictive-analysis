#!/usr/bin/env python3
"""
Stage 3b: Extract Leader Names from Civ VI Lua.log
Ultra simple approach - just find leader names in the current game.
"""

import os
import re
from find_lua_logs import find_lua_logs

def extract_leaders_from_log(log_path):
    """Extract leader names from the Lua.log file."""
    if not log_path or not os.path.exists(log_path):
        print("❌ No log file found!")
        return []
    
    print(f"📖 Reading Lua.log file: {log_path}")
    print("🔍 Searching for leader names...")
    print("=" * 50)
    
    leaders_found = set()  # Use set to avoid duplicates
    
    # Common patterns that might indicate leaders in Civ VI logs
    # These are educated guesses - we'll refine as we see real data
    leader_patterns = [
        r'LEADER_([A-Z_]+)',           # LEADER_GANDHI, LEADER_CLEOPATRA, etc.
        r'Leader.*?([A-Z][a-z]+)',     # Leader: Gandhi, etc.
        r'Civilization.*?([A-Z][a-z]+)', # Civilization: Egypt, etc.
        r'PlayerName.*?([A-Za-z]+)',   # PlayerName: Gandhi, etc.
        r'CivType.*?([A-Z_]+)',        # CivType: CIVILIZATION_INDIA, etc.
    ]
    
    try:
        with open(log_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            
        print(f"📊 Log file size: {len(content):,} characters")
        
        # Search for each pattern
        for pattern in leader_patterns:
            matches = re.findall(pattern, content, re.IGNORECASE)
            
            if matches:
                print(f"\n🎯 Pattern '{pattern}' found {len(matches)} matches:")
                for match in matches[:10]:  # Show first 10 matches
                    leaders_found.add(match.strip().title())
                    print(f"   - {match}")
                
                if len(matches) > 10:
                    print(f"   ... and {len(matches) - 10} more")
        
        # Also search for some known leader names directly
        known_leaders = [
            'Gandhi', 'Cleopatra', 'Caesar', 'Washington', 'Victoria', 
            'Peter', 'Catherine', 'Frederick', 'Montezuma', 'Gilgamesh',
            'Qin', 'Trajan', 'Pericles', 'Saladin', 'Mvemba', 'Hojo',
            'Philip', 'Chandragupta', 'Alexander', 'Cyrus', 'Dido'
        ]
        
        print(f"\n🔍 Searching for known leader names...")
        for leader in known_leaders:
            if leader.lower() in content.lower():
                leaders_found.add(leader)
                print(f"   ✅ Found: {leader}")
        
    except Exception as e:
        print(f"❌ Error reading log file: {e}")
        return []
    
    return list(leaders_found)

def display_results(leaders):
    """Display the leaders we found in a nice format."""
    print("\n" + "=" * 50)
    print("🎮 CURRENT GAME LEADERS FOUND:")
    print("=" * 50)
    
    if leaders:
        print(f"👥 Found {len(leaders)} leader(s) in the current game:")
        print()
        
        for i, leader in enumerate(sorted(leaders), 1):
            print(f"   {i:2d}. {leader}")
        
        print(f"\n🎉 SUCCESS! We can see Civ VI data!")
        print("🔗 Next: Connect this to database (Stage 4)")
        
    else:
        print("❌ No leaders found in the log")
        print("\n💡 Possible reasons:")
        print("   - Game not currently running")
        print("   - Log file from old/finished game")
        print("   - Different log format than expected")
        print("   - Leaders stored in different log file")
        
        print("\n🎮 Try this:")
        print("   1. Start Civ VI")
        print("   2. Start a new game or load existing")
        print("   3. Play a few turns")
        print("   4. Run this script again")

def main():
    """Main function to find logs and extract leaders."""
    print("🎮 Civ VI Leader Extractor - Stage 3b")
    print("Finding leaders in current game!")
    print()
    
    # First find the log file
    log_path = find_lua_logs()
    
    if not log_path:
        print("\n⏸️  STAGE 3B INCOMPLETE")
        print("🔍 No Lua.log file found. Please run find_lua_logs.py first")
        return
    
    # Extract leaders from the log
    leaders = extract_leaders_from_log(log_path)
    
    # Display results
    display_results(leaders)
    
    print(f"\n✅ STAGE 3B COMPLETE!")
    print("🎯 Next: Stage 3c - Better display and maybe real-time monitoring")

if __name__ == "__main__":
    main()
