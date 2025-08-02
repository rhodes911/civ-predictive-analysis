# 🔄 Superset Refresh Button Implementation

## Option 1: SQL Lab Refresh Query (Immediate Solution)

### Step 1: Create Refresh Query in SQL Lab
1. Go to **SQL Lab** in Superset
2. Create new query with this SQL:

```sql
-- Refresh Game Data Query
-- This will show latest turn data and trigger a refresh when executed

SELECT 
    'Data Refresh Complete!' as status,
    MAX(game_turn) as latest_turn,
    COUNT(DISTINCT civilization) as civilizations,
    COUNT(*) as total_records
FROM civ_game_data;

-- Show latest turn rankings
SELECT 
    civilization,
    total_score,
    yields_science,
    yields_culture,
    ROW_NUMBER() OVER (ORDER BY total_score DESC) as rank
FROM civ_game_data 
WHERE game_turn = (SELECT MAX(game_turn) FROM civ_game_data)
ORDER BY total_score DESC;
```

3. Save as "🔄 Refresh Game Data"
4. Users can click "Run Query" to refresh and see latest data

### Step 2: Add to Dashboard
- Add this query as a table chart on your dashboard
- Users click the chart's refresh button to update

## Option 2: Custom Superset Plugin (Advanced)

### Create Custom Refresh Plugin
This would require:
1. Custom React component
2. Superset plugin architecture
3. Docker container integration

Would you like me to implement Option 1 first, or explore the custom plugin approach?

## Option 3: External Web Interface (Middle Ground)

Create a simple web page that:
1. Shows current data status
2. Has a "Load New Turns" button
3. Triggers Docker command
4. Redirects back to Superset

This could be a lightweight Flask app in another container.

Which approach appeals to you most?
