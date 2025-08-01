#!/usr/bin/env python3
"""
Quick script to examine what's actually in the Lua.log file
"""

import os
from find_lua_logs import find_lua_logs

def examine_log_content():
    """Look at the actual content in the log file to understand patterns."""
    log_path = find_lua_logs()
    
    if not log_path:
        print("No log file found!")
        return
    
    print(f"\n🔍 EXAMINING LOG CONTENT")
    print(f"📁 File: {log_path}")
    print("=" * 60)
    
    try:
        with open(log_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        
        print(f"📊 Total size: {len(content):,} characters")
        print("\n📖 FIRST 1500 CHARACTERS:")
        print("-" * 50)
        print(content[:1500])
        
        print("\n📖 LAST 1000 CHARACTERS:")
        print("-" * 50)
        print(content[-1000:])
        
        print("\n🔍 SEARCHING FOR COMMON PATTERNS:")
        print("-" * 50)
        
        # Look for any mentions of common Civ VI terms
        search_terms = [
            'LEADER', 'Leader', 'CIVILIZATION', 'Civilization', 'Civ',
            'Player', 'PLAYER', 'Gandhi', 'Cleopatra', 'Caesar', 'Washington',
            'Game', 'Turn', 'City', 'Unit', 'Tech', 'Culture', 'Science'
        ]
        
        for term in search_terms:
            if term.lower() in content.lower():
                print(f"  ✅ Found '{term}' in log")
            else:
                print(f"  ❌ No '{term}' found")
        
    except Exception as e:
        print(f"❌ Error reading file: {e}")

if __name__ == "__main__":
    examine_log_content()
