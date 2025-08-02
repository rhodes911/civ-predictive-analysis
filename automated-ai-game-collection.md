# 🚀 Automated AI vs AI Game Collection Guide

**How to Run 50+ Complete Civ VI Games for ML Training Data**

---

## ⚡ Quick Strategy Overview

### **Time Optimization**
- **Game Speed**: Quick (150-200 turns) = ~45-90 minutes per game
- **Parallel Processing**: Run multiple instances simultaneously
- **Automation**: No human intervention required
- **24/7 Operation**: Let it run overnight/weekends

### **Expected Timeline**
```
Sequential: 50 games × 1.5 hours = 75 hours (3+ days continuous)
Parallel (4 instances): 75 hours ÷ 4 = ~19 hours (1 day)
Optimized settings: 50 games × 45 minutes ÷ 4 = ~9 hours
```

---

## 🎮 Civ VI Automation Methods

### **Method 1: Steam Workshop Mod Automation (RECOMMENDED)**

#### **AutoPlay Mod Setup**
```
Required Mods:
┌─────────────────────────────────────────────┐
│ 1. "AI Autoplay" - Fully automated AI games │
│ 2. "Quick Game Setup" - Skip setup screens  │
│ 3. "No Animations" - Speed up turn processing│
│ 4. "Fast Movement" - Reduce animation time  │
└─────────────────────────────────────────────┘
```

**Installation:**
1. Subscribe to mods in Steam Workshop
2. Enable in Civ VI Additional Content menu
3. Configure autoplay settings for full AI control

#### **Optimal Game Settings for Speed**
```ini
# Game setup for maximum speed
Game Speed: Quick
Map Size: Small (4 civs) or Standard (6 civs)
Map Type: Pangaea (faster than water maps)
Difficulty: Prince (balanced, predictable)
Victory Types: Science + Culture only (faster than Domination)
Barbarians: Off (reduces processing)
Natural Disasters: Off (reduces events)
```

### **Method 2: Command Line Automation**

#### **Batch Script for Multiple Games**
```batch
@echo off
REM automated_civ_games.bat
REM Runs multiple Civ VI games in sequence

setlocal enabledelayedexpansion
set GAME_COUNT=50
set CIV_PATH="C:\Program Files (x86)\Steam\steamapps\common\Sid Meier's Civilization VI"

for /L %%i in (1,1,%GAME_COUNT%) do (
    echo Starting AI Game %%i of %GAME_COUNT%
    
    REM Launch Civ VI with autoplay mod
    start /wait %CIV_PATH%\CivilizationVI.exe ^
        -autoplay ^
        -speed quick ^
        -mapsize small ^
        -difficulty prince ^
        -gamemode classic
    
    echo Game %%i completed, processing data...
    
    REM Process the completed game data
    python process_completed_game.py "game_%%i"
    
    echo Waiting 30 seconds before next game...
    timeout /t 30
)

echo All %GAME_COUNT% games completed!
```

### **Method 3: Parallel Instance Management**

#### **Multi-Instance Setup**
```python
# parallel_game_manager.py
import subprocess
import time
import threading
from pathlib import Path

class CivGameManager:
    def __init__(self, num_instances=4):
        self.num_instances = num_instances
        self.games_per_instance = 50 // num_instances
        self.civ_path = r"C:\Program Files (x86)\Steam\steamapps\common\Sid Meier's Civilization VI"
    
    def run_game_batch(self, instance_id, start_game, end_game):
        """Run a batch of games in one instance"""
        for game_num in range(start_game, end_game + 1):
            print(f"Instance {instance_id}: Starting game {game_num}")
            
            # Launch Civ VI with unique save folder
            cmd = [
                f"{self.civ_path}/CivilizationVI.exe",
                "-autoplay",
                "-speed", "quick",
                "-mapsize", "small", 
                "-savefolder", f"instance_{instance_id}",
                "-gameid", f"game_{game_num}"
            ]
            
            # Run game and wait for completion
            result = subprocess.run(cmd, capture_output=True)
            
            if result.returncode == 0:
                print(f"Instance {instance_id}: Game {game_num} completed successfully")
                # Process the game data immediately
                self.process_game_data(instance_id, game_num)
            else:
                print(f"Instance {instance_id}: Game {game_num} failed")
            
            time.sleep(30)  # Brief pause between games
    
    def run_parallel_collection(self):
        """Run multiple game instances in parallel"""
        threads = []
        
        for i in range(self.num_instances):
            start_game = i * self.games_per_instance + 1
            end_game = (i + 1) * self.games_per_instance
            
            thread = threading.Thread(
                target=self.run_game_batch,
                args=(i, start_game, end_game)
            )
            threads.append(thread)
            thread.start()
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
        
        print("All parallel game collection completed!")

# Usage
if __name__ == "__main__":
    manager = CivGameManager(num_instances=4)
    manager.run_parallel_collection()
```

