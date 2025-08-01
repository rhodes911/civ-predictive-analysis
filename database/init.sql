-- Stage 1: Basic Civ VI Database Schema
-- Simple table structure for testing database connectivity

-- Game sessions table
CREATE TABLE IF NOT EXISTS game_sessions (
    id SERIAL PRIMARY KEY,
    game_id VARCHAR(100) UNIQUE NOT NULL,
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    map_type VARCHAR(50),
    difficulty VARCHAR(50),
    num_players INTEGER
);

-- Basic game data table  
CREATE TABLE IF NOT EXISTS game_data (
    id SERIAL PRIMARY KEY,
    game_id VARCHAR(100) REFERENCES game_sessions(game_id),
    turn_number INTEGER,
    turn_display VARCHAR(10) GENERATED ALWAYS AS (LPAD(turn_number::TEXT, 3, '0')) STORED,
    player_name VARCHAR(50),
    civilization VARCHAR(50),
    science_per_turn REAL,
    culture_per_turn REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(game_id, turn_number, player_name)
);

-- Insert sample data for testing
INSERT INTO game_sessions (game_id, map_type, difficulty, num_players) 
VALUES 
    ('test_game_001', 'Pangaea', 'Emperor', 6),
    ('test_game_002', 'Continents', 'King', 8)
ON CONFLICT (game_id) DO NOTHING;

INSERT INTO game_data (game_id, turn_number, player_name, civilization, science_per_turn, culture_per_turn)
VALUES 
    -- Game 1: Early game (Turn 1-10)
    ('test_game_001', 1, 'Alice', 'Korea', 2.0, 1.5),
    ('test_game_001', 2, 'Alice', 'Korea', 2.5, 2.0),
    ('test_game_001', 3, 'Alice', 'Korea', 3.2, 2.8),
    ('test_game_001', 4, 'Alice', 'Korea', 4.1, 3.5),
    ('test_game_001', 5, 'Alice', 'Korea', 5.0, 4.2),
    ('test_game_001', 6, 'Alice', 'Korea', 6.2, 5.1),
    ('test_game_001', 7, 'Alice', 'Korea', 7.8, 6.3),
    ('test_game_001', 8, 'Alice', 'Korea', 9.5, 7.8),
    ('test_game_001', 9, 'Alice', 'Korea', 11.4, 9.2),
    ('test_game_001', 10, 'Alice', 'Korea', 13.6, 10.8),
    
    ('test_game_001', 1, 'Bob', 'Rome', 1.8, 2.2),
    ('test_game_001', 2, 'Bob', 'Rome', 2.3, 2.9),
    ('test_game_001', 3, 'Bob', 'Rome', 2.9, 3.8),
    ('test_game_001', 4, 'Bob', 'Rome', 3.7, 4.9),
    ('test_game_001', 5, 'Bob', 'Rome', 4.6, 6.1),
    ('test_game_001', 6, 'Bob', 'Rome', 5.8, 7.5),
    ('test_game_001', 7, 'Bob', 'Rome', 7.2, 9.1),
    ('test_game_001', 8, 'Bob', 'Rome', 8.9, 10.9),
    ('test_game_001', 9, 'Bob', 'Rome', 10.8, 12.8),
    ('test_game_001', 10, 'Bob', 'Rome', 12.9, 14.9),
    
    ('test_game_001', 1, 'Charlie', 'Egypt', 1.5, 2.8),
    ('test_game_001', 2, 'Charlie', 'Egypt', 2.1, 3.6),
    ('test_game_001', 3, 'Charlie', 'Egypt', 2.8, 4.7),
    ('test_game_001', 4, 'Charlie', 'Egypt', 3.6, 5.9),
    ('test_game_001', 5, 'Charlie', 'Egypt', 4.5, 7.3),
    ('test_game_001', 6, 'Charlie', 'Egypt', 5.6, 8.9),
    ('test_game_001', 7, 'Charlie', 'Egypt', 6.9, 10.7),
    ('test_game_001', 8, 'Charlie', 'Egypt', 8.4, 12.6),
    ('test_game_001', 9, 'Charlie', 'Egypt', 10.1, 14.8),
    ('test_game_001', 10, 'Charlie', 'Egypt', 12.0, 17.2)
ON CONFLICT DO NOTHING;
