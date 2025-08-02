# 🎯 Superset Dashboard Investigation: Civ VI Analytics Layout

## 📋 Project Goal
Design the optimal Apache Superset dashboard layout for Civ VI strategic analysis, focusing on the "I am [Civilization]" user experience with real-time game data insights.

---

## 🔍 Research: Apache Superset Latest Version Capabilities

### **Current Superset Features (2024-2025)**
- **Dashboard Filters**: Cross-filter functionality across multiple charts
- **Chart Types**: 50+ visualization types including heatmaps, scatter plots, time series
- **Real-time Data**: Live data refresh capabilities
- **Interactive Filters**: Dropdown, date range, text input filters
- **Mobile Responsive**: Adaptive layouts for different screen sizes
- **Custom CSS**: Advanced styling and branding options

### **Key Features for Civ VI Dashboard:**
1. **Global Dashboard Filters** - Apply civilization filter to all charts simultaneously
2. **Drill-down Capabilities** - Click on data points to explore deeper
3. **Comparative Analysis** - Side-by-side civilization comparisons
4. **Time Series Charts** - Track progression over turns
5. **Geographic/Spatial Charts** - Potential for territory visualization

---

## 🎨 Proposed Dashboard Layout

### **Header Section: Game Overview**
```
┌─────────────────────────────────────────────────────────────┐
│  🏛️ CIV VI STRATEGIC ANALYTICS - TURN 39                    │
│  Filter: [I am: CIVILIZATION_ROME ▼] [Turn: 39 ▼]          │
└─────────────────────────────────────────────────────────────┘
```

### **Row 1: Key Performance Indicators (KPIs)**
```
┌─────────────┬─────────────┬─────────────┬─────────────┐
│ 🏆 MY RANK  │ 📊 MY SCORE │ 🔬 SCIENCE  │ 🎭 CULTURE  │
│     #1      │     47      │      5      │      5      │
│  of 6 civs  │   +2 pts    │   Leading   │   Leading   │
└─────────────┴─────────────┴─────────────┴─────────────┘
```

### **Row 2: Comparative Analysis**
```
┌─────────────────────────────┬─────────────────────────────┐
│ 📈 LEADERBOARD              │ 🎯 MY POSITION vs ALL       │
│ 1. ROME        47 pts       │     Science: ████████ 5/5   │
│ 2. ENGLAND     46 pts       │     Culture: ████████ 5/5   │
│ 3. NETHERLANDS 39 pts       │     Military: ████▒▒▒ 3/8   │
│ 4. CHINA       33 pts       │     Economy:  ██████▒▒ 6/10  │
│ 5. GAUL        29 pts       │     Cities:   ██▒▒▒▒▒▒ 2/8   │
│ 6. CANADA      28 pts       │                             │
└─────────────────────────────┴─────────────────────────────┘
```

### **Row 3: Strategic Intelligence**
```
┌─────────────────────────────┬─────────────────────────────┐
│ ⚡ THREATS & OPPORTUNITIES  │ 📊 CIVILIZATION COMPARISON   │
│ Threats:                    │        SCI CUL MIL ECO TOT  │
│ • England close behind (-1) │ ROME    5   5   3   6  47   │
│ • China strong science (5)  │ ENGLAND 3   4   8   7  46   │
│                            │ ME ──>  5   5   3   6  47   │
│ Opportunities:              │ CHINA   5   5   2   4  33   │
│ • Military advantage needed │ GAUL    5   2   4   3  29   │
│ • Economic growth potential │ CANADA  3   5   1   5  28   │
└─────────────────────────────┴─────────────────────────────┘
```

### **Row 4: Detailed Analytics**
```
┌─────────────────────────────────────────────────────────────┐
│ 📈 TURN PROGRESSION (Last 10 Turns)                        │
│     Score ┌─┐                                              │
│       50  │ │ ♦ ROME                                       │
│       45  │ │ ■ ENGLAND                                    │
│       40  │♦│ ▲ NETHERLANDS                                │
│       35  │■│                                              │
│       30  │▲│                                              │
│           └─┴───────────────────────────────────────────   │
│           30 31 32 33 34 35 36 37 38 39 Turn              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Technical Implementation Plan

### **1. Dashboard Structure**
```yaml
Dashboard: "Civ VI Strategic Command Center"
Filters:
  - civilization: dropdown (global)
  - game_turn: slider/dropdown (global)
  - comparison_civs: multi-select (optional)

