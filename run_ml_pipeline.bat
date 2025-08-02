@echo off
REM ML Victory Prediction Pipeline
REM ===============================
REM This script runs the complete ML pipeline for Civ VI victory prediction

echo.
echo 🎯 CIV VI ML VICTORY PREDICTION PIPELINE
echo =========================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found! Please install Python first.
    pause
    exit /b 1
)

REM Check if required packages are installed
echo 📦 Checking ML dependencies...
python -c "import pandas, numpy, sklearn, psycopg2, matplotlib, seaborn" >nul 2>&1
if errorlevel 1 (
    echo ⚠️  Some ML packages missing. Installing...
    pip install pandas numpy scikit-learn psycopg2-binary matplotlib seaborn
    if errorlevel 1 (
        echo ❌ Failed to install packages. Please check your pip installation.
        pause
        exit /b 1
    )
)

echo ✅ Dependencies ready!
echo.

REM Run the ML pipeline
echo 🚀 STEP 1: Data Preparation
echo ----------------------------
python ml_data_preparation.py
if errorlevel 1 (
    echo ❌ Data preparation failed!
    pause
    exit /b 1
)

echo.
echo 🤖 STEP 2: Model Training
echo -------------------------
python victory_prediction_model.py
if errorlevel 1 (
    echo ❌ Model training failed!
    pause
    exit /b 1
)

echo.
echo 🔮 STEP 3: Live Prediction
echo --------------------------
python predict_winner.py
if errorlevel 1 (
    echo ❌ Prediction failed!
    pause
    exit /b 1
)

echo.
echo 🎉 ML PIPELINE COMPLETED SUCCESSFULLY!
echo =====================================
echo.
echo Generated Files:
echo   📊 training_data.csv - Training dataset
echo   📋 data_analysis_report.txt - Data insights
echo   📦 trained_model.pkl - ML model
echo   📈 feature_importance.csv - Important features
echo   📋 model_performance_report.txt - Model evaluation
echo   🔮 prediction_log.txt - Live predictions
echo.
echo Next Steps:
echo   1. Review the performance reports
echo   2. Run predict_winner.py anytime for live predictions
echo   3. Collect more game data to improve accuracy
echo.
pause
