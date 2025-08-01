@echo off
setlocal enabledelayedexpansion

if "%1"=="start" goto start_monitor
if "%1"=="stop" goto stop_monitor
if "%1"=="status" goto check_status
if "%1"=="install" goto install_deps

echo 🎮 Civ VI Live Data Monitor
echo.
echo Usage:
echo   live_monitor.bat start     - Start monitoring live data
echo   live_monitor.bat stop      - Stop monitoring 
echo   live_monitor.bat status    - Check connection status
echo   live_monitor.bat install   - Install Python dependencies
echo.
goto end

:install_deps
echo 📦 Installing Python dependencies...
pip install psycopg2-binary watchdog
echo ✅ Dependencies installed
goto end

:start_monitor
echo 🎯 Starting Civ VI Live Data Monitor...
echo.
echo Make sure:
echo ✅ 1. Database is running (stage2.bat start)
echo ✅ 2. Civ VI Live Data Exporter mod is installed
echo ✅ 3. Civ VI game is running
echo.
python live_monitor.py
goto end

:stop_monitor
echo 🛑 Stopping live monitor...
taskkill /f /im python.exe /fi "WINDOWTITLE eq live_monitor*" 2>nul
echo ✅ Monitor stopped
goto end

:check_status
echo 🔍 Checking live connection status...
if exist "live_data\connection_status.json" (
    echo.
    type "live_data\connection_status.json"
    echo.
) else (
    echo ❌ No connection status file found
    echo    Make sure the Civ VI mod is running
)

if exist "live_data\dashboard_status.json" (
    echo 📊 Dashboard Status:
    type "live_data\dashboard_status.json"
    echo.
) else (
    echo ⚠️ No dashboard status available
)
goto end

:end
