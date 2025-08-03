# 🔗 Civ VI CSV Relationship Analysis Report

**Generated:** 2025-08-03 19:23:01
**Total Files Analyzed:** 623

---

## 📊 File Categorization

### 🏆 Core Statistics Files (3)
- `Game_PlayerScores.csv`
- `Player_Stats.csv`
- `Player_Stats_2.csv`

### 🤖 AI Behavior Files (12)
- `AI_CityBuild.csv`
- `AI_Diplomacy.csv`
- `AI_Espionage.csv`
- `AI_Governors.csv`
- `AI_GovtPolicies.csv`
- `AI_MayhemTracker.csv`
- `AI_Military.csv`
- `AI_Operation.csv`
- `AI_Religious.csv`
- `AI_Research.csv`
- `AI_UnitEfficiency.csv`
- `AI_Victories.csv`

### ⚔️ Military & Combat Files (3)
- `Barbarians.csv`
- `Barbarians_Units.csv`
- `CombatLog.csv`

### 🤝 Diplomacy Files (2)
- `DiplomacyManager.csv`
- `DiplomacySummary.csv`

### 🏙️ City Management Files (1)
- `City_BuildQueue.csv`

### 🎭 Culture & Religion Files (2)
- `Cultural_Identity.csv`
- `Game_Religion.csv`

### 🎮 Game Systems Files (10)
- `Game_Boosts.csv`
- `Game_GreatPeople.csv`
- `Game_HeroesManager_HeroStats.csv`
- `Game_HeroesManager_PlayerStats.csv`
- `Game_Influence.csv`
- `Game_RandomEvents.csv`
- `Governors.csv`
- `Player_WarWeariness.csv`
- `Profile.csv`
- `UIWarnings.csv`

---

## 🔗 Relationship Networks

### ⏰ Temporal Network (Turn-based analysis)
**Files with Game Turn data:** 30
- `AI_GovtPolicies.csv`
- `DiplomacySummary.csv`
- `Cultural_Identity.csv`
- `AI_Espionage.csv`
- `Game_RandomEvents.csv`
- `City_BuildQueue.csv`
- `AI_CityBuild.csv`
- `Game_HeroesManager_HeroStats.csv`
- `DiplomacyManager.csv`
- `AI_Religious.csv`
- `Game_GreatPeople.csv`
- `Barbarians_Units.csv`
- `Player_Stats.csv`
- `AI_Military.csv`
- `Game_Boosts.csv`
- `AI_Victories.csv`
- `AI_Diplomacy.csv`
- `AI_Governors.csv`
- `Game_Religion.csv`
- `Player_Stats_2.csv`
- `Game_HeroesManager_PlayerStats.csv`
- `CombatLog.csv`
- `Game_PlayerScores.csv`
- `AI_MayhemTracker.csv`
- `Game_Influence.csv`
- `Barbarians.csv`
- `Governors.csv`
- `Game_TradeManager.csv`
- `AI_Research.csv`
- `AI_Operation.csv`

### 🏛️ Competitive Network (Player-based analysis)  
**Files with Player data:** 18
- `AI_GovtPolicies.csv`
- `AI_Governors.csv`
- `Game_Religion.csv`
- `AI_CityBuild.csv`
- `Player_Stats_2.csv`
- `Game_PlayerScores.csv`
- `AI_Religious.csv`
- `Player_WarWeariness.csv`
- `Game_HeroesManager_PlayerStats.csv`
- `Game_GreatPeople.csv`
- `AI_Research.csv`
- `Player_Stats.csv`
- `AI_Victories.csv`
- `AI_Espionage.csv`
- `AI_Military.csv`
- `Game_Boosts.csv`
- `AI_Operation.csv`
- `AI_Diplomacy.csv`

### 🏗️ Core Junction (Turn + Player)
**Files with both Turn and Player data:** 17
- `AI_GovtPolicies.csv`
- `AI_Governors.csv`
- `Game_Religion.csv`
- `AI_CityBuild.csv`
- `Player_Stats_2.csv`
- `AI_Operation.csv`
- `AI_Religious.csv`
- `AI_Military.csv`
- `Game_HeroesManager_PlayerStats.csv`
- `Game_GreatPeople.csv`
- `AI_Research.csv`
- `Player_Stats.csv`
- `AI_Espionage.csv`
- `Game_PlayerScores.csv`
- `Game_Boosts.csv`
- `AI_Victories.csv`
- `AI_Diplomacy.csv`

---

## 🔑 Join Key Analysis

### 🕐 Temporal Keys (Game Turn)
**Files:** 34
```
AI_CityBuild.csv: 'Game Turn'
AI_Diplomacy.csv: 'Game Turn'
AI_Espionage.csv: 'Game Turn'
AI_Governors.csv: 'Game Turn'
AI_GovtPolicies.csv: 'Game Turn'
AI_GovtPolicies.csv: ' Turns'
AI_MayhemTracker.csv: 'Game Turn'
AI_Military.csv: 'Game Turn'
AI_Operation.csv: 'Game Turn'
AI_Religious.csv: 'Game Turn'
... and 24 more files
```

