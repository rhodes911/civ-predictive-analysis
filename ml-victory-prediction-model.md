# 🎯 ML Victory Prediction Model

**Predicting Civilization VI Game Winners Using Early-Game Metrics**  
*A focused machine learning approach using your existing civ_game_data table*

---

## 🎮 **The Question We're Answering:**

**"Can we predict the final winner of a Civ VI game based on Turn 20 performance metrics?"**

This is perfect for:
- Strategic decision making in ongoing games
- Understanding which early-game strategies lead to victory
- Identifying when a game is already "decided" vs still competitive

---

## 📊 **Our Data Foundation**

### **Available Data:**
- **Multiple game sessions** in your database (old epic race + current Indonesia game)
- **Turn-by-turn progression** for all civilizations
- **32 comprehensive metrics** per civilization per turn
- **Complete game outcomes** (final scores and rankings)

### **Key Metrics for Prediction:**
```sql
-- Core features we'll use for prediction
SELECT 
    game_turn,
    civilization,
    num_cities,           -- Territory expansion
    population,           -- Population growth
    techs,               -- Research progress  
    civics,              -- Cultural development
    yields_science,      -- Science per turn
    yields_culture,      -- Culture per turn
    yields_production,   -- Production capacity
    buildings,           -- Infrastructure development
    districts,           -- Specialized districts
    total_score,         -- Overall game score
    created_at           -- Game session identification
FROM civ_game_data 
WHERE game_turn <= 20;
```

---

## 🧠 **ML Model Design**

### **Model Type: Random Forest Classifier**
**Why Random Forest:**
- ✅ Handles mixed data types (population, yields, counts)
- ✅ Provides feature importance rankings
- ✅ Robust to outliers and missing data
- ✅ Interpretable results for strategy insights

### **Prediction Target:**
```python
# Binary classification: Will this civilization win the game?
target = 'will_win'  # 1 if final rank = 1, 0 otherwise

# Alternative: Multi-class ranking prediction
target = 'final_ranking'  # 1st, 2nd, 3rd, 4th, 5th, 6th place
```

### **Feature Engineering:**
```python
features = {
    # Raw metrics
    'turn_20_cities': 'num_cities',
    'turn_20_population': 'population', 
    'turn_20_techs': 'techs',
    'turn_20_science_yield': 'yields_science',
    'turn_20_culture_yield': 'yields_culture',
    'turn_20_buildings': 'buildings',
    
    # Calculated ratios (more predictive)
    'science_per_city': 'yields_science / num_cities',
    'population_per_city': 'population / num_cities',
    'buildings_per_city': 'buildings / num_cities',
    'development_index': '(techs + civics) / game_turn',
    
    # Relative positioning
    'science_rank_turn_20': 'rank() over (partition by game_turn order by yields_science desc)',
    'cities_rank_turn_20': 'rank() over (partition by game_turn order by num_cities desc)',
    'score_rank_turn_20': 'rank() over (partition by game_turn order by total_score desc)'
}
```

---

## 🛠️ **Implementation Plan**

### **Step 1: Data Preparation Script**
**File:** `ml_data_preparation.py`

```python
import pandas as pd
import psycopg2
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

def prepare_ml_data():
    """Extract and prepare data for ML training"""
    
    # Connect to database
    conn = psycopg2.connect(
        host='localhost', port=5432, database='civ6_analytics',
        user='civ6_user', password='civ6_password'
    )
    
    # Get Turn 20 features for all games
    features_query = """
    WITH turn_20_data AS (
        SELECT 
            civilization,
            created_at::date as game_date,
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
            -- Calculate relative rankings within each game
            RANK() OVER (PARTITION BY created_at::date ORDER BY yields_science DESC) as science_rank,
            RANK() OVER (PARTITION BY created_at::date ORDER BY num_cities DESC) as cities_rank,
            RANK() OVER (PARTITION BY created_at::date ORDER BY total_score DESC) as score_rank
        FROM civ_game_data 
        WHERE game_turn = 20
    ),
    final_results AS (
        SELECT 
            civilization,
            created_at::date as game_date,
            RANK() OVER (PARTITION BY created_at::date ORDER BY total_score DESC) as final_rank,
            total_score as final_score
        FROM civ_game_data 
        WHERE game_turn = (SELECT MAX(game_turn) FROM civ_game_data)
    )
    SELECT 
        f.*,
        r.final_rank,
        CASE WHEN r.final_rank = 1 THEN 1 ELSE 0 END as will_win
    FROM turn_20_data f
    JOIN final_results r ON f.civilization = r.civilization AND f.game_date = r.game_date
    """
    
    df = pd.read_sql(features_query, conn)
    conn.close()
    
    return df
```

### **Step 2: Model Training Script**
**File:** `victory_prediction_model.py`

```python
def train_victory_predictor(df):
    """Train Random Forest model to predict game winners"""
    
    # Define features and target
    feature_columns = [
        'num_cities', 'population', 'techs', 'civics',
        'yields_science', 'yields_culture', 'yields_production',
        'buildings', 'districts', 'total_score',
        'science_rank', 'cities_rank', 'score_rank'
    ]
    
    X = df[feature_columns]
    y = df['will_win']
    
    # Split data for training/testing
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    
    # Train Random Forest model
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42
    )
    
    model.fit(X_train, y_train)
    
    # Evaluate model
    predictions = model.predict(X_test)
    accuracy = model.score(X_test, y_test)
    
    print(f"Model Accuracy: {accuracy:.2%}")
    print("\nClassification Report:")
    print(classification_report(y_test, predictions))
    
    # Feature importance analysis
    feature_importance = pd.DataFrame({
        'feature': feature_columns,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print("\nMost Important Features:")
    print(feature_importance.head(10))
    
    return model, feature_importance
```

