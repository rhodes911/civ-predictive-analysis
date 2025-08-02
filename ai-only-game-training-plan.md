# 🎯 AI-Only Game Training Data Collection Plan

**Creating a Robust Victory Prediction Model with Complete Game Data**

---

## 🚨 Current Problem Analysis

### **Why Our Current Model is Unreliable:**
- ❌ **No Complete Games**: We're training on incomplete/ongoing games
- ❌ **Unknown Outcomes**: We don't know who actually won these games
- ❌ **False Accuracy**: 97.6% accuracy is meaningless without true victory data
- ❌ **Biased Training**: Model learns patterns from games that may never finish

### **What We Need:**
- ✅ **Complete Games**: Full games from start to victory condition
- ✅ **Known Winners**: Clear victory outcomes (Science, Culture, Domination, etc.)
- ✅ **Diverse Scenarios**: Multiple game types, difficulties, and civilizations
- ✅ **Consistent Data**: Same CSV logging format throughout

---

## 🤖 AI-Only Game Data Collection Strategy

### **Phase 1: Automated Game Setup (Week 1)**

#### **1.1 Game Configuration**
```
Game Settings for Training Data:
┌─────────────────────────────────────────┐
│ Game Speed: Quick (150-200 turns)      │
│ Map Size: Standard (6 civilizations)   │
│ Difficulty: Prince (balanced AI)       │
│ Victory Types: All enabled             │
│ Civilizations: Random selection        │
│ Map Type: Continents (predictable)     │
└─────────────────────────────────────────┘
```

#### **1.2 Automation Requirements**
- **Target**: 50+ complete AI-only games
- **Duration**: Each game ~2-4 hours (Quick speed)
- **Data Points**: 6 civs × 150 turns × 50 games = 45,000+ records
- **Victory Distribution**: Mix of Science, Culture, Domination, Religious wins

#### **1.3 CSV Logging Verification**
```python
# Ensure consistent data collection
Required CSV Files per Game:
- Player_Stats.csv (core metrics)
- City_Stats.csv (city development)
- Victory_Progress.csv (victory condition tracking)
- Game_Summary.csv (final outcomes)
```

### **Phase 2: Data Collection Execution (Week 2-3)**

#### **2.1 Batch Game Execution**
```bash
# Automated game running schedule
Day 1-2:   Games 1-10   (Continents, Prince)
Day 3-4:   Games 11-20  (Pangaea, Prince)  
Day 5-6:   Games 21-30  (Island Plates, Prince)
Day 7-8:   Games 31-40  (Small Continents, Prince)
Day 9-10:  Games 41-50  (Mixed maps, Prince)
```

#### **2.2 Data Quality Monitoring**
- [ ] **Game Completion Check**: Verify each game reaches victory condition
- [ ] **CSV Integrity**: Ensure all CSV files generated completely
- [ ] **Victory Type Logging**: Record specific victory condition achieved
- [ ] **Turn Count Validation**: Confirm expected turn progression
- [ ] **Civilization Diversity**: Track which civs appear in dataset

#### **2.3 Real-Time Data Processing**
```python
# Process each completed game immediately
def process_completed_game(game_folder):
    """Process a completed AI game into training data"""
    
    # 1. Verify game completion
    victory_data = load_victory_summary(game_folder)
    if not victory_data['game_completed']:
        return False
    
    # 2. Extract winner and victory type
    winner = victory_data['winning_civilization']
    victory_type = victory_data['victory_condition']
    final_turn = victory_data['final_turn']
    
    # 3. Process turn-by-turn data with outcome labels
    training_records = []
    for turn in range(10, final_turn, 5):  # Every 5 turns from turn 10
        turn_data = extract_turn_data(game_folder, turn)
        for civ_data in turn_data:
            civ_data['will_win'] = 1 if civ_data['civilization'] == winner else 0
            civ_data['victory_type'] = victory_type
            civ_data['game_id'] = game_folder
            training_records.append(civ_data)
    
    return training_records
```

### **Phase 3: Enhanced Model Development (Week 4)**

#### **3.1 Improved Feature Engineering**
```python
# Enhanced features based on complete game data
features = {
    # Core metrics (existing)
    'turn_metrics': ['num_cities', 'population', 'techs', 'civics', 'yields_*'],
    
    # Victory-specific features (new)
    'science_victory_progress': ['current_science_projects', 'spaceport_cities'],
    'culture_victory_progress': ['tourism_output', 'visiting_tourists'],
    'domination_progress': ['cities_captured', 'capitals_owned'],
    'religious_progress': ['religion_spread', 'holy_sites'],
    
    # Advanced calculated features
    'momentum_indicators': ['science_per_turn_growth', 'culture_acceleration'],
    'relative_positioning': ['rank_in_science', 'rank_in_culture', 'rank_in_military'],
    'early_game_efficiency': ['techs_per_turn', 'cities_per_turn'],
    
    # Multi-turn trends
    'trend_features': ['last_5_turns_science_trend', 'population_growth_rate']
}
```

#### **3.2 Victory-Type Specific Models**
```python
# Separate models for different victory conditions
models = {
    'science_victory_predictor': RandomForestClassifier(),
    'culture_victory_predictor': RandomForestClassifier(), 
    'domination_victory_predictor': RandomForestClassifier(),
    'religious_victory_predictor': RandomForestClassifier(),
    'general_winner_predictor': RandomForestClassifier()  # Any victory type
}

# Victory-specific feature importance
science_features = ['techs', 'yields_science', 'campus_count', 'great_scientists']
culture_features = ['yields_culture', 'tourism', 'great_works', 'archeological_museums']
```

