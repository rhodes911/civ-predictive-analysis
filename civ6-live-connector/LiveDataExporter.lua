-- ========================================
-- Civ VI Live Data Exporter
-- Exports real-time game data for ML analysis
-- ========================================

print("Civ VI Live Data Exporter - Initializing...")

local ExportManager = {}
local gameStarted = false
local lastExportTurn = -1

-- ========================================
-- Configuration
-- ========================================
local EXPORT_FILE_PATH = "C:\\Users\\rhode\\source\\repos\\civ-predictive-analysis\\live_data\\current_game.json"
local CONNECTION_STATUS_FILE = "C:\\Users\\rhode\\source\\repos\\civ-predictive-analysis\\live_data\\connection_status.json"

-- ========================================
-- Helper Functions
-- ========================================
function ExportManager.WriteToFile(filepath, content)
    local file = io.open(filepath, "w")
    if file then
        file:write(content)
        file:close()
        print("✅ Data exported to: " .. filepath)
        return true
    else
        print("❌ Failed to write to: " .. filepath)
        return false
    end
end

function ExportManager.GetCurrentGameData()
    local pGame = Game
    local currentTurn = pGame.GetCurrentGameTurn()
    local pLocalPlayer = pGame.GetLocalPlayer()
    
    if not pLocalPlayer then
        print("⚠️ No local player found")
        return nil
    end
    
    local localPlayerID = pLocalPlayer:GetID()
    local gameData = {
        timestamp = os.time(),
        turn_number = currentTurn,
        game_id = "live_game_" .. tostring(os.time()),
        local_player_id = localPlayerID,
        players = {}
    }
    
    -- Get all alive players
    local pPlayerManager = PlayerManager
    for _, playerID in ipairs(pPlayerManager.GetAliveIDs()) do
        local pPlayer = pPlayerManager.GetPlayer(playerID)
        if pPlayer then
            local playerData = ExportManager.GetPlayerData(pPlayer)
            if playerData then
                table.insert(gameData.players, playerData)
            end
        end
    end
    
    return gameData
end

function ExportManager.GetPlayerData(pPlayer)
    if not pPlayer then return nil end
    
    local playerID = pPlayer:GetID()
    local pPlayerConfig = PlayerConfigurations[playerID]
    local pPlayerTechs = pPlayer:GetTechs()
    local pPlayerCulture = pPlayer:GetCulture()
    local pPlayerTreasury = pPlayer:GetTreasury()
    
    local playerData = {
        player_id = playerID,
        player_name = pPlayerConfig:GetPlayerName(),
        civilization = pPlayerConfig:GetCivilizationShortDescription(),
        leader = pPlayerConfig:GetLeaderName(),
        is_human = pPlayer:IsHuman(),
        is_local = pPlayer:IsLocalPlayer(),
        science_per_turn = pPlayerTechs:GetScienceYield(),
        culture_per_turn = pPlayerCulture:GetCultureYield(),
        gold_per_turn = pPlayerTreasury:GetGoldYield(),
        faith_per_turn = pPlayer:GetReligion():GetFaithYield(),
        cities = {},
        military_strength = 0  -- Will be calculated
    }
    
    -- Get city data
    local pPlayerCities = pPlayer:GetCities()
    for i, pCity in pPlayerCities:Members() do
        local cityData = ExportManager.GetCityData(pCity)
        if cityData then
            table.insert(playerData.cities, cityData)
        end
    end
    
    -- Calculate military strength
    local pPlayerUnits = pPlayer:GetUnits()
    local totalMilitaryStrength = 0
    for i, pUnit in pPlayerUnits:Members() do
        local pUnitDef = GameInfo.Units[pUnit:GetUnitType()]
        if pUnitDef and pUnitDef.Combat > 0 then
            totalMilitaryStrength = totalMilitaryStrength + pUnitDef.Combat
        end
    end
    playerData.military_strength = totalMilitaryStrength
    
    return playerData
end

function ExportManager.GetCityData(pCity)
    if not pCity then return nil end
    
    local pCityBuildings = pCity:GetBuildings()
    local pCityDistricts = pCity:GetDistricts()
    
    return {
        city_id = pCity:GetID(),
        name = pCity:GetName(),
        population = pCity:GetPopulation(),
        x = pCity:GetX(),
        y = pCity:GetY(),
        is_capital = pCity:IsCapital(),
        districts_count = pCityDistricts:GetNumDistricts(),
        buildings_count = pCityBuildings:GetNumBuildings(),
        production_per_turn = pCity:GetYield(GameInfo.Yields["YIELD_PRODUCTION"].Index),
        food_per_turn = pCity:GetYield(GameInfo.Yields["YIELD_FOOD"].Index),
        housing = pCity:GetGrowth():GetHousing()
    }
end

-- ========================================
-- Connection Status Management
-- ========================================
function ExportManager.UpdateConnectionStatus(status, message)
    local statusData = {
        connected = status,
        message = message or "",
        timestamp = os.time(),
        game_running = Game ~= nil,
        last_turn = Game and Game.GetCurrentGameTurn() or -1
    }
    
    local jsonContent = ExportManager.TableToJSON(statusData)
    ExportManager.WriteToFile(CONNECTION_STATUS_FILE, jsonContent)
end

-- ========================================
-- JSON Conversion (Simple)
-- ========================================
function ExportManager.TableToJSON(t)
    local function escape(s)
        return s:gsub('\\', '\\\\'):gsub('"', '\\"'):gsub('\n', '\\n'):gsub('\r', '\\r'):gsub('\t', '\\t')
    end
    
    if type(t) == "table" then
        local result = "{"
        local first = true
        for k, v in pairs(t) do
            if not first then result = result .. "," end
            result = result .. '"' .. escape(tostring(k)) .. '":' .. ExportManager.TableToJSON(v)
            first = false
        end
        return result .. "}"
    elseif type(t) == "string" then
        return '"' .. escape(t) .. '"'
    elseif type(t) == "number" then
        return tostring(t)
    elseif type(t) == "boolean" then
        return t and "true" or "false"
    else
        return '""'
    end
end

-- ========================================
-- Event Handlers
-- ========================================
function OnLocalPlayerTurnBegin()
    local currentTurn = Game.GetCurrentGameTurn()
    print("🎯 Turn " .. currentTurn .. " - Exporting live data...")
    
    if currentTurn ~= lastExportTurn then
        local gameData = ExportManager.GetCurrentGameData()
        if gameData then
            local jsonContent = ExportManager.TableToJSON(gameData)
            if ExportManager.WriteToFile(EXPORT_FILE_PATH, jsonContent) then
                ExportManager.UpdateConnectionStatus(true, "Live data exported for turn " .. currentTurn)
                lastExportTurn = currentTurn
            else
                ExportManager.UpdateConnectionStatus(false, "Failed to export data for turn " .. currentTurn)
            end
        else
            ExportManager.UpdateConnectionStatus(false, "No game data available")
        end
    end
end

function OnGameStart()
    print("🎮 Game started - Live Data Exporter active!")
    gameStarted = true
    ExportManager.UpdateConnectionStatus(true, "Game started - Live exporter connected")
end

-- ========================================
-- Event Registration
-- ========================================
Events.LocalPlayerTurnBegin.Add(OnLocalPlayerTurnBegin)
Events.GameCoreEventPublishComplete.Add(OnGameStart)

-- ========================================
-- Initialize
-- ========================================
print("✅ Civ VI Live Data Exporter - Ready!")
ExportManager.UpdateConnectionStatus(true, "Mod loaded - Waiting for game start")
