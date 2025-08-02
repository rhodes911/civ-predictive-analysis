# 📊 Civ VI CSV Data Analysis & Use Cases

**Complete Analysis of Available Data Sources in Civilization VI Logs**  
*Discovering analytics opportunities beyond basic player statistics*

---

## 🎯 Overview

Civilization VI generates **40+ CSV files** containing detailed game data across multiple categories. While we currently use only 3 files for basic player statistics, there's a wealth of untapped data for advanced analysis.

### **Current Usage vs Available Data**
- **Currently Used:** 3 files (Player_Stats.csv, Player_Stats_2.csv, Game_PlayerScores.csv)
- **Available:** 40+ comprehensive data sources
- **Opportunity:** Massive potential for advanced analytics

---

## 📈 Data Categories & Analysis Opportunities

### **1. 🏛️ Player & Civilization Core Stats**
**Files:** `Player_Stats.csv`, `Player_Stats_2.csv`, `Game_PlayerScores.csv`

**Data Includes:**
- Population, cities, land/naval units
- Science, culture, gold yields per turn  
- Technologies, civics research progress
- Buildings, districts, trade routes
- Diplomatic favor, tourism output

**✅ Currently Implemented** - Our main dashboard data source

**Potential Enhancements:**
- Military unit composition analysis
- Economic efficiency ratios (yield per city)
- Technology research velocity tracking

---

### **2. 🏗️ City Development & Production**
**Files:** `City_BuildQueue.csv`

**Data Includes:**
- City names and production queues
- Current items being built (units, buildings, wonders)
- Production points added per turn
- Production overflow tracking

**🔥 High-Value Use Cases:**
- **City Specialization Analysis:** Which cities focus on military vs infrastructure
- **Production Efficiency:** Time to complete different building types
- **Strategic Priority Tracking:** What each civilization prioritizes building
- **Economic Bottleneck Identification:** Cities with slow production

**Example Analysis:**
```sql
-- Which civilizations focus on military vs infrastructure?
SELECT civilization, 
       SUM(CASE WHEN current_item LIKE 'UNIT_%' THEN 1 ELSE 0 END) as military_builds,
       SUM(CASE WHEN current_item LIKE 'BUILDING_%' THEN 1 ELSE 0 END) as infrastructure_builds
FROM city_buildqueue GROUP BY civilization
```

---

### **3. 🧠 AI Decision Making Intelligence**
**Files:** `AI_Research.csv`, `AI_GovtPolicies.csv`, `AI_Planning.csv`

**Data Includes:**
- Technology research priorities and scoring
- Government policy selections
- Strategic planning decisions
- AI evaluation scores for different options

**🔥 High-Value Use Cases:**
- **AI Strategy Reverse Engineering:** Understand how AI prioritizes technologies
- **Policy Effectiveness Analysis:** Which government policies AI favors in different situations
- **Difficulty Scaling Analysis:** How AI behavior changes with difficulty levels
- **Meta Strategy Discovery:** Identify optimal research/policy paths

**Example Insights:**
- "AI consistently prioritizes TECH_POTTERY early game with 151.6 score"
- "Government policy preferences by civilization type"
- "Technology rush patterns for different victory conditions"

---

### **4. ⚔️ Military & Combat Analytics**
**Files:** `CombatLog.csv`, `AI_Tactical.csv`, `AI_Military.csv`

**Data Includes:**
- Detailed combat encounters (attacker/defender, damage, unit types)
- Military AI tactical decisions
- Unit efficiency and battle outcomes
- Strength modifiers and combat calculations

**🔥 High-Value Use Cases:**
- **Combat Effectiveness Analysis:** Which unit types perform best
- **Military Strategy Patterns:** How different civs approach warfare
- **Battle Outcome Prediction:** Factors that determine combat success
- **Unit Upgrade Timing:** Optimal moments for military modernization

**Example Analysis:**
```sql
-- Combat win rates by unit type
SELECT attacker_type, defender_type,
       AVG(CASE WHEN attacker_dmg > defender_dmg THEN 1.0 ELSE 0.0 END) as win_rate
FROM combat_log GROUP BY attacker_type, defender_type
```

---

### **5. 🕊️ Diplomacy & International Relations**
**Files:** `AI_Diplomacy.csv`, `DiplomacyManager.csv`, `DiplomacyModifiers.csv`

**Data Includes:**
- Diplomatic relationships between civilizations
- Threat and trust levels
- Diplomatic state changes
- Relationship modifiers and their impacts

**🔥 High-Value Use Cases:**
- **Alliance Pattern Analysis:** Which civs naturally ally vs conflict
- **Diplomatic Victory Tracking:** Path to diplomatic influence
- **Relationship Deterioration Prediction:** Early warning signs of war
- **Trade Partner Optimization:** Best diplomatic relationships for commerce

---

### **6. 🎭 Religion & Culture Systems**
**Files:** `Game_Religion.csv`, `AI_Religious.csv`

**Data Includes:**
- Pantheon and religion founding events
- Religious belief selections
- Faith-based AI decisions
- Religious spread and adoption

**🔥 High-Value Use Cases:**
- **Religious Victory Path Analysis:** Optimal belief combinations
- **Faith Economy Tracking:** Religious income vs other yield types
- **Cultural Influence Mapping:** How religious choices affect diplomacy
- **Belief Effectiveness Ranking:** Which pantheons/beliefs provide best benefits

---

### **7. 👑 Great People & Special Events**
**Files:** `Game_GreatPeople.csv`, `Game_RandomEvents.csv`

