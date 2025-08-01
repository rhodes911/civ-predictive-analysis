# 🤖 Civ VI ML Strategy Analysis

**🔒 Complete Local Docker Solution for the Civ VI Community**  
*Deploy once, everything works - no internet or setup required*

## � ### **Stage 3: Real Civ VI ### **Stage 3: Real Civ VI Data Connection** 🔧
**Status**: **BREAKTHROUGH!** - Found treasure trove of real game data

**🎯 Stage 3a Results ✅**
- **What Accomplished**: Created `find_lua_logs.py` script to locate Civ VI log files
- **Test Results**: Successfully found log file at `C:\Users\rhode\AppData\Local\Firaxis Games\Sid Meier's Civilization VI\Logs\Lua.log`
- **File Status**: 10,559 bytes with active game data
- **BREAKTHROUGH**: Discovered entire Logs directory with CSV files!

**🎯 Stage 3b Results ✅** 
- **What Accomplished**: Created `extract_leaders.py` script to parse log for leader names
- **Test Results**: Lua.log doesn't contain leader names, but found much better data!
- **DISCOVERY**: Found `Game_PlayerScores.csv` with turn-by-turn player data
- **DISCOVERY**: Found `DiplomacySummary.csv` with player interactions
- **Data Available**: Players 0-14 active, turns 1-11 recorded, real scores and diplomacy!

**🎯 Stage 3c Results ✅**
- **What Accomplished**: Created `show_civ_data.py` comprehensive display script
- **Status**: Ready to parse CSV files instead of Lua.log
- **REAL DATA FOUND**: 
  - ✅ Turn-by-turn player scores (Game_PlayerScores.csv)
  - ✅ Diplomatic actions between players (DiplomacySummary.csv)
  - ✅ 17+ CSV files with different game aspects
  - ✅ Live data updating as game progresses

**📝 Files Created:**
- ✅ `find_lua_logs.py` - Finds Civ VI log files in common Windows locations
- ✅ `extract_leaders.py` - Extracts leader names from Lua.log using multiple patterns  
- ✅ `show_civ_data.py` - Complete pipeline showing connection to real Civ VI data
- ✅ `examine_log.py` - Helper script to examine log content

**🎮 Current Status:**
- ✅ Scripts created and tested with active game
- ✅ Log file location confirmed and CSV treasure trove discovered
- ✅ **REAL GAME DATA CONFIRMED**: Players 0-14, Turns 1-11, scores, diplomacy
- ⏳ **NEXT**: Create CSV parser to extract meaningful player data
- ⏳ **THEN**: Display active players and their progress

**🔥 BREAKTHROUGH TEST RESULTS ✅**
- **Active Game Detected**: Turn 11, 15 active players
- **Player Scores Working**: Real progression data (Player 5 leading with score 17)
- **Diplomacy Tracking**: 70 diplomatic interactions recorded
- **Data Volume**: 171 data points across 11 turns
- **File Sources**: Game_PlayerScores.csv + DiplomacySummary.csv + 17 other CSV files
- **Update Status**: Live data, growing as game progresses

**🎉 STAGE 3 COMPLETE!**
- ✅ **Connection Established**: Successfully reading live Civ VI game data
- ✅ **Data Sources Identified**: CSV files much better than Lua.log 
- ✅ **Real Player Data**: 15 active players with turn-by-turn progression
- ✅ **Diplomatic Intelligence**: Player interactions and relationships tracked
- ✅ **Community Ready**: Ultra simple scripts that work with any Civ VI installation🔧
**Status**: **STARTING** - Ultra simple approach: Find logs, see leaders, done!

**🎯 Stage 3a Goal: Find Civ VI Lua.log File**
- **What**: Locate where Civ VI writes its Lua.log file
- **Why**: Need to know where to look for game data
- **How**: Check common Windows locations for Civ VI logs
- **Success**: Script finds and reports Lua.log location

**🎯 Stage 3b Goal: Extract Leader Names**
- **What**: Parse Lua.log to find leader names in current game
- **Why**: Simplest data we can extract to prove connection works
- **How**: Search log for leader-related text patterns
- **Success**: Display list of leaders currently in the game

**🎯 Stage 3c Goal: Show What We Found**
- **What**: Print the results to console - that's it!
- **Why**: Proof of concept before building anything complex
- **How**: Simple print statements showing leaders found
- **Success**: We see real Civ VI data on our screen

**📂 Common Civ VI Log Locations (Windows):**
- `%USERPROFILE%\Documents\My Games\Sid Meier's Civilization VI\Logs\Lua.log`
- `%LOCALAPPDATA%\Firaxis Games\Sid Meier's Civilization VI\Logs\Lua.log`
- Steam installation logs

