#!/usr/bin/env python3
"""
Stage 4b: Database Schema Design

Based on Stage 4a analysis, design the database tables we need.

Key Insights:
- Player_Stats.csv: Civilization names as strings, comprehensive stats
- Player_Stats_2.csv: Additional stats (some bogus like buildings)  
- Game_PlayerScores.csv: Player numbers (0-15), total scores + breakdown

Database Design:
- One main table: civ_game_data
- Combines all reliable data from the 3 CSV files
- Uses civilization names (not player numbers) for easy dashboard filtering
"""

def design_database_schema():
    """Design the database schema for our Civ VI data"""
    
    print("🏗️ STAGE 4B: DATABASE SCHEMA DESIGN")
    print("="*60)
    
    print("\n📋 PROPOSED DATABASE TABLE: civ_game_data")
    print("-" * 50)
    
    schema = """
    CREATE TABLE civ_game_data (
        -- Primary identifiers
        id SERIAL PRIMARY KEY,
        game_turn INTEGER NOT NULL,
        civilization VARCHAR(50) NOT NULL,
        is_city_state BOOLEAN DEFAULT FALSE,
        
        -- Core civilization stats (from Player_Stats.csv)
        num_cities INTEGER DEFAULT 0,
        population INTEGER DEFAULT 0,
        techs INTEGER DEFAULT 0,
        civics INTEGER DEFAULT 0,
        land_units INTEGER DEFAULT 0,
        naval_units INTEGER DEFAULT 0,
        tiles_owned INTEGER DEFAULT 0,
        tiles_improved INTEGER DEFAULT 0,
        
        -- Economy (from Player_Stats.csv)
        gold_balance INTEGER DEFAULT 0,
        faith_balance INTEGER DEFAULT 0,
        science_per_turn INTEGER DEFAULT 0,
        culture_per_turn INTEGER DEFAULT 0,
        gold_per_turn INTEGER DEFAULT 0,
        faith_per_turn INTEGER DEFAULT 0,
        production_per_turn INTEGER DEFAULT 0,
        food_per_turn INTEGER DEFAULT 0,
        
        -- Advanced stats (from Player_Stats_2.csv - reliable ones only)
        tiles_controlled INTEGER DEFAULT 0,
        districts INTEGER DEFAULT 0,
        trade_routes INTEGER DEFAULT 0,
        tourism INTEGER DEFAULT 0,
        diplomatic_favor INTEGER DEFAULT 0,
        
        -- Scores (from Game_PlayerScores.csv)
        total_score INTEGER DEFAULT 0,
        score_civics INTEGER DEFAULT 0,
        score_empire INTEGER DEFAULT 0,
        score_great_people INTEGER DEFAULT 0,
        score_religion INTEGER DEFAULT 0,
        score_tech INTEGER DEFAULT 0,
        score_wonder INTEGER DEFAULT 0,
        score_trade INTEGER DEFAULT 0,
        
        -- Metadata
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        
        -- Constraints
        UNIQUE(game_turn, civilization)
    );
    
    -- Index for fast dashboard queries
    CREATE INDEX idx_civ_turn ON civ_game_data(civilization, game_turn);
    CREATE INDEX idx_turn_score ON civ_game_data(game_turn, total_score DESC);
    """
    
    print(schema)
    
    print("\n🎯 KEY DESIGN DECISIONS:")
    print("-" * 30)
    print("✅ Use civilization names (not player numbers) - easier dashboard filtering")
    print("✅ Combine all 3 CSV files into single table - simpler queries") 
    print("✅ Skip 'Buildings' column - identified as bogus data")
    print("✅ Include city_state flag - separate major civs from city-states")
    print("✅ Add unique constraint - prevent duplicate turn/civ records")
    print("✅ Add indexes - optimize dashboard performance")
    
    print("\n📊 DASHBOARD FILTER EXAMPLES:")
    print("-" * 30)
    print("🔍 'I am Netherlands' → WHERE civilization = 'NETHERLANDS'")
    print("📈 'Turn 1-40' → WHERE game_turn BETWEEN 1 AND 40") 
    print("🏆 'Current Rankings' → ORDER BY total_score DESC")
    print("📊 'Science Progress' → SELECT science_per_turn, game_turn")
    
    print("\n💡 NEXT STEP: Create sample data transformation script")

if __name__ == "__main__":
    design_database_schema()