#### **3.3 Time-Based Prediction Models**
```python
# Different models for different game phases
prediction_phases = {
    'early_game': 'turns_10_30',    # Can we predict winner by turn 30?
    'mid_game': 'turns_30_60',      # Mid-game prediction accuracy
    'late_game': 'turns_60_plus',   # Late game confirmations
}

# Progressive accuracy expectations
target_accuracy = {
    'turn_30_prediction': '60%',    # Early prediction
    'turn_60_prediction': '80%',    # Mid-game prediction  
    'turn_100_prediction': '95%',   # Late game prediction
}
```

---

## 📊 Expected Data Structure

### **Complete Training Dataset Format**
```csv
game_id,civilization,game_turn,num_cities,population,techs,yields_science,
victory_type,will_win,final_turn,prediction_phase,civ_leader,map_type,difficulty
game_001,ENGLAND,15,2,8,3,4,SCIENCE,1,156,early_game,VICTORIA,CONTINENTS,PRINCE
game_001,FRANCE,15,3,12,2,3,SCIENCE,0,156,early_game,CATHERINE,CONTINENTS,PRINCE
game_001,GERMANY,15,2,7,4,5,SCIENCE,0,156,early_game,FREDERICK,CONTINENTS,PRINCE
...
```

### **Victory Condition Tracking**
```csv
game_id,winning_civ,victory_type,final_turn,runner_up,victory_margin,map_type
game_001,ENGLAND,SCIENCE,156,GERMANY,12_turns,CONTINENTS  
game_002,FRANCE,CULTURE,187,ENGLAND,2000_tourism,PANGAEA
game_003,ROME,DOMINATION,134,AZTEC,4_capitals,ISLAND_PLATES
```

---

## 🎯 Implementation Timeline

### **Week 1: Setup & Automation**
- [ ] Configure Civ VI for automated AI-only games
- [ ] Create game launch scripts and monitoring
- [ ] Test CSV data collection integrity
- [ ] Design game variant matrix (maps, civs, settings)

### **Week 2-3: Mass Data Collection**
- [ ] Run 50+ complete AI-only games
- [ ] Monitor data quality and game completion rates
- [ ] Process completed games into training format
- [ ] Track victory type distribution and game variety

### **Week 4: Advanced Model Training**
- [ ] Train victory-type specific models
- [ ] Implement time-based prediction accuracy
- [ ] Create ensemble model combining all predictors
- [ ] Validate accuracy against held-out complete games

### **Week 5: Integration & Testing**
- [ ] Deploy new models to prediction interface
- [ ] Test against ongoing human games (for fun)
- [ ] Create victory probability dashboards
- [ ] Document model accuracy and limitations

---

## 🔬 Expected Outcomes

### **Robust Prediction Accuracy**
```
Turn 30 Predictions:  ~65% accuracy (early strategic insights)
Turn 60 Predictions:  ~85% accuracy (mid-game confidence)
Turn 100 Predictions: ~95% accuracy (late-game confirmation)
```

### **Victory-Specific Insights**
- **Science Victory**: Focus on campus districts and research agreements
- **Culture Victory**: Tourism generation and wonder construction patterns
- **Domination Victory**: Military unit production and expansion timing
- **Religious Victory**: Faith generation and missionary effectiveness

### **Strategic Intelligence**
- **Early Warning System**: "Rome is building toward Domination victory"
- **Catch-Up Analysis**: "England needs 15% more science to stay competitive"
- **Victory Timeline**: "Current leader likely wins in 45 turns"
- **Counter-Strategy**: "Focus on culture defense against France's tourism"

---

## 🚀 Beyond Basic Prediction

### **Advanced Analytics Possibilities**
1. **Victory Path Optimization**: "Best tech path for Science victory from current position"
2. **Threat Assessment**: "Germany's military buildup suggests Domination attempt"
3. **Diplomatic Strategy**: "Form alliance with 2nd place to stop leader"
4. **Resource Allocation**: "Prioritize campuses over commercial hubs for win"

### **Multi-Player Applications**
- **Human vs AI Prediction**: How do human strategies differ from AI patterns?
- **Player Skill Assessment**: "This player's style matches a Science victory approach"
- **Live Strategy Coaching**: Real-time suggestions based on ML analysis

---

## 💡 Success Metrics

### **Data Quality Goals**
- ✅ 50+ complete games with known outcomes
- ✅ Balanced victory type distribution (25% each victory type)
- ✅ Diverse civilization and map representation
- ✅ Consistent CSV data format across all games

### **Model Performance Goals**
- ✅ 65%+ accuracy at Turn 30 (early game prediction)
- ✅ 85%+ accuracy at Turn 60 (mid game prediction)  
- ✅ 95%+ accuracy at Turn 100 (late game prediction)
- ✅ Victory-type specific insights and recommendations

### **User Experience Goals**
- ✅ Real-time victory probability updates
- ✅ Strategic recommendations based on current position
- ✅ Victory path analysis and optimization
- ✅ Competitive intelligence for multiplayer games

---

**This plan transforms the prediction system from "interesting but unreliable" to "strategically valuable and accurate" by using proper training data with known outcomes.** 🎯🏆
