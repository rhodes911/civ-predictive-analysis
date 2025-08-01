@echo off
REM Stage 2: Database + Superset Dashboard

setlocal enabledelayedexpansion

:show_help
if "%1"=="" goto help
if "%1"=="help" goto help
if "%1"=="--help" goto help
if "%1"=="-h" goto help
goto %1

:help
echo 🎮 Civ VI Analysis - Stage 2: Database + Dashboard
echo =================================================
echo.
echo Usage: stage2.bat [COMMAND]
echo.
echo Commands:
echo   start          Start full stack (Database + Superset)
echo   stop           Stop all services
echo   test           Test database and dashboard connections
echo   logs           Show all service logs
echo   clean          Remove all containers and volumes
echo   status         Show all container status
echo   dashboard      Open dashboard in browser
echo   help           Show this help message
echo.
echo Services:
echo   Database:  localhost:5432 (civ6_user/civ6_password)
echo   Dashboard: localhost:8088 (admin/admin)
echo.
goto end

:start
echo ℹ️  Starting full Civ VI analytics stack...
docker-compose up -d
echo ✅ Stack started!
echo 📊 Database: localhost:5432
echo 🎯 Dashboard: localhost:8088 (admin/admin)
echo ⏰ Superset may take 1-2 minutes to fully initialize...
goto end

:stop
echo ℹ️  Stopping all services...
docker-compose down
echo ✅ All services stopped!
goto end

:test
echo ℹ️  Testing database connection...
docker-compose exec postgres psql -U civ6_user -d civ6_analytics -c "SELECT COUNT(*) FROM game_sessions;"
echo.
echo ℹ️  Testing Superset connection...
curl -f http://localhost:8088/health 2>nul
if %errorlevel% == 0 (
    echo ✅ Superset is responding!
) else (
    echo ⚠️  Superset not ready yet, try again in a minute...
)
goto end

:logs
echo ℹ️  Showing all service logs...
docker-compose logs -f
goto end

:clean
echo ℹ️  Cleaning up all containers and volumes...
docker-compose down -v
echo ✅ All containers and volumes removed!
goto end

:status
echo ℹ️  All container status:
docker-compose ps
goto end

:dashboard
echo ℹ️  Opening dashboard in browser...
start http://localhost:8088
echo 🎯 Dashboard opened! Login with admin/admin
goto end

:error
echo ❌ Unknown command: %1
echo.
goto help

:end