---

## 🛠️ Technical Optimization

### **System Requirements for Fast Parallel Processing**
```
Recommended Specs:
┌─────────────────────────────────────────┐
│ CPU: 8+ cores (for 4 parallel instances)│
│ RAM: 16+ GB (4GB per Civ VI instance)   │
│ Storage: SSD (faster save/load times)   │
│ GPU: Mid-range (for graphics processing)│
└─────────────────────────────────────────┘
```

### **Performance Optimization Settings**
```ini
# Civ VI Graphics Settings for Speed
Resolution: 1920x1080 (or lower)
Graphics Quality: Medium (balance speed/stability)
Anti-Aliasing: Off
Shadows: Low
Effects: Low
Terrain Detail: Medium
Water Quality: Low
Animation Speed: Fast
```

### **CSV Data Collection Automation**
```python
# game_data_monitor.py
import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class GameDataCollector(FileSystemEventHandler):
    def __init__(self, game_instance_id):
        self.instance_id = game_instance_id
        self.csv_folder = f"C:/Users/{os.getenv('USERNAME')}/Documents/My Games/Sid Meier's Civilization VI/Logs"
        self.collection_folder = f"./collected_games/instance_{game_instance_id}"
        os.makedirs(self.collection_folder, exist_ok=True)
    
    def on_modified(self, event):
        if event.is_directory:
            return
        
        # Check if it's a CSV file indicating game completion
        if event.src_path.endswith('.csv') and 'Player_Stats' in event.src_path:
            print(f"Instance {self.instance_id}: Game data detected, collecting...")
            self.collect_game_data()
    
    def collect_game_data(self):
        """Copy all CSV files from the current game to collection folder"""
        csv_files = [
            'Player_Stats.csv',
            'City_Stats.csv', 
            'Victory_Progress.csv'
        ]
        
        game_folder = f"{self.collection_folder}/game_{int(time.time())}"
        os.makedirs(game_folder, exist_ok=True)
        
        for csv_file in csv_files:
            src = f"{self.csv_folder}/{csv_file}"
            dst = f"{game_folder}/{csv_file}"
            if os.path.exists(src):
                shutil.copy2(src, dst)
                print(f"Collected {csv_file}")

# Start monitoring for each instance
def start_data_collection(num_instances=4):
    observers = []
    
    for i in range(num_instances):
        collector = GameDataCollector(i)
        observer = Observer()
        observer.schedule(collector, collector.csv_folder, recursive=False)
        observer.start()
        observers.append(observer)
    
    return observers
```

---

## 📋 Complete Automation Workflow

### **Step 1: Environment Setup**
```bash
# Create dedicated folders for parallel processing
mkdir civ_ai_training
cd civ_ai_training
mkdir instance_0 instance_1 instance_2 instance_3
mkdir collected_games processed_data

# Install required Python packages
pip install watchdog pandas psycopg2-binary
```

### **Step 2: Game Configuration Template**
```python
# game_config_generator.py
def generate_game_configs(num_games=50):
    """Generate diverse game configurations for training variety"""
    
    configs = []
    maps = ['PANGAEA', 'CONTINENTS', 'ISLAND_PLATES', 'SMALL_CONTINENTS']
    difficulties = ['CHIEFTAIN', 'WARLORD', 'PRINCE', 'KING']
    game_speeds = ['QUICK', 'STANDARD']
    
    for i in range(num_games):
        config = {
            'game_id': f'training_game_{i:03d}',
            'map_type': maps[i % len(maps)],
            'difficulty': difficulties[i % len(difficulties)],
            'game_speed': game_speeds[i % len(game_speeds)],
            'num_civs': 6 if i % 2 == 0 else 4,  # Alternate between 4 and 6 civs
            'victory_types': ['SCIENCE', 'CULTURE', 'DOMINATION']
        }
        configs.append(config)
    
    return configs

# Save configurations for each instance
configs = generate_game_configs(50)
for i in range(4):  # 4 parallel instances
    instance_configs = configs[i::4]  # Distribute games across instances
    with open(f'instance_{i}_config.json', 'w') as f:
        json.dump(instance_configs, f, indent=2)
```

