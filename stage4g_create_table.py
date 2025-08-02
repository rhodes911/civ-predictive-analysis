#!/usr/bin/env python3
"""
Stage 4g: Create Database Table
Create the actual PostgreSQL table for Civ VI data and test connection
"""

import psycopg2
import sys
from datetime import datetime

def create_database_table():
    """Create the civ_game_data table in PostgreSQL"""
    
    print("🗄️ STAGE 4G: Creating Database Table")
    print("=" * 50)
    
    # Database connection settings (from docker-compose.yml)
    db_config = {
        'host': 'localhost',
        'port': 5432,
        'database': 'civ6_analytics',
        'user': 'civ6_user',
        'password': 'civ6_password'
    }
    
    try:
        # Connect to PostgreSQL
        print(f"📡 Connecting to PostgreSQL at {db_config['host']}:{db_config['port']}")
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()
        
        print("✅ Database connection successful!")
        
        # Drop table if exists (for testing)
        print("🧹 Dropping existing table if it exists...")
        cursor.execute("DROP TABLE IF EXISTS civ_game_data CASCADE;")
        
        # Create the table based on our Stage 4b design
        print("🏗️ Creating civ_game_data table...")
        
        create_table_sql = """
        CREATE TABLE civ_game_data (
            -- Primary identification
            id SERIAL PRIMARY KEY,
            game_turn INTEGER NOT NULL,
            civilization VARCHAR(100) NOT NULL,
            player_number INTEGER,
            
            -- Basic civilization stats
            num_cities INTEGER DEFAULT 0,
            population INTEGER DEFAULT 0,
            techs INTEGER DEFAULT 0,
            civics INTEGER DEFAULT 0,
            
            -- Military units
            land_units INTEGER DEFAULT 0,
            corps INTEGER DEFAULT 0,
            armies INTEGER DEFAULT 0,
            naval_units INTEGER DEFAULT 0,
            
            -- Territory
            tiles_owned INTEGER DEFAULT 0,
            tiles_improved INTEGER DEFAULT 0,
            
            -- Resources and yields (NOTE: Rounded to integers by Civ VI CSV export)
            balance_gold INTEGER DEFAULT 0,
            balance_faith INTEGER DEFAULT 0,
            yields_science INTEGER DEFAULT 0,
            yields_culture INTEGER DEFAULT 0,
            yields_gold INTEGER DEFAULT 0,
            yields_faith INTEGER DEFAULT 0,
            yields_production INTEGER DEFAULT 0,
            yields_food INTEGER DEFAULT 0,
            
            -- Advanced stats
            buildings INTEGER DEFAULT 0,  -- Note: May contain erroneous data
            districts INTEGER DEFAULT 0,
            outgoing_trade_routes INTEGER DEFAULT 0,
            tourism INTEGER DEFAULT 0,
            diplo_victory INTEGER DEFAULT 0,
            balance_favor INTEGER DEFAULT 0,
            lifetime_favor INTEGER DEFAULT 0,
            co2_per_turn INTEGER DEFAULT 0,
            
            -- Scoring
            total_score INTEGER DEFAULT 0,
            
            -- Metadata
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            
            -- Constraints
            UNIQUE(game_turn, civilization)
        );
        """
        
        cursor.execute(create_table_sql)
        
        # Create indexes for dashboard performance
        print("📊 Creating performance indexes...")
        
        indexes = [
            "CREATE INDEX idx_civ_game_data_turn ON civ_game_data(game_turn);",
            "CREATE INDEX idx_civ_game_data_civilization ON civ_game_data(civilization);",
            "CREATE INDEX idx_civ_game_data_turn_civ ON civ_game_data(game_turn, civilization);",
            "CREATE INDEX idx_civ_game_data_score ON civ_game_data(total_score DESC);",
        ]
        
        for idx_sql in indexes:
            cursor.execute(idx_sql)
        
        # Commit the changes
        conn.commit()
        print("✅ Table and indexes created successfully!")
        
        # Verify table structure
        print("\n🔍 Verifying table structure...")
        cursor.execute("""
            SELECT column_name, data_type, is_nullable, column_default 
            FROM information_schema.columns 
            WHERE table_name = 'civ_game_data' 
            ORDER BY ordinal_position;
        """)
        
        columns = cursor.fetchall()
        print(f"📋 Table has {len(columns)} columns:")
        
        for col_name, data_type, nullable, default in columns:
            nullable_str = "NULL" if nullable == "YES" else "NOT NULL"
            default_str = f" DEFAULT {default}" if default else ""
            print(f"  {col_name}: {data_type} {nullable_str}{default_str}")
        
        # Test insert and select
        print("\n🧪 Testing insert and select operations...")
        
        test_data = {
            'game_turn': 1,
            'civilization': 'TEST_CIVILIZATION',
            'player_number': 0,
            'num_cities': 1,
            'population': 2,
            'yields_science': 4,  # This would be 4.5 in game but rounded to 4 in CSV
            'yields_culture': 4,  # This would be 4.5 in game but rounded to 4 in CSV
            'total_score': 10
        }
        
        insert_sql = """
        INSERT INTO civ_game_data 
        (game_turn, civilization, player_number, num_cities, population, yields_science, yields_culture, total_score)
        VALUES (%(game_turn)s, %(civilization)s, %(player_number)s, %(num_cities)s, %(population)s, %(yields_science)s, %(yields_culture)s, %(total_score)s)
        """
        
        cursor.execute(insert_sql, test_data)
        
        # Select the test data back
        cursor.execute("SELECT * FROM civ_game_data WHERE civilization = 'TEST_CIVILIZATION'")
        result = cursor.fetchone()
        
        if result:
            print("✅ Insert/Select test successful!")
            print(f"   Test record: Turn {result[1]}, {result[2]}, Science: {result[16]}, Culture: {result[17]}")
        else:
            print("❌ Insert/Select test failed!")
        
        # Clean up test data
        cursor.execute("DELETE FROM civ_game_data WHERE civilization = 'TEST_CIVILIZATION'")
        conn.commit()
        
        print("\n🎉 DATABASE TABLE READY!")
        print("=" * 30)
        print("✅ Table: civ_game_data created")
        print("✅ Indexes: Performance indexes added")
        print("✅ Constraints: Unique(game_turn, civilization)")
        print("✅ Testing: Insert/Select operations verified")
        print("⚠️  Note: Science/Culture values will be rounded integers (CSV limitation)")
        print("\n🎯 NEXT: Stage 4h - Insert real Civ VI data")
        
    except psycopg2.Error as e:
        print(f"❌ Database error: {e}")
        print("💡 Make sure Docker containers are running: docker-compose up -d")
        return False
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False
        
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()
    
    return True

if __name__ == "__main__":
    success = create_database_table()
    if not success:
        sys.exit(1)