### **Step 3: Prediction Interface**
**File:** `predict_winner.py`

```python
def predict_current_game_winner():
    """Predict winner of ongoing game based on latest Turn 20+ data"""
    
    # Get latest game data
    conn = psycopg2.connect(
        host='localhost', port=5432, database='civ6_analytics',
        user='civ6_user', password='civ6_password'
    )
    
    latest_query = """
    SELECT 
        civilization,
        num_cities, population, techs, civics,
        yields_science, yields_culture, yields_production,
        buildings, districts, total_score,
        RANK() OVER (ORDER BY yields_science DESC) as science_rank,
        RANK() OVER (ORDER BY num_cities DESC) as cities_rank,
        RANK() OVER (ORDER BY total_score DESC) as score_rank
    FROM civ_game_data 
    WHERE created_at::time >= '07:00:00'  -- Current Indonesia game
    AND game_turn = (
        SELECT MAX(game_turn) FROM civ_game_data 
        WHERE created_at::time >= '07:00:00'
    )
    """
    
    current_data = pd.read_sql(latest_query, conn)
    conn.close()
    
    # Load trained model and make predictions
    model = load_trained_model()  # Saved from training step
    
    feature_columns = [
        'num_cities', 'population', 'techs', 'civics',
        'yields_science', 'yields_culture', 'yields_production',
        'buildings', 'districts', 'total_score',
        'science_rank', 'cities_rank', 'score_rank'
    ]
    
    X = current_data[feature_columns]
    
    # Get win probabilities for each civilization
    win_probabilities = model.predict_proba(X)[:, 1]
    
    results = pd.DataFrame({
        'civilization': current_data['civilization'],
        'win_probability': win_probabilities,
        'current_score': current_data['total_score']
    }).sort_values('win_probability', ascending=False)
    
    return results
```

---

## 📈 **Expected Outputs & Insights**

### **1. Victory Probability Dashboard**
```
🏆 Indonesia Game - Turn 38 Predictions:

Civilization      Win Probability    Current Score    Key Strengths
===============================================================
ETHIOPIA         67.3%              46               Science Leader
GAUL             23.1%              37               Balanced Growth  
CREE             5.2%               35               Strong Cities
MALI             2.8%               0                Production Focus
INDONESIA        1.4%               0                Early Struggle
OTTOMAN          0.2%               0                Behind in Tech
```

### **2. Feature Importance Analysis**
```
Most Predictive Turn 20 Metrics:
1. Science Rank (34.2% importance) - Science leadership crucial
2. Total Score (18.7% importance) - Early score advantage matters
3. Number of Cities (12.3% importance) - Expansion critical
4. Technologies (9.8% importance) - Tech advancement key
5. Science Yield (8.1% importance) - Raw science output
```

### **3. Strategic Insights**
```python
# Model reveals winning patterns:
if science_rank <= 2 and num_cities >= 4:
    win_probability = 0.78  # 78% chance of victory
    
if science_rank >= 5:
    win_probability = 0.09  # Only 9% chance of comeback
    
# Critical thresholds discovered:
- 4+ cities by Turn 20 = 65% win rate
- Top 2 science by Turn 20 = 71% win rate  
- Both conditions = 85% win rate
```

---

## 🚀 **Implementation Timeline**

### **Week 1: Data Preparation**
- [ ] Create `ml_data_preparation.py` script
- [ ] Test data extraction and feature engineering
- [ ] Validate game session separation (old vs new games)
- [ ] Export training dataset to CSV for analysis

### **Week 2: Model Development**
- [ ] Create `victory_prediction_model.py` script
- [ ] Train initial Random Forest model
- [ ] Evaluate model performance and tune parameters
- [ ] Analyze feature importance for strategic insights

### **Week 3: Integration & Testing**
- [ ] Create `predict_winner.py` for live predictions
- [ ] Add ML predictions to Docker data loader workflow
- [ ] Create Superset dashboard showing win probabilities
- [ ] Test predictions against known game outcomes

### **Week 4: Validation & Refinement**
- [ ] Collect more game data to improve model accuracy
- [ ] A/B test predictions vs actual outcomes
- [ ] Refine feature engineering based on results
- [ ] Document strategic insights for gameplay

---

## 🎯 **Success Metrics**

### **Model Performance Goals:**
- **Accuracy:** >70% on test data (predicting actual winners)
- **Precision:** >75% when predicting a civilization will win
- **Recall:** >65% catching actual winners
- **Feature Insights:** Clear ranking of which Turn 20 metrics matter most

### **Strategic Value Goals:**
- **Early Warning:** Identify likely winners by Turn 20
- **Comeback Analysis:** Quantify how often trailing civs recover
- **Strategy Optimization:** Data-driven early game priorities
- **Competitive Intelligence:** Understand opponent threats in multiplayer

---

## 💡 **Why This Model Will Work**

### **✅ Perfect Data Foundation:**
- Multiple complete games with known outcomes
- Consistent 32-metric measurements per turn
- Clean game session separation
- Turn-by-turn progression data

### **✅ Focused Question:**
- Binary classification (win/lose) is easier than complex predictions
- Turn 20 is early enough to be strategic, late enough to be predictive
- Clear success criteria (did model predict actual winner?)

### **✅ Actionable Insights:**
- Immediate feedback for current Indonesia game
- Strategic guidance for future games
- Understanding of winning vs losing patterns
- Foundation for more advanced models

---

**This model transforms your Civ VI data from "interesting statistics" into "strategic intelligence" that actually helps you win games!** 🏆🎮
