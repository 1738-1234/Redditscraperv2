# Reddit Scraper Bot

A Telegram bot that scrapes Reddit for potential leads and provides analytics.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables in `.env`:
```
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password
REDDIT_USER_AGENT=your_reddit_user_agent
```

3. Run the bot:
```bash
python main.py
```

## Project Structure

- `src/`: Source code files
- `data/`: Database and data files
- `logs/`: Log files