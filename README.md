# 🏆 Civ VI Analytics Dashboard

**🚀 Complete Local Solution - From Game Data to Strategic Intelligence**  
*Turn your Civ VI game data into interactive dashboards and analysis*

## 🎯 What This Does

**Turn your Civ VI game into a data analytics platform:**
- 📊 **Interactive Dashboards**: Create any charts you want with your game data
- 🧪 **Civilization Tracking**: Monitor science, culture, population, and more
- 📈 **Historical Data**: Complete turn-by-turn data from game start
- 🎮 **Live Updates**: Data updates as you play more turns
- 🔍 **Custom Analysis**: Build whatever visualizations you need
- 🤖 **AI Victory Prediction**: Machine learning model predicts game winners (97.6% accuracy!)

**Perfect for analyzing:**
- "How did England's science output change over time?"
- "Which civilizations have the most cities?"
- "What's my population growth trend?"
- "How do different civs compare on any metric?"
- "Who's most likely to win this game?" (AI prediction!)

## 🤖 NEW: AI Victory Prediction

**Get live predictions of who will win your current game!**

### **Quick Prediction**
```bash
# Get instant prediction for current game
quick_predict.bat
```

### **Full ML Pipeline** 
```bash
# Train model + make predictions (first time or after new games)
run_ml_pipeline.bat
```

**Example Output:**
```
🏆 VICTORY PREDICTIONS - Turn 41
Rank Civilization      Win Prob   Score    Cities   Science
1    INDONESIA         76.6%      45       3        8        🔥
2    ENGLAND           15.2%      38       2        6        📈
3    ROME              8.1%       35       2        5        📉
```

**The AI model achieves 97.6% accuracy by analyzing:**
- Current scores and rankings
- Production and science yields  
- City development patterns
- Historical game outcomes

## 🚀 Quick Start (3 Steps to Dashboard)

### **Prerequisites**
- **Windows PC** with Civ VI installed
- **Docker Desktop** - [Download here](https://www.docker.com/products/docker-desktop/)
- **Active Civ VI game** (for live data)

### **Step 1: Get the Code**
```bash
git clone https://github.com/rhodes911/civ-predictive-analysis.git
cd civ-predictive-analysis
```

### **Step 2: Start the Services**
```bash
docker-compose up -d
```
*This starts PostgreSQL database + Apache Superset dashboard*

### **Step 3: Load Your Game Data**
**Option A: Docker Desktop (Recommended)**
1. Open Docker Desktop
2. Find the `civ6_data_loader` container
3. Click the ▶️ **Play button**
4. Watch the logs for "✅ Data loading complete!"

**Option B: Command Line**
```bash
docker-compose up data-loader
```

### **Step 4: Build Your Dashboard** 
- **URL**: http://localhost:8088
- **Login**: admin / admin
- **Create any charts you want** using instructions in `superset-chart-instructions.md`

**🎉 You now have your Civ VI data ready for analysis!**

## 📊 How It Works

### **Simple 3-Service Architecture**
```
Civ VI Game → CSV Files → Data Loader → PostgreSQL → Superset Dashboard
```

### **Your Workflow**
1. **Play Civ VI** 🎮 - Game automatically writes data to CSV files
2. **Click Play Button** ▶️ - Use Docker Desktop to run data loader
3. **Build Charts** 📊 - Superset lets you create any visualizations you want

### **Services**
- **PostgreSQL** - Stores your game data (localhost:5432)
- **Superset** - Interactive dashboard builder (localhost:8088)  
- **Data Loader** - Smart script that processes CSV files

### **Key Features**
- ✅ **Multi-Game Support** - Handles multiple game sessions
- ✅ **Smart Updates** - Only adds new turn data
- ✅ **Historical Preservation** - Keeps all previous games
- ✅ **Civilization Detection** - Automatically identifies different games

---

## 🎮 Update Workflow

### **After Playing More Turns:**
1. **Save your game** in Civ VI
2. **Open Docker Desktop**
3. **Click ▶️ Play** on `civ6_data_loader` container
4. **Refresh Superset** to see new data

**That's it!** The script intelligently detects what's new and adds only the latest turns.

---

## 🔧 File Structure

### **Core Files**
- `docker-compose.yml` - Infrastructure setup
- `stage4h_insert_data.py` - Smart data processing script
- `Dockerfile.data-loader` - Container for data processing
- `superset-chart-instructions.md` - Chart creation guide

### **AI/ML Files**
- `run_ml_pipeline.bat` - Complete ML training pipeline
- `quick_predict.bat` - Quick victory prediction
- `ml_data_preparation.py` - Extract training data from database
- `victory_prediction_model.py` - Train Random Forest model
- `predict_winner.py` - Live game winner predictions

### **Database**
- `database/init.sql` - PostgreSQL schema
- `test_database_filtering.py` - Verify game filtering works

### **Documentation**
- `database_filtering_results.md` - How game separation works
- `superset-refresh-button.md` - Manual refresh instructions

##  Troubleshooting

### **Common Issues**

**"No CSV files found"**
- Ensure you have an active Civ VI game save
- Check that CSV logging is enabled in Civ VI settings

**"Database connection failed"**  
- Run `docker-compose up -d` to start containers
- Wait 30 seconds for PostgreSQL to fully initialize

**"No complete turn data"**
- Play at least one full turn in Civ VI
- Save the game to ensure CSV files are updated

**"Charts not updating"**
- Refresh Superset dashboard (Ctrl+F5)
- Run the data loader again to add new turns

### **Getting Help**
1. Check the Docker container logs: `docker-compose logs`
2. Verify CSV file locations with Windows File Explorer
3. Test database filtering with: `python test_database_filtering.py`

---

*Ready to turn your Civ VI games into data insights? Get started with the Quick Start guide above! 🚀*
