# Civ VI AI Logger: Real-Time Game Data Extraction for ML + Analytics

This project sets up a complete pipeline for **automatically logging Civilization VI game data** (e.g. science per turn) from AI vs AI games, storing it in a database, and visualizing it using Apache Superset. The data can also be used to train machine learning models to analyze and improve gameplay strategies.

---

## 🧠 Purpose

We want to:
- Automatically log per-turn stats for every player in Civ VI (e.g. science, culture, gold, cities, etc.)
- Use AI vs AI autoplay games to generate thousands of datapoints
- Store the structured logs in a local database
- Feed that into Superset for visual dashboards
- Later: Use the data to train models that learn how to win or optimize play

---

## 🔁 Workflow Overview

```
Civ VI Lua Script
     ↓
Log Data via print()
     ↓
Lua.log File
     ↓
Python Log Parser
     ↓
SQLite / PostgreSQL DB
     ↓
Apache Superset Dashboard
```

---

## ⚙️ What Happens Step by Step

### 1. Hook Into Civ VI Turn Events Using Lua

- We use a mod or FireTuner to register:
  ```lua
  Events.TurnEnd.Add(OnTurnEnd)
  ```

- This function runs at the end of every full game turn.

- Inside `OnTurnEnd`, we extract stats like:
  ```lua
  local sci = player:GetTechs():GetScienceYield()
  local culture = player:GetCulture():GetCultureYield()
  local gold = player:GetTreasury():GetGoldYield()
  local cities = player:GetCities():GetCount()
  ```

---

### 2. Log the Stats Using `print()`

- Civ VI cannot write files directly, but it **logs all `print()` statements** to:
  ```
  Documents/My Games/Sid Meier's Civilization VI/Logs/Lua.log
  ```

- Sample log output:
  ```
  Turn 10: Player 0 -> Science=24, Culture=20, Gold=18, Cities=3
  Turn 10: Player 1 -> Science=20, Culture=12, Gold=30, Cities=2
  ```

---

### 3. Parse `Lua.log` Using a Python Script

- The parser watches or reads `Lua.log`
- Filters out our structured lines
- Parses data like:
  ```json
  {
    "turn": 10,
    "player": 0,
    "science": 24,
    "culture": 20,
    "gold": 18,
    "cities": 3
  }
  ```

- Inserts into a database (e.g. SQLite or PostgreSQL)

---

### 4. Store Game Data in a Relational Database

- Example schema:
  ```sql
  CREATE TABLE turn_stats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    turn INTEGER,
    player INTEGER,
    science INTEGER,
    culture INTEGER,
    gold INTEGER,
    faith INTEGER,
    cities INTEGER,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
  );
  ```

---

### 5. Visualize in Apache Superset (Running in Docker)

- Mount the database file or connect to Postgres from your Superset container
- Add a new Dataset in Superset:
  - Table: `turn_stats`
  - Time Column: `timestamp` or `turn`
- Build charts like:
  - Science over time per player
  - Culture or gold deltas
  - Victory conditions vs early stats

---

## 🛠️ Requirements

### Civ VI Setup

- Civ VI on PC (with mod support)
- Enable logging:
  - `EnableTuner = 1` in `AppOptions.txt`
  - `EnableLogging = 1` in `Config.ini`
- Install or write a Lua mod (or use FireTuner first)
- Log file: `Lua.log` (auto-created by game)

### Python Parser

- Python 3
- Libraries: `sqlite3` or `psycopg2`, `re`, `watchdog` (optional for live monitoring)

### Apache Superset (Docker)

- Clone Superset repo
- Run via `docker-compose`
- Add SQLite or Postgres as a data source
- Build dashboards from parsed `turn_stats` data

---

## 🧪 Example Use Cases

- 🧠 Train a model to predict victory type from turn 50 data
- 📈 Visualize player progression curves (science, culture, gold)
- 🧬 Compare civs over many AI-only games
- 🤖 Build a recommendation engine for better build orders
- 🔁 Run long AI vs AI simulations and analyze win paths

---

## 🗂️ Project Structure (Example)

```
civ6-ai-logger/
│
├── mod/
│   └── TurnLogger.lua       # Lua script (mod or tuner)
│
├── parser/
│   └── parse_log.py         # Reads Lua.log and writes to DB
│
├── data/
│   └── turn_data.db         # SQLite database
│
├── superset/
│   └── docker-compose.yml   # Superset deployment
│
└── README.md                # This file
```

---

## ✅ Next Steps

1. 🔧 Set up Lua script with logging
2. 🧪 Confirm `Lua.log` prints data
3. 🐍 Run parser script to write to DB
4. 🚢 Spin up Superset container
5. 📊 Create your first dashboard!

---

## 💡 Tips

- Start by using FireTuner to test Lua
- Watch `Lua.log` live with a log viewer or script
- Format printed logs for easy parsing (CSV or JSON-style)
- Add one stat at a time to keep logs readable

---

## 🔐 Security / Privacy Note

This system only logs **offline, local AI games**. No user data, accounts, or multiplayer sessions are touched. All data remains on your machine.

---

## 🤝 Contributing

This is an experimental project to blend modding, data science, and ML. Contributions, ideas, or testing help are welcome!

---

## 📚 References

- https://civilization.fandom.com/wiki/Modding_(Civ6)
- https://forums.civfanatics.com/threads/using-the-tuner-in-civ-vi.600719/
- https://superset.apache.org/docs/
