#!/usr/bin/env python3
"""
Data Loader - Database interface for Civ VI analytics
Handles loading, querying, and managing game data
"""

import psycopg2
import pandas as pd
from datetime import datetime, timedelta
from typing import List, Dict, Optional


class DataLoader:
    def __init__(self, db_config=None):
        self.db_config = db_config or {
            'host': 'localhost',
            'port': 5432,
            'database': 'civ6_analytics',
            'user': 'civ6_user',
            'password': 'civ6_password'
        }
        self.connection = None
        self.connect()
    
    def connect(self):
        """Connect to the database"""
        try:
            self.connection = psycopg2.connect(**self.db_config)
            return True
        except Exception as e:
            print(f"❌ Database connection failed: {e}")
            return False
    
    def get_recent_games(self, limit=10) -> List[Dict]:
        """Get recent game sessions with their data"""
        if not self.connection:
            return []
        
        try:
            query = """
            SELECT DISTINCT gs.game_id, gs.started_at, gs.map_type, gs.difficulty, gs.num_players,
                   MAX(gd.turn_number) as max_turn,
                   COUNT(DISTINCT gd.player_name) as active_players
            FROM game_sessions gs
            LEFT JOIN game_data gd ON gs.game_id = gd.game_id
            GROUP BY gs.game_id, gs.started_at, gs.map_type, gs.difficulty, gs.num_players
            ORDER BY gs.started_at DESC
            LIMIT %s
            """
            
            cursor = self.connection.cursor()
            cursor.execute(query, (limit,))
            
            columns = [desc[0] for desc in cursor.description]
            games = []
            
            for row in cursor.fetchall():
                game = dict(zip(columns, row))
                games.append(game)
            
            return games
            
        except Exception as e:
            print(f"❌ Error fetching recent games: {e}")
            return []
    
    def get_game_data(self, game_id: str) -> pd.DataFrame:
        """Get all turn data for a specific game"""
        if not self.connection:
            return pd.DataFrame()
        
        try:
            query = """
            SELECT turn_number, player_name, civilization, 
                   science_per_turn, culture_per_turn, created_at
            FROM game_data 
            WHERE game_id = %s
            ORDER BY turn_number, player_name
            """
            
            return pd.read_sql_query(query, self.connection, params=(game_id,))
            
        except Exception as e:
            print(f"❌ Error fetching game data: {e}")
            return pd.DataFrame()
    
    def get_player_progression(self, game_id: str, player_name: str) -> pd.DataFrame:
        """Get turn-by-turn progression for a specific player"""
        if not self.connection:
            return pd.DataFrame()
        
        try:
            query = """
            SELECT turn_number, civilization, science_per_turn, culture_per_turn, created_at
            FROM game_data 
            WHERE game_id = %s AND player_name = %s
            ORDER BY turn_number
            """
            
            return pd.read_sql_query(query, self.connection, params=(game_id, player_name))
            
        except Exception as e:
            print(f"❌ Error fetching player progression: {e}")
            return pd.DataFrame()
    
    def get_civilization_stats(self) -> pd.DataFrame:
        """Get aggregated statistics by civilization"""
        if not self.connection:
            return pd.DataFrame()
        
        try:
            query = """
            SELECT civilization,
                   COUNT(DISTINCT game_id) as games_played,
                   AVG(science_per_turn) as avg_science,
                   AVG(culture_per_turn) as avg_culture,
                   MAX(turn_number) as longest_game
            FROM game_data
            GROUP BY civilization
            ORDER BY avg_science DESC
            """
            
            return pd.read_sql_query(query, self.connection)
            
        except Exception as e:
            print(f"❌ Error fetching civilization stats: {e}")
            return pd.DataFrame()
    
    def get_turn_analytics(self, game_id: str) -> Dict:
        """Get analytical data for a specific game"""
        if not self.connection:
            return {}
        
        try:
            cursor = self.connection.cursor()
            
            # Basic game info
            cursor.execute("""
                SELECT MAX(turn_number) as total_turns,
                       COUNT(DISTINCT player_name) as players,
                       AVG(science_per_turn) as avg_science,
                       AVG(culture_per_turn) as avg_culture
                FROM game_data WHERE game_id = %s
            """, (game_id,))
            
            basic_stats = cursor.fetchone()
            
            # Leader analysis (who's ahead in science/culture)
            cursor.execute("""
                SELECT player_name, civilization,
                       AVG(science_per_turn) as avg_science,
                       AVG(culture_per_turn) as avg_culture,
                       MAX(turn_number) as last_turn
                FROM game_data 
                WHERE game_id = %s
                GROUP BY player_name, civilization
                ORDER BY avg_science DESC
            """, (game_id,))
            
            player_rankings = cursor.fetchall()
            
            return {
                'total_turns': basic_stats[0] if basic_stats[0] else 0,
                'player_count': basic_stats[1] if basic_stats[1] else 0,
                'avg_science': round(basic_stats[2], 1) if basic_stats[2] else 0,
                'avg_culture': round(basic_stats[3], 1) if basic_stats[3] else 0,
                'leaders': [
                    {
                        'player': row[0],
                        'civilization': row[1],
                        'avg_science': round(row[2], 1),
                        'avg_culture': round(row[3], 1),
                        'last_turn': row[4]
                    }
                    for row in player_rankings
                ]
            }
            
        except Exception as e:
            print(f"❌ Error fetching turn analytics: {e}")
            return {}
    
    def get_total_records(self) -> int:
        """Get total number of records in database"""
        if not self.connection:
            return 0
        
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM game_data")
            return cursor.fetchone()[0]
        except:
            return 0
    
    def export_game_csv(self, game_id: str, filepath: str) -> bool:
        """Export game data to CSV file"""
        try:
            df = self.get_game_data(game_id)
            if not df.empty:
                df.to_csv(filepath, index=False)
                print(f"✅ Game data exported to: {filepath}")
                return True
            return False
        except Exception as e:
            print(f"❌ Error exporting to CSV: {e}")
            return False
    
    def cleanup_old_data(self, days=30):
        """Remove data older than specified days"""
        if not self.connection:
            return False
        
        try:
            cutoff_date = datetime.now() - timedelta(days=days)
            cursor = self.connection.cursor()
            
            cursor.execute("""
                DELETE FROM game_data 
                WHERE created_at < %s
            """, (cutoff_date,))
            
            cursor.execute("""
                DELETE FROM game_sessions 
                WHERE started_at < %s
            """, (cutoff_date,))
            
            self.connection.commit()
            print(f"✅ Cleaned up data older than {days} days")
            return True
            
        except Exception as e:
            print(f"❌ Error cleaning up data: {e}")
            if self.connection:
                self.connection.rollback()
            return False
