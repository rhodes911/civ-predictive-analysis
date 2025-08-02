# Superset Chart Creation Instructions

## 🎯 Exact Superset Configuration (Based on Your Interface)

### **X-AXIS** 
- Drag `game_turn` into the **"Drop a column here or click"** box

### **METRICS**
- Drag `total_score` into the **"Drop columns/metrics here or click"** box
- Change aggregation to **AVG** if needed

### **DIMENSIONS** 
- Drag `civilization` into the **"Drop columns or click"** box

### **CONTRIBUTION MODE**
- Leave as **"None"**

### **FILTERS FOR GAME SELECTION**

**⚠️ IMPORTANT: Choose ONE filter option based on what you want to analyze:**

**Option A: CURRENT INDONESIA GAME ONLY (Latest 15 turns)**
- Add `created_at` filter: `created_at::time >= '07:00:00' AND game_turn <= 15`
- Shows: Indonesia, Ethiopia, Mali, Cree, Ottoman progression

**Option B: OLD COMPLETE RACE (77-turn epic)**  
- Add `created_at` filter: `created_at::time < '07:00:00'`
- Shows: Rome, England, Netherlands, China, Canada, Gaul complete race

**Option C: ALL HISTORICAL DATA (Both games combined)**
- No filters needed
- Shows: Both games together (may be confusing due to turn overlap)

### **FILTERS**
- Remove the `created_at (No filter)` by clicking the **X** 
- Click **"Drop columns/metrics here or click"**
- Add your chosen filter from options above

### **SERIES LIMIT**
- Change from **"None"** to **"10"** (to show all 6 civilizations)

### **SORT BY**
- Leave empty or add `game_turn` if needed

### **ROW LIMIT**
- Keep at **1000** (this is fine)

## 🔧 Step-by-Step Instructions

1. **First, remove the created_at filter:**
   - Click the **X** next to "created_at (No filter)"

2. **Set up X-AXIS:**
   - Click in the X-AXIS box
   - Select `game_turn` from the column list

3. **Set up METRICS:**
   - Click in the METRICS box  
   - Select `total_score`
   - Make sure it shows as `AVG(total_score)`

4. **Set up DIMENSIONS:**
   - Click in the DIMENSIONS box
   - Select `civilization`

5. **Fix SERIES LIMIT:**
   - Click the "None" dropdown under SERIES LIMIT
   - Change to **"10"** (ensures all civilizations show)

6. **Add proper FILTERS to select which game:**
   
   **For OLD GAME (turns 1-77, Rome/England/China/Netherlands/Canada/Gaul):**
   - Add `created_at` filter
   - Set START: **2025-08-02 00:00:00** 
   - Set END: **2025-08-02 02:00:00**
   
   **For NEW GAME (turns 1-15, Indonesia/Ethiopia/Mali/Cree/Ottoman/Gaul):**
   - Add `created_at` filter  
   - Set START: **2025-08-02 07:00:00**
   - Set END: **2025-08-02 12:00:00** (or leave blank)

7. **Click "CREATE CHART"** at the bottom

This will create a line chart showing each civilization's score progression. Choose your time filter above to select which game to analyze:

**OLD GAME (77 turns)**: Epic race between Rome, England, China, Netherlands, Canada, and Gaul
**NEW GAME (15 turns)**: Current race with Indonesia, Ethiopia, Mali, Cree, Ottoman, and Gaul

## 📊 Additional Chart Variations

### Science Race Chart
- **METRICS:** `yields_science` (AVG)
- **X-AXIS:** `game_turn`
- **DIMENSIONS:** `civilization`
- **Title:** "Science Race: Research Output Over Time"

### Culture Race Chart  
- **METRICS:** `yields_culture` (AVG)
- **X-AXIS:** `game_turn`
- **DIMENSIONS:** `civilization`
- **Title:** "Culture Race: Cultural Output Over Time"

### Population Growth Chart
- **METRICS:** `population` (AVG)
- **X-AXIS:** `game_turn`
- **DIMENSIONS:** `civilization`
- **Title:** "Population Growth Over Time"

### Cities Expansion Chart
- **METRICS:** `num_cities` (AVG)
- **X-AXIS:** `game_turn`
- **DIMENSIONS:** `civilization`
- **Title:** "City Expansion Over Time"

## 🏆 Advanced: Ranking Position Chart

For a ranking chart, use **SQL Lab** with this query:

```sql
SELECT 
    game_turn,
    civilization,
    total_score,
    RANK() OVER (PARTITION BY game_turn ORDER BY total_score DESC) as position
FROM civ_game_data
ORDER BY game_turn, position
```

Then create chart with:
- **X-AXIS:** `game_turn`
- **METRICS:** `position` (AVG)
- **DIMENSIONS:** `civilization`
- **Y-Axis:** Reverse scale (1 at top, 6 at bottom)

## 🎮 Dashboard Tips

1. **Auto-refresh:** Set to 30 seconds to catch new game data
2. **Filter by Turn Range:** Add dashboard filter for `game_turn`
3. **Filter by Civilization:** Add multi-select filter for `civilization`
4. **Color Consistency:** Use same color scheme across all charts for each civilization

## 🔄 Data Updates

When you play more turns:
1. Run: `python stage4h_insert_data.py`
2. Superset will automatically show new data (with auto-refresh)
3. Charts will extend to show continued race progression

Your race analysis dashboard will now show the complete story of your Civ VI game progression! 🚀
