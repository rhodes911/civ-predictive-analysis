@echo off
REM Script to add new game data without restarting containers
REM Usage: add_game_data.bat [game_id] [turn] [player] [civ] [science] [culture]

if "%~6"=="" (
    echo Usage: add_game_data.bat [game_id] [turn] [player] [civ] [science] [culture]
    echo Example: add_game_data.bat test_game_001 11 Alice Korea 15.2 12.1
    exit /b 1
)

set GAME_ID=%1
set TURN=%2
set PLAYER=%3
set CIV=%4
set SCIENCE=%5
set CULTURE=%6

echo Adding game data: Turn %TURN% - %PLAYER% (%CIV%) - Science: %SCIENCE%, Culture: %CULTURE%

docker exec civ6_database psql -U civ6_user -d civ6_analytics -c "INSERT INTO game_data (game_id, turn_number, player_name, civilization, science_per_turn, culture_per_turn) VALUES ('%GAME_ID%', %TURN%, '%PLAYER%', '%CIV%', %SCIENCE%, %CULTURE%) ON CONFLICT DO NOTHING;"

echo Data added successfully!
