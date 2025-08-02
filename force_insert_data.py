#!/usr/bin/env python3
"""
Force insert new game data - ignores existing turns and adds current game
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Run the original script but modify the logic to force insert
if __name__ == "__main__":
    # Import and run with force flag
    print("🔄 Force inserting current game data...")
    
    # Add a simple command line argument
    if "--force" not in sys.argv:
        sys.argv.append("--force")
    
    # Import and modify the main script
    from stage4h_insert_data import main
    
    # Temporarily modify the script behavior
    print("💾 FORCE INSERT: Current Indonesia Game")
    print("=" * 50)
    
    # Run with force mode
    result = main()
    
    if result:
        print("✅ Successfully inserted current game data!")
    else:
        print("❌ Failed to insert current game data")
