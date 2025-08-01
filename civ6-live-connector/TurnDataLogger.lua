-- ========================================
-- Civ VI Data Logger (DeepResearch Method)
-- Uses print() statements to log data via Lua.log
-- More reliable than direct file writing
-- ========================================

print("🎮 Civ VI Data Logger - DeepResearch Method Initializing...")

local DataLogger = {}
local gameStarted = false
local lastLoggedTurn = -1
local gameID = "game_" .. tostring(os.time())

-- ========================================
-- Game Event Handlers
-- ========================================

function OnGameStart()
    gameStarted = true
    gameID = "game_" .. tostring(os.time())
    
    print("GAME_START: " .. gameID)
    
    -- Log game info
    local pGame = Game
    local gameInfo = "Unknown"
    
    print("GAME_INFO: Map=Unknown, Difficulty=Unknown, Players=" .. tostring(PlayerManager.GetAliveMajorsCount()))
    
    -- Log all players
    for _, playerID in ipairs(PlayerManager.GetAliveMajorIDs()) do
        local pPlayer = PlayerManager.GetPlayer(playerID)
        if pPlayer then
            local pPlayerConfig = PlayerConfigurations[playerID]
            local playerName = pPlayerConfig:GetPlayerName() or ("Player_" .. tostring(playerID))
            local civName = pPlayerConfig:GetCivilizationShortDescription() or "Unknown"
            local leaderName = pPlayerConfig:GetLeaderName() or "Unknown"
            local isHuman = pPlayer:IsHuman() and "True" or "False"
            
            print("PLAYER: ID=" .. tostring(playerID) .. ", Name=" .. playerName .. ", Civ=" .. civName .. ", Leader=" .. leaderName .. ", Human=" .. isHuman)
        end
    end
    
    print("✅ Game logging initialized for: " .. gameID)
end

function OnTurnEnd()
    local pGame = Game
    local currentTurn = pGame.GetCurrentGameTurn()
    
    -- Only log each turn once
    if currentTurn <= lastLoggedTurn then
        return
    end
    
    print("🎯 Logging Turn " .. tostring(currentTurn) .. " data...")
    
    -- Log data for all alive players
    for _, playerID in ipairs(PlayerManager.GetAliveMajorIDs()) do
        local pPlayer = PlayerManager.GetPlayer(playerID)
        if pPlayer then
            LogPlayerData(pPlayer, currentTurn)
        end
    end
    
    lastLoggedTurn = currentTurn
end

-- ========================================
-- Data Extraction Functions
-- ========================================

function LogPlayerData(pPlayer, turn)
    if not pPlayer then
        return
    end
    
    local playerID = pPlayer:GetID()
    local pPlayerConfig = PlayerConfigurations[playerID]
    
    -- Get player info
    local civName = pPlayerConfig:GetCivilizationShortDescription() or "Unknown"
    
    -- Get yields
    local pPlayerTechs = pPlayer:GetTechs()
    local pPlayerCulture = pPlayer:GetCulture()
    local pPlayerTreasury = pPlayer:GetTreasury()
    local pPlayerReligion = pPlayer:GetReligion()
    
    local scienceYield = pPlayerTechs and pPlayerTechs:GetScienceYield() or 0
    local cultureYield = pPlayerCulture and pPlayerCulture:GetCultureYield() or 0
    local goldYield = pPlayerTreasury and pPlayerTreasury:GetGoldYield() or 0
    local faithYield = pPlayerReligion and pPlayerReligion:GetFaithYield() or 0
    
    -- Get city count
    local pPlayerCities = pPlayer:GetCities()
    local cityCount = pPlayerCities and pPlayerCities:GetNumCities() or 0
    
    -- Format and print the structured log line
    local logLine = string.format(
        "Turn %d: Player %d (%s) -> Science=%.1f, Culture=%.1f, Gold=%.1f, Faith=%.1f, Cities=%d",
        turn, playerID, civName, scienceYield, cultureYield, goldYield, faithYield, cityCount
    )
    
    print(logLine)
end

-- ========================================
-- Utility Functions  
-- ========================================

function GetPlayerCityData(pPlayer)
    local cities = {}
    local pPlayerCities = pPlayer:GetCities()
    
    if pPlayerCities then
        for i, pCity in pPlayerCities:Members() do
            local cityData = {
                name = pCity:GetName(),
                population = pCity:GetPopulation(),
                isCapital = pCity:IsCapital()
            }
            table.insert(cities, cityData)
        end
    end
    
    return cities
end

function GetPlayerMilitaryStrength(pPlayer)
    local totalStrength = 0
    local pPlayerUnits = pPlayer:GetUnits()
    
    if pPlayerUnits then
        for i, pUnit in pPlayerUnits:Members() do
            local pUnitDef = GameInfo.Units[pUnit:GetUnitType()]
            if pUnitDef and pUnitDef.Combat and pUnitDef.Combat > 0 then
                totalStrength = totalStrength + pUnitDef.Combat
            end
        end
    end
    
    return totalStrength
end

-- ========================================
-- Event Registration
-- ========================================

-- Register for game events
Events.GameCoreEventPublishComplete.Add(OnGameStart)
Events.TurnEnd.Add(OnTurnEnd)

-- Also try local player turn begin for more responsive logging
Events.LocalPlayerTurnBegin.Add(function()
    if gameStarted then
        OnTurnEnd()
    end
end)

-- ========================================
-- Initialize
-- ========================================

print("✅ Civ VI Data Logger (DeepResearch Method) - Ready!")
print("📝 Logging method: print() statements to Lua.log")
print("🎯 Data will appear in: Documents/My Games/Sid Meier's Civilization VI/Logs/Lua.log")
print("📊 Use log_parser.py to feed data into database")

-- Test if we're already in a game
if Game then
    local currentTurn = Game.GetCurrentGameTurn()
    if currentTurn and currentTurn > 0 then
        print("🎮 Game already in progress - Turn " .. tostring(currentTurn))
        OnGameStart()
    end
end
