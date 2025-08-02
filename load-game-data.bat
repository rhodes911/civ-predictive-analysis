@echo off
echo 🎮 Loading Civ VI Data into Dashboard...
echo.
echo This will read your current Civ VI game data and update the dashboard.
echo Make sure you have saved your game recently for latest data.
echo.
pause

echo 📊 Starting data import...
docker-compose --profile data-import up data-loader

echo.
echo ✅ Data import complete!
echo 🌐 Refresh your dashboard at: http://localhost:8088
echo.
pause
