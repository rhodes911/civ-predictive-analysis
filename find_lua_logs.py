#!/usr/bin/env python3
"""
Stage 3a: Find Civ VI Lua.log File
Ultra simple approach - just find the log file and report where it is.
"""

import os
import sys
from pathlib import Path

def find_lua_logs():
    """Find Civ VI Lua.log files in common Windows locations."""
    print("🔍 Searching for Civ VI Lua.log files...")
    print("=" * 50)
    
    # Common Civ VI log locations on Windows
    possible_locations = [
        # Documents folder
        os.path.expandvars(r"%USERPROFILE%\Documents\My Games\Sid Meier's Civilization VI\Logs\Lua.log"),
        # Local AppData
        os.path.expandvars(r"%LOCALAPPDATA%\Firaxis Games\Sid Meier's Civilization VI\Logs\Lua.log"),
        # Alternative Documents location
        os.path.expandvars(r"%USERPROFILE%\Documents\My Games\Civilization VI\Logs\Lua.log"),
        # Steam cloud saves sometimes go here
        os.path.expandvars(r"%USERPROFILE%\Documents\My Games\Sid Meier's Civilization VI (Epic)\Logs\Lua.log"),
    ]
    
    found_logs = []
    
    for location in possible_locations:
        print(f"Checking: {location}")
        
        if os.path.exists(location):
            file_size = os.path.getsize(location)
            modified_time = os.path.getmtime(location)
            
            print(f"  ✅ FOUND! Size: {file_size:,} bytes")
            print(f"  📅 Last modified: {os.path.getctime(location)}")
            
            found_logs.append({
                'path': location,
                'size': file_size,
                'modified': modified_time
            })
        else:
            print(f"  ❌ Not found")
        
        print()
    
    print("=" * 50)
    
    if found_logs:
        print(f"🎉 SUCCESS! Found {len(found_logs)} Lua.log file(s)")
        
        # Find the most recently modified one
        latest_log = max(found_logs, key=lambda x: x['modified'])
        print(f"\n📍 Most recent log file:")
        print(f"   Path: {latest_log['path']}")
        print(f"   Size: {latest_log['size']:,} bytes")
        
        return latest_log['path']
    else:
        print("❌ No Lua.log files found!")
        print("\n💡 Possible reasons:")
        print("   - Civ VI not installed")
        print("   - Game hasn't been launched yet")
        print("   - Logs disabled in game settings")
        print("   - Non-standard installation location")
        
        return None

def peek_at_log(log_path):
    """Take a quick peek at the log file to see what's inside."""
    if not log_path or not os.path.exists(log_path):
        return
    
    print("\n" + "=" * 50)
    print("👀 Quick peek at the log file (last 10 lines):")
    print("=" * 50)
    
    try:
        with open(log_path, 'r', encoding='utf-8', errors='ignore') as file:
            lines = file.readlines()
            
            if lines:
                # Show last 10 lines
                for line in lines[-10:]:
                    print(f"  {line.strip()}")
            else:
                print("  (Log file is empty)")
                
    except Exception as e:
        print(f"  ❌ Error reading log: {e}")

if __name__ == "__main__":
    print("🎮 Civ VI Lua.log Finder - Stage 3a")
    print("Just finding logs, nothing fancy!")
    print()
    
    log_path = find_lua_logs()
    
    if log_path:
        # Take a quick peek at what's in the log
        peek_at_log(log_path)
        
        print(f"\n✅ STAGE 3A COMPLETE!")
        print(f"📍 Log found at: {log_path}")
        print("🎯 Next: Create extract_leaders.py to find leader names")
    else:
        print(f"\n⏸️  STAGE 3A INCOMPLETE")
        print("🎮 Try launching Civ VI first, then run this script again")
