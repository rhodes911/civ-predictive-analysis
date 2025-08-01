# 🎮 Civ VI Live Data Exporter - Installation Guide

## 🔧 Installation Options

### Option 1: Automatic Installation
```batch
stage3.bat install
```

### Option 2: Manual Installation
If automatic installation fails, follow these steps:

#### 1. Install Python Dependencies
```batch
pip install psycopg2-binary watchdog
```

#### 2. Install the Civ VI Mod Manually

**Find your Civ VI Mods directory:**
- Windows: `%USERPROFILE%\Documents\My Games\Sid Meier's Civilization VI\Mods`
- Windows (OneDrive): `%USERPROFILE%\OneDrive\Documents\My Games\Sid Meier's Civilization VI\Mods`
- Steam Deck: `~/.local/share/Steam/steamapps/compatdata/289070/pfx/drive_c/users/steamuser/Documents/My Games/Sid Meier's Civilization VI/Mods`

**Copy the mod files:**
1. Create folder: `CivVILiveDataExporter` in your mods directory
2. Copy these files:
   - `civ6-live-connector/LiveDataExporter.lua`
   - `civ6-live-connector/LiveDataExporter.modinfo`

#### 3. Enable the Mod in Civ VI
1. Start Civilization VI
2. Go to **Additional Content**
3. Click **Mods**
4. Enable **"Civ VI Live Data Exporter"**
5. **Restart Civ VI**

## 🚀 Usage

### Start Live Monitoring
```batch
stage3.bat start
```

This will start:
- Live data monitor (watches for game data)
- Status server (http://localhost:8089)
- Database connection

### Check Status
```batch
stage3.bat status
```

### Play Civ VI
1. Start a new game with the mod enabled
2. Play a few turns
3. Watch http://localhost:8089 for connection status
4. Check http://localhost:8088 for live data in Superset

## 🔍 Troubleshooting

### Mod Not Working
- Make sure mod is enabled in Civ VI Additional Content
- Restart Civ VI after enabling the mod
- Check the game log for Lua errors

### No Data Appearing
- Verify the mod is exporting files to `live_data/` directory
- Check `live_data/connection_status.json` for status
- Make sure `live_monitor.py` is running

### Database Connection Issues
- Ensure PostgreSQL is running: `stage2.bat start`
- Check database connection: `stage2.bat test`

## 📊 What Data is Collected

The mod exports:
- **Turn number** and **timestamp**
- **Player information**: Name, civilization, leader
- **Per-turn yields**: Science, culture, gold, faith
- **City data**: Population, districts, buildings
- **Military strength** calculations

All data is exported to JSON files and automatically imported into the PostgreSQL database for analysis in Superset.
