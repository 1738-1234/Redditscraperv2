import os
import shutil
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

def cleanup_and_organize():
    # Define the essential files and their new locations
    essential_files = {
        'main.py': 'main.py',
        'telegram_bot.py': 'src/telegram_bot.py',
        'reddit_scraper.py': 'src/reddit_scraper.py',
        'database.py': 'src/database.py',
        'requirements.txt': 'requirements.txt',
        '.env': '.env',
        'reddit_scraper.db': 'data/reddit_scraper.db',
        'posted_ids.txt': 'data/posted_ids.txt'
    }

    # Create necessary directories
    directories = ['src', 'data', 'logs']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    # Move essential files to their new locations
    for old_path, new_path in essential_files.items():
        if os.path.exists(old_path):
            try:
                # Create parent directory if it doesn't exist
                os.makedirs(os.path.dirname(new_path), exist_ok=True)
                shutil.move(old_path, new_path)
                logger.info(f"Moved {old_path} to {new_path}")
            except Exception as e:
                logger.error(f"Error moving {old_path}: {str(e)}")

    # Files to delete
    files_to_delete = [
        'run_bot_and_scraper.py',
        'run_all.py',
        'run_telegram_bot.bat',
        'run_both.bat',
        'telegram_bot_runner.py',
        'test_token.py',
        'scraper_runner.py'
    ]

    # Delete unnecessary files
    for file in files_to_delete:
        if os.path.exists(file):
            try:
                os.remove(file)
                logger.info(f"Deleted {file}")
            except Exception as e:
                logger.error(f"Error deleting {file}: {str(e)}")

    # Delete unnecessary directories
    dirs_to_delete = [
        '__pycache__',
        'reddit_scraper_bot_v2 (2)'
    ]

    for directory in dirs_to_delete:
        if os.path.exists(directory):
            try:
                shutil.rmtree(directory)
                logger.info(f"Deleted directory {directory}")
            except Exception as e:
                logger.error(f"Error deleting directory {directory}: {str(e)}")

    # Move log files to logs directory
    log_files = [f for f in os.listdir('.') if f.endswith('.log')]
    for log_file in log_files:
        try:
            shutil.move(log_file, f'logs/{log_file}')
            logger.info(f"Moved {log_file} to logs directory")
        except Exception as e:
            logger.error(f"Error moving {log_file}: {str(e)}")

    # Create a new .gitignore file
    gitignore_content = """
# Python
__pycache__/
*.py[cod]
*$py.class

# Environment
.env
.venv
env/
venv/

# Logs
logs/
*.log

# Database
*.db

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
"""
    with open('.gitignore', 'w') as f:
        f.write(gitignore_content.strip())
    logger.info("Created .gitignore file")

    # Create a README.md file
    readme_content = """
# Reddit Scraper Bot

A Telegram bot that scrapes Reddit for potential leads and provides analytics.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
