@echo off
REM DeepResearch Method - Lua.log Parser Approach
REM Replaces the live connection method with reliable log parsing

if "%1"=="install" goto install_deepresearch
if "%1"=="start" goto start_parser
if "%1"=="stop" goto stop_parser
if "%1"=="status" goto check_status
if "%1"=="test" goto test_parsing
if "%1"=="analyze" goto run_analysis

echo 🎮 Civ VI DeepResearch Method - Lua.log Parser
echo ===============================================
echo.
echo This uses the reliable print() logging approach instead of live file export
echo.
echo Usage:
echo   deepresearch.bat install   - Install mod and Python dependencies
echo   deepresearch.bat start     - Start log parsing and monitoring
echo   deepresearch.bat stop      - Stop log parser
echo   deepresearch.bat status    - Check system status
echo   deepresearch.bat test      - Test log parsing with sample data
echo   deepresearch.bat analyze   - Run ML analysis on collected data
echo.
echo Setup:
echo   1. Run: deepresearch.bat install
echo   2. Enable mod in Civ VI: "Civ VI Turn Data Logger"
echo   3. Run: deepresearch.bat start
echo   4. Play Civ VI and watch data flow into database
echo.
goto end

:install_deepresearch
echo 📦 Installing DeepResearch Method...
echo.

echo 1. Installing Python dependencies...
pip install -r requirements.txt

echo.
echo 2. Creating models directory...
if not exist "models" mkdir "models"

echo.
echo 3. Installing Civ VI mod...
set "CIV6_MODS_DIR=%USERPROFILE%\Documents\My Games\Sid Meier's Civilization VI\Mods"
if not exist "%CIV6_MODS_DIR%" (
    set "CIV6_MODS_DIR=%USERPROFILE%\OneDrive\Documents\My Games\Sid Meier's Civilization VI\Mods"
)

if not exist "%CIV6_MODS_DIR%" (
    echo ❌ Civ VI mods directory not found!
    echo    Please make sure Civ VI is installed
    goto end
)

set "MOD_DIR=%CIV6_MODS_DIR%\CivVITurnDataLogger"
if not exist "%MOD_DIR%" mkdir "%MOD_DIR%"

copy "civ6-live-connector\TurnDataLogger.lua" "%MOD_DIR%\"
copy "civ6-live-connector\TurnDataLogger.modinfo" "%MOD_DIR%\"

echo ✅ Mod installed to: %MOD_DIR%
echo.
echo 📋 Next steps:
echo    1. Start Civ VI
echo    2. Go to Additional Content → Mods
echo    3. Enable "Civ VI Turn Data Logger"
echo    4. Restart Civ VI
echo    5. Run: deepresearch.bat start
echo    6. Start a new game and play a few turns
echo.
goto end

:start_parser
echo 🚀 Starting DeepResearch log parser...
echo.

echo 1. Checking database...
docker ps | findstr civ6_database >nul
if errorlevel 1 (
    echo ⚠️ Database not running, starting it...
    call stage2.bat start
    timeout /t 10 >nul
)

echo 2. Starting log parser...
start "Civ VI Log Parser" python src/data/log_parser.py

echo 3. Starting main application...
start "Civ VI ML Pipeline" python src/main.py monitor

echo.
echo ✅ DeepResearch parser started!
echo.
echo 📋 What's running:
echo    🔍 Log Parser: Watching Lua.log file
echo    🧠 ML Pipeline: Ready for analysis
echo    📊 Database: localhost:5432
echo    🎯 Dashboard: http://localhost:8088
echo.
echo 📋 To see data flowing:
echo    1. Start Civ VI with the mod enabled
echo    2. Start a new game
echo    3. Play a few turns
echo    4. Watch the parser terminal for new data
echo.
goto end

:stop_parser
echo 🛑 Stopping DeepResearch parser...
taskkill /f /im python.exe /fi "WINDOWTITLE eq Civ VI*" 2>nul
echo ✅ Parser stopped
goto end

:check_status
echo 🔍 DeepResearch Method Status
echo ============================
echo.

echo 📊 Database Status:
docker ps | findstr civ6_database >nul
if errorlevel 1 (
    echo ❌ Database not running
) else (
    echo ✅ Database running
)

echo.
echo 🎮 Civ VI Mod Status:
set "CIV6_MODS_DIR=%USERPROFILE%\Documents\My Games\Sid Meier's Civilization VI\Mods"
if not exist "%CIV6_MODS_DIR%" (
    set "CIV6_MODS_DIR=%USERPROFILE%\OneDrive\Documents\My Games\Sid Meier's Civilization VI\Mods"
)

if exist "%CIV6_MODS_DIR%\CivVITurnDataLogger\TurnDataLogger.lua" (
    echo ✅ Mod installed
) else (
    echo ❌ Mod not installed - run: deepresearch.bat install
)

echo.
echo 📝 Lua.log Status:
set "LUA_LOG=C:\Users\%USERNAME%\AppData\Local\Firaxis Games\Sid Meier's Civilization VI\Logs\Lua.log"
if not exist "%LUA_LOG%" (
    set "LUA_LOG=%USERPROFILE%\Documents\My Games\Sid Meier's Civilization VI\Logs\Lua.log"
)
if not exist "%LUA_LOG%" (
    set "LUA_LOG=%USERPROFILE%\OneDrive\Documents\My Games\Sid Meier's Civilization VI\Logs\Lua.log"
)

if exist "%LUA_LOG%" (
    echo ✅ Lua.log found: %LUA_LOG%
    for %%I in ("%LUA_LOG%") do (
        if %%~zI GTR 0 (
            echo    Size: %%~zI bytes - Contains game data
        ) else (
            echo    Size: 0 bytes - Empty (no mod data yet)
        )
    )
) else (
    echo ❌ Lua.log not found - play at least one turn in Civ VI
)

echo.
echo 📊 Data Status:
python -c "import sys; sys.path.append('src'); from src.data.loader import DataLoader; loader = DataLoader(); count = loader.get_total_records(); print(f'Total records in database: {count}')"

goto end

:test_parsing
echo 🧪 Testing log parsing with sample data...
echo.

echo Creating sample Lua.log data...
set "TEST_LOG=test_lua.log"

echo Turn 1: Player 0 (Korea) -^> Science=2.5, Culture=1.8, Gold=3.2, Faith=0.0, Cities=1 > "%TEST_LOG%"
echo Turn 1: Player 1 (Rome) -^> Science=2.0, Culture=2.2, Gold=2.8, Faith=0.0, Cities=1 >> "%TEST_LOG%"
echo Turn 2: Player 0 (Korea) -^> Science=3.1, Culture=2.4, Gold=4.1, Faith=0.5, Cities=1 >> "%TEST_LOG%"
echo Turn 2: Player 1 (Rome) -^> Science=2.8, Culture=2.9, Gold=3.5, Faith=0.8, Cities=1 >> "%TEST_LOG%"

echo Testing parser...
python -c "import sys; sys.path.append('src'); from src.data.log_parser import LuaLogParser; parser = LuaLogParser(); parser.current_game_id = 'test_game_123'; parser.parse_lua_log('test_lua.log'); print('✅ Test parsing completed')"

del "%TEST_LOG%" 2>nul
echo ✅ Test completed - check database for test data
goto end

:run_analysis
echo 🧠 Running ML analysis...
C:/Users/rhode/source/repos/civ-predictive-analysis/.venv/Scripts/python.exe src/main.py analyze
goto end

:end
