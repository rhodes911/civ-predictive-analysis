# 🏆 Civ VI Race Analysis Dashboard

**🚀 Complete Local Solution - From Game Data to Strategic Intelligence**  
*Real-time civilization tracking and race analysis for Civ VI players*

## 🎯 What This Does

**Turn your Civ VI game into a strategic intelligence dashboard:**
- 📊 **Race Analysis**: Track civilization score progression over time
- 🧪 **Science/Culture Tracking**: See who's leading in research and culture
- 📈 **Historical Data**: Complete turn-by-turn progression from game start
- 🎮 **Live Updates**: Data updates as you play more turns
- 🔍 **Strategic Insights**: Identify rising/falling civilizations and trends

**Perfect for answering:**
- "How did England overtake Rome to become #1?"
- "Which civilization has the strongest science output?"
- "Who's been consistently rising in the rankings?"
- "What turn did my civilization peak?"

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

### **Step 4: Create Your Dashboard** 
- **URL**: http://localhost:8088
- **Login**: admin / admin
- **Create charts** using instructions in `superset-chart-instructions.md`

**🎉 You now have a working Civ VI race analysis dashboard!**

## 📊 How It Works

### **Simple 3-Service Architecture**
```
Civ VI Game → CSV Files → Data Loader → PostgreSQL → Superset Dashboard
```

### **Your Workflow**
1. **Play Civ VI** 🎮 - Game automatically writes data to CSV files
2. **Click Play Button** ▶️ - Use Docker Desktop to run data loader
3. **View Dashboard** 📊 - Superset shows your race progression

### **Services**
- **PostgreSQL** - Stores your game data (localhost:5432)
- **Superset** - Interactive dashboard (localhost:8088)  
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
- `superset-chart-instructions.md` - Dashboard creation guide

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

*Ready to turn your Civ VI games into strategic intelligence? Get started with the Quick Start guide above! 🚀*
