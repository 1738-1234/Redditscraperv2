@echo off
echo Starting Reddit Scraper Bot...
echo.

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH
    echo Please install Python 3.10 or higher
    pause
    exit /b 1
)

:: Check if virtual environment exists, if not create it
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    call venv\Scripts\activate
    echo Installing requirements...
    pip install -r requirements.txt
) else (
    call venv\Scripts\activate
)

:: Set PYTHONPATH to include the current directory
set PYTHONPATH=%PYTHONPATH%;%CD%

:: Create logs directory if it doesn't exist
if not exist "logs" mkdir logs

:: Run the bot
echo Starting bot...
python main.py

:: If the bot crashes, pause to show error
if errorlevel 1 (
    echo.
    echo Bot crashed! Check the logs for details.
    pause
) 