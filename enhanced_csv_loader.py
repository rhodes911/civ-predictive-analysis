#!/usr/bin/env python3
"""
Enhanced CSV Data Loader for Civ VI Key Files
Focuses on the 3 most important CSV files for ML training
"""

import pandas as pd
import os
import numpy as np
from pathlib import Path
import psycopg2
from psycopg2.extras import execute_values
import logging
from datetime import datetime

class CivDataLoader:
    def __init__(self):
        self.logs_path = Path(os.path.expandvars(r"${LOCALAPPDATA}\Firaxis Games\Sid Meier's Civilization VI\Logs"))
        self.setup_logging()
        
        # Key CSV files for ML training
        self.key_files = {
            'player_stats': 'Player_Stats.csv',
            'player_stats_2': 'Player_Stats_2.csv', 
            'game_scores': 'Game_PlayerScores.csv'
        }
        
        # Database connection parameters
        self.db_params = {
            'host': 'localhost',
            'port': 5432,
            'database': 'civ6_analytics',
            'user': 'civ6_user',
            'password': 'civ6_password'
        }
    
    def setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('civ_data_loader.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def clean_column_names(self, df):
        """Clean column names by removing leading/trailing spaces"""
        df.columns = df.columns.str.strip()
        return df
    
    def clean_player_names(self, df, player_col='Player'):
        """Clean player names by removing leading spaces"""
        if player_col in df.columns:
            df[player_col] = df[player_col].str.strip()
        return df
    
    def load_player_stats(self):
        """Load and clean Player_Stats.csv"""
        file_path = self.logs_path / self.key_files['player_stats']
        
        try:
            self.logger.info(f"Loading {file_path}")
            df = pd.read_csv(file_path)
            
            # Clean column names and data
            df = self.clean_column_names(df)
            df = self.clean_player_names(df, 'Player')
            
            # Rename columns for database consistency
            column_mapping = {
                'Game Turn': 'game_turn',
                'Player': 'player_name',
                'Num Cities': 'num_cities',
                'Population': 'population',
                'Techs': 'techs',
                'Civics': 'civics',
                'Land Units': 'land_units',
                'corps': 'corps',
                'Armies': 'armies',
                'Naval Units': 'naval_units',
                'TILES: Owned': 'tiles_owned',
                'Improved': 'tiles_improved',
                'BALANCE: Gold': 'balance_gold',
                'Faith': 'balance_faith',
                'YIELDS: Science': 'yield_science',
                'Culture': 'yield_culture',
                'Gold': 'yield_gold',
                'Faith.1': 'yield_faith',
                'Production': 'yield_production',
                'Food': 'yield_food'
            }
            
            df = df.rename(columns=column_mapping)
            
            # Add metadata
            df['data_source'] = 'player_stats'
            df['loaded_at'] = datetime.now()
            
            self.logger.info(f"Loaded Player_Stats: {len(df)} rows, {len(df.columns)} columns")
            return df
            
        except Exception as e:
            self.logger.error(f"Error loading Player_Stats.csv: {e}")
            return None
    
    def load_player_stats_2(self):
        """Load and clean Player_Stats_2.csv"""
        file_path = self.logs_path / self.key_files['player_stats_2']
        
        try:
            self.logger.info(f"Loading {file_path}")
            df = pd.read_csv(file_path)
            
            # Clean column names and data
            df = self.clean_column_names(df)
            df = self.clean_player_names(df, 'Player')
            
            # Rename columns for database consistency
            column_mapping = {
                'Game Turn': 'game_turn',
                'Player': 'player_name',
                'BY TYPE: Tiles': 'tiles_by_type',
                'Buildings': 'buildings',
                'Districts': 'districts',
                'Population': 'population_alt',
                'Outgoing Trade Routes': 'outgoing_trade_routes',
                'TOURISM': 'tourism',
                'Diplo Victory': 'diplo_victory_points',
                'BALANCE: Favor': 'balance_favor',
                'LIFETIME: Favor': 'lifetime_favor',
                'CO2 Per Turn': 'co2_per_turn'
            }
            
            df = df.rename(columns=column_mapping)
            
            # Add metadata
            df['data_source'] = 'player_stats_2'
            df['loaded_at'] = datetime.now()
            
            self.logger.info(f"Loaded Player_Stats_2: {len(df)} rows, {len(df.columns)} columns")
            return df
            
        except Exception as e:
            self.logger.error(f"Error loading Player_Stats_2.csv: {e}")
            return None
    
    def load_game_scores(self):
        """Load and clean Game_PlayerScores.csv"""
        file_path = self.logs_path / self.key_files['game_scores']
        
        try:
            self.logger.info(f"Loading {file_path}")
            df = pd.read_csv(file_path)
            
            # Clean column names
            df = self.clean_column_names(df)
            
            # Rename columns for database consistency
            column_mapping = {
                'Game Turn': 'game_turn',
                'Player': 'player_id',
                'Score': 'total_score',
                'CATEGORY_CIVICS': 'score_civics',
                'CATEGORY_EMPIRE': 'score_empire',
                'CATEGORY_GREAT_PEOPLE': 'score_great_people',
                'CATEGORY_RELIGION': 'score_religion',
                'CATEGORY_TECH': 'score_tech',
                'CATEGORY_WONDER': 'score_wonder',
                'CATEGORY_TRADE': 'score_trade',
                'CATEGORY_PILLAGE': 'score_pillage',
                'CATEGORY_INCOME': 'score_income',
                'CATEGORY_SCENARIO1': 'score_scenario1',
                'CATEGORY_SCENARIO2': 'score_scenario2',
                'CATEGORY_SCENARIO3': 'score_scenario3',
                'CATEGORY_E': 'score_category_e'
            }
            
            df = df.rename(columns=column_mapping)
            
            # Add metadata
            df['data_source'] = 'game_scores'
            df['loaded_at'] = datetime.now()
            
            self.logger.info(f"Loaded Game_PlayerScores: {len(df)} rows, {len(df.columns)} columns")
            return df
            
        except Exception as e:
            self.logger.error(f"Error loading Game_PlayerScores.csv: {e}")
            return None
    
    def create_merged_dataset(self):
        """Create a merged dataset for ML training"""
        self.logger.info("Creating merged dataset for ML training")
        
        # Load all datasets
        df_stats = self.load_player_stats()
        df_stats2 = self.load_player_stats_2()
        df_scores = self.load_game_scores()
        
        if df_stats is None or df_stats2 is None or df_scores is None:
            self.logger.error("Failed to load one or more key datasets")
            return None
        
        # Create player mapping for scores (player_id to player_name)
        # We'll use the first turn to establish the mapping
        player_mapping = df_stats[df_stats['game_turn'] == 1][['player_name']].reset_index()
        player_mapping['player_id'] = player_mapping.index
        player_mapping = player_mapping[['player_id', 'player_name']]
        
        # Add player names to scores dataframe
        df_scores_with_names = df_scores.merge(player_mapping, on='player_id', how='left')
        
        # Merge datasets on game_turn and player_name
        merged_df = df_stats.merge(
            df_stats2,
            on=['game_turn', 'player_name'],
            how='outer',
            suffixes=('', '_ext')
        )
        
        merged_df = merged_df.merge(
            df_scores_with_names,
            on=['game_turn', 'player_name'],
            how='outer',
            suffixes=('', '_score')
        )
        
        # Add derived features for ML
        merged_df['total_yields'] = (
            merged_df['yield_science'].fillna(0) + 
            merged_df['yield_culture'].fillna(0) + 
            merged_df['yield_production'].fillna(0)
        )
        
        merged_df['total_military'] = (
            merged_df['land_units'].fillna(0) + 
            merged_df['naval_units'].fillna(0)
        )
        
        merged_df['infrastructure_total'] = (
            merged_df['buildings'].fillna(0) + 
            merged_df['districts'].fillna(0)
        )
        
        # Calculate game phase
        max_turns = merged_df['game_turn'].max()
        merged_df['game_phase'] = pd.cut(
            merged_df['game_turn'], 
            bins=[0, max_turns//3, 2*max_turns//3, max_turns],
            labels=['Early', 'Mid', 'Late']
        )
        
        self.logger.info(f"Created merged dataset: {len(merged_df)} rows, {len(merged_df.columns)} columns")
        return merged_df
    
    def save_to_csv(self, df, filename):
        """Save dataframe to CSV file"""
        if df is not None:
            output_path = f"{filename}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            df.to_csv(output_path, index=False)
            self.logger.info(f"Saved dataset to: {output_path}")
            return output_path
        return None
    
    def analyze_data_quality(self, df):
        """Analyze data quality and completeness"""
        if df is None:
            return
        
        self.logger.info("="*60)
        self.logger.info("DATA QUALITY ANALYSIS")
        self.logger.info("="*60)
        
        # Basic stats
        self.logger.info(f"Total records: {len(df):,}")
        self.logger.info(f"Total columns: {len(df.columns)}")
        self.logger.info(f"Game turns: {df['game_turn'].min()} - {df['game_turn'].max()}")
        self.logger.info(f"Unique players: {df['player_name'].nunique()}")
        
        # Missing data analysis
        missing_data = df.isnull().sum()
        missing_pct = (missing_data / len(df)) * 100
        
        self.logger.info("\nMISSING DATA:")
        for col in missing_data[missing_data > 0].index:
            self.logger.info(f"  {col}: {missing_data[col]:,} ({missing_pct[col]:.1f}%)")
        
        # Value distributions for key columns
        key_cols = ['yield_science', 'yield_culture', 'tourism', 'diplo_victory_points', 'total_score']
        
        self.logger.info("\nKEY METRICS DISTRIBUTION:")
        for col in key_cols:
            if col in df.columns:
                col_data = df[col].dropna()
                if len(col_data) > 0:
                    self.logger.info(f"  {col}: min={col_data.min()}, max={col_data.max()}, mean={col_data.mean():.1f}")
        
        # Players by turn analysis
        players_per_turn = df.groupby('game_turn')['player_name'].nunique()
        self.logger.info(f"\nPLAYERS PER TURN:")
        self.logger.info(f"  Average: {players_per_turn.mean():.1f}")
        self.logger.info(f"  Range: {players_per_turn.min()} - {players_per_turn.max()}")
        
        # Final turn analysis (potential winners)
        final_turn = df['game_turn'].max()
        final_turn_data = df[df['game_turn'] == final_turn].sort_values('total_score', ascending=False)
        
        self.logger.info(f"\nFINAL TURN ({final_turn}) RANKINGS:")
        for i, (_, row) in enumerate(final_turn_data.head(5).iterrows()):
            self.logger.info(f"  {i+1}. {row['player_name']}: {row['total_score']} points")

def main():
    """Main execution function"""
    print("🚀 Starting Enhanced Civ VI Data Loading...")
    
    loader = CivDataLoader()
    
    # Load individual datasets
    print("\n📊 Loading individual CSV files...")
    df_stats = loader.load_player_stats()
    df_stats2 = loader.load_player_stats_2()
    df_scores = loader.load_game_scores()
    
    # Create merged dataset
    print("\n🔄 Creating merged ML dataset...")
    merged_df = loader.create_merged_dataset()
    
    if merged_df is not None:
        # Analyze data quality
        loader.analyze_data_quality(merged_df)
        
        # Save results
        print("\n💾 Saving results...")
        output_file = loader.save_to_csv(merged_df, "civ6_ml_training_data")
        
        if output_file:
            print(f"✅ ML training dataset saved to: {output_file}")
            print(f"📊 Dataset contains {len(merged_df):,} records ready for victory prediction modeling!")
        
        # Save individual cleaned datasets too
        if df_stats is not None:
            loader.save_to_csv(df_stats, "civ6_player_stats_cleaned")
        if df_stats2 is not None:
            loader.save_to_csv(df_stats2, "civ6_player_stats_2_cleaned")
        if df_scores is not None:
            loader.save_to_csv(df_scores, "civ6_game_scores_cleaned")
    
    else:
        print("❌ Failed to create merged dataset")
    
    print("\n✅ Data loading complete!")

if __name__ == "__main__":
    main()