### **Step 3: Master Control Script**
```python
# master_game_controller.py
import json
import subprocess
import threading
import time
from datetime import datetime

class MasterGameController:
    def __init__(self):
        self.start_time = datetime.now()
        self.completed_games = 0
        self.total_games = 50
        
    def run_instance(self, instance_id):
        """Run all games for one instance"""
        with open(f'instance_{instance_id}_config.json', 'r') as f:
            configs = json.load(f)
        
        for config in configs:
            print(f"Instance {instance_id}: Starting {config['game_id']}")
            
            # Launch Civ VI with this configuration
            self.launch_civ_game(instance_id, config)
            
            # Process completed game
            self.process_completed_game(instance_id, config)
            
            self.completed_games += 1
            progress = (self.completed_games / self.total_games) * 100
            elapsed = datetime.now() - self.start_time
            
            print(f"Progress: {self.completed_games}/{self.total_games} ({progress:.1f}%) - Elapsed: {elapsed}")
    
    def launch_civ_game(self, instance_id, config):
        """Launch Civ VI with specific configuration"""
        cmd = [
            "CivilizationVI.exe",
            "-autoplay",
            "-speed", config['game_speed'].lower(),
            "-maptype", config['map_type'].lower(),
            "-difficulty", config['difficulty'].lower(),
            "-numcivs", str(config['num_civs']),
            "-savefolder", f"instance_{instance_id}",
            "-gameid", config['game_id']
        ]
        
        # Run and wait for completion
        subprocess.run(cmd, cwd="C:/Program Files (x86)/Steam/steamapps/common/Sid Meier's Civilization VI")
    
    def run_parallel_collection(self):
        """Run all 4 instances in parallel"""
        threads = []
        
        for i in range(4):
            thread = threading.Thread(target=self.run_instance, args=(i,))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        total_time = datetime.now() - self.start_time
        print(f"🎉 All {self.total_games} games completed in {total_time}!")

# Run the complete automation
if __name__ == "__main__":
    controller = MasterGameController()
    controller.run_parallel_collection()
```

---

## ⏱️ Realistic Time Estimates

### **Single Instance Performance**
```
Game Speed Settings vs Time:
┌─────────────────────────────────────────┐
│ Quick + Small Map + 4 Civs = 30-45 min │
│ Quick + Standard + 6 Civs = 45-75 min  │
│ Standard + Standard + 6 Civs = 2-3 hrs │
└─────────────────────────────────────────┘
```

### **Parallel Processing Benefits**
```
Scenario: 50 games, Quick speed, 4 parallel instances

Sequential: 50 × 45 minutes = 37.5 hours
Parallel:   37.5 hours ÷ 4 = ~9.5 hours
Weekend:    Friday 6pm → Saturday 4am = DONE! ✅
```

### **Optimization Impact**
```
Performance Improvements:
- No animations: -20% time
- Small maps: -30% time  
- 4 civs instead of 6: -25% time
- SSD storage: -10% time
- Combined optimization: ~50% faster!
```

---

## 🎯 Expected Training Data Output

### **Data Volume per 50 Games**
```
Per Game: 6 civs × 150 turns = 900 records
50 Games: 900 × 50 = 45,000 training records
Victory Distribution: ~12-13 games per victory type
CSV Storage: ~500MB of raw game data
```

### **Quality Assurance**
```python
# data_quality_checker.py
def validate_game_collection():
    """Ensure all 50 games completed successfully"""
    
    required_files = ['Player_Stats.csv', 'Victory_Summary.csv']
    
    for game_id in range(1, 51):
        game_folder = f"collected_games/game_{game_id:03d}"
        
        # Check if game completed
        if not os.path.exists(game_folder):
            print(f"❌ Game {game_id}: Folder missing")
            continue
            
        # Check if all CSV files present
        missing_files = []
        for file in required_files:
            if not os.path.exists(f"{game_folder}/{file}"):
                missing_files.append(file)
        
        if missing_files:
            print(f"⚠️  Game {game_id}: Missing {missing_files}")
        else:
            print(f"✅ Game {game_id}: Complete")

validate_game_collection()
```

---

## 🚀 Quick Start Commands

### **Option 1: Basic Automation (Easiest)**
```bash
# Download AutoPlay mod from Steam Workshop
# Run this simple script:
automated_civ_games.bat
```

### **Option 2: Advanced Parallel Processing**
```bash
# Setup parallel environment
python game_config_generator.py
python -c "from game_data_monitor import start_data_collection; start_data_collection(4)"
python master_game_controller.py
```

### **Option 3: Weekend Long Run**
```bash
# Friday evening setup:
python setup_weekend_run.py --games 50 --instances 4 --speed quick
# Let it run all weekend, check Sunday morning!
```

---

**With this setup, you can realistically collect 50+ complete AI vs AI games in 8-12 hours of automated processing, giving you the solid training data needed for accurate victory prediction models!** 🎮🤖