### 👑 Player Keys  
**Files:** 19
```
AI_CityBuild.csv: ' Player'
AI_Diplomacy.csv: ' Player'
AI_Espionage.csv: ' Player'
AI_Governors.csv: ' Player'
AI_GovtPolicies.csv: ' Player'
AI_Military.csv: ' Player'
AI_Operation.csv: ' Player'
AI_Religious.csv: ' Player'
AI_Research.csv: ' Player'
AI_Victories.csv: ' Player'
... and 9 more files
```

### 🏘️ City Keys
**Files:** 8
```
AI_CityBuild.csv: ' City'
AI_Espionage.csv: ' City'
City_BuildQueue.csv: ' City'
Cultural_Identity.csv: ' CityName'
Game_Religion.csv: ' City'
Game_TradeManager.csv: ' Origin City'
Game_TradeManager.csv: ' Destination City'
Governors.csv: ' City'
```

---

## 💾 Recommended Database Schema


-- Master player statistics table
CREATE TABLE player_stats (
    game_turn INTEGER,
    player_name VARCHAR(50),
    num_cities INTEGER,
    population INTEGER,
    techs INTEGER,
    civics INTEGER,
    yield_science INTEGER,
    yield_culture INTEGER,
    yield_production INTEGER,
    total_score INTEGER,
    PRIMARY KEY (game_turn, player_name)
);

-- Player scoring breakdown
CREATE TABLE player_scores (
    game_turn INTEGER,
    player_id INTEGER,
    total_score INTEGER,
    score_civics INTEGER,
    score_empire INTEGER,
    score_tech INTEGER,
    score_religion INTEGER,
    FOREIGN KEY (game_turn) REFERENCES player_stats(game_turn)
);



-- AI decision tracking
CREATE TABLE ai_decisions (
    game_turn INTEGER,
    player_name VARCHAR(50),
    decision_type VARCHAR(100),
    decision_value VARCHAR(500),
    priority_score DECIMAL,
    FOREIGN KEY (game_turn, player_name) REFERENCES player_stats(game_turn, player_name)
);

-- AI military strategy
CREATE TABLE ai_military_strategy (
    game_turn INTEGER,
    player_name VARCHAR(50),
    strategy_type VARCHAR(100),
    target_player VARCHAR(50),
    unit_allocation JSON,
    FOREIGN KEY (game_turn, player_name) REFERENCES player_stats(game_turn, player_name)
);



-- City management decisions
CREATE TABLE city_decisions (
    game_turn INTEGER,
    player_name VARCHAR(50),
    city_name VARCHAR(100),
    decision_type VARCHAR(100),
    production_item VARCHAR(100),
    priority_score DECIMAL,
    FOREIGN KEY (game_turn, player_name) REFERENCES player_stats(game_turn, player_name)
);

-- Trade and economic data
CREATE TABLE economic_state (
    game_turn INTEGER,
    player_name VARCHAR(50),
    gold_balance INTEGER,
    gold_per_turn INTEGER,
    trade_routes INTEGER,
    luxury_resources JSON,
    FOREIGN KEY (game_turn, player_name) REFERENCES player_stats(game_turn, player_name)
);


---

## 🎯 ML Analysis Opportunities

### Victory Prediction Models
- **Data Sources:** AI_GovtPolicies.csv, AI_Governors.csv, Game_Religion.csv, AI_CityBuild.csv, Player_Stats_2.csv...
- **Key Features:** Science yields, Culture yields, Military units, Diplomacy scores
- **Prediction Target:** Victory type and timing

### Strategic Decision Analysis  
- **Data Sources:** AI_CityBuild.csv, AI_Diplomacy.csv, AI_Espionage.csv...
- **Key Features:** AI decision patterns, Resource allocation, Priority scoring
- **Analysis Target:** Optimal strategy identification

### Economic Modeling
- **Data Sources:** City_BuildQueue.csv, Game_TradeManager.csv
- **Key Features:** City production, Trade routes, Resource management
- **Modeling Target:** Economic efficiency optimization

---

## 🚀 Implementation Priority

### Phase 1: Core Data Pipeline
1. Load core statistics files (3 files)
2. Establish temporal and player relationships
3. Create unified player progression dataset

### Phase 2: AI Behavior Integration
1. Process AI decision files (12 files)  
2. Link decisions to outcomes
3. Build decision effectiveness models

### Phase 3: Advanced Analytics
1. Integrate all domain-specific files
2. Create comprehensive game state representation
3. Build predictive models for all victory types

---

**🎮 Result: Complete relational framework for Civilization VI game intelligence and ML analysis!**
