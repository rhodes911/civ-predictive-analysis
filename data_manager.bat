@echo off
REM Advanced data management for Civ VI Analytics
REM Supports adding data, clearing data, and viewing data

if "%1"=="" goto :help

if "%1"=="add" goto :add_data
if "%1"=="clear" goto :clear_data
if "%1"=="view" goto :view_data
if "%1"=="latest" goto :latest_data
if "%1"=="turns" goto :view_by_turns
goto :help

:add_data
if "%~7"=="" (
    echo Missing parameters for add command
    echo Usage: data_manager.bat add [game_id] [turn] [player] [civ] [science] [culture]
    exit /b 1
)
echo Adding: Turn %3 - %4 (%5) - Science: %6, Culture: %7
docker exec civ6_database psql -U civ6_user -d civ6_analytics -c "INSERT INTO game_data (game_id, turn_number, player_name, civilization, science_per_turn, culture_per_turn) VALUES ('%2', %3, '%4', '%5', %6, %7) ON CONFLICT DO NOTHING;"
echo ✅ Data added!
goto :end

:clear_data
echo ⚠️  WARNING: This will delete ALL game data!
set /p confirm="Are you sure? (y/N): "
if /i "%confirm%"=="y" (
    docker exec civ6_database psql -U civ6_user -d civ6_analytics -c "DELETE FROM game_data; DELETE FROM game_sessions;"
    echo ✅ All data cleared!
) else (
    echo ❌ Operation cancelled
)
goto :end

:view_data
echo 📊 Current Game Data:
docker exec civ6_database psql -U civ6_user -d civ6_analytics -c "SELECT turn_number, player_name, civilization, science_per_turn, culture_per_turn FROM game_data ORDER BY turn_number ASC, player_name ASC;"
goto :end

:latest_data
echo 📈 Latest Turn Data:
docker exec civ6_database psql -U civ6_user -d civ6_analytics -c "SELECT turn_number, player_name, civilization, science_per_turn, culture_per_turn FROM game_data WHERE turn_number = (SELECT MAX(turn_number) FROM game_data) ORDER BY player_name ASC;"
goto :end

:view_by_turns
echo 🎯 Data by Turn (Chronological):
docker exec civ6_database psql -U civ6_user -d civ6_analytics -c "SELECT turn_number, COUNT(*) as players, CAST(AVG(science_per_turn) AS DECIMAL(10,1)) as avg_science, CAST(AVG(culture_per_turn) AS DECIMAL(10,1)) as avg_culture FROM game_data GROUP BY turn_number ORDER BY turn_number ASC;"
goto :end

:help
echo 🎮 Civ VI Analytics - Data Manager
echo.
echo Commands:
echo   add [game_id] [turn] [player] [civ] [science] [culture]  - Add new turn data
echo   view                                                     - View all data
echo   turns                                                    - View turn summary
echo   latest                                                   - View latest turn only
echo   clear                                                    - Clear all data
echo.
echo Examples:
echo   data_manager.bat add test_game_001 11 Alice Korea 15.2 12.1
echo   data_manager.bat view
echo   data_manager.bat latest

:end
