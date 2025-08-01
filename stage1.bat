@echo off
REM Stage 1: Basic Database Setup and Testing

setlocal enabledelayedexpansion

:show_help
if "%1"=="" goto help
if "%1"=="help" goto help
if "%1"=="--help" goto help
if "%1"=="-h" goto help
goto %1

:help
echo 🎮 Civ VI Analysis - Stage 1: Database Setup
echo ============================================
echo.
echo Usage: stage1.bat [COMMAND]
echo.
echo Commands:
echo   start          Start PostgreSQL database
echo   stop           Stop database
echo   test           Test database connection
echo   logs           Show database logs
echo   clean          Remove database and volumes
echo   status         Show container status
echo   help           Show this help message
echo.
echo Database Info:
echo   Host: localhost:5432
echo   Database: civ6_analytics
echo   User: civ6_user
echo   Password: civ6_password
echo.
goto end

:start
echo ℹ️  Starting PostgreSQL database...
docker-compose up -d postgres
echo ✅ Database started! Available at localhost:5432
echo 📊 Database: civ6_analytics
echo 👤 User: civ6_user / civ6_password
goto end

:stop
echo ℹ️  Stopping database...
docker-compose down
echo ✅ Database stopped!
goto end

:test
echo ℹ️  Testing database connection...
echo 📝 Running test query...
docker-compose exec postgres psql -U civ6_user -d civ6_analytics -c "SELECT COUNT(*) FROM game_sessions;"
echo ✅ Database test completed!
goto end

:logs
echo ℹ️  Showing database logs...
docker-compose logs -f postgres
goto end

:clean
echo ℹ️  Cleaning up database and volumes...
docker-compose down -v
echo ✅ Database and volumes removed!
goto end

:status
echo ℹ️  Container status:
docker-compose ps
goto end

:error
echo ❌ Unknown command: %1
echo.
goto help

:end
