-- Test script to verify mod file path access
-- This simulates what our Civ VI mod does

local EXPORT_FILE_PATH = "C:\\Users\\rhode\\source\\repos\\civ-predictive-analysis\\live_data\\test_output.json"

print("Testing mod file path access...")

-- Test JSON content
local testData = {
    test = true,
    message = "Mod path test successful",
    timestamp = os.time()
}

-- Simple JSON conversion
local function tableToJSON(t)
    local result = "{"
    local first = true
    for k, v in pairs(t) do
        if not first then result = result .. "," end
        if type(v) == "string" then
            result = result .. '"' .. k .. '":"' .. v .. '"'
        elseif type(v) == "number" then
            result = result .. '"' .. k .. '":' .. v
        elseif type(v) == "boolean" then
            result = result .. '"' .. k .. '":' .. (v and "true" or "false")
        end
        first = false
    end
    return result .. "}"
end

-- Try to write file
local file = io.open(EXPORT_FILE_PATH, "w")
if file then
    file:write(tableToJSON(testData))
    file:close()
    print("✅ SUCCESS: File written to " .. EXPORT_FILE_PATH)
else
    print("❌ ERROR: Could not write to " .. EXPORT_FILE_PATH)
end
