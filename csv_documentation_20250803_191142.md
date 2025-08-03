# Civ VI CSV Files Analysis & Documentation

**Generated:** 2025-08-03 19:11:42

**Total Files Analyzed:** 45

---

## AI_Behavior_Trees.csv

**File Statistics:**
- Size: 285297.56 KB
- Rows: 0
- Columns: 0
- Memory Usage: 0 MB

❌ **Error:** Error tokenizing data. C error: Expected 7 fields in line 11, saw 8


## AI_ChokePoint.csv

**File Statistics:**
- Size: 1142.35 KB
- Rows: 0
- Columns: 0
- Memory Usage: 0 MB

❌ **Error:** Error tokenizing data. C error: Expected 4 fields in line 4643, saw 7


## AI_CityBuild.csv

**File Statistics:**
- Size: 3746.63 KB
- Rows: 29,340
- Columns: 7
- Memory Usage: 10.57 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Game Turn` | object | 28,702 | 2,177 |  YIELD_PRODUCTION: 0.0,  YIELD_PRODUCTION: 0.0,   |  |
| ` Player` | object | 26,634 | 26 |  YIELD_GOLD: 0.0,  YIELD_GOLD: 0.1,   |  |
| ` City` | object | 26,634 | 4,236 |  YIELD_SCIENCE: 0.1,  YIELD_SCIENCE: 0.0,  Valu... |  |
| ` Food Adv.` | object | 25,846 | 15 |  YIELD_CULTURE: 0.0,  YIELD_CULTURE: 0.0,  YIEL... | Top:  Build City Improvement,  Build City Building |
| ` Prod. Adv.` | object | 150 | 3 |  YIELD_FAITH: 0.0,  YIELD_FAITH: 0.0,  YIELD_FA... | Top:  YIELD_FAITH: 0.0,  YIELD_FAITH: 0.1 |
| ` Construct` | object | 150 | 1 |  ,  ,   | Top:   |
| ` Order Source` | object | 150 | 1 |  ,  ,   | Top:   |

### Sample Data

```json
[
  {
    "Game Turn": " YIELD_PRODUCTION: 0.0",
    " Player": " YIELD_GOLD: 0.0",
    " City": " YIELD_SCIENCE: 0.1",
    " Food Adv.": " YIELD_CULTURE: 0.0",
    " Prod. Adv.": " YIELD_FAITH: 0.0",
    " Construct": " ",
    " Order Source": " "
  },
  {
    "Game Turn": " YIELD_PRODUCTION: 0.0",
    " Player": " YIELD_GOLD: 0.1",
    " City": " YIELD_SCIENCE: 0.0",
    " Food Adv.": " YIELD_CULTURE: 0.0",
    " Prod. Adv.": " YIELD_FAITH: 0.0",
    " Construct": " ",
    " Order Source": " "
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `ai_citybuild`

**Column Mappings:**
- `Game Turn` → VARCHAR(100)
- ` Player` → VARCHAR(100)
- ` City` → VARCHAR(100)
- ` Food Adv.` → VARCHAR(100)
- ` Prod. Adv.` → VARCHAR(100)
- ` Construct` → VARCHAR(100)
- ` Order Source` → VARCHAR(100)

---

## AI_Diplomacy.csv

**File Statistics:**
- Size: 3505.93 KB
- Rows: 16,900
- Columns: 21
- Memory Usage: 5.86 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Game Turn` | float64 | 0 | 0 |  | Range: nan - nan |
| ` Player` | float64 | 0 | 0 |  | Range: nan - nan |
| ` Action` | float64 | 0 | 0 |  | Range: nan - nan |
| ` ` | float64 | 0 | 0 |  | Range: nan - nan |
| ` 0` | float64 | 0 | 0 |  | Range: nan - nan |
| ` 1` | float64 | 0 | 0 |  | Range: nan - nan |
| ` 2` | float64 | 0 | 0 |  | Range: nan - nan |
| ` 3` | float64 | 0 | 0 |  | Range: nan - nan |
| ` 4` | float64 | 0 | 0 |  | Range: nan - nan |
| ` 5` | float64 | 0 | 0 |  | Range: nan - nan |
| ` 6` | float64 | 0 | 0 |  | Range: nan - nan |
| ` 7` | float64 | 0 | 0 |  | Range: nan - nan |
| ` 8` | float64 | 0 | 0 |  | Range: nan - nan |
| ` 9` | float64 | 0 | 0 |  | Range: nan - nan |
| ` 10` | float64 | 0 | 0 |  | Range: nan - nan |
| ` 11` | float64 | 0 | 0 |  | Range: nan - nan |
| ` 12` | float64 | 0 | 0 |  | Range: nan - nan |
| ` 13` | float64 | 0 | 0 |  | Range: nan - nan |
| ` 14` | float64 | 0 | 0 |  | Range: nan - nan |
| ` 62` | object | 8,104 | 9 |  0:DIPLO_STATE_FREE_CITIES_NEU,  0.00:1:0.00,  ... | Top:  0:DIPLO_STATE_FREE_CITIES_NEUTRAL,  0.00:2:0.00 |
| ` 63` | object | 15,078 | 8 |  0:,  0.00:1:0.00,  0: | Top:  0:,  0.00:2:0.00 |

### Sample Data

```json
[
  {
    "Game Turn": NaN,
    " Player": NaN,
    " Action": NaN,
    " ": NaN,
    " 0": NaN,
    " 1": NaN,
    " 2": NaN,
    " 3": NaN,
    " 4": NaN,
    " 5": NaN,
    " 6": NaN,
    " 7": NaN,
    " 8": NaN,
    " 9": NaN,
    " 10": NaN,
    " 11": NaN,
    " 12": NaN,
    " 13": NaN,
    " 14": NaN,
    " 62": " 0:DIPLO_STATE_FREE_CITIES_NEUTRAL",
    " 63": " 0:"
  },
  {
    "Game Turn": NaN,
    " Player": NaN,
    " Action": NaN,
    " ": NaN,
    " 0": NaN,
    " 1": NaN,
    " 2": NaN,
    " 3": NaN,
    " 4": NaN,
    " 5": NaN,
    " 6": NaN,
    " 7": NaN,
    " 8": NaN,
    " 9": NaN,
    " 10": NaN,
    " 11": NaN,
    " 12": NaN,
    " 13": NaN,
    " 14": NaN,
    " 62": " 0.00:1:0.00",
    " 63": " 0.00:1:0.00"
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `ai_diplomacy`

**Column Mappings:**
- `Game Turn` → DECIMAL(10,2)
- ` Player` → DECIMAL(10,2)
- ` Action` → DECIMAL(10,2)
- ` ` → DECIMAL(10,2)
- ` 0` → DECIMAL(10,2)
- ` 1` → DECIMAL(10,2)
- ` 2` → DECIMAL(10,2)
- ` 3` → DECIMAL(10,2)
- ` 4` → DECIMAL(10,2)
- ` 5` → DECIMAL(10,2)
- ` 6` → DECIMAL(10,2)
- ` 7` → DECIMAL(10,2)
- ` 8` → DECIMAL(10,2)
- ` 9` → DECIMAL(10,2)
- ` 10` → DECIMAL(10,2)
- ` 11` → DECIMAL(10,2)
- ` 12` → DECIMAL(10,2)
- ` 13` → DECIMAL(10,2)
- ` 14` → DECIMAL(10,2)
- ` 62` → VARCHAR(100)
- ` 63` → VARCHAR(100)

---

## AI_Espionage.csv

**File Statistics:**
- Size: 11659.31 KB
- Rows: 88,254
- Columns: 10
- Memory Usage: 15.63 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Game Turn` | object | 88,254 | 3 |  -9999.00,  -9999.00,  -9999.00 | Top:  -9999.00,  BEGIN |
| ` Player` | object | 88,254 | 1,202 |  -9999.00,  -9999.00,  -9999.00 |  |
| ` City` | float64 | 87,777 | 18 | -9999.0, -9999.0, -9999.0 | Range: -9999.0 - 1024.41 |
| ` UNITOPERATION_SPY_LISTENING_POST` | float64 | 87,777 | 12 | -9999.0, -9999.0, -9999.0 | Range: -9999.0 - 853.86 |
| ` UNITOPERATION_SPY_GAIN_SOURCES` | float64 | 87,777 | 1,874 | -9999.0, -9999.0, -9999.0 | Range: -9999.0 - 6278.28 |
| ` UNITOPERATION_SPY_STEAL_TECH_BOOST` | float64 | 87,777 | 10,360 | -9999.0, -9999.0, -9999.0 | Range: -9999.0 - 9262.65 |
| ` UNITOPERATION_SPY_GREAT_WORK_HEIST` | float64 | 87,777 | 11 | -9999.0, -9999.0, -9999.0 | Range: -9999.0 - 2250.0 |
| ` UNITOPERATION_SPY_SABOTAGE_PRODUCTION` | float64 | 87,777 | 2 | -9999.0, -9999.0, -9999.0 | Range: -9999.0 - 0.0 |
| ` UNITOPERATION_SPY_SIPHON_FUNDS` | float64 | 87,777 | 11 | -9999.0, -9999.0, -9999.0 | Range: -9999.0 - 2715.16 |
| ` UNITOPERATION_SPY_REC` | float64 | 87,777 | 5,623 | -9999.0, -9999.0, -9999.0 | Range: -9999.0 - 7988.63 |

### Sample Data

```json
[
  {
    "Game Turn": " -9999.00",
    " Player": " -9999.00",
    " City": -9999.0,
    " UNITOPERATION_SPY_LISTENING_POST": -9999.0,
    " UNITOPERATION_SPY_GAIN_SOURCES": -9999.0,
    " UNITOPERATION_SPY_STEAL_TECH_BOOST": -9999.0,
    " UNITOPERATION_SPY_GREAT_WORK_HEIST": -9999.0,
    " UNITOPERATION_SPY_SABOTAGE_PRODUCTION": -9999.0,
    " UNITOPERATION_SPY_SIPHON_FUNDS": -9999.0,
    " UNITOPERATION_SPY_REC": -9999.0
  },
  {
    "Game Turn": " -9999.00",
    " Player": " -9999.00",
    " City": -9999.0,
    " UNITOPERATION_SPY_LISTENING_POST": -9999.0,
    " UNITOPERATION_SPY_GAIN_SOURCES": -9999.0,
    " UNITOPERATION_SPY_STEAL_TECH_BOOST": -9999.0,
    " UNITOPERATION_SPY_GREAT_WORK_HEIST": -9999.0,
    " UNITOPERATION_SPY_SABOTAGE_PRODUCTION": -9999.0,
    " UNITOPERATION_SPY_SIPHON_FUNDS": -9999.0,
    " UNITOPERATION_SPY_REC": -9999.0
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `ai_espionage`

**Column Mappings:**
- `Game Turn` → VARCHAR(100)
- ` Player` → VARCHAR(100)
- ` City` → DECIMAL(10,2)
- ` UNITOPERATION_SPY_LISTENING_POST` → DECIMAL(10,2)
- ` UNITOPERATION_SPY_GAIN_SOURCES` → DECIMAL(10,2)
- ` UNITOPERATION_SPY_STEAL_TECH_BOOST` → DECIMAL(10,2)
- ` UNITOPERATION_SPY_GREAT_WORK_HEIST` → DECIMAL(10,2)
- ` UNITOPERATION_SPY_SABOTAGE_PRODUCTION` → DECIMAL(10,2)
- ` UNITOPERATION_SPY_SIPHON_FUNDS` → DECIMAL(10,2)
- ` UNITOPERATION_SPY_REC` → DECIMAL(10,2)

---

## AI_Governors.csv

**File Statistics:**
- Size: 7094.93 KB
- Rows: 24,168
- Columns: 5
- Memory Usage: 11.24 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Game Turn` | object | 24,168 | 471 |  10:GOVERNOR_PROMOTION_GARRISO,  10:GOVERNOR_PR... |  |
| ` Player` | object | 24,168 | 140 |  10:GOVERNOR_PROMOTION_DEFENSE,  10:GOVERNOR_PR... |  |
| ` Governor` | object | 24,168 | 216 |  10:GOVERNOR_PROMOTION_EMBRASU,  10:GOVERNOR_PR... |  |
| ` Assignment` | object | 24,168 | 156 |  10:GOVERNOR_PROMOTION_AIR_DEF,  10:GOVERNOR_PR... |  |
| ` Promotions` | object | 24,168 | 428 |  10:GOVERNOR_PROMOTION_EDUCATO,  10:GOVERNOR_PR... |  |

### Sample Data

```json
[
  {
    "Game Turn": " 10:GOVERNOR_PROMOTION_GARRISON_COMMANDER",
    " Player": " 10:GOVERNOR_PROMOTION_DEFENSE_LOGISTICS",
    " Governor": " 10:GOVERNOR_PROMOTION_EMBRASURE",
    " Assignment": " 10:GOVERNOR_PROMOTION_AIR_DEFENSE_INITIATIVE",
    " Promotions": " 10:GOVERNOR_PROMOTION_EDUCATOR_ARMS_RACE_PROPONENT"
  },
  {
    "Game Turn": " 10:GOVERNOR_PROMOTION_AMBASSADOR_EMISSARY",
    " Player": " 10:GOVERNOR_PROMOTION_AMBASSADOR_AFFLUENCE",
    " Governor": " 10:GOVERNOR_PROMOTION_LOCAL_INFORMANTS",
    " Assignment": " 10:GOVERNOR_PROMOTION_AMBASSADOR_FOREIGN_INVESTOR",
    " Promotions": " 10:GOVERNOR_PROMOTION_AMBASSADOR_PUPPETEER"
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `ai_governors`

**Column Mappings:**
- `Game Turn` → VARCHAR(100)
- ` Player` → VARCHAR(100)
- ` Governor` → VARCHAR(100)
- ` Assignment` → VARCHAR(100)
- ` Promotions` → VARCHAR(100)

---

## AI_GovtPolicies.csv

**File Statistics:**
- Size: 11518.28 KB
- Rows: 254,164
- Columns: 6
- Memory Usage: 38.52 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Game Turn` | int64 | 254,164 | 503 | 1, 1, 1 | Range: 1 - 503 |
| ` Player` | int64 | 254,164 | 16 | 0, 0, 0 | Range: 0 - 62 |
| ` Action` | object | 254,164 | 5 |  Civic,  Civic,  Civic | Top:  Policies,  Civic |
| ` Policy` | object | 254,164 | 182 |  CIVIC_CODE_OF_LAWS,  CIVIC_CRAFTSMANSHIP,  CIV... |  |
| ` Score` | float64 | 253,816 | 31,270 | 145.2, 204.9, 204.9 | Range: 0.0 - 154489.6 |
| ` Turns` | float64 | 100,482 | 1,274 | 20.0, 60.0, 60.0 | Range: 1.0 - 14069.0 |

### Sample Data

```json
[
  {
    "Game Turn": 1,
    " Player": 0,
    " Action": " Civic",
    " Policy": " CIVIC_CODE_OF_LAWS",
    " Score": 145.2,
    " Turns": 20.0
  },
  {
    "Game Turn": 1,
    " Player": 0,
    " Action": " Civic",
    " Policy": " CIVIC_CRAFTSMANSHIP",
    " Score": 204.9,
    " Turns": 60.0
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `ai_govtpolicies`

**Column Mappings:**
- `Game Turn` → INTEGER
- ` Player` → INTEGER
- ` Action` → VARCHAR(100)
- ` Policy` → VARCHAR(100)
- ` Score` → DECIMAL(10,2)
- ` Turns` → DECIMAL(10,2)

---

## AI_Knowledge.csv

**File Statistics:**
- Size: 20105.21 KB
- Rows: 0
- Columns: 0
- Memory Usage: 0 MB

❌ **Error:** Error tokenizing data. C error: Expected 11 fields in line 331, saw 15


## AI_MayhemTracker.csv

**File Statistics:**
- Size: 197.03 KB
- Rows: 3,173
- Columns: 8
- Memory Usage: 0.81 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Game Turn` | int64 | 3,173 | 468 | 4, 4, 5 | Range: 4 - 503 |
| ` Event` | object | 3,173 | 13 |  Barb Combat,  Barb Combat,  Barb Combat | Top:  Barb Combat,  Combat |
| ` Attacker` | int64 | 3,173 | 18 | 3, 12, 12 | Range: -1 - 63 |
| ` Unit` | object | 3,173 | 50 |  UNIT_WARRIOR,  UNIT_WARRIOR,  UNIT_WARRIOR |  |
| ` Defender` | object | 3,173 | 18 |  63,  63,  63 | Top:  63,  5 |
| ` Unit.1` | object | 3,173 | 112 |  UNIT_SCOUT,  UNIT_SPEARMAN,  UNIT_SPEARMAN |  |
| ` Mayhem` | float64 | 3,173 | 5 | 0.5, 0.5, 0.5 | Range: 0.5 - 4.0 |
| ` Current Total` | float64 | 3,173 | 3,173 | 0.5, 1.0, 1.5 | Range: 0.5 - 2851.5 |

### Sample Data

```json
[
  {
    "Game Turn": 4,
    " Event": " Barb Combat",
    " Attacker": 3,
    " Unit": " UNIT_WARRIOR",
    " Defender": " 63",
    " Unit.1": " UNIT_SCOUT",
    " Mayhem": 0.5,
    " Current Total": 0.5
  },
  {
    "Game Turn": 4,
    " Event": " Barb Combat",
    " Attacker": 12,
    " Unit": " UNIT_WARRIOR",
    " Defender": " 63",
    " Unit.1": " UNIT_SPEARMAN",
    " Mayhem": 0.5,
    " Current Total": 1.0
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `ai_mayhemtracker`

**Column Mappings:**
- `Game Turn` → INTEGER
- ` Event` → VARCHAR(100)
- ` Attacker` → INTEGER
- ` Unit` → VARCHAR(100)
- ` Defender` → VARCHAR(100)
- ` Unit.1` → VARCHAR(100)
- ` Mayhem` → DECIMAL(10,2)
- ` Current Total` → DECIMAL(10,2)

---

## AI_Military.csv

**File Statistics:**
- Size: 374.16 KB
- Rows: 8,023
- Columns: 9
- Memory Usage: 1.99 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Game Turn` | int64 | 8,023 | 503 | 1, 1, 1 | Range: 1 - 503 |
| ` Player` | int64 | 8,023 | 16 | 0, 1, 2 | Range: 0 - 62 |
| ` Regional Strength` | object | 8,023 | 288 |  0,  0,  0 |  |
| ` Enemy Strength` | float64 | 7,948 | 127 | 0.0, 0.0, 0.0 | Range: 0.0 - 1995.0 |
| ` Other Strength` | float64 | 7,948 | 169 | 0.0, 0.0, 0.0 | Range: 0.0 - 1995.0 |
| ` Current Explorers` | object | 7,948 | 12 |  1:0,  1:0,  1:0 | Top:  0:0,  1:0 |
| ` Desired Explorers` | object | 7,948 | 7 |  3:1,  3:1,  3:1 | Top:  0:0,  1:1 |
| ` Fav Tech` | object | 7,948 | 32 |  NO_TECH,  NO_TECH,  NO_TECH |  |
| ` Combat Desire` | float64 | 7,948 | 203 | 0.0, 0.0, 0.0 | Range: -0.1 - 77.5 |

### Sample Data

```json
[
  {
    "Game Turn": 1,
    " Player": 0,
    " Regional Strength": " 0",
    " Enemy Strength": 0.0,
    " Other Strength": 0.0,
    " Current Explorers": " 1:0",
    " Desired Explorers": " 3:1",
    " Fav Tech": " NO_TECH",
    " Combat Desire": 0.0
  },
  {
    "Game Turn": 1,
    " Player": 1,
    " Regional Strength": " 0",
    " Enemy Strength": 0.0,
    " Other Strength": 0.0,
    " Current Explorers": " 1:0",
    " Desired Explorers": " 3:1",
    " Fav Tech": " NO_TECH",
    " Combat Desire": 0.0
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `ai_military`

**Column Mappings:**
- `Game Turn` → INTEGER
- ` Player` → INTEGER
- ` Regional Strength` → VARCHAR(100)
- ` Enemy Strength` → DECIMAL(10,2)
- ` Other Strength` → DECIMAL(10,2)
- ` Current Explorers` → VARCHAR(100)
- ` Desired Explorers` → VARCHAR(100)
- ` Fav Tech` → VARCHAR(100)
- ` Combat Desire` → DECIMAL(10,2)

---

## AI_Operation.csv

**File Statistics:**
- Size: 6049.35 KB
- Rows: 93,713
- Columns: 8
- Memory Usage: 34.15 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Game Turn` | int64 | 93,713 | 503 | 1, 1, 1 | Range: 1 - 503 |
| ` Player` | object | 93,713 | 29 |  1,  1,  1 |  |
| ` Operation` | object | 93,713 | 47 |  Settle New City,  Settle New City running,  Se... |  |
| ` Notes` | object | 93,713 | 211 |  Started,  TARGET -9999:-9999,   |  |
| ` Team` | object | 74,528 | 100 | 0,  No backup, 0 |  |
| ` Team Notes` | object | 74,156 | 3,335 |  Not Ready,  Not Ready,  Not Ready |  |
| ` Team Members` | object | 73,351 | 1,837 |  ,  ,   |  |
| ` Terrain` | object | 11,754 | 1,843 |  7:23,  8:23,  Attack 8:23 |  |

### Sample Data

```json
[
  {
    "Game Turn": 1,
    " Player": " 1",
    " Operation": " Settle New City",
    " Notes": " Started",
    " Team": NaN,
    " Team Notes": NaN,
    " Team Members": NaN,
    " Terrain": NaN
  },
  {
    "Game Turn": 1,
    " Player": " 1",
    " Operation": " Settle New City running",
    " Notes": " TARGET -9999:-9999",
    " Team": NaN,
    " Team Notes": NaN,
    " Team Members": NaN,
    " Terrain": NaN
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `ai_operation`

**Column Mappings:**
- `Game Turn` → INTEGER
- ` Player` → VARCHAR(100)
- ` Operation` → VARCHAR(100)
- ` Notes` → VARCHAR(100)
- ` Team` → VARCHAR(100)
- ` Team Notes` → VARCHAR(100)
- ` Team Members` → VARCHAR(100)
- ` Terrain` → VARCHAR(100)

---

## AI_Operation_Eval.csv

**File Statistics:**
- Size: 7303.16 KB
- Rows: 0
- Columns: 0
- Memory Usage: 0 MB

❌ **Error:** Error tokenizing data. C error: Expected 5 fields in line 70, saw 6


## AI_Planning.csv

**File Statistics:**
- Size: 44197.53 KB
- Rows: 0
- Columns: 0
- Memory Usage: 0 MB

❌ **Error:** Error tokenizing data. C error: Expected 20 fields in line 4, saw 28


## AI_Religious.csv

**File Statistics:**
- Size: 17453.99 KB
- Rows: 498,550
- Columns: 4
- Memory Usage: 45.06 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Game Turn` | int64 | 498,550 | 503 | 1, 1, 1 | Range: 1 - 503 |
| ` Player` | int64 | 498,550 | 17 | 0, 0, 0 | Range: 0 - 63 |
| ` Belief` | object | 498,550 | 59 |  BELIEF_DANCE_OF_THE_AURORA,  BELIEF_DESERT_FOL... |  |
| ` Score` | float64 | 498,550 | 1,337 | 0.0, 0.0, 0.0 | Range: -5.0 - 6247.0 |

### Sample Data

```json
[
  {
    "Game Turn": 1,
    " Player": 0,
    " Belief": " BELIEF_DANCE_OF_THE_AURORA",
    " Score": 0.0
  },
  {
    "Game Turn": 1,
    " Player": 0,
    " Belief": " BELIEF_DESERT_FOLKLORE",
    " Score": 0.0
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `ai_religious`

**Column Mappings:**
- `Game Turn` → INTEGER
- ` Player` → INTEGER
- ` Belief` → VARCHAR(100)
- ` Score` → DECIMAL(10,2)

---

## AI_Research.csv

**File Statistics:**
- Size: 17653.89 KB
- Rows: 382,184
- Columns: 7
- Memory Usage: 75.04 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Game Turn` | int64 | 382,184 | 503 | 1, 1, 1 | Range: 1 - 503 |
| ` Player` | int64 | 382,184 | 16 | 0, 0, 0 | Range: 0 - 62 |
| ` Action` | object | 382,184 | 784 |  Tech,  Tech,  Tech |  |
| ` Tech` | object | 382,184 | 77 |  TECH_POTTERY,  TECH_ANIMAL_HUSBANDRY,  TECH_MI... |  |
| ` Score` | float64 | 382,184 | 23,519 | 151.6, 116.6, 116.6 | Range: -14963.0 - 53218.4 |
| ` Boost` | object | 374,099 | 5 |  ,  ,   | Top:  OWNED,   |
| ` Turns` | float64 | 374,099 | 1,406 | 25.0, 25.0, 25.0 | Range: -1.0 - 13998.0 |

### Sample Data

```json
[
  {
    "Game Turn": 1,
    " Player": 0,
    " Action": " Tech",
    " Tech": " TECH_POTTERY",
    " Score": 151.6,
    " Boost": " ",
    " Turns": 25.0
  },
  {
    "Game Turn": 1,
    " Player": 0,
    " Action": " Tech",
    " Tech": " TECH_ANIMAL_HUSBANDRY",
    " Score": 116.6,
    " Boost": " ",
    " Turns": 25.0
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `ai_research`

**Column Mappings:**
- `Game Turn` → INTEGER
- ` Player` → INTEGER
- ` Action` → VARCHAR(100)
- ` Tech` → VARCHAR(100)
- ` Score` → DECIMAL(10,2)
- ` Boost` → VARCHAR(100)
- ` Turns` → DECIMAL(10,2)

---

## AI_Tactical.csv

**File Statistics:**
- Size: 2192.94 KB
- Rows: 0
- Columns: 0
- Memory Usage: 0 MB

❌ **Error:** Error tokenizing data. C error: Expected 7 fields in line 95, saw 8


## AI_UnitEfficiency.csv

**File Statistics:**
- Size: 135.65 KB
- Rows: 144
- Columns: 145
- Memory Usage: 0.17 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Unnamed: 0` | object | 144 | 144 | UNIT_SETTLER, UNIT_BUILDER, UNIT_TRADER |  |
| `UNIT_SETTLER` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_BUILDER` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_TRADER` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_MISSIONARY` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_APOSTLE` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_INQUISITOR` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_GURU` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_WARRIOR_MONK` | float64 | 144 | 67 | 0.01, 0.01, 0.01 | Range: 0.01 - 104.0 |
| `UNIT_ARCHAEOLOGIST` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_GREAT_GENERAL` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_GREAT_ADMIRAL` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_GREAT_ENGINEER` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_GREAT_MERCHANT` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_GREAT_PROPHET` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_GREAT_SCIENTIST` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_GREAT_WRITER` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_GREAT_ARTIST` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_GREAT_MUSICIAN` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_SPY` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_NATURALIST` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_SCOUT` | float64 | 144 | 47 | 0.01, 0.01, 0.01 | Range: 0.01 - 210.0 |
| `UNIT_WARRIOR` | float64 | 144 | 64 | 0.01, 0.01, 0.01 | Range: 0.01 - 206.0 |
| `UNIT_SLINGER` | float64 | 144 | 55 | 0.01, 0.01, 0.01 | Range: 0.0 - 103.0 |
| `UNIT_BARBARIAN_HORSEMAN` | float64 | 144 | 60 | 0.01, 0.01, 0.01 | Range: 0.01 - 204.0 |
| `UNIT_BARBARIAN_HORSE_ARCHER` | float64 | 144 | 54 | 0.01, 0.01, 0.01 | Range: 0.0 - 102.0 |
| `UNIT_SUMERIAN_WAR_CART` | float64 | 144 | 63 | 0.01, 0.01, 0.01 | Range: 0.01 - 204.0 |
| `UNIT_GALLEY` | float64 | 144 | 64 | 0.01, 0.01, 0.01 | Range: 0.01 - 204.0 |
| `UNIT_NORWEGIAN_LONGSHIP` | float64 | 144 | 65 | 0.01, 0.01, 0.01 | Range: 0.01 - 104.0 |
| `UNIT_ARCHER` | float64 | 144 | 70 | 0.01, 0.01, 0.01 | Range: 0.0 - 103.0 |
| `UNIT_SPEARMAN` | float64 | 144 | 81 | 0.01, 0.01, 0.01 | Range: 0.01 - 206.0 |
| `UNIT_HEAVY_CHARIOT` | float64 | 144 | 70 | 0.01, 0.01, 0.01 | Range: 0.01 - 206.0 |
| `UNIT_BATTERING_RAM` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_GREEK_HOPLITE` | float64 | 144 | 81 | 0.01, 0.01, 0.01 | Range: 0.01 - 206.0 |
| `UNIT_SWORDSMAN` | float64 | 144 | 74 | 0.01, 0.01, 0.01 | Range: 0.01 - 106.0 |
| `UNIT_HORSEMAN` | float64 | 144 | 71 | 0.01, 0.01, 0.01 | Range: 0.01 - 104.0 |
| `UNIT_SCYTHIAN_HORSE_ARCHER` | float64 | 144 | 60 | 0.01, 0.01, 0.01 | Range: 0.0 - 102.0 |
| `UNIT_ROMAN_LEGION` | float64 | 144 | 75 | 0.01, 0.01, 0.01 | Range: 0.01 - 106.0 |
| `UNIT_KONGO_SHIELD_BEARER` | float64 | 144 | 73 | 0.01, 0.01, 0.01 | Range: 0.01 - 106.0 |
| `UNIT_CATAPULT` | float64 | 144 | 76 | 0.01, 0.01, 0.01 | Range: 0.0 - 53.0 |
| `UNIT_SIEGE_TOWER` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_QUADRIREME` | float64 | 144 | 59 | 0.01, 0.01, 0.01 | Range: 0.0 - 102.0 |
| `UNIT_EGYPTIAN_CHARIOT_ARCHER` | float64 | 144 | 81 | 0.01, 0.01, 0.01 | Range: 0.0 - 53.0 |
| `UNIT_JAPANESE_SAMURAI` | float64 | 144 | 73 | 0.01, 0.01, 0.01 | Range: 0.01 - 102.0 |
| `UNIT_NORWEGIAN_BERSERKER` | float64 | 144 | 71 | 0.01, 0.01, 0.01 | Range: 0.01 - 68.66 |
| `UNIT_KNIGHT` | float64 | 144 | 71 | 0.01, 0.01, 0.01 | Range: 0.01 - 100.0 |
| `UNIT_INDIAN_VARU` | float64 | 144 | 76 | 0.01, 0.01, 0.01 | Range: 0.01 - 106.0 |
| `UNIT_ARABIAN_MAMLUK` | float64 | 144 | 71 | 0.01, 0.01, 0.01 | Range: 0.01 - 100.0 |
| `UNIT_CROSSBOWMAN` | float64 | 144 | 82 | 0.01, 0.01, 0.01 | Range: 0.0 - 53.0 |
| `UNIT_CHINESE_CROUCHING_TIGER` | float64 | 144 | 69 | 0.01, 0.01, 0.01 | Range: 0.0 - 51.0 |
| `UNIT_MILITARY_ENGINEER` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_PIKEMAN` | float64 | 144 | 81 | 0.01, 0.01, 0.01 | Range: 0.01 - 106.0 |
| `UNIT_MUSKETMAN` | float64 | 144 | 72 | 0.01, 0.01, 0.01 | Range: 0.01 - 72.66 |
| `UNIT_SPANISH_CONQUISTADOR` | float64 | 144 | 72 | 0.01, 0.01, 0.01 | Range: 0.01 - 56.0 |
| `UNIT_CARAVEL` | float64 | 144 | 64 | 0.01, 0.01, 0.01 | Range: 0.01 - 70.66 |
| `UNIT_BOMBARD` | float64 | 144 | 78 | 0.01, 0.01, 0.01 | Range: 0.0 - 51.0 |
| `UNIT_FRIGATE` | float64 | 144 | 64 | 0.01, 0.01, 0.01 | Range: 0.0 - 35.33 |
| `UNIT_PRIVATEER` | float64 | 144 | 72 | 0.01, 0.01, 0.01 | Range: 0.0 - 50.0 |
| `UNIT_ENGLISH_SEADOG` | float64 | 144 | 65 | 0.01, 0.01, 0.01 | Range: 0.0 - 35.33 |
| `UNIT_FIELD_CANNON` | float64 | 144 | 74 | 0.01, 0.01, 0.01 | Range: 0.0 - 34.33 |
| `UNIT_CAVALRY` | float64 | 144 | 63 | 0.01, 0.01, 0.01 | Range: 0.01 - 50.0 |
| `UNIT_RUSSIAN_COSSACK` | float64 | 144 | 59 | 0.01, 0.01, 0.01 | Range: 0.01 - 35.33 |
| `UNIT_ENGLISH_REDCOAT` | float64 | 144 | 61 | 0.01, 0.01, 0.01 | Range: 0.01 - 35.33 |
| `UNIT_FRENCH_GARDE_IMPERIALE` | float64 | 144 | 62 | 0.01, 0.01, 0.01 | Range: 0.01 - 39.33 |
| `UNIT_MEDIC` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_IRONCLAD` | float64 | 144 | 51 | 0.01, 0.01, 0.01 | Range: 0.01 - 35.33 |
| `UNIT_RANGER` | float64 | 144 | 65 | 0.01, 0.01, 0.01 | Range: 0.0 - 34.33 |
| `UNIT_OBSERVATION_BALLOON` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_BIPLANE` | float64 | 144 | 41 | 0.01, 0.01, 0.01 | Range: 0.01 - 36.16 |
| `UNIT_INFANTRY` | float64 | 144 | 59 | 0.01, 0.01, 0.01 | Range: 0.01 - 35.33 |
| `UNIT_ARTILLERY` | float64 | 144 | 63 | 0.01, 0.01, 0.01 | Range: 0.0 - 26.0 |
| `UNIT_BATTLESHIP` | float64 | 144 | 47 | 0.01, 0.01, 0.01 | Range: 0.0 - 20.0 |
| `UNIT_BRAZILIAN_MINAS_GERAES` | float64 | 144 | 41 | 0.01, 0.01, 0.01 | Range: 0.0 - 14.29 |
| `UNIT_SUBMARINE` | float64 | 144 | 48 | 0.01, 0.01, 0.01 | Range: 0.0 - 21.0 |
| `UNIT_GERMAN_UBOAT` | float64 | 144 | 48 | 0.01, 0.01, 0.01 | Range: 0.0 - 21.0 |
| `UNIT_AT_CREW` | float64 | 144 | 60 | 0.01, 0.01, 0.01 | Range: 0.01 - 35.33 |
| `UNIT_TANK` | float64 | 144 | 44 | 0.01, 0.01, 0.01 | Range: 0.01 - 20.0 |
| `UNIT_FIGHTER` | float64 | 144 | 30 | 0.01, 0.01, 0.01 | Range: 0.0 - 8.36 |
| `UNIT_AMERICAN_P51` | float64 | 144 | 28 | 0.01, 0.01, 0.01 | Range: 0.0 - 7.39 |
| `UNIT_BOMBER` | float64 | 144 | 31 | 0.01, 0.01, 0.01 | Range: 0.01 - 7.48 |
| `UNIT_ANTIAIR_GUN` | float64 | 144 | 16 | 0.01, 0.01, 0.01 | Range: 0.0 - 131.92 |
| `UNIT_MACHINE_GUN` | float64 | 144 | 52 | 0.01, 0.01, 0.01 | Range: 0.0 - 13.5 |
| `UNIT_AIRCRAFT_CARRIER` | float64 | 144 | 54 | 0.01, 0.01, 0.01 | Range: 0.01 - 52.0 |
| `UNIT_DESTROYER` | float64 | 144 | 35 | 0.01, 0.01, 0.01 | Range: 0.0 - 20.0 |
| `UNIT_HELICOPTER` | float64 | 144 | 44 | 0.01, 0.01, 0.01 | Range: 0.01 - 20.0 |
| `UNIT_NUCLEAR_SUBMARINE` | float64 | 144 | 36 | 0.01, 0.01, 0.01 | Range: 0.0 - 11.11 |
| `UNIT_MECHANIZED_INFANTRY` | float64 | 144 | 43 | 0.01, 0.01, 0.01 | Range: 0.01 - 22.0 |
| `UNIT_ROCKET_ARTILLERY` | float64 | 144 | 43 | 0.01, 0.01, 0.01 | Range: 0.0 - 13.5 |
| `UNIT_MOBILE_SAM` | float64 | 144 | 13 | 0.01, 0.01, 0.01 | Range: 0.0 - 131.92 |
| `UNIT_JET_FIGHTER` | float64 | 144 | 24 | 0.01, 0.01, 0.01 | Range: 0.0 - 6.62 |
| `UNIT_JET_BOMBER` | float64 | 144 | 27 | 0.01, 0.01, 0.01 | Range: 0.0 - 6.33 |
| `UNIT_MISSILE_CRUISER` | float64 | 144 | 34 | 0.01, 0.01, 0.01 | Range: 0.0 - 11.11 |
| `UNIT_MODERN_AT` | float64 | 144 | 45 | 0.01, 0.01, 0.01 | Range: 0.01 - 22.0 |
| `UNIT_MODERN_ARMOR` | float64 | 144 | 37 | 0.01, 0.01, 0.01 | Range: 0.01 - 12.5 |
| `UNIT_MAN_AT_ARMS` | float64 | 144 | 69 | 0.01, 0.01, 0.01 | Range: 0.01 - 106.0 |
| `UNIT_LINE_INFANTRY` | float64 | 144 | 64 | 0.01, 0.01, 0.01 | Range: 0.01 - 52.0 |
| `UNIT_TREBUCHET` | float64 | 144 | 85 | 0.01, 0.01, 0.01 | Range: 0.0 - 53.0 |
| `UNIT_AZTEC_EAGLE_WARRIOR` | float64 | 144 | 71 | 0.01, 0.01, 0.01 | Range: 0.01 - 206.0 |
| `UNIT_INDONESIAN_JONG` | float64 | 144 | 63 | 0.01, 0.01, 0.01 | Range: 0.0 - 34.33 |
| `UNIT_KHMER_DOMREY` | float64 | 144 | 78 | 0.01, 0.01, 0.01 | Range: 0.0 - 51.0 |
| `UNIT_POLISH_HUSSAR` | float64 | 144 | 66 | 0.01, 0.01, 0.01 | Range: 0.01 - 50.0 |
| `UNIT_NUBIAN_PITATI` | float64 | 144 | 69 | 0.01, 0.01, 0.01 | Range: 0.0 - 102.0 |
| `UNIT_MACEDONIAN_HYPASPIST` | float64 | 144 | 73 | 0.01, 0.01, 0.01 | Range: 0.01 - 106.0 |
| `UNIT_MACEDONIAN_HETAIROI` | float64 | 144 | 71 | 0.01, 0.01, 0.01 | Range: 0.01 - 104.0 |
| `UNIT_PERSIAN_IMMORTAL` | float64 | 144 | 82 | 0.01, 0.01, 0.01 | Range: 0.01 - 106.0 |
| `UNIT_DIGGER` | float64 | 144 | 53 | 0.01, 0.01, 0.01 | Range: 0.01 - 27.0 |
| `UNIT_ZULU_IMPI` | float64 | 144 | 81 | 0.01, 0.01, 0.01 | Range: 0.01 - 106.0 |
| `UNIT_KOREAN_HWACHA` | float64 | 144 | 69 | 0.01, 0.01, 0.01 | Range: 0.0 - 34.33 |
| `UNIT_SCOTTISH_HIGHLANDER` | float64 | 144 | 63 | 0.01, 0.01, 0.01 | Range: 0.0 - 34.33 |
| `UNIT_DE_ZEVEN_PROVINCIEN` | float64 | 144 | 64 | 0.01, 0.01, 0.01 | Range: 0.0 - 33.33 |
| `UNIT_MONGOLIAN_KESHIG` | float64 | 144 | 81 | 0.01, 0.01, 0.01 | Range: 0.0 - 52.0 |
| `UNIT_GEORGIAN_KHEVSURETI` | float64 | 144 | 73 | 0.01, 0.01, 0.01 | Range: 0.01 - 102.0 |
| `UNIT_MAPUCHE_MALON_RAIDER` | float64 | 144 | 71 | 0.01, 0.01, 0.01 | Range: 0.01 - 70.66 |
| `UNIT_CREE_OKIHTCITAW` | float64 | 144 | 56 | 0.01, 0.01, 0.01 | Range: 0.01 - 204.0 |
| `UNIT_SPEC_OPS` | float64 | 144 | 57 | 0.01, 0.01, 0.01 | Range: 0.0 - 26.0 |
| `UNIT_DRONE` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_PIKE_AND_SHOT` | float64 | 144 | 81 | 0.01, 0.01, 0.01 | Range: 0.01 - 72.66 |
| `UNIT_SUPPLY_CONVOY` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_SKIRMISHER` | float64 | 144 | 60 | 0.01, 0.01, 0.01 | Range: 0.0 - 102.0 |
| `UNIT_COURSER` | float64 | 144 | 71 | 0.01, 0.01, 0.01 | Range: 0.01 - 102.0 |
| `UNIT_CUIRASSIER` | float64 | 144 | 66 | 0.01, 0.01, 0.01 | Range: 0.01 - 50.0 |
| `UNIT_GIANT_DEATH_ROBOT` | float64 | 144 | 10 | 0.01, 0.01, 0.01 | Range: 0.0 - 1.0 |
| `UNIT_ROCK_BAND` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_CANADA_MOUNTIE` | float64 | 144 | 63 | 0.01, 0.01, 0.01 | Range: 0.01 - 50.0 |
| `UNIT_HUNGARY_BLACK_ARMY` | float64 | 144 | 71 | 0.01, 0.01, 0.01 | Range: 0.01 - 100.0 |
| `UNIT_HUNGARY_HUSZAR` | float64 | 144 | 63 | 0.01, 0.01, 0.01 | Range: 0.01 - 50.0 |
| `UNIT_INCA_WARAKAQ` | float64 | 144 | 58 | 0.01, 0.01, 0.01 | Range: 0.0 - 52.0 |
| `UNIT_MALI_MANDEKALU_CAVALRY` | float64 | 144 | 71 | 0.01, 0.01, 0.01 | Range: 0.01 - 70.66 |
| `UNIT_MAORI_TOA` | float64 | 144 | 73 | 0.01, 0.01, 0.01 | Range: 0.01 - 106.0 |
| `UNIT_OTTOMAN_BARBARY_CORSAIR` | float64 | 144 | 74 | 0.01, 0.01, 0.01 | Range: 0.0 - 50.0 |
| `UNIT_PHOENICIA_BIREME` | float64 | 144 | 63 | 0.01, 0.01, 0.01 | Range: 0.01 - 104.0 |
| `UNIT_SULEIMAN_JANISSARY` | float64 | 144 | 65 | 0.01, 0.01, 0.01 | Range: 0.01 - 56.0 |
| `UNIT_SWEDEN_CAROLEAN` | float64 | 144 | 68 | 0.01, 0.01, 0.01 | Range: 0.01 - 52.0 |
| `UNIT_AMERICAN_ROUGH_RIDER` | float64 | 144 | 59 | 0.01, 0.01, 0.01 | Range: 0.01 - 35.33 |
| `UNIT_MAYAN_HULCHE` | float64 | 144 | 69 | 0.01, 0.01, 0.01 | Range: 0.0 - 103.0 |
| `UNIT_LAHORE_NIHANG` | float64 | 144 | 69 | 0.01, 0.01, 0.01 | Range: 0.01 - 206.0 |
| `UNIT_COMANDANTE_GENERAL` | float64 | 144 | 2 | 1.0, 1.0, 1.0 | Range: 1.0 - 100.0 |
| `UNIT_COLOMBIAN_LLANERO` | float64 | 144 | 63 | 0.01, 0.01, 0.01 | Range: 0.01 - 50.0 |
| `UNIT_BYZANTINE_DROMON` | float64 | 144 | 63 | 0.01, 0.01, 0.01 | Range: 0.01 - 52.0 |
| `UNIT_BYZANTINE_TAGMA` | float64 | 144 | 71 | 0.01, 0.01, 0.01 | Range: 0.01 - 100.0 |
| `UNIT_GAUL_GAESATAE` | float64 | 144 | 70 | 0.01, 0.01, 0.01 | Range: 0.01 - 206.0 |
| `UNIT_VIETNAMESE_VOI_CHIEN` | float64 | 144 | 76 | 0.01, 0.01, 0.01 | Range: 0.0 - 52.0 |
| `UNIT_ETHIOPIAN_OROMO_CAVALRY` | float64 | 144 | 68 | 0.01, 0.01, 0.01 | Range: 0.01 - 100.0 |
| `UNIT_BABYLONIAN_SABUM_KIBITTUM` | float64 | 144 | 65 | 0.01, 0.01, 0.01 | Range: 0.01 - 204.0 |
| `UNIT_PORTUGUESE_NAU` | float64 | 144 | 64 | 0.01, 0.01, 0.01 | Range: 0.01 - 70.66 |

### Sample Data

```json
[
  {
    "Unnamed: 0": "UNIT_SETTLER",
    "UNIT_SETTLER": 1.0,
    "UNIT_BUILDER": 1.0,
    "UNIT_TRADER": 1.0,
    "UNIT_MISSIONARY": 1.0,
    "UNIT_APOSTLE": 1.0,
    "UNIT_INQUISITOR": 1.0,
    "UNIT_GURU": 1.0,
    "UNIT_WARRIOR_MONK": 0.01,
    "UNIT_ARCHAEOLOGIST": 1.0,
    "UNIT_GREAT_GENERAL": 1.0,
    "UNIT_GREAT_ADMIRAL": 1.0,
    "UNIT_GREAT_ENGINEER": 1.0,
    "UNIT_GREAT_MERCHANT": 1.0,
    "UNIT_GREAT_PROPHET": 1.0,
    "UNIT_GREAT_SCIENTIST": 1.0,
    "UNIT_GREAT_WRITER": 1.0,
    "UNIT_GREAT_ARTIST": 1.0,
    "UNIT_GREAT_MUSICIAN": 1.0,
    "UNIT_SPY": 1.0,
    "UNIT_NATURALIST": 1.0,
    "UNIT_SCOUT": 0.01,
    "UNIT_WARRIOR": 0.01,
    "UNIT_SLINGER": 0.01,
    "UNIT_BARBARIAN_HORSEMAN": 0.01,
    "UNIT_BARBARIAN_HORSE_ARCHER": 0.01,
    "UNIT_SUMERIAN_WAR_CART": 0.01,
    "UNIT_GALLEY": 0.01,
    "UNIT_NORWEGIAN_LONGSHIP": 0.01,
    "UNIT_ARCHER": 0.01,
    "UNIT_SPEARMAN": 0.01,
    "UNIT_HEAVY_CHARIOT": 0.01,
    "UNIT_BATTERING_RAM": 1.0,
    "UNIT_GREEK_HOPLITE": 0.01,
    "UNIT_SWORDSMAN": 0.01,
    "UNIT_HORSEMAN": 0.01,
    "UNIT_SCYTHIAN_HORSE_ARCHER": 0.01,
    "UNIT_ROMAN_LEGION": 0.01,
    "UNIT_KONGO_SHIELD_BEARER": 0.01,
    "UNIT_CATAPULT": 0.01,
    "UNIT_SIEGE_TOWER": 1.0,
    "UNIT_QUADRIREME": 0.01,
    "UNIT_EGYPTIAN_CHARIOT_ARCHER": 0.01,
    "UNIT_JAPANESE_SAMURAI": 0.01,
    "UNIT_NORWEGIAN_BERSERKER": 0.01,
    "UNIT_KNIGHT": 0.01,
    "UNIT_INDIAN_VARU": 0.01,
    "UNIT_ARABIAN_MAMLUK": 0.01,
    "UNIT_CROSSBOWMAN": 0.01,
    "UNIT_CHINESE_CROUCHING_TIGER": 0.01,
    "UNIT_MILITARY_ENGINEER": 1.0,
    "UNIT_PIKEMAN": 0.01,
    "UNIT_MUSKETMAN": 0.01,
    "UNIT_SPANISH_CONQUISTADOR": 0.01,
    "UNIT_CARAVEL": 0.01,
    "UNIT_BOMBARD": 0.01,
    "UNIT_FRIGATE": 0.01,
    "UNIT_PRIVATEER": 0.01,
    "UNIT_ENGLISH_SEADOG": 0.01,
    "UNIT_FIELD_CANNON": 0.01,
    "UNIT_CAVALRY": 0.01,
    "UNIT_RUSSIAN_COSSACK": 0.01,
    "UNIT_ENGLISH_REDCOAT": 0.01,
    "UNIT_FRENCH_GARDE_IMPERIALE": 0.01,
    "UNIT_MEDIC": 1.0,
    "UNIT_IRONCLAD": 0.01,
    "UNIT_RANGER": 0.01,
    "UNIT_OBSERVATION_BALLOON": 1.0,
    "UNIT_BIPLANE": 0.01,
    "UNIT_INFANTRY": 0.01,
    "UNIT_ARTILLERY": 0.01,
    "UNIT_BATTLESHIP": 0.01,
    "UNIT_BRAZILIAN_MINAS_GERAES": 0.01,
    "UNIT_SUBMARINE": 0.01,
    "UNIT_GERMAN_UBOAT": 0.01,
    "UNIT_AT_CREW": 0.01,
    "UNIT_TANK": 0.01,
    "UNIT_FIGHTER": 0.01,
    "UNIT_AMERICAN_P51": 0.01,
    "UNIT_BOMBER": 0.01,
    "UNIT_ANTIAIR_GUN": 0.01,
    "UNIT_MACHINE_GUN": 0.01,
    "UNIT_AIRCRAFT_CARRIER": 0.01,
    "UNIT_DESTROYER": 0.01,
    "UNIT_HELICOPTER": 0.01,
    "UNIT_NUCLEAR_SUBMARINE": 0.01,
    "UNIT_MECHANIZED_INFANTRY": 0.01,
    "UNIT_ROCKET_ARTILLERY": 0.01,
    "UNIT_MOBILE_SAM": 0.01,
    "UNIT_JET_FIGHTER": 0.01,
    "UNIT_JET_BOMBER": 0.01,
    "UNIT_MISSILE_CRUISER": 0.01,
    "UNIT_MODERN_AT": 0.01,
    "UNIT_MODERN_ARMOR": 0.01,
    "UNIT_MAN_AT_ARMS": 0.01,
    "UNIT_LINE_INFANTRY": 0.01,
    "UNIT_TREBUCHET": 0.01,
    "UNIT_AZTEC_EAGLE_WARRIOR": 0.01,
    "UNIT_INDONESIAN_JONG": 0.01,
    "UNIT_KHMER_DOMREY": 0.01,
    "UNIT_POLISH_HUSSAR": 0.01,
    "UNIT_NUBIAN_PITATI": 0.01,
    "UNIT_MACEDONIAN_HYPASPIST": 0.01,
    "UNIT_MACEDONIAN_HETAIROI": 0.01,
    "UNIT_PERSIAN_IMMORTAL": 0.01,
    "UNIT_DIGGER": 0.01,
    "UNIT_ZULU_IMPI": 0.01,
    "UNIT_KOREAN_HWACHA": 0.01,
    "UNIT_SCOTTISH_HIGHLANDER": 0.01,
    "UNIT_DE_ZEVEN_PROVINCIEN": 0.01,
    "UNIT_MONGOLIAN_KESHIG": 0.01,
    "UNIT_GEORGIAN_KHEVSURETI": 0.01,
    "UNIT_MAPUCHE_MALON_RAIDER": 0.01,
    "UNIT_CREE_OKIHTCITAW": 0.01,
    "UNIT_SPEC_OPS": 0.01,
    "UNIT_DRONE": 1.0,
    "UNIT_PIKE_AND_SHOT": 0.01,
    "UNIT_SUPPLY_CONVOY": 1.0,
    "UNIT_SKIRMISHER": 0.01,
    "UNIT_COURSER": 0.01,
    "UNIT_CUIRASSIER": 0.01,
    "UNIT_GIANT_DEATH_ROBOT": 0.01,
    "UNIT_ROCK_BAND": 1.0,
    "UNIT_CANADA_MOUNTIE": 0.01,
    "UNIT_HUNGARY_BLACK_ARMY": 0.01,
    "UNIT_HUNGARY_HUSZAR": 0.01,
    "UNIT_INCA_WARAKAQ": 0.01,
    "UNIT_MALI_MANDEKALU_CAVALRY": 0.01,
    "UNIT_MAORI_TOA": 0.01,
    "UNIT_OTTOMAN_BARBARY_CORSAIR": 0.01,
    "UNIT_PHOENICIA_BIREME": 0.01,
    "UNIT_SULEIMAN_JANISSARY": 0.01,
    "UNIT_SWEDEN_CAROLEAN": 0.01,
    "UNIT_AMERICAN_ROUGH_RIDER": 0.01,
    "UNIT_MAYAN_HULCHE": 0.01,
    "UNIT_LAHORE_NIHANG": 0.01,
    "UNIT_COMANDANTE_GENERAL": 1.0,
    "UNIT_COLOMBIAN_LLANERO": 0.01,
    "UNIT_BYZANTINE_DROMON": 0.01,
    "UNIT_BYZANTINE_TAGMA": 0.01,
    "UNIT_GAUL_GAESATAE": 0.01,
    "UNIT_VIETNAMESE_VOI_CHIEN": 0.01,
    "UNIT_ETHIOPIAN_OROMO_CAVALRY": 0.01,
    "UNIT_BABYLONIAN_SABUM_KIBITTUM": 0.01,
    "UNIT_PORTUGUESE_NAU": 0.01
  },
  {
    "Unnamed: 0": "UNIT_BUILDER",
    "UNIT_SETTLER": 1.0,
    "UNIT_BUILDER": 1.0,
    "UNIT_TRADER": 1.0,
    "UNIT_MISSIONARY": 1.0,
    "UNIT_APOSTLE": 1.0,
    "UNIT_INQUISITOR": 1.0,
    "UNIT_GURU": 1.0,
    "UNIT_WARRIOR_MONK": 0.01,
    "UNIT_ARCHAEOLOGIST": 1.0,
    "UNIT_GREAT_GENERAL": 1.0,
    "UNIT_GREAT_ADMIRAL": 1.0,
    "UNIT_GREAT_ENGINEER": 1.0,
    "UNIT_GREAT_MERCHANT": 1.0,
    "UNIT_GREAT_PROPHET": 1.0,
    "UNIT_GREAT_SCIENTIST": 1.0,
    "UNIT_GREAT_WRITER": 1.0,
    "UNIT_GREAT_ARTIST": 1.0,
    "UNIT_GREAT_MUSICIAN": 1.0,
    "UNIT_SPY": 1.0,
    "UNIT_NATURALIST": 1.0,
    "UNIT_SCOUT": 0.01,
    "UNIT_WARRIOR": 0.01,
    "UNIT_SLINGER": 0.01,
    "UNIT_BARBARIAN_HORSEMAN": 0.01,
    "UNIT_BARBARIAN_HORSE_ARCHER": 0.01,
    "UNIT_SUMERIAN_WAR_CART": 0.01,
    "UNIT_GALLEY": 0.01,
    "UNIT_NORWEGIAN_LONGSHIP": 0.01,
    "UNIT_ARCHER": 0.01,
    "UNIT_SPEARMAN": 0.01,
    "UNIT_HEAVY_CHARIOT": 0.01,
    "UNIT_BATTERING_RAM": 1.0,
    "UNIT_GREEK_HOPLITE": 0.01,
    "UNIT_SWORDSMAN": 0.01,
    "UNIT_HORSEMAN": 0.01,
    "UNIT_SCYTHIAN_HORSE_ARCHER": 0.01,
    "UNIT_ROMAN_LEGION": 0.01,
    "UNIT_KONGO_SHIELD_BEARER": 0.01,
    "UNIT_CATAPULT": 0.01,
    "UNIT_SIEGE_TOWER": 1.0,
    "UNIT_QUADRIREME": 0.01,
    "UNIT_EGYPTIAN_CHARIOT_ARCHER": 0.01,
    "UNIT_JAPANESE_SAMURAI": 0.01,
    "UNIT_NORWEGIAN_BERSERKER": 0.01,
    "UNIT_KNIGHT": 0.01,
    "UNIT_INDIAN_VARU": 0.01,
    "UNIT_ARABIAN_MAMLUK": 0.01,
    "UNIT_CROSSBOWMAN": 0.01,
    "UNIT_CHINESE_CROUCHING_TIGER": 0.01,
    "UNIT_MILITARY_ENGINEER": 1.0,
    "UNIT_PIKEMAN": 0.01,
    "UNIT_MUSKETMAN": 0.01,
    "UNIT_SPANISH_CONQUISTADOR": 0.01,
    "UNIT_CARAVEL": 0.01,
    "UNIT_BOMBARD": 0.01,
    "UNIT_FRIGATE": 0.01,
    "UNIT_PRIVATEER": 0.01,
    "UNIT_ENGLISH_SEADOG": 0.01,
    "UNIT_FIELD_CANNON": 0.01,
    "UNIT_CAVALRY": 0.01,
    "UNIT_RUSSIAN_COSSACK": 0.01,
    "UNIT_ENGLISH_REDCOAT": 0.01,
    "UNIT_FRENCH_GARDE_IMPERIALE": 0.01,
    "UNIT_MEDIC": 1.0,
    "UNIT_IRONCLAD": 0.01,
    "UNIT_RANGER": 0.01,
    "UNIT_OBSERVATION_BALLOON": 1.0,
    "UNIT_BIPLANE": 0.01,
    "UNIT_INFANTRY": 0.01,
    "UNIT_ARTILLERY": 0.01,
    "UNIT_BATTLESHIP": 0.01,
    "UNIT_BRAZILIAN_MINAS_GERAES": 0.01,
    "UNIT_SUBMARINE": 0.01,
    "UNIT_GERMAN_UBOAT": 0.01,
    "UNIT_AT_CREW": 0.01,
    "UNIT_TANK": 0.01,
    "UNIT_FIGHTER": 0.01,
    "UNIT_AMERICAN_P51": 0.01,
    "UNIT_BOMBER": 0.01,
    "UNIT_ANTIAIR_GUN": 0.01,
    "UNIT_MACHINE_GUN": 0.01,
    "UNIT_AIRCRAFT_CARRIER": 0.01,
    "UNIT_DESTROYER": 0.01,
    "UNIT_HELICOPTER": 0.01,
    "UNIT_NUCLEAR_SUBMARINE": 0.01,
    "UNIT_MECHANIZED_INFANTRY": 0.01,
    "UNIT_ROCKET_ARTILLERY": 0.01,
    "UNIT_MOBILE_SAM": 0.01,
    "UNIT_JET_FIGHTER": 0.01,
    "UNIT_JET_BOMBER": 0.01,
    "UNIT_MISSILE_CRUISER": 0.01,
    "UNIT_MODERN_AT": 0.01,
    "UNIT_MODERN_ARMOR": 0.01,
    "UNIT_MAN_AT_ARMS": 0.01,
    "UNIT_LINE_INFANTRY": 0.01,
    "UNIT_TREBUCHET": 0.01,
    "UNIT_AZTEC_EAGLE_WARRIOR": 0.01,
    "UNIT_INDONESIAN_JONG": 0.01,
    "UNIT_KHMER_DOMREY": 0.01,
    "UNIT_POLISH_HUSSAR": 0.01,
    "UNIT_NUBIAN_PITATI": 0.01,
    "UNIT_MACEDONIAN_HYPASPIST": 0.01,
    "UNIT_MACEDONIAN_HETAIROI": 0.01,
    "UNIT_PERSIAN_IMMORTAL": 0.01,
    "UNIT_DIGGER": 0.01,
    "UNIT_ZULU_IMPI": 0.01,
    "UNIT_KOREAN_HWACHA": 0.01,
    "UNIT_SCOTTISH_HIGHLANDER": 0.01,
    "UNIT_DE_ZEVEN_PROVINCIEN": 0.01,
    "UNIT_MONGOLIAN_KESHIG": 0.01,
    "UNIT_GEORGIAN_KHEVSURETI": 0.01,
    "UNIT_MAPUCHE_MALON_RAIDER": 0.01,
    "UNIT_CREE_OKIHTCITAW": 0.01,
    "UNIT_SPEC_OPS": 0.01,
    "UNIT_DRONE": 1.0,
    "UNIT_PIKE_AND_SHOT": 0.01,
    "UNIT_SUPPLY_CONVOY": 1.0,
    "UNIT_SKIRMISHER": 0.01,
    "UNIT_COURSER": 0.01,
    "UNIT_CUIRASSIER": 0.01,
    "UNIT_GIANT_DEATH_ROBOT": 0.01,
    "UNIT_ROCK_BAND": 1.0,
    "UNIT_CANADA_MOUNTIE": 0.01,
    "UNIT_HUNGARY_BLACK_ARMY": 0.01,
    "UNIT_HUNGARY_HUSZAR": 0.01,
    "UNIT_INCA_WARAKAQ": 0.01,
    "UNIT_MALI_MANDEKALU_CAVALRY": 0.01,
    "UNIT_MAORI_TOA": 0.01,
    "UNIT_OTTOMAN_BARBARY_CORSAIR": 0.01,
    "UNIT_PHOENICIA_BIREME": 0.01,
    "UNIT_SULEIMAN_JANISSARY": 0.01,
    "UNIT_SWEDEN_CAROLEAN": 0.01,
    "UNIT_AMERICAN_ROUGH_RIDER": 0.01,
    "UNIT_MAYAN_HULCHE": 0.01,
    "UNIT_LAHORE_NIHANG": 0.01,
    "UNIT_COMANDANTE_GENERAL": 1.0,
    "UNIT_COLOMBIAN_LLANERO": 0.01,
    "UNIT_BYZANTINE_DROMON": 0.01,
    "UNIT_BYZANTINE_TAGMA": 0.01,
    "UNIT_GAUL_GAESATAE": 0.01,
    "UNIT_VIETNAMESE_VOI_CHIEN": 0.01,
    "UNIT_ETHIOPIAN_OROMO_CAVALRY": 0.01,
    "UNIT_BABYLONIAN_SABUM_KIBITTUM": 0.01,
    "UNIT_PORTUGUESE_NAU": 0.01
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `ai_unitefficiency`

**Column Mappings:**
- `Unnamed: 0` → VARCHAR(100)
- `UNIT_SETTLER` → DECIMAL(10,2)
- `UNIT_BUILDER` → DECIMAL(10,2)
- `UNIT_TRADER` → DECIMAL(10,2)
- `UNIT_MISSIONARY` → DECIMAL(10,2)
- `UNIT_APOSTLE` → DECIMAL(10,2)
- `UNIT_INQUISITOR` → DECIMAL(10,2)
- `UNIT_GURU` → DECIMAL(10,2)
- `UNIT_WARRIOR_MONK` → DECIMAL(10,2)
- `UNIT_ARCHAEOLOGIST` → DECIMAL(10,2)
- `UNIT_GREAT_GENERAL` → DECIMAL(10,2)
- `UNIT_GREAT_ADMIRAL` → DECIMAL(10,2)
- `UNIT_GREAT_ENGINEER` → DECIMAL(10,2)
- `UNIT_GREAT_MERCHANT` → DECIMAL(10,2)
- `UNIT_GREAT_PROPHET` → DECIMAL(10,2)
- `UNIT_GREAT_SCIENTIST` → DECIMAL(10,2)
- `UNIT_GREAT_WRITER` → DECIMAL(10,2)
- `UNIT_GREAT_ARTIST` → DECIMAL(10,2)
- `UNIT_GREAT_MUSICIAN` → DECIMAL(10,2)
- `UNIT_SPY` → DECIMAL(10,2)
- `UNIT_NATURALIST` → DECIMAL(10,2)
- `UNIT_SCOUT` → DECIMAL(10,2)
- `UNIT_WARRIOR` → DECIMAL(10,2)
- `UNIT_SLINGER` → DECIMAL(10,2)
- `UNIT_BARBARIAN_HORSEMAN` → DECIMAL(10,2)
- `UNIT_BARBARIAN_HORSE_ARCHER` → DECIMAL(10,2)
- `UNIT_SUMERIAN_WAR_CART` → DECIMAL(10,2)
- `UNIT_GALLEY` → DECIMAL(10,2)
- `UNIT_NORWEGIAN_LONGSHIP` → DECIMAL(10,2)
- `UNIT_ARCHER` → DECIMAL(10,2)
- `UNIT_SPEARMAN` → DECIMAL(10,2)
- `UNIT_HEAVY_CHARIOT` → DECIMAL(10,2)
- `UNIT_BATTERING_RAM` → DECIMAL(10,2)
- `UNIT_GREEK_HOPLITE` → DECIMAL(10,2)
- `UNIT_SWORDSMAN` → DECIMAL(10,2)
- `UNIT_HORSEMAN` → DECIMAL(10,2)
- `UNIT_SCYTHIAN_HORSE_ARCHER` → DECIMAL(10,2)
- `UNIT_ROMAN_LEGION` → DECIMAL(10,2)
- `UNIT_KONGO_SHIELD_BEARER` → DECIMAL(10,2)
- `UNIT_CATAPULT` → DECIMAL(10,2)
- `UNIT_SIEGE_TOWER` → DECIMAL(10,2)
- `UNIT_QUADRIREME` → DECIMAL(10,2)
- `UNIT_EGYPTIAN_CHARIOT_ARCHER` → DECIMAL(10,2)
- `UNIT_JAPANESE_SAMURAI` → DECIMAL(10,2)
- `UNIT_NORWEGIAN_BERSERKER` → DECIMAL(10,2)
- `UNIT_KNIGHT` → DECIMAL(10,2)
- `UNIT_INDIAN_VARU` → DECIMAL(10,2)
- `UNIT_ARABIAN_MAMLUK` → DECIMAL(10,2)
- `UNIT_CROSSBOWMAN` → DECIMAL(10,2)
- `UNIT_CHINESE_CROUCHING_TIGER` → DECIMAL(10,2)
- `UNIT_MILITARY_ENGINEER` → DECIMAL(10,2)
- `UNIT_PIKEMAN` → DECIMAL(10,2)
- `UNIT_MUSKETMAN` → DECIMAL(10,2)
- `UNIT_SPANISH_CONQUISTADOR` → DECIMAL(10,2)
- `UNIT_CARAVEL` → DECIMAL(10,2)
- `UNIT_BOMBARD` → DECIMAL(10,2)
- `UNIT_FRIGATE` → DECIMAL(10,2)
- `UNIT_PRIVATEER` → DECIMAL(10,2)
- `UNIT_ENGLISH_SEADOG` → DECIMAL(10,2)
- `UNIT_FIELD_CANNON` → DECIMAL(10,2)
- `UNIT_CAVALRY` → DECIMAL(10,2)
- `UNIT_RUSSIAN_COSSACK` → DECIMAL(10,2)
- `UNIT_ENGLISH_REDCOAT` → DECIMAL(10,2)
- `UNIT_FRENCH_GARDE_IMPERIALE` → DECIMAL(10,2)
- `UNIT_MEDIC` → DECIMAL(10,2)
- `UNIT_IRONCLAD` → DECIMAL(10,2)
- `UNIT_RANGER` → DECIMAL(10,2)
- `UNIT_OBSERVATION_BALLOON` → DECIMAL(10,2)
- `UNIT_BIPLANE` → DECIMAL(10,2)
- `UNIT_INFANTRY` → DECIMAL(10,2)
- `UNIT_ARTILLERY` → DECIMAL(10,2)
- `UNIT_BATTLESHIP` → DECIMAL(10,2)
- `UNIT_BRAZILIAN_MINAS_GERAES` → DECIMAL(10,2)
- `UNIT_SUBMARINE` → DECIMAL(10,2)
- `UNIT_GERMAN_UBOAT` → DECIMAL(10,2)
- `UNIT_AT_CREW` → DECIMAL(10,2)
- `UNIT_TANK` → DECIMAL(10,2)
- `UNIT_FIGHTER` → DECIMAL(10,2)
- `UNIT_AMERICAN_P51` → DECIMAL(10,2)
- `UNIT_BOMBER` → DECIMAL(10,2)
- `UNIT_ANTIAIR_GUN` → DECIMAL(10,2)
- `UNIT_MACHINE_GUN` → DECIMAL(10,2)
- `UNIT_AIRCRAFT_CARRIER` → DECIMAL(10,2)
- `UNIT_DESTROYER` → DECIMAL(10,2)
- `UNIT_HELICOPTER` → DECIMAL(10,2)
- `UNIT_NUCLEAR_SUBMARINE` → DECIMAL(10,2)
- `UNIT_MECHANIZED_INFANTRY` → DECIMAL(10,2)
- `UNIT_ROCKET_ARTILLERY` → DECIMAL(10,2)
- `UNIT_MOBILE_SAM` → DECIMAL(10,2)
- `UNIT_JET_FIGHTER` → DECIMAL(10,2)
- `UNIT_JET_BOMBER` → DECIMAL(10,2)
- `UNIT_MISSILE_CRUISER` → DECIMAL(10,2)
- `UNIT_MODERN_AT` → DECIMAL(10,2)
- `UNIT_MODERN_ARMOR` → DECIMAL(10,2)
- `UNIT_MAN_AT_ARMS` → DECIMAL(10,2)
- `UNIT_LINE_INFANTRY` → DECIMAL(10,2)
- `UNIT_TREBUCHET` → DECIMAL(10,2)
- `UNIT_AZTEC_EAGLE_WARRIOR` → DECIMAL(10,2)
- `UNIT_INDONESIAN_JONG` → DECIMAL(10,2)
- `UNIT_KHMER_DOMREY` → DECIMAL(10,2)
- `UNIT_POLISH_HUSSAR` → DECIMAL(10,2)
- `UNIT_NUBIAN_PITATI` → DECIMAL(10,2)
- `UNIT_MACEDONIAN_HYPASPIST` → DECIMAL(10,2)
- `UNIT_MACEDONIAN_HETAIROI` → DECIMAL(10,2)
- `UNIT_PERSIAN_IMMORTAL` → DECIMAL(10,2)
- `UNIT_DIGGER` → DECIMAL(10,2)
- `UNIT_ZULU_IMPI` → DECIMAL(10,2)
- `UNIT_KOREAN_HWACHA` → DECIMAL(10,2)
- `UNIT_SCOTTISH_HIGHLANDER` → DECIMAL(10,2)
- `UNIT_DE_ZEVEN_PROVINCIEN` → DECIMAL(10,2)
- `UNIT_MONGOLIAN_KESHIG` → DECIMAL(10,2)
- `UNIT_GEORGIAN_KHEVSURETI` → DECIMAL(10,2)
- `UNIT_MAPUCHE_MALON_RAIDER` → DECIMAL(10,2)
- `UNIT_CREE_OKIHTCITAW` → DECIMAL(10,2)
- `UNIT_SPEC_OPS` → DECIMAL(10,2)
- `UNIT_DRONE` → DECIMAL(10,2)
- `UNIT_PIKE_AND_SHOT` → DECIMAL(10,2)
- `UNIT_SUPPLY_CONVOY` → DECIMAL(10,2)
- `UNIT_SKIRMISHER` → DECIMAL(10,2)
- `UNIT_COURSER` → DECIMAL(10,2)
- `UNIT_CUIRASSIER` → DECIMAL(10,2)
- `UNIT_GIANT_DEATH_ROBOT` → DECIMAL(10,2)
- `UNIT_ROCK_BAND` → DECIMAL(10,2)
- `UNIT_CANADA_MOUNTIE` → DECIMAL(10,2)
- `UNIT_HUNGARY_BLACK_ARMY` → DECIMAL(10,2)
- `UNIT_HUNGARY_HUSZAR` → DECIMAL(10,2)
- `UNIT_INCA_WARAKAQ` → DECIMAL(10,2)
- `UNIT_MALI_MANDEKALU_CAVALRY` → DECIMAL(10,2)
- `UNIT_MAORI_TOA` → DECIMAL(10,2)
- `UNIT_OTTOMAN_BARBARY_CORSAIR` → DECIMAL(10,2)
- `UNIT_PHOENICIA_BIREME` → DECIMAL(10,2)
- `UNIT_SULEIMAN_JANISSARY` → DECIMAL(10,2)
- `UNIT_SWEDEN_CAROLEAN` → DECIMAL(10,2)
- `UNIT_AMERICAN_ROUGH_RIDER` → DECIMAL(10,2)
- `UNIT_MAYAN_HULCHE` → DECIMAL(10,2)
- `UNIT_LAHORE_NIHANG` → DECIMAL(10,2)
- `UNIT_COMANDANTE_GENERAL` → DECIMAL(10,2)
- `UNIT_COLOMBIAN_LLANERO` → DECIMAL(10,2)
- `UNIT_BYZANTINE_DROMON` → DECIMAL(10,2)
- `UNIT_BYZANTINE_TAGMA` → DECIMAL(10,2)
- `UNIT_GAUL_GAESATAE` → DECIMAL(10,2)
- `UNIT_VIETNAMESE_VOI_CHIEN` → DECIMAL(10,2)
- `UNIT_ETHIOPIAN_OROMO_CAVALRY` → DECIMAL(10,2)
- `UNIT_BABYLONIAN_SABUM_KIBITTUM` → DECIMAL(10,2)
- `UNIT_PORTUGUESE_NAU` → DECIMAL(10,2)

---

## AI_Victories.csv

**File Statistics:**
- Size: 17.63 KB
- Rows: 391
- Columns: 4
- Memory Usage: 0.06 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Game Turn` | int64 | 391 | 154 | 1, 1, 1 | Range: 1 - 499 |
| ` Player` | int64 | 391 | 17 | 0, 0, 0 | Range: 0 - 63 |
| ` Strategy` | object | 391 | 15 |  STRATEGY_EARLY_EXPLORATION,  STRATEGY_RAPID_EX... | Top:  STRATEGY_RAPID_EXPANSION,  VICTORY_STRATEGY_SCIENCE_VICTORY |
| ` Status` | object | 391 | 4 |  Following,  Following,  Following | Top:  Forbidden,  Following |

### Sample Data

```json
[
  {
    "Game Turn": 1,
    " Player": 0,
    " Strategy": " STRATEGY_EARLY_EXPLORATION",
    " Status": " Following"
  },
  {
    "Game Turn": 1,
    " Player": 0,
    " Strategy": " STRATEGY_RAPID_EXPANSION",
    " Status": " Following"
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `ai_victories`

**Column Mappings:**
- `Game Turn` → INTEGER
- ` Player` → INTEGER
- ` Strategy` → VARCHAR(100)
- ` Status` → VARCHAR(100)

---

## Barbarians.csv

**File Statistics:**
- Size: 15.58 KB
- Rows: 533
- Columns: 7
- Memory Usage: 0.1 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Turn` | int64 | 533 | 502 | 1, 1, 1 | Range: 1 - 502 |
| ` Num Camps` | object | 533 | 32 |  LOC_BARBARIAN_MELEE_3,  LOC_BARBARIAN_MELEE_2,... |  |
| ` Desired Camps` | object | 533 | 4 |  UNIT_SPEARMAN,  UNIT_SPEARMAN,  UNIT_SPEARMAN | Top:  18,  UNIT_SPEARMAN |
| ` Added This Turn` | object | 533 | 34 |  8-23,  68-32,  16-28 |  |
| ` Land Plots` | float64 | 502 | 4 | 1235.0, 1235.0, 1235.0 | Range: 1161.0 - 1235.0 |
| ` No Visibility` | float64 | 502 | 322 | 1078.0, 1057.0, 1071.0 | Range: 4.0 - 1078.0 |
| ` Tribes` | float64 | 502 | 28 | 4.0, 5.0, 6.0 | Range: 4.0 - 31.0 |

### Sample Data

```json
[
  {
    "Turn": 1,
    " Num Camps": " LOC_BARBARIAN_MELEE_3",
    " Desired Camps": " UNIT_SPEARMAN",
    " Added This Turn": " 8-23",
    " Land Plots": NaN,
    " No Visibility": NaN,
    " Tribes": NaN
  },
  {
    "Turn": 1,
    " Num Camps": " LOC_BARBARIAN_MELEE_2",
    " Desired Camps": " UNIT_SPEARMAN",
    " Added This Turn": " 68-32",
    " Land Plots": NaN,
    " No Visibility": NaN,
    " Tribes": NaN
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `barbarians`

**Column Mappings:**
- `Turn` → INTEGER
- ` Num Camps` → VARCHAR(100)
- ` Desired Camps` → VARCHAR(100)
- ` Added This Turn` → VARCHAR(100)
- ` Land Plots` → DECIMAL(10,2)
- ` No Visibility` → DECIMAL(10,2)
- ` Tribes` → DECIMAL(10,2)

---

## Barbarians_Units.csv

**File Statistics:**
- Size: 7.01 KB
- Rows: 233
- Columns: 3
- Memory Usage: 0.02 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Turn` | int64 | 233 | 150 | 1, 1, 1 | Range: 1 - 417 |
| ` TribeIndex` | int64 | 233 | 31 | 0, 0, 1 | Range: 0 - 30 |
| ` Unit Spawned` | object | 233 | 20 |  LOC_UNIT_SPEARMAN_NAME,  LOC_UNIT_SCOUT_NAME, ... | Top:  LOC_UNIT_WARRIOR_NAME,  LOC_UNIT_SCOUT_NAME |

### Sample Data

```json
[
  {
    "Turn": 1,
    " TribeIndex": 0,
    " Unit Spawned": " LOC_UNIT_SPEARMAN_NAME"
  },
  {
    "Turn": 1,
    " TribeIndex": 0,
    " Unit Spawned": " LOC_UNIT_SCOUT_NAME"
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `barbarians_units`

**Column Mappings:**
- `Turn` → INTEGER
- ` TribeIndex` → INTEGER
- ` Unit Spawned` → VARCHAR(100)

---

## City_BuildQueue.csv

**File Statistics:**
- Size: 1699.74 KB
- Rows: 24,765
- Columns: 7
- Memory Usage: 4.25 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Game Turn` | int64 | 24,765 | 502 | 2, 2, 2 | Range: 2 - 503 |
| ` City` | object | 24,765 | 86 |  LOC_CITY_NAME_KRAKOW,  LOC_CITY_NAME_NIDAROS, ... |  |
| ` Production Added` | float64 | 24,765 | 1,131 | 7.0, 6.0, 6.0 | Range: 0.0 - 3000.0 |
| ` Current Item` | object | 24,765 | 187 |  BUILDING_MONUMENT,  UNIT_SCOUT,  UNIT_SCOUT |  |
| ` Current Production` | float64 | 24,765 | 6,325 | 7.0, 6.0, 6.0 | Range: 0.0 - 3295.0 |
| ` Production Needed` | int64 | 24,765 | 312 | 60, 30, 30 | Range: 0 - 3200 |
| ` Overflow` | float64 | 24,765 | 423 | 0.0, 0.0, 0.0 | Range: 0.0 - 183.4 |

### Sample Data

```json
[
  {
    "Game Turn": 2,
    " City": " LOC_CITY_NAME_KRAKOW",
    " Production Added": 7.0,
    " Current Item": " BUILDING_MONUMENT",
    " Current Production": 7.0,
    " Production Needed": 60,
    " Overflow": 0.0
  },
  {
    "Game Turn": 2,
    " City": " LOC_CITY_NAME_NIDAROS",
    " Production Added": 6.0,
    " Current Item": " UNIT_SCOUT",
    " Current Production": 6.0,
    " Production Needed": 30,
    " Overflow": 0.0
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `city_buildqueue`

**Column Mappings:**
- `Game Turn` → INTEGER
- ` City` → VARCHAR(100)
- ` Production Added` → DECIMAL(10,2)
- ` Current Item` → VARCHAR(100)
- ` Current Production` → DECIMAL(10,2)
- ` Production Needed` → INTEGER
- ` Overflow` → DECIMAL(10,2)

---

## CombatLog.csv

**File Statistics:**
- Size: 177.6 KB
- Rows: 2,055
- Columns: 15
- Memory Usage: 0.66 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Game Turn` | int64 | 2,055 | 450 | 4, 4, 5 | Range: 4 - 502 |
| ` Attacking Civ` | int64 | 2,055 | 17 | 3, 12, 12 | Range: 0 - 63 |
| ` DefendingCiv` | int64 | 2,055 | 18 | 63, 63, 63 | Range: -1 - 63 |
| ` AttackerObjType` | object | 2,055 | 4 |  1:1,  1:1,  1:1 | Top:  1:1,  3:1 |
| ` DefenderObjType` | object | 2,055 | 1,087 |  131073:655369,  131073:65536,  131073:65536 |  |
| ` Attacker Type` | object | 2,055 | 49 |  UNIT_WARRIOR,  UNIT_WARRIOR,  UNIT_WARRIOR |  |
| ` Defender Type` | object | 2,055 | 46 |  UNIT_SCOUT,  UNIT_SPEARMAN,  UNIT_SPEARMAN |  |
| ` AttackerID` | int64 | 2,055 | 34 | 20, 20, 20 | Range: 3 - 130 |
| ` DefenderID` | int64 | 2,055 | 39 | 10, 25, 25 | Range: 0 - 30210 |
| ` AttackerStr` | int64 | 2,055 | 50 | 0, 5, 0 | Range: -30 - 27 |
| ` DefenderStr` | int64 | 2,055 | 60 | 3, 9, 7 | Range: -24 - 62 |
| ` AttackerStrMod` | int64 | 2,055 | 74 | 19, 47, 44 | Range: 0 - 100 |
| ` DefenderStrMod` | int64 | 2,055 | 112 | 35, 20, 15 | Range: 0 - 200 |
| ` AttackerDmg` | float64 | 0 | 0 |  | Range: nan - nan |
| ` DefenderDmg` | float64 | 0 | 0 |  | Range: nan - nan |

### Sample Data

```json
[
  {
    "Game Turn": 4,
    " Attacking Civ": 3,
    " DefendingCiv": 63,
    " AttackerObjType": " 1:1",
    " DefenderObjType": " 131073:655369",
    " Attacker Type": " UNIT_WARRIOR",
    " Defender Type": " UNIT_SCOUT",
    " AttackerID": 20,
    " DefenderID": 10,
    " AttackerStr": 0,
    " DefenderStr": 3,
    " AttackerStrMod": 19,
    " DefenderStrMod": 35,
    " AttackerDmg": NaN,
    " DefenderDmg": NaN
  },
  {
    "Game Turn": 4,
    " Attacking Civ": 12,
    " DefendingCiv": 63,
    " AttackerObjType": " 1:1",
    " DefenderObjType": " 131073:65536",
    " Attacker Type": " UNIT_WARRIOR",
    " Defender Type": " UNIT_SPEARMAN",
    " AttackerID": 20,
    " DefenderID": 25,
    " AttackerStr": 5,
    " DefenderStr": 9,
    " AttackerStrMod": 47,
    " DefenderStrMod": 20,
    " AttackerDmg": NaN,
    " DefenderDmg": NaN
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `combatlog`

**Column Mappings:**
- `Game Turn` → INTEGER
- ` Attacking Civ` → INTEGER
- ` DefendingCiv` → INTEGER
- ` AttackerObjType` → VARCHAR(100)
- ` DefenderObjType` → VARCHAR(100)
- ` Attacker Type` → VARCHAR(100)
- ` Defender Type` → VARCHAR(100)
- ` AttackerID` → INTEGER
- ` DefenderID` → INTEGER
- ` AttackerStr` → INTEGER
- ` DefenderStr` → INTEGER
- ` AttackerStrMod` → INTEGER
- ` DefenderStrMod` → INTEGER
- ` AttackerDmg` → DECIMAL(10,2)
- ` DefenderDmg` → DECIMAL(10,2)

---

## Cultural_Identity.csv

**File Statistics:**
- Size: 3.8 KB
- Rows: 32
- Columns: 11
- Memory Usage: 0.02 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Turn` | int64 | 32 | 29 | 129, 156, 158 | Range: 129 - 494 |
| ` EventType` | object | 32 | 2 |  City Captured,  City Captured,  City Transferred | Top:  City Captured,  City Transferred |
| ` CityName` | object | 32 | 19 |  LOC_CITY_NAME_SARPSBORG,  LOC_CITY_NAME_WENTE_... | Top:  LOC_CITY_NAME_HAMAR,  LOC_CITY_NAME_HAMBURG |
| ` Owner` | int64 | 32 | 5 | 5, 5, 62 | Range: 0 - 62 |
| ` OwnerName` | object | 32 | 5 |  LOC_LEADER_LADY_SIX_SKY_NAME,  LOC_LEADER_LADY... | Top:  LOC_LEADER_LADY_SIX_SKY_NAME,  LOC_CIVILIZATION_FREE_CITIES_NAME |
| ` Pop` | int64 | 32 | 12 | 1, 5, 2 | Range: 1 - 12 |
| ` IdentityA` | object | 32 | 8 |  NULL,  NULL,  NULL | Top:  NULL,  Player:1 Total:122 |
| ` IdentityB` | object | 32 | 8 |  NULL,  NULL,  NULL | Top:  NULL,  Player:5 Total:134 |
| ` IdentityC` | object | 32 | 1 |  NULL,  NULL,  NULL | Top:  NULL |
| ` IdentityD` | object | 32 | 1 |  NULL,  NULL,  NULL | Top:  NULL |
| ` IdentityE` | object | 32 | 1 |  NULL,  NULL,  NULL | Top:  NULL |

### Sample Data

```json
[
  {
    "Turn": 129,
    " EventType": " City Captured",
    " CityName": " LOC_CITY_NAME_SARPSBORG",
    " Owner": 5,
    " OwnerName": " LOC_LEADER_LADY_SIX_SKY_NAME",
    " Pop": 1,
    " IdentityA": " NULL",
    " IdentityB": " NULL",
    " IdentityC": " NULL",
    " IdentityD": " NULL",
    " IdentityE": " NULL"
  },
  {
    "Turn": 156,
    " EventType": " City Captured",
    " CityName": " LOC_CITY_NAME_WENTE_MAPU",
    " Owner": 5,
    " OwnerName": " LOC_LEADER_LADY_SIX_SKY_NAME",
    " Pop": 5,
    " IdentityA": " NULL",
    " IdentityB": " NULL",
    " IdentityC": " NULL",
    " IdentityD": " NULL",
    " IdentityE": " NULL"
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `cultural_identity`

**Column Mappings:**
- `Turn` → INTEGER
- ` EventType` → VARCHAR(100)
- ` CityName` → VARCHAR(100)
- ` Owner` → INTEGER
- ` OwnerName` → VARCHAR(100)
- ` Pop` → INTEGER
- ` IdentityA` → VARCHAR(100)
- ` IdentityB` → VARCHAR(100)
- ` IdentityC` → VARCHAR(100)
- ` IdentityD` → VARCHAR(100)
- ` IdentityE` → VARCHAR(100)

---

## DiplomacyManager.csv

**File Statistics:**
- Size: 87.22 KB
- Rows: 1,075
- Columns: 7
- Memory Usage: 0.34 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Game Turn` | int64 | 1,075 | 6 | 0, 4, 5 | Range: 0 - 5 |
| ` From` | int64 | 1,075 | 8 | 4, 0, 2 | Range: 0 - 14 |
| ` To` | object | 1,075 | 2 |  ?,  ?,  ? | Top:  -1,  ? |
| ` Initiator` | object | 1,075 | 15 |  SET_DELEGATION,  SET_DELEGATION,  SET_DELEGATION | Top:  MAKE_PROMISE,  DIPLOMATIC_HIDDEN_AGENDA_KUDO |
| ` Type` | object | 1,075 | 7 |  ffffffff,  ffffffff,  ffffffff | Top:  NONE,  ffffffff |
| ` SubType` | object | 1,075 | 3 |  ?,  ?,  ? | Top:  ?,  00000000 |
| ` Message` | object | 1,075 | 3 |  Processing Action From AI to ,  Processing Act... | Top:  Processing Action From AI to AI,  Requesting Session (B) |

### Sample Data

```json
[
  {
    "Game Turn": 0,
    " From": 4,
    " To": " ?",
    " Initiator": " SET_DELEGATION",
    " Type": " ffffffff",
    " SubType": " ?",
    " Message": " Processing Action From AI to AI"
  },
  {
    "Game Turn": 4,
    " From": 0,
    " To": " ?",
    " Initiator": " SET_DELEGATION",
    " Type": " ffffffff",
    " SubType": " ?",
    " Message": " Processing Action From AI to AI"
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `diplomacymanager`

**Column Mappings:**
- `Game Turn` → INTEGER
- ` From` → INTEGER
- ` To` → VARCHAR(100)
- ` Initiator` → VARCHAR(100)
- ` Type` → VARCHAR(100)
- ` SubType` → VARCHAR(100)
- ` Message` → VARCHAR(100)

---

## DiplomacyModifiers.csv

**File Statistics:**
- Size: 443.47 KB
- Rows: 0
- Columns: 0
- Memory Usage: 0 MB

❌ **Error:** Error tokenizing data. C error: Expected 11 fields in line 205, saw 12


## DiplomacySummary.csv

**File Statistics:**
- Size: 131.23 KB
- Rows: 1,728
- Columns: 7
- Memory Usage: 0.39 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Game Turn` | int64 | 1,728 | 327 | 1, 1, 1 | Range: 1 - 503 |
| ` Initiator` | int64 | 1,728 | 17 | 63, 0, 63 | Range: 0 - 63 |
| ` Recipient` | object | 1,728 | 32 |  0,  63,  0 |  |
| ` Action` | object | 1,728 | 26 |  Met,  Met,  At War |  |
| ` Details` | object | 1,728 | 159 |  ,  ,  Surprise |  |
| ` Mayhem` | float64 | 1,728 | 543 | 0.0, 0.0, 0.0 | Range: 0.0 - 2851.5 |
| ` Visibility` | float64 | 1,514 | 5 | 0.0, 0.0, 0.0 | Range: 0.0 - 4.0 |

### Sample Data

```json
[
  {
    "Game Turn": 1,
    " Initiator": 63,
    " Recipient": " 0",
    " Action": " Met",
    " Details": " ",
    " Mayhem": 0.0,
    " Visibility": 0.0
  },
  {
    "Game Turn": 1,
    " Initiator": 0,
    " Recipient": " 63",
    " Action": " Met",
    " Details": " ",
    " Mayhem": 0.0,
    " Visibility": 0.0
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `diplomacysummary`

**Column Mappings:**
- `Game Turn` → INTEGER
- ` Initiator` → INTEGER
- ` Recipient` → VARCHAR(100)
- ` Action` → VARCHAR(100)
- ` Details` → VARCHAR(100)
- ` Mayhem` → DECIMAL(10,2)
- ` Visibility` → DECIMAL(10,2)

---

## DynamicEmpires.csv

**File Statistics:**
- Size: 17.3 KB
- Rows: 0
- Columns: 0
- Memory Usage: 0 MB

❌ **Error:** Error tokenizing data. C error: Expected 23 fields in line 8, saw 30


## Game_Boosts.csv

**File Statistics:**
- Size: 14.5 KB
- Rows: 392
- Columns: 4
- Memory Usage: 0.05 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Game Turn` | int64 | 392 | 233 | 1, 1, 1 | Range: 1 - 493 |
| ` Player` | int64 | 392 | 16 | 0, 9, 1 | Range: 0 - 62 |
| ` Boosted System` | object | 392 | 89 |  CIVIC_FOREIGN_TRADE,  CIVIC_FOREIGN_TRADE,  TE... |  |
| ` Progress` | object | 392 | 3 |  Unstarted,  Unstarted,  Unstarted | Top:  Unstarted,  Completed |

### Sample Data

```json
[
  {
    "Game Turn": 1,
    " Player": 0,
    " Boosted System": " CIVIC_FOREIGN_TRADE",
    " Progress": " Unstarted"
  },
  {
    "Game Turn": 1,
    " Player": 9,
    " Boosted System": " CIVIC_FOREIGN_TRADE",
    " Progress": " Unstarted"
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `game_boosts`

**Column Mappings:**
- `Game Turn` → INTEGER
- ` Player` → INTEGER
- ` Boosted System` → VARCHAR(100)
- ` Progress` → VARCHAR(100)

---

## Game_Emergencies.csv

**File Statistics:**
- Size: 3.74 KB
- Rows: 0
- Columns: 0
- Memory Usage: 0 MB

❌ **Error:** Error tokenizing data. C error: Expected 5 fields in line 4, saw 6


## Game_GreatPeople.csv

**File Statistics:**
- Size: 43.51 KB
- Rows: 383
- Columns: 8
- Memory Usage: 0.12 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Turn` | int64 | 383 | 186 | 1, 1, 1 | Range: 1 - 480 |
| ` Event` | object | 383 | 3 |  Added to Present Timeline,  Added to Present T... | Top:  Great Person Activated,  Added to Present Timeline |
| ` GP Individual` | object | 383 | 112 |  GREAT_PERSON_INDIVIDUAL_BOUDI,  GREAT_PERSON_I... |  |
| ` GP Class` | object | 383 | 9 |  GREAT_PERSON_CLASS_GENERAL,  GREAT_PERSON_CLAS... | Top:  GREAT_PERSON_CLASS_GENERAL,  GREAT_PERSON_CLASS_ARTIST |
| ` GP Era` | object | 383 | 8 |  ERA_CLASSICAL,  ERA_CLASSICAL,  ERA_MEDIEVAL | Top:  Era TBD,  ERA_MODERN |
| ` GP Cost` | int64 | 383 | 19 | 60, 60, 120 | Range: 0 - 1715 |
| ` Recipient Player` | float64 | 224 | 7 | -1.0, -1.0, -1.0 | Range: -1.0 - 5.0 |
| ` Timeline Index` | float64 | 224 | 91 | -1.0, -1.0, -1.0 | Range: -1.0 - 465.0 |

### Sample Data

```json
[
  {
    "Turn": 1,
    " Event": " Added to Present Timeline",
    " GP Individual": " GREAT_PERSON_INDIVIDUAL_BOUDICA",
    " GP Class": " GREAT_PERSON_CLASS_GENERAL",
    " GP Era": " ERA_CLASSICAL",
    " GP Cost": 60,
    " Recipient Player": -1.0,
    " Timeline Index": -1.0
  },
  {
    "Turn": 1,
    " Event": " Added to Present Timeline",
    " GP Individual": " GREAT_PERSON_INDIVIDUAL_ARTEMISIA",
    " GP Class": " GREAT_PERSON_CLASS_ADMIRAL",
    " GP Era": " ERA_CLASSICAL",
    " GP Cost": 60,
    " Recipient Player": -1.0,
    " Timeline Index": -1.0
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `game_greatpeople`

**Column Mappings:**
- `Turn` → INTEGER
- ` Event` → VARCHAR(100)
- ` GP Individual` → VARCHAR(100)
- ` GP Class` → VARCHAR(100)
- ` GP Era` → VARCHAR(100)
- ` GP Cost` → INTEGER
- ` Recipient Player` → DECIMAL(10,2)
- ` Timeline Index` → DECIMAL(10,2)

---

## Game_HeroesManager_HeroStats.csv

**File Statistics:**
- Size: 0.04 KB
- Rows: 0
- Columns: 4
- Memory Usage: 0.0 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Turn` | object | 0 | 0 |  | Top:  |
| ` Hero` | object | 0 | 0 |  | Top:  |
| ` Discoveries` | object | 0 | 0 |  | Top:  |
| ` Appearances` | object | 0 | 0 |  | Top:  |
### Database Mapping Suggestions

**Recommended Table Name:** `game_heroesmanager_herostats`

**Column Mappings:**
- `Turn` → VARCHAR(100)
- ` Hero` → VARCHAR(100)
- ` Discoveries` → VARCHAR(100)
- ` Appearances` → VARCHAR(100)

---

## Game_HeroesManager_PlayerStats.csv

**File Statistics:**
- Size: 141.0 KB
- Rows: 3,018
- Columns: 7
- Memory Usage: 0.48 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Turn` | int64 | 3,018 | 503 | 1, 1, 1 | Range: 1 - 503 |
| ` PlayerIndex` | int64 | 3,018 | 6 | 0, 1, 2 | Range: 0 - 5 |
| ` Control` | object | 3,018 | 2 |  Human,  AI,  AI | Top:  AI,  Human |
| ` HeroesDiscovered` | int64 | 3,018 | 1 | 0, 0, 0 | Range: 0 - 0 |
| ` HeroesClaimed` | int64 | 3,018 | 1 | 0, 0, 0 | Range: 0 - 0 |
| ` HeroesRecalled` | int64 | 3,018 | 1 | 0, 0, 0 | Range: 0 - 0 |
| ` DiscoveryOrder` | object | 3,018 | 1 |  Rebuilding Discovery Order,  Rebuilding Discov... | Top:  Rebuilding Discovery Order |

### Sample Data

```json
[
  {
    "Turn": 1,
    " PlayerIndex": 0,
    " Control": " Human",
    " HeroesDiscovered": 0,
    " HeroesClaimed": 0,
    " HeroesRecalled": 0,
    " DiscoveryOrder": " Rebuilding Discovery Order"
  },
  {
    "Turn": 1,
    " PlayerIndex": 1,
    " Control": " AI",
    " HeroesDiscovered": 0,
    " HeroesClaimed": 0,
    " HeroesRecalled": 0,
    " DiscoveryOrder": " Rebuilding Discovery Order"
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `game_heroesmanager_playerstats`

**Column Mappings:**
- `Turn` → INTEGER
- ` PlayerIndex` → INTEGER
- ` Control` → VARCHAR(100)
- ` HeroesDiscovered` → INTEGER
- ` HeroesClaimed` → INTEGER
- ` HeroesRecalled` → INTEGER
- ` DiscoveryOrder` → VARCHAR(100)

---

## Game_Influence.csv

**File Statistics:**
- Size: 11.71 KB
- Rows: 378
- Columns: 5
- Memory Usage: 0.04 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Turn` | int64 | 378 | 155 | 3, 6, 7 | Range: 3 - 501 |
| ` Event` | object | 378 | 12 |  Token used by 3,  Token used by 2,  Token used... | Top:  Token used by 4,  Token used by 5 |
| ` Origin Civ` | int64 | 378 | 6 | 3, 2, 5 | Range: 0 - 5 |
| ` Destination Civ` | int64 | 378 | 9 | 10, 6, 12 | Range: 6 - 14 |
| ` Total Tokens Given` | int64 | 378 | 14 | 1, 1, 1 | Range: 1 - 14 |

### Sample Data

```json
[
  {
    "Turn": 3,
    " Event": " Token used by 3",
    " Origin Civ": 3,
    " Destination Civ": 10,
    " Total Tokens Given": 1
  },
  {
    "Turn": 6,
    " Event": " Token used by 2",
    " Origin Civ": 2,
    " Destination Civ": 6,
    " Total Tokens Given": 1
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `game_influence`

**Column Mappings:**
- `Turn` → INTEGER
- ` Event` → VARCHAR(100)
- ` Origin Civ` → INTEGER
- ` Destination Civ` → INTEGER
- ` Total Tokens Given` → INTEGER

---

## Game_PlayerScores.csv

**File Statistics:**
- Size: 459.03 KB
- Rows: 8,450
- Columns: 16
- Memory Usage: 1.03 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Game Turn` | int64 | 8,450 | 503 | 1, 1, 1 | Range: 1 - 503 |
| ` Player` | int64 | 8,450 | 17 | 0, 1, 2 | Range: 0 - 63 |
| ` Score` | int64 | 8,450 | 1,126 | 4, 0, 0 | Range: 0 - 1866 |
| ` CATEGORY_CIVICS` | int64 | 8,450 | 68 | 0, 0, 0 | Range: 0 - 201 |
| ` CATEGORY_EMPIRE` | int64 | 8,450 | 539 | 0, 0, 0 | Range: 0 - 815 |
| ` CATEGORY_GREAT_PEOPLE` | int64 | 8,450 | 44 | 0, 0, 0 | Range: 0 - 215 |
| ` CATEGORY_RELIGION` | int64 | 8,450 | 48 | 0, 0, 0 | Range: 0 - 94 |
| ` CATEGORY_TECH` | int64 | 8,450 | 88 | 0, 0, 0 | Range: 0 - 174 |
| ` CATEGORY_WONDER` | int64 | 8,450 | 14 | 0, 0, 0 | Range: 0 - 195 |
| ` CATEGORY_TRADE` | int64 | 8,450 | 1 | 0, 0, 0 | Range: 0 - 0 |
| ` CATEGORY_PILLAGE` | int64 | 8,450 | 1 | 0, 0, 0 | Range: 0 - 0 |
| ` CATEGORY_INCOME` | int64 | 8,450 | 1 | 0, 0, 0 | Range: 0 - 0 |
| ` CATEGORY_SCENARIO1` | int64 | 8,450 | 1 | 0, 0, 0 | Range: 0 - 0 |
| ` CATEGORY_SCENARIO2` | int64 | 8,450 | 1 | 0, 0, 0 | Range: 0 - 0 |
| ` CATEGORY_SCENARIO3` | int64 | 8,450 | 1 | 0, 0, 0 | Range: 0 - 0 |
| ` CATEGORY_E` | int64 | 8,450 | 237 | 4, 0, 0 | Range: 0 - 281 |

### Sample Data

```json
[
  {
    "Game Turn": 1,
    " Player": 0,
    " Score": 4,
    " CATEGORY_CIVICS": 0,
    " CATEGORY_EMPIRE": 0,
    " CATEGORY_GREAT_PEOPLE": 0,
    " CATEGORY_RELIGION": 0,
    " CATEGORY_TECH": 0,
    " CATEGORY_WONDER": 0,
    " CATEGORY_TRADE": 0,
    " CATEGORY_PILLAGE": 0,
    " CATEGORY_INCOME": 0,
    " CATEGORY_SCENARIO1": 0,
    " CATEGORY_SCENARIO2": 0,
    " CATEGORY_SCENARIO3": 0,
    " CATEGORY_E": 4
  },
  {
    "Game Turn": 1,
    " Player": 1,
    " Score": 0,
    " CATEGORY_CIVICS": 0,
    " CATEGORY_EMPIRE": 0,
    " CATEGORY_GREAT_PEOPLE": 0,
    " CATEGORY_RELIGION": 0,
    " CATEGORY_TECH": 0,
    " CATEGORY_WONDER": 0,
    " CATEGORY_TRADE": 0,
    " CATEGORY_PILLAGE": 0,
    " CATEGORY_INCOME": 0,
    " CATEGORY_SCENARIO1": 0,
    " CATEGORY_SCENARIO2": 0,
    " CATEGORY_SCENARIO3": 0,
    " CATEGORY_E": 0
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `game_playerscores`

**Column Mappings:**
- `Game Turn` → INTEGER
- ` Player` → INTEGER
- ` Score` → INTEGER
- ` CATEGORY_CIVICS` → INTEGER
- ` CATEGORY_EMPIRE` → INTEGER
- ` CATEGORY_GREAT_PEOPLE` → INTEGER
- ` CATEGORY_RELIGION` → INTEGER
- ` CATEGORY_TECH` → INTEGER
- ` CATEGORY_WONDER` → INTEGER
- ` CATEGORY_TRADE` → INTEGER
- ` CATEGORY_PILLAGE` → INTEGER
- ` CATEGORY_INCOME` → INTEGER
- ` CATEGORY_SCENARIO1` → INTEGER
- ` CATEGORY_SCENARIO2` → INTEGER
- ` CATEGORY_SCENARIO3` → INTEGER
- ` CATEGORY_E` → INTEGER

---

## Game_RandomEvents.csv

**File Statistics:**
- Size: 83.39 KB
- Rows: 1,136
- Columns: 16
- Memory Usage: 0.53 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Game Turn` | int64 | 1,136 | 502 | 2, 3, 4 | Range: 2 - 503 |
| ` Realism` | object | 1,136 | 10 |  2,  2,  2 | Top:  2,  ONEOFF |
| ` Total CO2` | object | 1,136 | 364 |  0,  0,  0 |  |
| ` CO2 Bldgs` | object | 1,136 | 387 |  0,  0,  0 |  |
| ` CO2 Projects` | object | 1,042 | 228 |  0,  0,  0 |  |
| ` CO2 Routes` | object | 973 | 95 |  0,  0,  0 |  |
| ` CO2 Units` | object | 730 | 229 |  0,  0,  0 |  |
| ` Deforestation` | object | 718 | 36 |  0,  0,  0 |  |
| ` ClimateChange` | object | 708 | 50 |  0,  0,  0 |  |
| ` Volcanoes (Total)` | float64 | 519 | 17 | 6.0, 6.0, 6.0 | Range: 6.0 - 3140.0 |
| ` NW Volcanoes` | float64 | 502 | 1 | 1.0, 1.0, 1.0 | Range: 1.0 - 1.0 |
| ` Volcanoes (Active)` | float64 | 502 | 5 | 0.0, 0.0, 0.0 | Range: 0.0 - 4.0 |
| ` Eruptions` | float64 | 502 | 42 | 0.0, 0.0, 0.0 | Range: 0.0 - 41.0 |
| ` Floodable Rivers` | float64 | 502 | 6 | 9.0, 9.0, 9.0 | Range: 9.0 - 14.0 |
| ` Floods` | float64 | 502 | 76 | 0.0, 0.0, 0.0 | Range: 0.0 - 75.0 |
| ` NaturalWonderEruptions` | float64 | 502 | 8 | 0.0, 0.0, 0.0 | Range: 0.0 - 7.0 |

### Sample Data

```json
[
  {
    "Game Turn": 2,
    " Realism": " 2",
    " Total CO2": " 0",
    " CO2 Bldgs": " 0",
    " CO2 Projects": " 0",
    " CO2 Routes": " 0",
    " CO2 Units": " 0",
    " Deforestation": " 0",
    " ClimateChange": " 0",
    " Volcanoes (Total)": 6.0,
    " NW Volcanoes": 1.0,
    " Volcanoes (Active)": 0.0,
    " Eruptions": 0.0,
    " Floodable Rivers": 9.0,
    " Floods": 0.0,
    " NaturalWonderEruptions": 0.0
  },
  {
    "Game Turn": 3,
    " Realism": " 2",
    " Total CO2": " 0",
    " CO2 Bldgs": " 0",
    " CO2 Projects": " 0",
    " CO2 Routes": " 0",
    " CO2 Units": " 0",
    " Deforestation": " 0",
    " ClimateChange": " 0",
    " Volcanoes (Total)": 6.0,
    " NW Volcanoes": 1.0,
    " Volcanoes (Active)": 0.0,
    " Eruptions": 0.0,
    " Floodable Rivers": 9.0,
    " Floods": 0.0,
    " NaturalWonderEruptions": 0.0
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `game_randomevents`

**Column Mappings:**
- `Game Turn` → INTEGER
- ` Realism` → VARCHAR(100)
- ` Total CO2` → VARCHAR(100)
- ` CO2 Bldgs` → VARCHAR(100)
- ` CO2 Projects` → VARCHAR(100)
- ` CO2 Routes` → VARCHAR(100)
- ` CO2 Units` → VARCHAR(100)
- ` Deforestation` → VARCHAR(100)
- ` ClimateChange` → VARCHAR(100)
- ` Volcanoes (Total)` → DECIMAL(10,2)
- ` NW Volcanoes` → DECIMAL(10,2)
- ` Volcanoes (Active)` → DECIMAL(10,2)
- ` Eruptions` → DECIMAL(10,2)
- ` Floodable Rivers` → DECIMAL(10,2)
- ` Floods` → DECIMAL(10,2)
- ` NaturalWonderEruptions` → DECIMAL(10,2)

---

## Game_Religion.csv

**File Statistics:**
- Size: 32.36 KB
- Rows: 630
- Columns: 5
- Memory Usage: 0.12 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Game Turn` | int64 | 630 | 17 | 16, 16, 37 | Range: 16 - 218 |
| ` Player` | int64 | 630 | 16 | 5, 5, 1 | Range: 0 - 62 |
| ` Action` | object | 630 | 8 |  Found Pantheon,  Adopt Pantheon,  Found Pantheon | Top:  Adopt Religion,  Adopt Pantheon |
| ` Belief` | object | 630 | 27 |  BELIEF_RELIGIOUS_SETTLEMENTS,  N/A,  BELIEF_GO... |  |
| ` City` | object | 630 | 48 |  N/A,  LOC_CITY_NAME_NARANJO,  N/A |  |

### Sample Data

```json
[
  {
    "Game Turn": 16,
    " Player": 5,
    " Action": " Found Pantheon",
    " Belief": " BELIEF_RELIGIOUS_SETTLEMENTS",
    " City": " N/A"
  },
  {
    "Game Turn": 16,
    " Player": 5,
    " Action": " Adopt Pantheon",
    " Belief": " N/A",
    " City": " LOC_CITY_NAME_NARANJO"
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `game_religion`

**Column Mappings:**
- `Game Turn` → INTEGER
- ` Player` → INTEGER
- ` Action` → VARCHAR(100)
- ` Belief` → VARCHAR(100)
- ` City` → VARCHAR(100)

---

## Game_TradeManager.csv

**File Statistics:**
- Size: 78.38 KB
- Rows: 440
- Columns: 6
- Memory Usage: 0.05 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Turn` | float64 | 440 | 2 | 0.0, 0.0, 0.0 | Range: 0.0 - 2.0 |
| ` Event` | float64 | 440 | 2 | 0.0, 0.0, 0.0 | Range: 0.0 - 2.0 |
| ` Origin City` | float64 | 440 | 3 | 0.0, 0.0, 0.0 | Range: 0.0 - 4.0 |
| ` Destination City` | float64 | 440 | 2 | 0.0, 0.0, 0.0 | Range: 0.0 - 2.0 |
| ` Attached Resource` | float64 | 440 | 2 | 0.0, 0.0, 0.0 | Range: 0.0 - 2.0 |
| ` Origin Yields` | float64 | 440 | 1 | 0.0, 0.0, 0.0 | Range: 0.0 - 0.0 |

### Sample Data

```json
[
  {
    "Turn": 0.0,
    " Event": 0.0,
    " Origin City": 0.0,
    " Destination City": 0.0,
    " Attached Resource": 0.0,
    " Origin Yields": 0.0
  },
  {
    "Turn": 0.0,
    " Event": 0.0,
    " Origin City": 0.0,
    " Destination City": 0.0,
    " Attached Resource": 0.0,
    " Origin Yields": 0.0
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `game_trademanager`

**Column Mappings:**
- `Turn` → DECIMAL(10,2)
- ` Event` → DECIMAL(10,2)
- ` Origin City` → DECIMAL(10,2)
- ` Destination City` → DECIMAL(10,2)
- ` Attached Resource` → DECIMAL(10,2)
- ` Origin Yields` → DECIMAL(10,2)

---

## Governors.csv

**File Statistics:**
- Size: 89.44 KB
- Rows: 973
- Columns: 5
- Memory Usage: 0.27 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Turn` | int64 | 973 | 347 | 36, 36, 36 | Range: 36 - 502 |
| ` EventType` | object | 973 | 5 |  Governor Promoted,  Governor Appointed,  Gover... | Top:  Governor Assigned,  Governor Established |
| ` GovernorName` | object | 973 | 7 |  LOC_GOVERNOR_THE_CARDINAL_NAM,  LOC_GOVERNOR_T... | Top:  LOC_GOVERNOR_THE_MERCHANT_NAME,  LOC_GOVERNOR_THE_DEFENDER_NAME |
| ` Owner` | object | 973 | 6 |  CIVILIZATION_GERMANY,  CIVILIZATION_GERMANY,  ... | Top:  CIVILIZATION_MAYA,  CIVILIZATION_MAPUCHE |
| ` City` | object | 973 | 66 |  NO CITY,  NO CITY,  LOC_CITY_NAME_MUNICH_CAPITAL |  |

### Sample Data

```json
[
  {
    "Turn": 36,
    " EventType": " Governor Promoted",
    " GovernorName": " LOC_GOVERNOR_THE_CARDINAL_NAME",
    " Owner": " CIVILIZATION_GERMANY",
    " City": " NO CITY"
  },
  {
    "Turn": 36,
    " EventType": " Governor Appointed",
    " GovernorName": " LOC_GOVERNOR_THE_CARDINAL_NAME",
    " Owner": " CIVILIZATION_GERMANY",
    " City": " NO CITY"
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `governors`

**Column Mappings:**
- `Turn` → INTEGER
- ` EventType` → VARCHAR(100)
- ` GovernorName` → VARCHAR(100)
- ` Owner` → VARCHAR(100)
- ` City` → VARCHAR(100)

---

## Player_Stats.csv

**File Statistics:**
- Size: 707.95 KB
- Rows: 7,948
- Columns: 20
- Memory Usage: 1.68 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Game Turn` | int64 | 7,948 | 503 | 1, 1, 1 | Range: 1 - 503 |
| ` Player` | object | 7,948 | 16 |  CIVILIZATION_POLAND,  CIVILIZATION_NORWAY,  CI... | Top:  CIVILIZATION_POLAND,  CIVILIZATION_NORWAY |
| ` Num Cities` | int64 | 7,948 | 26 | 0, 0, 0 | Range: 0 - 26 |
| ` Population` | int64 | 7,948 | 196 | 0, 0, 0 | Range: 0 - 249 |
| ` Techs` | int64 | 7,948 | 78 | 0, 0, 0 | Range: 0 - 77 |
| ` Civics` | int64 | 7,948 | 62 | 0, 0, 0 | Range: 0 - 61 |
| ` Land Units` | int64 | 7,948 | 18 | 1, 1, 1 | Range: 0 - 17 |
| ` corps` | int64 | 7,948 | 5 | 0, 0, 0 | Range: 0 - 4 |
| ` Armies` | int64 | 7,948 | 6 | 0, 0, 0 | Range: 0 - 5 |
| ` Naval Units` | int64 | 7,948 | 6 | 0, 0, 0 | Range: 0 - 5 |
| ` TILES: Owned` | int64 | 7,948 | 385 | 0, 0, 0 | Range: 0 - 538 |
| ` Improved` | int64 | 7,948 | 128 | 0, 0, 0 | Range: 0 - 174 |
| ` BALANCE: Gold` | int64 | 7,948 | 1,469 | 10, 10, 10 | Range: 0 - 7147 |
| ` Faith` | int64 | 7,948 | 2,746 | 0, 0, 0 | Range: 0 - 79488 |
| ` YIELDS: Science` | int64 | 7,948 | 388 | 0, 0, 0 | Range: 0 - 501 |
| ` Culture` | int64 | 7,948 | 394 | 0, 0, 0 | Range: 0 - 668 |
| ` Gold` | int64 | 7,948 | 533 | 0, 0, 0 | Range: 0 - 799 |
| ` Faith.1` | int64 | 7,948 | 277 | 0, 0, 0 | Range: 0 - 356 |
| ` Production` | int64 | 7,948 | 564 | 0, 0, 0 | Range: 0 - 958 |
| ` Food` | int64 | 7,948 | 413 | 0, 0, 0 | Range: 0 - 580 |

### Sample Data

```json
[
  {
    "Game Turn": 1,
    " Player": " CIVILIZATION_POLAND",
    " Num Cities": 0,
    " Population": 0,
    " Techs": 0,
    " Civics": 0,
    " Land Units": 1,
    " corps": 0,
    " Armies": 0,
    " Naval Units": 0,
    " TILES: Owned": 0,
    " Improved": 0,
    " BALANCE: Gold": 10,
    " Faith": 0,
    " YIELDS: Science": 0,
    " Culture": 0,
    " Gold": 0,
    " Faith.1": 0,
    " Production": 0,
    " Food": 0
  },
  {
    "Game Turn": 1,
    " Player": " CIVILIZATION_NORWAY",
    " Num Cities": 0,
    " Population": 0,
    " Techs": 0,
    " Civics": 0,
    " Land Units": 1,
    " corps": 0,
    " Armies": 0,
    " Naval Units": 0,
    " TILES: Owned": 0,
    " Improved": 0,
    " BALANCE: Gold": 10,
    " Faith": 0,
    " YIELDS: Science": 0,
    " Culture": 0,
    " Gold": 0,
    " Faith.1": 0,
    " Production": 0,
    " Food": 0
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `player_stats`

**Column Mappings:**
- `Game Turn` → INTEGER
- ` Player` → VARCHAR(100)
- ` Num Cities` → INTEGER
- ` Population` → INTEGER
- ` Techs` → INTEGER
- ` Civics` → INTEGER
- ` Land Units` → INTEGER
- ` corps` → INTEGER
- ` Armies` → INTEGER
- ` Naval Units` → INTEGER
- ` TILES: Owned` → INTEGER
- ` Improved` → INTEGER
- ` BALANCE: Gold` → INTEGER
- ` Faith` → INTEGER
- ` YIELDS: Science` → INTEGER
- ` Culture` → INTEGER
- ` Gold` → INTEGER
- ` Faith.1` → INTEGER
- ` Production` → INTEGER
- ` Food` → INTEGER

---

## Player_Stats_2.csv

**File Statistics:**
- Size: 473.7 KB
- Rows: 7,948
- Columns: 12
- Memory Usage: 1.2 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Game Turn` | int64 | 7,948 | 503 | 1, 1, 1 | Range: 1 - 503 |
| ` Player` | object | 7,948 | 16 |  CIVILIZATION_POLAND,  CIVILIZATION_NORWAY,  CI... | Top:  CIVILIZATION_POLAND,  CIVILIZATION_NORWAY |
| ` BY TYPE: Tiles` | int64 | 7,948 | 385 | 0, 0, 0 | Range: 0 - 538 |
| ` Buildings` | int64 | 7,948 | 476 | 0, 0, 0 | Range: 0 - 877 |
| ` Districts` | int64 | 7,948 | 85 | 0, 0, 0 | Range: 0 - 99 |
| ` Population` | int64 | 7,948 | 195 | 0, 0, 0 | Range: 0 - 231 |
| ` Outgoing Trade Routes` | int64 | 7,948 | 128 | 0, 0, 0 | Range: 0 - 209 |
| ` TOURISM` | int64 | 7,948 | 259 | 0, 0, 0 | Range: 0 - 591 |
| ` Diplo Victory` | int64 | 7,948 | 21 | 0, 0, 0 | Range: 0 - 23 |
| ` BALANCE: Favor` | int64 | 7,948 | 442 | 0, 0, 0 | Range: 0 - 701 |
| ` LIFETIME: Favor` | int64 | 7,948 | 1,408 | 0, 0, 0 | Range: 0 - 2761 |
| ` CO2 Per Turn` | int64 | 7,948 | 27 | 0, 0, 0 | Range: -39 - 25 |

### Sample Data

```json
[
  {
    "Game Turn": 1,
    " Player": " CIVILIZATION_POLAND",
    " BY TYPE: Tiles": 0,
    " Buildings": 0,
    " Districts": 0,
    " Population": 0,
    " Outgoing Trade Routes": 0,
    " TOURISM": 0,
    " Diplo Victory": 0,
    " BALANCE: Favor": 0,
    " LIFETIME: Favor": 0,
    " CO2 Per Turn": 0
  },
  {
    "Game Turn": 1,
    " Player": " CIVILIZATION_NORWAY",
    " BY TYPE: Tiles": 0,
    " Buildings": 0,
    " Districts": 0,
    " Population": 0,
    " Outgoing Trade Routes": 0,
    " TOURISM": 0,
    " Diplo Victory": 0,
    " BALANCE: Favor": 0,
    " LIFETIME: Favor": 0,
    " CO2 Per Turn": 0
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `player_stats_2`

**Column Mappings:**
- `Game Turn` → INTEGER
- ` Player` → VARCHAR(100)
- ` BY TYPE: Tiles` → INTEGER
- ` Buildings` → INTEGER
- ` Districts` → INTEGER
- ` Population` → INTEGER
- ` Outgoing Trade Routes` → INTEGER
- ` TOURISM` → INTEGER
- ` Diplo Victory` → INTEGER
- ` BALANCE: Favor` → INTEGER
- ` LIFETIME: Favor` → INTEGER
- ` CO2 Per Turn` → INTEGER

---

## Player_WarWeariness.csv

**File Statistics:**
- Size: 29.1 KB
- Rows: 1,054
- Columns: 5
- Memory Usage: 0.09 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `Player` | int64 | 1,054 | 15 | 5, 5, 5 | Range: 0 - 14 |
| `FromPlayer` | int64 | 1,054 | 15 | 1, 1, 1 | Range: 0 - 14 |
| `Delta` | int64 | 1,054 | 24 | 68, 68, -50 | Range: -2000 - 249 |
| `New Total Weariness` | int64 | 1,054 | 621 | 68, 136, 86 | Range: 0 - 3090 |
| `Reason` | object | 1,054 | 6 |  Attacking,  Attacking,  At War Decay | Top:  Attacking,  At War Decay |

### Sample Data

```json
[
  {
    "Player": 5,
    "FromPlayer": 1,
    "Delta": 68,
    "New Total Weariness": 68,
    "Reason": " Attacking"
  },
  {
    "Player": 5,
    "FromPlayer": 1,
    "Delta": 68,
    "New Total Weariness": 136,
    "Reason": " Attacking"
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `player_warweariness`

**Column Mappings:**
- `Player` → INTEGER
- `FromPlayer` → INTEGER
- `Delta` → INTEGER
- `New Total Weariness` → INTEGER
- `Reason` → VARCHAR(100)

---

## Profile.csv

**File Statistics:**
- Size: 261.75 KB
- Rows: 3,486
- Columns: 3
- Memory Usage: 0.72 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `[2025-08-03 17:32:06]	` | object | 3,486 | 794 | [2025-08-03 17:32:06]	, [2025-08-03 17:32:06]	,... |  |
| `                UIManager_Update` | object | 3,486 | 1,312 |         UIUpdateJob_Update,     Civ6App_UpdateF... |  |
| ` 132.65 ms` | object | 2,482 | 2,213 |  132.94 ms,  137.12 ms,  103.14 ms |  |

### Sample Data

```json
[
  {
    "[2025-08-03 17:32:06]\t": "[2025-08-03 17:32:06]\t",
    "                UIManager_Update": "        UIUpdateJob_Update",
    " 132.65 ms": " 132.94 ms"
  },
  {
    "[2025-08-03 17:32:06]\t": "[2025-08-03 17:32:06]\t",
    "                UIManager_Update": "    Civ6App_UpdateFrame",
    " 132.65 ms": " 137.12 ms"
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `profile`

**Column Mappings:**
- `[2025-08-03 17:32:06]	` → VARCHAR(100)
- `                UIManager_Update` → VARCHAR(100)
- ` 132.65 ms` → VARCHAR(100)

---

## RandCalls.csv

**File Statistics:**
- Size: 3231.26 KB
- Rows: 0
- Columns: 0
- Memory Usage: 0 MB

❌ **Error:** Error tokenizing data. C error: Expected 6 fields in line 12093, saw 7


## UIWarnings.csv

**File Statistics:**
- Size: 532.11 KB
- Rows: 3,169
- Columns: 2
- Memory Usage: 0.81 MB

### Column Details

| Column | Type | Non-Null | Unique | Sample Values | Notes |
|--------|------|----------|--------|---------------|-------|
| `AutoSize attribute is deprecated` | object | 3,169 | 5 | SetSize called on parent-sized, SetSize called ... | Top: SetSize called on auto-sized control on X-axis, SetSize called on parent-sized control on Y-axis |
| `ToolTips.xml/BG` | object | 3,169 | 254 | /FrontEnd/FrontEndContainer/Ma, /FrontEnd/Front... |  |

### Sample Data

```json
[
  {
    "AutoSize attribute is deprecated": "SetSize called on parent-sized control on X-axis",
    "ToolTips.xml/BG": "/FrontEnd/FrontEndContainer/MainMenu/Options/MainGrid/MainWindow/Content/Container/GameOptions/GameOptionsScrollPanel/Stack/Stack/QuickCombatPullDown/Grid/ScrollPanel"
  },
  {
    "AutoSize attribute is deprecated": "SetSize called on parent-sized control on X-axis",
    "ToolTips.xml/BG": "/FrontEnd/FrontEndContainer/MainMenu/Options/MainGrid/MainWindow/Content/Container/GameOptions/GameOptionsScrollPanel/Stack/Stack/QuickMovementPullDown/Grid/ScrollPanel"
  }
]
```

### Database Mapping Suggestions

**Recommended Table Name:** `uiwarnings`

**Column Mappings:**
- `AutoSize attribute is deprecated` → VARCHAR(100)
- `ToolTips.xml/BG` → VARCHAR(202)

---

## World_Congress.csv

**File Statistics:**
- Size: 24.79 KB
- Rows: 0
- Columns: 0
- Memory Usage: 0 MB

❌ **Error:** Error tokenizing data. C error: Expected 5 fields in line 4, saw 6


