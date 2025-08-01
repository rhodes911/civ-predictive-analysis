@echo off
echo 🎮 Civ VI Live Connection Setup
echo =====================================
echo.

if "%1"=="install" goto install_mod
if "%1"=="start" goto start_all
if "%1"=="stop" goto stop_all
if "%1"=="status" goto check_all_status

echo Usage:
echo   stage3.bat install   - Install Civ VI mod and dependencies
echo   stage3.bat start     - Start live monitoring system
echo   stage3.bat stop      - Stop live monitoring
echo   stage3.bat status    - Check all connections
echo.
goto end

:install_mod
echo 📦 Installing Civ VI Live Data Exporter...
echo.

echo 1. Installing Python dependencies...
pip install psycopg2-binary watchdog

echo.
echo 2. Copying mod to Civ VI directory...
set "CIV6_MODS_DIR=%USERPROFILE%\OneDrive\Documents\My Games\Sid Meier's Civilization VI\Mods"

if not exist "%CIV6_MODS_DIR%" (
    echo ❌ Civ VI mods directory not found!
    echo    Expected: %CIV6_MODS_DIR%
    echo    Please make sure Civ VI is installed
    goto end
)

set "MOD_DIR=%CIV6_MODS_DIR%\CivVILiveDataExporter"
if not exist "%MOD_DIR%" mkdir "%MOD_DIR%"

copy "civ6-live-connector\LiveDataExporter.lua" "%MOD_DIR%\"
copy "civ6-live-connector\LiveDataExporter.modinfo" "%MOD_DIR%\"

echo ✅ Mod installed to: %MOD_DIR%
echo.
echo 📋 Next steps:
echo    1. Start Civ VI
echo    2. Enable "Civ VI Live Data Exporter" mod in Additional Content
echo    3. Start a new game
echo    4. Run: stage3.bat start
echo.
goto end

:start_all
echo 🚀 Starting live monitoring system...
echo.

echo 1. Checking if database is running...
docker ps | findstr civ6_database >nul
if errorlevel 1 (
    echo ⚠️ Database not running, starting it...
    call stage2.bat start
    timeout /t 10 >nul
)

echo 2. Starting status server...
start "Civ VI Status Server" python status_server.py

echo 3. Starting live data monitor...
start "Civ VI Live Monitor" python live_monitor.py

echo.
echo ✅ Live monitoring system started!
echo.
echo 🌐 Status Page: http://localhost:8089
echo 📊 Dashboard: http://localhost:8088
echo 🔗 Database: localhost:5432
echo.
echo 📋 To see live data:
echo    1. Make sure Civ VI is running with the mod enabled
echo    2. Start a game and play a few turns
echo    3. Check the status page for connection
echo.
goto end

:stop_all
echo 🛑 Stopping live monitoring system...
taskkill /f /im python.exe /fi "WINDOWTITLE eq Civ VI*" 2>nul
echo ✅ All monitors stopped
goto end

:check_all_status
echo 🔍 Checking all system status...
echo.

echo 📊 Database Status:
docker ps | findstr civ6_database >nul
if errorlevel 1 (
    echo ❌ Database not running
) else (
    echo ✅ Database running
)

echo.
echo 📊 Superset Dashboard:
docker ps | findstr civ6_superset >nul
if errorlevel 1 (
    echo ❌ Superset not running  
) else (
    echo ✅ Superset running at http://localhost:8088
)

echo.
echo 🔗 Live Connection Status:
if exist "live_data\connection_status.json" (
    type "live_data\connection_status.json"
) else (
    echo ❌ No connection status file
)

echo.
echo 🌐 Status Server:
netstat -an | findstr ":8089" >nul
if errorlevel 1 (
    echo ❌ Status server not running
) else (
    echo ✅ Status server running at http://localhost:8089
)

goto end

:end
