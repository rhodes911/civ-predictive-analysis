#!/usr/bin/env python3
"""
Test script to debug imports and functionality
"""

def test_basic_imports():
    print("🧪 Testing basic imports...")
    
    try:
        import pandas as pd
        print("✅ pandas imported")
    except Exception as e:
        print(f"❌ pandas failed: {e}")
    
    try:
        import numpy as np
        print("✅ numpy imported")
    except Exception as e:
        print(f"❌ numpy failed: {e}")
    
    try:
        import psycopg2
        print("✅ psycopg2 imported")
    except Exception as e:
        print(f"❌ psycopg2 failed: {e}")
    
    try:
        import watchdog
        print("✅ watchdog imported")
    except Exception as e:
        print(f"❌ watchdog failed: {e}")

def test_database_connection():
    print("\n🔗 Testing database connection...")
    
    try:
        import psycopg2
        conn = psycopg2.connect(
            host="localhost",
            port=5432,
            database="civ6_analytics",
            user="civ6_user",
            password="civ6_password"
        )
        print("✅ Database connection successful")
        conn.close()
    except Exception as e:
        print(f"❌ Database connection failed: {e}")

def test_log_parser():
    print("\n📝 Testing log parser...")
    
    try:
        import sys
        import os
        sys.path.append('src')
        
        from src.data.log_parser import LuaLogParser
        print("✅ LuaLogParser imported")
        
        # Test basic functionality without database
        parser = LuaLogParser()
        print("✅ LuaLogParser instance created")
        
    except Exception as e:
        print(f"❌ Log parser test failed: {e}")

if __name__ == "__main__":
    print("🎮 Civ VI DeepResearch Method - System Test")
    print("=" * 50)
    
    test_basic_imports()
    test_database_connection()
    test_log_parser()
    
    print("\n✅ System test complete!")
