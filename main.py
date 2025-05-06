import os
import logging
import sys
from datetime import datetime
from dotenv import load_dotenv
from src.telegram_bot import run_telegram_bot
from src.reddit_scraper import RedditScraper
import traceback

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(f'logs/bot_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
    ]
)

logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

def main():
    """Main entry point for the bot."""
    try:
        logger.info("Starting Reddit Scraper Bot...")
        
        # Create logs directory if it doesn't exist
        os.makedirs('logs', exist_ok=True)
        
        # Initialize Reddit scraper
        logger.debug("Initializing Reddit scraper...")
        scraper = RedditScraper()
        
        # Start Telegram bot
        logger.debug("Starting Telegram bot...")
        run_telegram_bot(scraper)
        
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        sys.exit(1)

if __name__ == "__main__":
    main() 