Charts:
  1. KPI_Cards: Big Numbers (4 cards)
  2. Leaderboard: Table (sorted by score)
  3. Position_Radar: Radar Chart (my stats vs average)
  4. Threats_Table: Table (custom SQL)
  5. Comparison_Matrix: Table (multi-civ stats)
  6. Turn_Progression: Line Chart (time series)
```

### **2. Required Queries & Chart Types**

#### **Query 1: KPI Cards (Big Number Charts)**
```sql
-- My Current Stats
SELECT 
    total_score,
    yields_science,
    yields_culture,
    (SELECT COUNT(*) + 1 FROM civ_game_data c2 
     WHERE c2.game_turn = c1.game_turn AND c2.total_score > c1.total_score) as rank
FROM civ_game_data c1
WHERE civilization = '{{ civilization_filter }}'
  AND game_turn = {{ turn_filter }}
```

#### **Query 2: Leaderboard Table**
```sql
-- All Civilizations Ranked
SELECT 
    civilization,
    total_score,
    yields_science,
    yields_culture,
    population,
    num_cities
FROM civ_game_data
WHERE game_turn = {{ turn_filter }}
ORDER BY total_score DESC
```

#### **Query 3: Comparative Radar Chart**
```sql
-- My Stats vs Average
SELECT 
    'Science' as metric, yields_science as my_value, 
    (SELECT AVG(yields_science) FROM civ_game_data WHERE game_turn = {{ turn_filter }}) as avg_value
FROM civ_game_data WHERE civilization = '{{ civilization_filter }}' AND game_turn = {{ turn_filter }}
UNION ALL
SELECT 'Culture', yields_culture, 
    (SELECT AVG(yields_culture) FROM civ_game_data WHERE game_turn = {{ turn_filter }})
FROM civ_game_data WHERE civilization = '{{ civilization_filter }}' AND game_turn = {{ turn_filter }}
-- ... repeat for other metrics
```

#### **Query 4: Turn Progression (Time Series)**
```sql
-- Historical Performance
SELECT 
    game_turn,
    civilization,
    total_score
FROM civ_game_data
WHERE game_turn >= {{ turn_filter }} - 10
  AND civilization IN ({{ selected_civilizations }})
