@echo off
REM Quick ML Prediction Script
REM ========================
REM This script quickly runs a prediction on the current game state

echo.
echo 🔮 QUICK CIV VI VICTORY PREDICTION
echo ==================================
echo.

REM Check if model exists
if not exist "trained_model.pkl" (
    echo ⚠️  No trained model found. Running full pipeline...
    call run_ml_pipeline.bat
    goto :end
)

REM Run quick prediction
echo 🎯 Making prediction for current game...
python predict_winner.py
if errorlevel 1 (
    echo ❌ Prediction failed! Try running the full pipeline.
    echo Run: run_ml_pipeline.bat
    pause
    exit /b 1
)

:end
echo.
echo 💡 TIP: To retrain the model with new data, run: run_ml_pipeline.bat
echo.
pause
