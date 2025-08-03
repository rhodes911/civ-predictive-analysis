# Civ VI CSV Files - Database Mapping & Analysis Summary

**Generated:** 2025-08-03  
**Full Game:** 500+ turns complete  
**Total CSV Files:** 45 files analyzed  
**Successfully Parsed:** 34 files  
**Data Volume:** ~438 MB total

---

## 🎯 Key Files for ML Victory Prediction

### **Primary Data Sources (Successfully Parsed)**

#### 1. **Player_Stats.csv** ⭐⭐⭐
- **Purpose:** Core civilization statistics per turn
- **Size:** 708 KB, 7,948 rows, 20 columns
- **Coverage:** 503 turns × 16 civilizations
- **Key Metrics:** Cities, Population, Tech/Civics progress, Military units, Resources, Yields

```sql
-- Recommended table structure
CREATE TABLE player_stats (
    game_turn INTEGER,
    player_name VARCHAR(50),
    num_cities INTEGER,
    population INTEGER,
    techs INTEGER,
    civics INTEGER,
    land_units INTEGER,
    corps INTEGER,
    armies INTEGER,
    naval_units INTEGER,
    tiles_owned INTEGER,
    tiles_improved INTEGER,
    balance_gold INTEGER,
    balance_faith INTEGER,
    yield_science INTEGER,
    yield_culture INTEGER,
    yield_gold INTEGER,
    yield_faith INTEGER,
    yield_production INTEGER,
    yield_food INTEGER
);
```

#### 2. **Player_Stats_2.csv** ⭐⭐⭐  
- **Purpose:** Extended civilization metrics
- **Size:** 474 KB, 7,948 rows, 12 columns
- **Key Metrics:** Buildings, Districts, Trade Routes, Tourism, Diplomacy, Environmental

```sql
CREATE TABLE player_stats_extended (
    game_turn INTEGER,
    player_name VARCHAR(50),
    tiles_by_type INTEGER,
    buildings INTEGER,
    districts INTEGER,
    population_alt INTEGER,
    outgoing_trade_routes INTEGER,
    tourism INTEGER,
    diplo_victory_points INTEGER,
    balance_favor INTEGER,
    lifetime_favor INTEGER,
    co2_per_turn INTEGER
);
```

#### 3. **Game_PlayerScores.csv** ⭐⭐⭐
- **Purpose:** Detailed scoring breakdown by category
- **Size:** 459 KB, 8,450 rows, 16 columns  
- **Key Metrics:** Total score plus category breakdowns

```sql
CREATE TABLE player_scores (
    game_turn INTEGER,
    player_id INTEGER,
    total_score INTEGER,
    score_civics INTEGER,
    score_empire INTEGER,
    score_great_people INTEGER,
    score_religion INTEGER,
    score_tech INTEGER,
    score_wonder INTEGER,
    score_trade INTEGER,
    score_pillage INTEGER,
    score_income INTEGER,
    score_scenario1 INTEGER,
    score_scenario2 INTEGER,
    score_scenario3 INTEGER,
    score_category_e INTEGER
);
```

---

## 🔍 Secondary Data Sources (High Value)

#### 4. **Game_GreatPeople.csv** ⭐⭐
- **Purpose:** Great People recruitment tracking
- **Size:** 20 KB, 230 rows, 8 columns
- **Value:** Great People often correlate with victory conditions

#### 5. **Game_Religion.csv** ⭐⭐
- **Purpose:** Religious spread and founding
- **Size:** 96 KB, 1,545 rows, 8 columns
- **Value:** Essential for Religious Victory tracking

#### 6. **Cultural_Identity.csv** ⭐⭐
- **Purpose:** Cultural influence between civilizations
- **Size:** 3.7 MB, 51,588 rows, 6 columns
- **Value:** Important for Cultural Victory analysis

#### 7. **DiplomacySummary.csv** ⭐⭐
- **Purpose:** Diplomatic relationships overview
- **Size:** 4.5 MB, 60,398 rows, 6 columns
- **Value:** Key for Diplomatic Victory prediction

---

## 📊 Data Quality & Coverage Analysis

### **Temporal Coverage**
```
Game Duration: 503 turns (full game completion)
Turn 1-100: Early game establishment
Turn 101-300: Mid-game expansion & competition  
Turn 301-503: Late game victory push & completion
```

### **Civilization Coverage**
```
Total Civilizations: 16 active
Major Civilizations: ~6-8 consistently tracked
City-States/Barbarians: Included in some logs
Player ID Mapping: 0-63 range (sparse)
```

### **Data Completeness**
```
✅ Player_Stats.csv: 100% coverage (7,948/7,948 records)
✅ Player_Stats_2.csv: 100% coverage (7,948/7,948 records)  
✅ Game_PlayerScores.csv: Full coverage (8,450 records)
⚠️  Some files malformed (11/45 files had parsing errors)
```