**🔍 Baby Steps Plan:**
- ⏳ **Step 1**: Create `find_lua_logs.py` - Check if Lua.log exists anywhere
- ⏳ **Step 2**: Create `extract_leaders.py` - Find leader names in the log
- ⏳ **Step 3**: Test with real game - Start Civ VI, see if we can spot leaders*Required Software:**
- **Docker Desktop** for Windows - [Download here](https://www.docker.com/products/docker-desktop/)
- **Git** (to clone the repository)

That's it! Everything else is included in the Docker containers.

## �🛠️ Development Stages

Building step-by-step, testing each stage thoroughly:

### **Stage 1: Self-Contained Database** ✅
- **Tech**: Docker Compose, PostgreSQL container
- **Goal**: One-command database deployment 
- **Community Impact**: `docker-compose up` = instant Civ VI database
- **Status**: **COMPLETED** - Database running and tested
- **Note**: 🔒 Zero configuration required

### **Stage 2: Working Dashboard with Sample Data** ✅  
- **Stage 2a**: Get Superset connecting to PostgreSQL database ✅
- **Stage 2b**: Create basic charts from existing sample data ✅
- **Stage 2c**: Verify dashboard displays data correctly ✅
- **Community Impact**: Working dashboard showing sample Civ VI analytics
- **Status**: **COMPLETED** - Dashboard working with data management system!
- **Note**: 🔒 Baby steps approach successful - ready for real data

### **Stage 3: Real Civ VI Data Connection** 🔧
- **Stage 3a**: Find Civ VI Lua.log file 🔍
- **Stage 3b**: Extract leader names from current game �
- **Stage 3c**: Display what we found (no database yet) �
- **Tech**: Simple Python file reading, basic text parsing
- **Goal**: Just see SOMETHING from real Civ VI data
- **Community Impact**: Proof that we can read live game data
- **Status**: **STARTING** - Ultra simple approach
- **Note**: 🔒 Find logs, see leaders, that's it!


### **Stage 4: Live Game Tracking** 🔄
- **Tech**: Real-time file monitoring, live dashboard updates
- **Goal**: Watch games as they happen with live charts
- **Community Impact**: Stream-friendly live analysis overlay
- **Status**: **READY TO START** - Stage 3 live connection complete
- **Note**: 🔒 Foundation ready - now enhance with real-time chart updates

### **Stage 5: ML-Powered Insights** ⏳
- **Tech**: Pre-trained models, instant predictions
- **Goal**: AI recommendations and win predictions
- **Community Impact**: "Upload game → Get strategy advice"
- **Status**: Pending Stage 4
- **Note**: 🔒 Models included in container

### **Stage 6: Local LLM Decision Agents** ⏳
- **Tech**: Local LLM (Ollama/LLaMA), real-time game state analysis
- **Goal**: AI agents that make decisions as you play
- **Community Impact**: "AI co-pilot for live Civ VI games"
- **Status**: Future - after Stage 5
- **Note**: 🔒 Fully local LLM, no cloud dependencies

---

## 📝 Progress Log

*Will be updated as we complete each stage with findings, issues, and solutions*

### **Stage 1 Issues & Solutions ✅**

**Issue 1: PostgreSQL Environment Variables Not Working**
- **Problem**: `POSTGRES_PASSWORD is not specified` error on container startup
- **Root Cause**: Docker Compose YAML dictionary format not being read properly
- **Solution**: Changed from `POSTGRES_DB: value` to `- POSTGRES_DB=value` array format
- **Files Changed**: `docker-compose.yml` - environment section
- **Result**: Database now starts successfully with proper authentication

**Issue 2: Docker Compose Version Warning**
- **Problem**: Warning about obsolete `version` attribute
- **Root Cause**: Modern Docker Compose doesn't need version specification
- **Solution**: Removed `version: '3.8'` line from docker-compose.yml
- **Files Changed**: `docker-compose.yml`
- **Result**: Cleaner startup without warnings

### **Stage 2 Issues & Solutions ✅**

**Issue 3: Superset Missing PostgreSQL Driver**
- **Problem**: `ModuleNotFoundError: No module named 'psycopg2'`
- **Root Cause**: Apache Superset image doesn't include PostgreSQL connectivity by default
- **Solution**: Added `pip install psycopg2-binary` to container startup command
- **Files Changed**: `docker-compose.yml` - superset command section
- **Result**: Superset can now connect to PostgreSQL databases

**Issue 4: Superset JWT Secret Too Short**
- **Problem**: `AsyncQueryTokenException: Please provide a JWT secret at least 32 bytes long`
- **Root Cause**: Default secret key was too short for Superset's security requirements
- **Solution**: Extended secret key to 100+ characters in environment variables
- **Files Changed**: `docker-compose.yml` - SUPERSET_SECRET_KEY environment variable
- **Result**: Superset starts without JWT errors

**Issue 5: Superset Complex Configuration Conflicts**
- **Problem**: Custom superset_config.py causing async query and JWT conflicts
- **Root Cause**: Advanced configuration features requiring additional setup
- **Solution**: Simplified approach - removed custom config, used basic Superset setup
- **Files Changed**: Removed superset_config.py volume mount from docker-compose.yml
- **Result**: Superset starts successfully with default configuration

**Issue 6: Superset Turn Number Filter Sorting**
- **Problem**: Turn number filter dropdown displays in wrong order (1, 10, 11, 2, 3...) despite correct database ordering
- **Root Cause**: Superset UI caching treats INTEGER columns as strings in filter dropdowns
- **Solution Attempted**: Added `turn_display` column with zero-padded values (001, 002, 003...) for proper sorting
- **Files Changed**: `database/init.sql` - added computed column for sortable display
- **Current Status**: Functionality works correctly, minor UI display quirk in filter dropdown only
- **Community Impact**: Charts and data display correctly, filter dropdown cosmetic issue doesn't affect functionality

### **Key Learnings for Community**

**✅ Baby Steps Approach Works**
- Complex configurations often fail - start simple, add features incrementally
- Test each component in isolation before combining
- Always confirm each stage works before proceeding

**✅ Docker Environment Variable Best Practices**
- Use array format (`- KEY=value`) instead of dictionary format in docker-compose.yml
- Make secrets long enough for production requirements (32+ bytes for JWT)
- Remove obsolete configuration to avoid warnings

**✅ Superset Setup Gotchas**
- Default Apache Superset image needs PostgreSQL driver installed manually
- Custom configurations can cause more problems than they solve initially
- Start with default setup, customize later once basic functionality works

**✅ Debugging Process**
- Always check container logs: `docker-compose logs [service-name]`
- Use container status to identify failing services: `docker-compose ps`
- Test database connectivity separately from dashboard connectivity

### **Development Database Results ✅**
- ✅ PostgreSQL database running in Docker container
- ✅ Database accessible at localhost:5432
- ✅ Sample Civ VI schema created with test data
- ✅ Database connection tested successfully - query executed properly
- ✅ Management scripts working (start/stop/test/status)
- ✅ **Issue resolved**: Fixed PostgreSQL environment variable format in docker-compose.yml

### **Stage 2a Results ✅** 
- ✅ Superset container running and healthy
- ✅ Dashboard accessible at localhost:8088
- ✅ Login working (admin/admin)
- ✅ **Issue resolved**: Simplified Superset config removed JWT complexity

### **Stage 2b Results ✅**
- ✅ PostgreSQL database connection configured in Superset UI
- ✅ Database connection test successful - "Database connected" message confirmed
- ✅ Superset can now access sample Civ VI data (game_sessions and game_data tables)

### **Stage 2c Results ✅**
- ✅ First working chart created: "Average Science Per Turn by Civilization"
- ✅ Table format showing civilization science comparison
- ✅ Data feeding system working without container restarts
- ✅ Realistic turn progression data (turns 1-11) 
- ✅ Data management scripts (`data_manager.bat`) working perfectly
- ✅ Database schema includes both `turn_number` (INTEGER) and `turn_display` (padded) for sorting
- ⚠️ **Minor Issue**: Superset filter dropdown caching causes turn number display quirk (functionality unaffected)

### **Stage 2 Complete! 🎉**
- ✅ **Database**: PostgreSQL with realistic Civ VI sample data (Alice/Korea, Bob/Rome, Charlie/Egypt)
- ✅ **Dashboard**: Apache Superset connected and displaying meaningful charts
- ✅ **Data Management**: Live data feeding system without container restarts (`data_manager.bat`)
- ✅ **Community Ready**: Single command deployment (`docker-compose up`)
- ✅ **Data Quality**: Clean, easy-to-read progression data (turns 1-11)

### **Stage 3: Real Civ VI Data Integration** 🔧
**Status**: **STARTING** - Taking baby steps to find and connect to Lua logs first

**🎯 Stage 3a Goal: Find Civ VI Lua.log Location**
- **What**: Locate where Civ VI writes its Lua.log file
- **Why**: Need to know where to look for game data before we can read it
- **How**: Create simple Python script to check common Civ VI log locations
- **Success**: Script finds existing Lua.log file and reports location

**� Common Civ VI Log Locations (Windows):**
- `%USERPROFILE%\Documents\My Games\Sid Meier's Civilization VI\Logs\Lua.log`
- `%LOCALAPPDATA%\Firaxis Games\Sid Meier's Civilization VI\Logs\Lua.log`
- Steam installation folder logs

**🔍 Next Baby Steps:**
- ✅ **Step 1**: Create `find_lua_logs.py` - Simple script to check if Lua.log exists
- ⏳ **Step 2**: Monitor log file for changes (basic file watching)
- ⏳ **Step 3**: Read and display new lines as they're written
