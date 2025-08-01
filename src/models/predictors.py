#!/usr/bin/env python3
"""
Victory Prediction Models for Civ VI Analytics
Uses machine learning to predict game outcomes based on early game statistics
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from typing import Dict, List, Optional
import pickle
import os
from datetime import datetime


class VictoryPredictor:
    def __init__(self, model_path="models/victory_predictor.pkl"):
        self.model = None
        self.scaler = StandardScaler()
        self.feature_columns = [
            'avg_science_early', 'avg_culture_early', 'science_trend', 'culture_trend',
            'relative_science_rank', 'relative_culture_rank', 'turn_count'
        ]
        self.model_path = model_path
        self.load_or_create_model()
    
    def load_or_create_model(self):
        """Load existing model or create a new one"""
        if os.path.exists(self.model_path):
            try:
                with open(self.model_path, 'rb') as f:
                    model_data = pickle.load(f)
                    self.model = model_data['model']
                    self.scaler = model_data['scaler']
                print(f"✅ Loaded existing model from {self.model_path}")
            except Exception as e:
                print(f"⚠️ Error loading model: {e}, creating new one")
                self.create_default_model()
        else:
            self.create_default_model()
    
    def create_default_model(self):
        """Create a default model with synthetic training data"""
        print("🧠 Creating default victory prediction model...")
        
        # Generate synthetic training data based on Civ VI game patterns
        synthetic_data = self.generate_synthetic_training_data()
        
        # Train the model
        self.train_model(synthetic_data)
        print("✅ Default model created with synthetic data")
    
    def generate_synthetic_training_data(self) -> pd.DataFrame:
        """Generate synthetic training data based on Civ VI patterns"""
        np.random.seed(42)
        n_samples = 1000
        
        data = []
        
        for i in range(n_samples):
            # Victory types: Science, Culture, Domination, Religious, Diplomatic
            victory_type = np.random.choice(['Science', 'Culture', 'Domination', 'Religious', 'Diplomatic'])
            
            # Generate features based on victory type patterns
            if victory_type == 'Science':
                avg_science_early = np.random.normal(15, 3)  # Higher science
                avg_culture_early = np.random.normal(8, 2)   # Lower culture
                science_trend = np.random.normal(1.2, 0.2)   # Positive trend
                culture_trend = np.random.normal(0.8, 0.2)   # Slower culture growth
                relative_science_rank = np.random.uniform(0.7, 1.0)  # High rank
                relative_culture_rank = np.random.uniform(0.3, 0.7)  # Medium rank
                
            elif victory_type == 'Culture':
                avg_science_early = np.random.normal(10, 2)  # Medium science
                avg_culture_early = np.random.normal(12, 3)  # Higher culture
                science_trend = np.random.normal(0.9, 0.2)   # Slower science
                culture_trend = np.random.normal(1.3, 0.2)   # Strong culture trend
                relative_science_rank = np.random.uniform(0.3, 0.7)  # Medium rank
                relative_culture_rank = np.random.uniform(0.7, 1.0)  # High rank
                
            else:  # Other victory types
                avg_science_early = np.random.normal(12, 3)  # Medium science
                avg_culture_early = np.random.normal(10, 3)  # Medium culture
                science_trend = np.random.normal(1.0, 0.3)   # Balanced
                culture_trend = np.random.normal(1.0, 0.3)   # Balanced
                relative_science_rank = np.random.uniform(0.2, 0.8)  # Variable
                relative_culture_rank = np.random.uniform(0.2, 0.8)  # Variable
            
            turn_count = np.random.randint(5, 25)  # Early game analysis (turns 5-25)
            
            data.append({
                'avg_science_early': max(0, avg_science_early),
                'avg_culture_early': max(0, avg_culture_early),
                'science_trend': science_trend,
                'culture_trend': culture_trend,
                'relative_science_rank': np.clip(relative_science_rank, 0, 1),
                'relative_culture_rank': np.clip(relative_culture_rank, 0, 1),
                'turn_count': turn_count,
                'victory_type': victory_type
            })
        
        return pd.DataFrame(data)
    
    def train_model(self, data: pd.DataFrame):
        """Train the victory prediction model"""
        X = data[self.feature_columns]
        y = data['victory_type']
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Scale features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Train Random Forest model
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train_scaled, y_train)
        
        # Evaluate model
        y_pred = self.model.predict(X_test_scaled)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"📊 Model accuracy: {accuracy:.2f}")
        
        # Save model
        self.save_model()
    
    def save_model(self):
        """Save the trained model"""
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        
        model_data = {
            'model': self.model,
            'scaler': self.scaler,
            'feature_columns': self.feature_columns,
            'created_at': datetime.now().isoformat()
        }
        
        with open(self.model_path, 'wb') as f:
            pickle.dump(model_data, f)
        print(f"💾 Model saved to {self.model_path}")
    
    def predict_victory(self, game_data: Dict) -> Dict:
        """Predict victory type for a game"""
        if not self.model:
            return {'error': 'Model not available'}
        
        try:
            # Extract features from game data
            features = self.extract_features(game_data)
            if not features:
                return {'error': 'Insufficient data for prediction'}
            
            # Make prediction
            X = np.array([list(features.values())])
            X_scaled = self.scaler.transform(X)
            
            prediction = self.model.predict(X_scaled)[0]
            probabilities = self.model.predict_proba(X_scaled)[0]
            
            # Get class labels
            classes = self.model.classes_
            prob_dict = {cls: prob for cls, prob in zip(classes, probabilities)}
            
            return {
                'predicted_victory': prediction,
                'confidence': max(probabilities),
                'probabilities': prob_dict,
                'features_used': features
            }
            
        except Exception as e:
            return {'error': f'Prediction failed: {e}'}
    
    def extract_features(self, game_data: Dict) -> Optional[Dict]:
        """Extract features from game data for prediction"""
        try:
            # This would typically come from DataLoader
            # For now, simulate feature extraction
            
            if 'leaders' not in game_data or not game_data['leaders']:
                return None
            
            leaders = game_data['leaders']
            
            # Calculate average early game stats
            avg_science = np.mean([leader['avg_science'] for leader in leaders])
            avg_culture = np.mean([leader['avg_culture'] for leader in leaders])
            
            # Simple trend calculation (would be more sophisticated with time series)
            science_trend = 1.0  # Placeholder
            culture_trend = 1.0  # Placeholder
            
            # Relative rankings (top player = 1.0, bottom = 0.0)
            science_values = [leader['avg_science'] for leader in leaders]
            culture_values = [leader['avg_culture'] for leader in leaders]
            
            if len(science_values) > 1:
                science_rank = (max(science_values) - min(science_values))
                culture_rank = (max(culture_values) - min(culture_values))
                relative_science_rank = science_rank / max(science_values) if max(science_values) > 0 else 0.5
                relative_culture_rank = culture_rank / max(culture_values) if max(culture_values) > 0 else 0.5
            else:
                relative_science_rank = 0.5
                relative_culture_rank = 0.5
            
            features = {
                'avg_science_early': avg_science,
                'avg_culture_early': avg_culture,
                'science_trend': science_trend,
                'culture_trend': culture_trend,
                'relative_science_rank': relative_science_rank,
                'relative_culture_rank': relative_culture_rank,
                'turn_count': game_data.get('total_turns', 10)
            }
            
            return features
            
        except Exception as e:
            print(f"❌ Error extracting features: {e}")
            return None
    
    def retrain_with_real_data(self, real_data: pd.DataFrame):
        """Retrain model with real game data"""
        print("🔄 Retraining model with real game data...")
        
        # Combine with synthetic data for better performance
        synthetic_data = self.generate_synthetic_training_data()
        combined_data = pd.concat([synthetic_data, real_data], ignore_index=True)
        
        self.train_model(combined_data)
        print("✅ Model retrained with real data")


class GameAnalyzer:
    """Additional analysis tools for Civ VI games"""
    
    @staticmethod
    def analyze_civilization_strength(data: pd.DataFrame) -> Dict:
        """Analyze which civilizations perform best"""
        if data.empty:
            return {}
        
        civ_stats = data.groupby('civilization').agg({
            'science_per_turn': ['mean', 'max'],
            'culture_per_turn': ['mean', 'max'],
            'turn_number': 'max'
        }).round(2)
        
        return civ_stats.to_dict()
    
    @staticmethod
    def detect_victory_patterns(data: pd.DataFrame) -> List[Dict]:
        """Detect patterns that might indicate victory paths"""
        patterns = []
        
        # Science victory pattern: High science growth
        science_leaders = data.groupby(['game_id', 'player_name'])['science_per_turn'].mean().reset_index()
        science_leaders = science_leaders.nlargest(5, 'science_per_turn')
        
        for _, row in science_leaders.iterrows():
            patterns.append({
                'type': 'Science Victory Candidate',
                'game_id': row['game_id'],
                'player': row['player_name'],
                'science_per_turn': row['science_per_turn']
            })
        
        # Culture victory pattern: High culture growth
        culture_leaders = data.groupby(['game_id', 'player_name'])['culture_per_turn'].mean().reset_index()
        culture_leaders = culture_leaders.nlargest(5, 'culture_per_turn')
        
        for _, row in culture_leaders.iterrows():
            patterns.append({
                'type': 'Culture Victory Candidate',
                'game_id': row['game_id'],
                'player': row['player_name'],
                'culture_per_turn': row['culture_per_turn']
            })
        
        return patterns