---

## 🗺️ Column Mapping Reference

### **Core Victory Prediction Features**

| CSV File | Column | Database Column | Type | ML Feature |
|----------|--------|-----------------|------|------------|
| Player_Stats.csv | ` YIELDS: Science` | yield_science | INTEGER | Science Victory |
| Player_Stats.csv | ` Culture` | yield_culture | INTEGER | Culture Victory |
| Player_Stats.csv | ` Num Cities` | num_cities | INTEGER | Domination Victory |
| Player_Stats_2.csv | ` Diplo Victory` | diplo_victory_points | INTEGER | Diplomatic Victory |
| Player_Stats_2.csv | ` TOURISM` | tourism | INTEGER | Culture Victory |
| Game_PlayerScores.csv | ` Score` | total_score | INTEGER | Overall Progress |

### **Supporting Features**

| Feature Category | Primary Source | Key Columns |
|------------------|----------------|-------------|
| **Military Power** | Player_Stats.csv | Land Units, corps, Armies, Naval Units |
| **Economic Strength** | Player_Stats.csv | BALANCE: Gold, Gold yield, Production |
| **Religious Influence** | Player_Stats.csv | Faith, Faith.1 + Game_Religion.csv |
| **Territory Control** | Player_Stats.csv | TILES: Owned, Improved |
| **Infrastructure** | Player_Stats_2.csv | Buildings, Districts |
| **Technology Progress** | Player_Stats.csv | Techs, Civics |

---

## 🔧 Implementation Strategy

### **Phase 1: Core Data Integration**
```sql
-- Create unified view for ML features
CREATE VIEW ml_training_data AS
SELECT 
    ps.game_turn,
    ps.player_name,
    ps.yield_science,
    ps.yield_culture, 
    ps.num_cities,
    ps2.diplo_victory_points,
    ps2.tourism,
    sc.total_score,
    -- Add derived features
    (ps.yield_science + ps.yield_culture + ps.yield_production) as total_yields,
    (ps.land_units + ps.naval_units) as total_military,
    ps2.buildings + ps2.districts as infrastructure_total
FROM player_stats ps
JOIN player_stats_extended ps2 ON ps.game_turn = ps2.game_turn AND ps.player_name = ps2.player_name  
JOIN player_scores sc ON ps.game_turn = sc.game_turn AND ps.player_name = sc.player_name;
```

### **Phase 2: Data Processing Pipeline**
1. **CSV Import Script:** Automated loading with data validation
2. **Data Cleaning:** Handle malformed records, normalize civilization names
3. **Feature Engineering:** Create derived metrics, rolling averages, ratios
4. **Victory Detection:** Identify winner and victory type from final turns

### **Phase 3: ML Feature Set**
```python
# Primary features for victory prediction
CORE_FEATURES = [
    'yield_science', 'yield_culture', 'tourism', 
    'diplo_victory_points', 'num_cities', 'total_score'
]

# Supporting features
EXTENDED_FEATURES = [
    'population', 'techs', 'civics', 'total_military',
    'infrastructure_total', 'balance_gold', 'tiles_owned'
]

# Time-based features
TEMPORAL_FEATURES = [
    'turn_number', 'game_phase', 'time_to_end',
    'science_growth_rate', 'culture_growth_rate'
]
```

---

## ⚠️ Known Issues & Limitations

### **Malformed CSV Files (11 files)**
```
❌ AI_Behavior_Trees.csv (285MB) - Embedded commas in data
❌ AI_Planning.csv (44MB) - Column count mismatch  
❌ AI_Knowledge.csv (20MB) - Extra fields
❌ DynamicEmpires.csv - Quote escaping issues
❌ RandCalls.csv - Inconsistent field counts
```

### **Data Inconsistencies**
- Player names have leading spaces (` CIVILIZATION_POLAND`)
- Duplicate Faith columns (`Faith` and `Faith.1`)
- Some category scores always zero (Trade, Pillage, Income)

### **Parsing Solutions**
```python
# Robust CSV parsing for malformed files
def parse_malformed_csv(file_path):
    try:
        # Try standard parsing first
        return pd.read_csv(file_path)
    except:
        # Fallback: custom parsing with error handling
        return pd.read_csv(file_path, 
                          error_bad_lines=False, 
                          warn_bad_lines=True,
                          quoting=csv.QUOTE_NONE)
```

---

## 🎯 Next Steps

1. **Create enhanced data loader** targeting the 3 core CSV files
2. **Implement data validation** and cleaning pipeline  
3. **Build feature engineering** pipeline with derived metrics
4. **Design victory detection** logic for training labels
5. **Test ML pipeline** with this rich 500-turn dataset

This analysis shows we have excellent data coverage for ML training with **7,948 civilization-turn records** across **503 turns** and **16 civilizations**! 🎮📊
