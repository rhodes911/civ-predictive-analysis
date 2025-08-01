#!/usr/bin/env python3
"""
Simple test script to verify the DeepResearch implementation
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Test all critical imports"""
    print("🧪 Testing DeepResearch imports...")
    
    try:
        from src.data.log_parser import LuaLogParser
        print("✅ LuaLogParser import successful")
    except Exception as e:
        print(f"❌ LuaLogParser import failed: {e}")
        return False
    
    try:
        from src.data.loader import DataLoader
        print("✅ DataLoader import successful")
    except Exception as e:
        print(f"❌ DataLoader import failed: {e}")
        return False
    
    try:
        from src.models.predictors import VictoryPredictor
        print("✅ VictoryPredictor import successful")
    except Exception as e:
        print(f"❌ VictoryPredictor import failed: {e}")
        return False
    
    return True

def test_sample_parsing():
    """Test log parsing with sample data"""
    print("\n📝 Testing sample log parsing...")
    
    try:
        from src.data.log_parser import LuaLogParser
        
        # Create sample log data
        sample_log = """
GAME_START: test_game_123
GAME_INFO: Map=Pangaea, Difficulty=King, Players=2
PLAYER: ID=0, Name=TestPlayer1, Civ=Korea, Leader=Sejong, Human=False
PLAYER: ID=1, Name=TestPlayer2, Civ=Rome, Leader=Trajan, Human=False
Turn 1: Player 0 (Korea) -> Science=2.5, Culture=1.8, Gold=3.2, Faith=0.0, Cities=1
Turn 1: Player 1 (Rome) -> Science=2.0, Culture=2.2, Gold=2.8, Faith=0.0, Cities=1
Turn 2: Player 0 (Korea) -> Science=3.1, Culture=2.4, Gold=4.1, Faith=0.5, Cities=1
Turn 2: Player 1 (Rome) -> Science=2.8, Culture=2.9, Gold=3.5, Faith=0.8, Cities=1
"""
        
        # Write sample log file
        with open('test_sample.log', 'w') as f:
            f.write(sample_log)
        
        # Test parsing (without database for now)
        parser = LuaLogParser()
        parser.current_game_id = 'test_game_123'
        
        lines = sample_log.strip().split('\n')
        for line in lines:
            if line.strip():
                parser.process_log_line(line.strip())
        
        print("✅ Sample parsing test completed")
        
        # Cleanup
        if os.path.exists('test_sample.log'):
            os.remove('test_sample.log')
        
        return True
        
    except Exception as e:
        print(f"❌ Sample parsing failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🎮 DeepResearch Method - System Test")
    print("=" * 40)
    
    # Test imports
    if not test_imports():
        print("\n❌ Import tests failed - check dependencies")
        return False
    
    # Test parsing logic
    if not test_sample_parsing():
        print("\n❌ Parsing tests failed - check implementation")
        return False
    
    print("\n✅ All tests passed!")
    print("\n📋 Next steps:")
    print("   1. Ensure Docker database is running: stage2.bat start")
    print("   2. Install Civ VI mod: deepresearch.bat install")
    print("   3. Start monitoring: deepresearch.bat start")
    print("   4. Play Civ VI and watch data flow")
    
    return True

if __name__ == "__main__":
    main()
