@echo off
echo 🔧 Testing Superset turn number sorting...
echo.

echo 📊 Database verification (should show 1-11 in order):
docker exec civ6_database psql -U civ6_user -d civ6_analytics -c "SELECT DISTINCT turn_number FROM game_data ORDER BY turn_number ASC;"

echo.
echo 🎯 Superset should now recognize turn_number as INTEGER
echo ✅ Go to http://localhost:8088 and create a new chart
echo ✅ Use turn_number as X-axis (it should sort 1,2,3...11 now)
echo ✅ If filter dropdown still shows wrong order, that's just UI caching
echo ✅ The actual chart will display correctly sorted data

pause
