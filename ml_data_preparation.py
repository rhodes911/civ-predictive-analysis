#!/usr/bin/env python3
"""
ML Data Preparation Script for Civ VI Victory Prediction
========================================================

This script extracts Turn 20 features and final game outcomes from the database
to create a training dataset for the ML victory prediction model.

Usage:
    python ml_data_preparation.py

Output:
    - training_data.csv: Features and outcomes for model training
    - data_analysis_report.txt: Summary statistics and insights
"""

import pandas as pd
import psycopg2
import numpy as np
from datetime import datetime
import os

class CivMLDataPreparation:
    def __init__(self):
        """Initialize database connection parameters"""
        self.db_config = {
            'host': 'localhost',
            'port': 5432,
            'database': 'civ6_analytics',
            'user': 'civ6_user',
            'password': 'civ6_password'
        }
        
    def connect_database(self):
        """Establish database connection"""
        try:
            conn = psycopg2.connect(**self.db_config)
            print("✅ Database connection established")
            return conn
        except Exception as e:
            print(f"❌ Database connection failed: {e}")
            return None
    
    def analyze_available_games(self):
        """Analyze what game sessions are available in the database"""
        conn = self.connect_database()
        if not conn:
            return None
            
        try:
            # Get overview of all game sessions
            query = """
            SELECT 
                created_at::date as game_date,
                created_at::time as game_time,
                COUNT(DISTINCT civilization) as num_civilizations,
                MIN(game_turn) as min_turn,
                MAX(game_turn) as max_turn,
                COUNT(*) as total_records
            FROM civ_game_data 
            GROUP BY created_at::date, created_at::time
            ORDER BY created_at::date, created_at::time;
            """
            
            df = pd.read_sql(query, conn)
            conn.close()
            
            print("\n📊 Available Game Sessions:")
            print("=" * 80)
            for _, row in df.iterrows():
                print(f"Date: {row['game_date']} | Time: {row['game_time']} | "
                      f"Civs: {row['num_civilizations']} | "
                      f"Turns: {row['min_turn']}-{row['max_turn']} | "
                      f"Records: {row['total_records']}")
                
            return df
            
        except Exception as e:
            print(f"❌ Error analyzing games: {e}")
            conn.close()
            return None
    
    def extract_training_features(self):
        """Extract features from all available turns and final outcomes for ML training"""
        conn = self.connect_database()
        if not conn:
            return None
            
        try:
            # Simplified query to get ALL turn data + final outcomes
            query = """
            WITH game_sessions AS (
                -- Identify distinct game sessions and their final turns
                SELECT DISTINCT 
                    created_at::date as game_date,
                    created_at::time as game_time,
                    CONCAT(created_at::date, '_', created_at::time) as game_id,
                    MAX(game_turn) OVER (PARTITION BY created_at::date, created_at::time) as final_turn
                FROM civ_game_data
            ),
            all_turn_data AS (
                -- Get features for ALL turns for each civilization in each game
                SELECT 
                    CONCAT(created_at::date, '_', created_at::time) as game_id,
                    civilization,
                    game_turn,
                    num_cities,
                    population,
                    techs,
                    civics,
                    yields_science,
                    yields_culture,
                    yields_production,
                    buildings,
                    districts,
                    total_score,
                    -- Calculate relative rankings within each game session and turn
                    RANK() OVER (
                        PARTITION BY created_at::date, created_at::time, game_turn 
                        ORDER BY yields_science DESC
                    ) as science_rank,
                    RANK() OVER (
                        PARTITION BY created_at::date, created_at::time, game_turn 
                        ORDER BY num_cities DESC
                    ) as cities_rank,
                    RANK() OVER (
                        PARTITION BY created_at::date, created_at::time, game_turn 
                        ORDER BY total_score DESC
                    ) as score_rank,
                    RANK() OVER (
                        PARTITION BY created_at::date, created_at::time, game_turn 
                        ORDER BY population DESC
                    ) as population_rank
                FROM civ_game_data 
            ),
            final_results AS (
                -- Get final game outcomes (last turn for each game session)
                SELECT 
                    CONCAT(created_at::date, '_', created_at::time) as game_id,
                    civilization,
                    game_turn as final_turn,
                    total_score as final_score,
                    RANK() OVER (
                        PARTITION BY created_at::date, created_at::time 
                        ORDER BY total_score DESC
                    ) as final_rank
                FROM civ_game_data t1
                WHERE game_turn = (
                    SELECT MAX(game_turn) 
                    FROM civ_game_data t2 
                    WHERE t2.created_at::date = t1.created_at::date 
                    AND t2.created_at::time = t1.created_at::time
                )
            )
            SELECT 
                atd.game_id,
                atd.civilization,
                atd.game_turn,
                -- Raw features
                atd.num_cities,
                atd.population,
                atd.techs,
                atd.civics,
                atd.yields_science,
                atd.yields_culture,
                atd.yields_production,
                atd.buildings,
                atd.districts,
                atd.total_score as current_score,
                -- Calculated features
                CASE WHEN atd.num_cities > 0 
                     THEN atd.yields_science::float / atd.num_cities 
                     ELSE 0 END as science_per_city,
                CASE WHEN atd.num_cities > 0 
                     THEN atd.population::float / atd.num_cities 
                     ELSE 0 END as population_per_city,
                CASE WHEN atd.num_cities > 0 
                     THEN atd.buildings::float / atd.num_cities 
                     ELSE 0 END as buildings_per_city,
                CASE WHEN atd.game_turn > 0 
                     THEN (atd.techs + atd.civics)::float / atd.game_turn 
                     ELSE 0 END as development_index,
                -- Relative rankings
                atd.science_rank,
                atd.cities_rank,
                atd.score_rank,
                atd.population_rank,
                -- Final outcomes
                fr.final_turn,
                fr.final_score,
                fr.final_rank,
                CASE WHEN fr.final_rank = 1 THEN 1 ELSE 0 END as will_win,
                -- Game metadata
                CASE WHEN atd.game_id LIKE '%07:%' OR atd.game_id LIKE '%10:%' THEN 'Current_Game' 
                     ELSE 'Previous_Game' END as game_session
            FROM all_turn_data atd
            JOIN final_results fr ON atd.game_id = fr.game_id AND atd.civilization = fr.civilization
            WHERE atd.game_turn >= 10  -- Only use turns 10+ for meaningful data
            ORDER BY atd.game_id, atd.game_turn, fr.final_rank;
            """
            
            df = pd.read_sql(query, conn)
            conn.close()
            
            print(f"\n✅ Extracted {len(df)} civilization records for ML training")
            return df
            
        except Exception as e:
            print(f"❌ Error extracting training data: {e}")
            conn.close()
            return None
    
    def generate_data_analysis_report(self, df):
        """Generate comprehensive analysis report of the training data"""
        if df is None or len(df) == 0:
            print("❌ No data available for analysis")
            return
            
        report = []
        report.append("🎯 CIV VI ML TRAINING DATA ANALYSIS REPORT")
        report.append("=" * 60)
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        # Basic statistics
        report.append("📊 DATASET OVERVIEW:")
        report.append(f"Total Records: {len(df)}")
        report.append(f"Unique Games: {df['game_id'].nunique()}")
        report.append(f"Unique Civilizations: {df['civilization'].nunique()}")
        report.append("")
        
        # Game session breakdown
        report.append("🎮 GAME SESSION BREAKDOWN:")
        session_counts = df['game_session'].value_counts()
        for session, count in session_counts.items():
            report.append(f"{session}: {count} records")
        report.append("")
        
        # Winner distribution
        report.append("🏆 WINNER DISTRIBUTION:")
        winners = df[df['will_win'] == 1]
        report.append(f"Total Winners: {len(winners)}")
        for civ in winners['civilization'].value_counts().head(10).items():
            report.append(f"{civ[0]}: {civ[1]} victories")
        report.append("")
        
        # Feature statistics
        report.append("📈 CURRENT TURN FEATURE STATISTICS:")
        numeric_cols = ['num_cities', 'population', 'techs', 'civics', 
                       'yields_science', 'yields_culture', 'yields_production',
                       'buildings', 'districts', 'current_score', 'game_turn']
        
        for col in numeric_cols:
            winners_mean = df[df['will_win'] == 1][col].mean()
            losers_mean = df[df['will_win'] == 0][col].mean()
            report.append(f"{col.replace('_', ' ').title()}:")
            report.append(f"  Winners Average: {winners_mean:.1f}")
            report.append(f"  Losers Average: {losers_mean:.1f}")
            if losers_mean > 0:
                advantage = ((winners_mean/losers_mean - 1) * 100)
                report.append(f"  Winner Advantage: {advantage:.1f}%")
            else:
                report.append(f"  Winner Advantage: N/A (no losers data)")
            report.append("")
        
        # Ranking analysis
        report.append("🎯 CURRENT TURN RANKING ANALYSIS:")
        for rank_col in ['science_rank', 'cities_rank', 'score_rank']:
            winner_ranks = df[df['will_win'] == 1][rank_col]
            report.append(f"{rank_col.replace('_', ' ').title()}:")
            report.append(f"  Winners Average Rank: {winner_ranks.mean():.1f}")
            report.append(f"  % Winners in Top 2: {(winner_ranks <= 2).mean() * 100:.1f}%")
            report.append("")
        
        # Data quality checks
        report.append("🔍 DATA QUALITY CHECKS:")
        report.append(f"Missing Values: {df.isnull().sum().sum()}")
        report.append(f"Duplicate Records: {df.duplicated().sum()}")
        
        # Games with incomplete data
        games_with_issues = []
        for game_id in df['game_id'].unique():
            game_data = df[df['game_id'] == game_id]
            if len(game_data) < 4:  # Expecting at least 4 civilizations
                games_with_issues.append(f"{game_id} ({len(game_data)} civs)")
        
        if games_with_issues:
            report.append("⚠️  Games with <4 civilizations:")
            for game in games_with_issues:
                report.append(f"  {game}")
        else:
            report.append("✅ All games have adequate civilization count")
        
        report.append("")
        
        # ML readiness assessment
        report.append("🤖 ML MODEL READINESS:")
        total_winners = (df['will_win'] == 1).sum()
        total_records = len(df)
        win_rate = total_winners / total_records
        
        report.append(f"Class Balance: {win_rate:.1%} winners, {(1-win_rate):.1%} non-winners")
        
        if total_records >= 30:
            report.append("✅ Sufficient data for initial model training")
        else:
            report.append("⚠️  Limited data - model may need more games for reliability")
            
        if 0.1 <= win_rate <= 0.4:
            report.append("✅ Good class balance for binary classification")
        else:
            report.append("⚠️  Class imbalance - may need sampling techniques")
        
        # Save report
        report_text = "\n".join(report)
        with open('data_analysis_report.txt', 'w', encoding='utf-8') as f:
            f.write(report_text)
        
        print("\n" + report_text)
        print(f"\n📋 Full report saved to: data_analysis_report.txt")
    
    def save_training_data(self, df):
        """Save prepared training data to CSV"""
        if df is None or len(df) == 0:
            print("❌ No data to save")
            return False
            
        try:
            # Save full dataset
            df.to_csv('training_data.csv', index=False)
            print(f"✅ Training data saved to: training_data.csv ({len(df)} records)")
            
            # Also save a sample for quick inspection
            sample_df = df.head(10)
            sample_df.to_csv('training_data_sample.csv', index=False)
            print(f"✅ Sample data saved to: training_data_sample.csv (first 10 records)")
            
            return True
            
        except Exception as e:
            print(f"❌ Error saving data: {e}")
            return False
    
    def run_preparation(self):
        """Run the complete data preparation process"""
        print("🚀 Starting ML Data Preparation for Civ VI Victory Prediction")
        print("=" * 70)
        
        # Step 1: Analyze available games
        print("\nStep 1: Analyzing available game sessions...")
        game_sessions = self.analyze_available_games()
        
        # Step 2: Extract training features
        print("\nStep 2: Extracting Turn 20 features and final outcomes...")
        training_data = self.extract_training_features()
        
        if training_data is not None:
            # Step 3: Generate analysis report
            print("\nStep 3: Generating data analysis report...")
            self.generate_data_analysis_report(training_data)
            
            # Step 4: Save training data
            print("\nStep 4: Saving training data files...")
            self.save_training_data(training_data)
            
            print("\n🎉 Data preparation completed successfully!")
            print("Next steps:")
            print("  1. Review data_analysis_report.txt for insights")
            print("  2. Inspect training_data.csv for quality")
            print("  3. Run victory_prediction_model.py to train the ML model")
            
        else:
            print("\n❌ Data preparation failed - check database connection and data")

if __name__ == "__main__":
    # Run the data preparation process
    prep = CivMLDataPreparation()
    prep.run_preparation()