**Data Includes:**
- Great People availability and recruitment
- Random events (storms, natural disasters)
- Great Person cost progression
- Environmental and climate effects

**🔥 High-Value Use Cases:**
- **Great People Strategy Optimization:** Which GPs to prioritize when
- **Event Impact Analysis:** How random events affect civilization performance
- **Climate Change Tracking:** Environmental effects on gameplay
- **Great Person Economics:** Cost vs benefit analysis of different GP types

---

### **8. 🏛️ Government & Civic Evolution**
**Files:** `AI_Governors.csv`, `AI_GovtPolicies.csv`

**Data Includes:**
- Governor assignments and promotions
- Government policy changes
- Civic tree progression decisions
- Administrative efficiency metrics

**🔥 High-Value Use Cases:**
- **Governance Optimization:** Best governor/policy combinations
- **Administrative Efficiency:** Governor impact on city performance
- **Civic Path Analysis:** Optimal progression through government types
- **Policy Synergy Discovery:** Which policies work well together

---

### **9. 🌍 World Events & Environmental**
**Files:** `Game_RandomEvents.csv`, `Barbarians.csv`, `World_Congress.csv`

**Data Includes:**
- Natural disasters and climate events
- Barbarian activity and camps
- World Congress resolutions
- Global CO2 and environmental tracking

**🔥 High-Value Use Cases:**
- **Disaster Preparedness Analysis:** Impact of natural events on cities
- **Barbarian Threat Assessment:** Early game security challenges
- **Global Policy Impact:** World Congress effect on civilizations
- **Environmental Strategy:** Climate change adaptation patterns

---

## 🚀 Implementation Roadmap

### **Phase 1: Enhanced Core Analytics** *(Easy wins)*
1. **City Production Analysis** - Add City_BuildQueue.csv data
2. **Combat Effectiveness** - Basic CombatLog.csv integration
3. **Research Strategy** - AI_Research.csv for technology insights

### **Phase 2: Strategic Intelligence** *(Medium complexity)*
1. **Diplomatic Relations Dashboard** - Multi-civ relationship tracking
2. **Military Planning** - Combat prediction and unit efficiency
3. **Great People Economics** - GP cost/benefit optimization

### **Phase 3: Advanced AI Analysis** *(Complex but high-value)*
1. **AI Strategy Reverse Engineering** - Full AI decision analysis
2. **Predictive Modeling** - Game outcome prediction based on patterns
3. **Meta Strategy Discovery** - Optimal play pattern identification

---

## 💡 Specific Dashboard Ideas

### **Military Intelligence Dashboard**
- Unit composition by civilization
- Combat win rates by unit matchup
- Military production focus analysis
- Battle hotspot mapping

### **Economic Optimization Dashboard**  
- Yield efficiency by city and civilization
- Production queue optimization analysis
- Trade route effectiveness metrics
- Resource allocation patterns

### **Diplomatic Relations Map**
- Real-time relationship status between all civs
- Diplomatic modifier tracking
- Alliance formation predictions
- Trade partnership analysis

### **Victory Condition Tracker**
- Science victory progress (space race projects)
- Religious victory spread analysis
- Diplomatic favor accumulation
- Cultural tourism influence tracking

### **AI Strategy Analysis**
- Technology prioritization patterns
- Government policy preferences
- Governor placement strategies
- Combat tactical decision analysis

---

## 🛠️ Technical Implementation Notes

### **Database Schema Expansion**
Current single-table approach would need expansion to:
- Multiple normalized tables for different data types
- Proper foreign key relationships
- Time-series optimization for trend analysis

### **Data Processing Challenges**
- **Volume:** Some files (AI_Behavior_Trees.csv) are 6MB+ per game
- **Complexity:** AI decision files have complex nested data structures
- **Real-time:** Some data updates mid-turn vs end-of-turn

### **Superset Dashboard Complexity**
- Multi-table joins for comprehensive analysis
- Real-time filtering across multiple data sources
- Custom metrics and calculated fields
- Performance optimization for large datasets

---

## 🎯 Quick Wins for Immediate Value

### **1. City Production Dashboard** *(2-3 hours implementation)*
- Show what each civilization is building
- Production efficiency by city
- Strategic focus analysis (military vs infrastructure)

### **2. Combat Analysis** *(4-5 hours implementation)*
- Unit effectiveness tracking
- Combat outcome analysis
- Military strategy patterns

### **3. Research Intelligence** *(3-4 hours implementation)*
- AI technology prioritization
- Research path optimization
- Tech tree efficiency analysis

---

## 📊 Data Quality Assessment

### **High Quality/Reliable:**
- ✅ Player_Stats.csv - Core metrics, very reliable
- ✅ CombatLog.csv - Complete battle records
- ✅ City_BuildQueue.csv - Accurate production data
- ✅ Game_Religion.csv - Religious events well-tracked

### **Medium Quality/Some Gaps:**
- ⚠️ AI_Diplomacy.csv - Complex format, needs parsing
- ⚠️ AI_Research.csv - AI internal scoring, interpretation needed
- ⚠️ Game_RandomEvents.csv - Mixed format data

### **Complex/Requires Analysis:**
- 🔍 AI_Behavior_Trees.csv - Very large, complex AI decision trees
- 🔍 AI_Planning.csv - Strategic AI decisions, needs domain knowledge
- 🔍 RandCalls.csv - Random number generation, statistical analysis

---

*This analysis reveals that Civ VI generates incredibly rich data far beyond basic player statistics. The opportunity for advanced analytics is enormous, limited mainly by implementation complexity rather than data availability.*