ORDER BY game_turn, total_score DESC
```

### **3. Dashboard Filters Configuration**

#### **Primary Filter: "I am [Civilization]"**
- **Type**: Dropdown Filter
- **Column**: `civilization`
- **Default**: User selects their civilization
- **Scope**: All charts (global filter)

#### **Secondary Filter: Turn Selection**
- **Type**: Dropdown or Slider
- **Column**: `game_turn`
- **Default**: Latest available turn
- **Scope**: All charts (global filter)

#### **Optional Filter: Compare With**
- **Type**: Multi-select Dropdown
- **Column**: `civilization`
- **Purpose**: Select other civilizations for comparison charts
- **Scope**: Comparison-specific charts only

### **4. Chart-Specific Configurations**

#### **KPI Cards Setup:**
- **Chart Type**: Big Number
- **Metrics**: `total_score`, `yields_science`, `yields_culture`, calculated rank
- **Conditional Formatting**: Green if above average, red if below

#### **Leaderboard Setup:**
- **Chart Type**: Table
- **Columns**: civilization, total_score, yields_science, yields_culture
- **Conditional Formatting**: Highlight user's civilization row
- **Sorting**: total_score DESC

#### **Radar Chart Setup:**
- **Chart Type**: Radar Chart
- **Metrics**: Science, Culture, Military, Economy (normalized 0-100%)
- **Comparison**: User's civilization vs. average vs. leader

#### **Time Series Setup:**
- **Chart Type**: Line Chart
- **X-Axis**: game_turn
- **Y-Axis**: total_score
- **Series**: Selected civilizations
- **Annotations**: Mark current turn

---

## 🎯 User Experience Flow

### **Scenario: "I am Rome, Turn 39"**

1. **User selects**: "I am CIVILIZATION_ROME" from dropdown
2. **Dashboard updates** to show:
   - "You are #1 of 6 civilizations"
   - "Your score: 47 points"
   - "Leading in: Science (5), Culture (5)"
   - "Threats: England is close behind (46 points)"
   - "Strengths: Balanced development"

3. **Strategic insights automatically generated**:
   - Recommendation: "Focus on military - you're vulnerable"
   - Warning: "England gaining fast - maintain science lead"
   - Opportunity: "Consider cultural victory path"

### **Key Questions Dashboard Answers:**
- ❓ "How am I doing compared to everyone else?"
- ❓ "Who are my biggest threats?"
- ❓ "What are my strengths/weaknesses?"
- ❓ "Am I improving or falling behind?"
- ❓ "What should I focus on next?"

---

## 🚀 Implementation Priority

### **Phase 1: Core Dashboard (MVP)**
1. ✅ Basic leaderboard table (DONE)
2. 🔄 Add civilization filter (NEXT)
3. 🔄 Add KPI cards for score/science/culture
4. 🔄 Add turn filter

### **Phase 2: Strategic Intelligence**
1. Comparative analysis charts
2. Radar chart for strengths/weaknesses
3. Threat analysis table

### **Phase 3: Advanced Analytics**
1. Turn progression time series
2. Predictive analytics
3. Custom recommendations engine

---

## 📊 Success Metrics

**Dashboard Effectiveness:**
- ⏱️ **Speed**: User gets strategic insight in <5 seconds
- 🎯 **Clarity**: Immediate answer to "How am I doing?"
- 🔄 **Actionability**: Clear next steps provided
- 📱 **Usability**: Works on mobile devices
- 🎮 **Gaming Value**: Actually useful during live gameplay

**Technical Metrics:**
- 📊 Data refresh: <2 seconds
- 🖥️ Dashboard load: <3 seconds  
- 📱 Mobile responsive: 100%
- 🔄 Real-time updates: Live CSV monitoring

---

## 🔗 Current Implementation Status

### **Database Schema (COMPLETE ✅)**
Table: `civ_game_data`
- **Primary Keys**: `id`, `game_turn`, `civilization`
- **Metrics**: `yields_science`, `yields_culture`, `total_score`, `population`, etc.
- **Data Source**: Real Civ VI CSV files (Player_Stats.csv, Player_Stats_2.csv, Game_PlayerScores.csv)
- **Current Data**: Turn 39, 6 major civilizations

### **Current Leaderboard (Turn 39)**
1. 🥇 **ROME**: 47 points (Science: 5, Culture: 5)
2. 🥈 **ENGLAND**: 46 points (Science: 3, Culture: 4)
3. 🥉 **NETHERLANDS**: 39 points (Science: 4, Culture: 4)
4. **CHINA**: 33 points (Science: 5, Culture: 5)
5. **GAUL**: 29 points (Science: 5, Culture: 2)
6. **CANADA**: 28 points (Science: 3, Culture: 5)

### **Data Precision Notes**
- ⚠️ **CSV Limitation**: Science/Culture values are rounded to integers (e.g., 4.5 becomes 4)
- ✅ **Trend Analysis**: Still excellent for comparative analysis and strategic insights
- ✅ **Real-time Updates**: Data updates automatically as game progresses

---

## 🎮 Next Steps

1. **Fix Superset Chart Configuration**:
   - Remove `created_at` filter
   - Add proper `game_turn = 39` filter
   - Fix sorting to use `total_score` (not MAX function)

2. **Implement "I am [Civilization]" Filter**:
   - Add global civilization dropdown filter
   - Configure cross-chart filtering

3. **Create KPI Cards**:
   - My Rank, My Score, Science, Culture
   - Conditional formatting for performance indicators

4. **Build Comparative Analysis**:
   - Radar chart for strengths/weaknesses
   - Threat analysis table

This investigation provides the complete blueprint for creating a world-class Civ VI strategic dashboard that gives players the competitive edge they need during live gameplay!
