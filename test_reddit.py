import os
import praw
from dotenv import load_dotenv
import logging
import sys
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Reddit API credentials
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")
REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

def test_reddit_connection():
    """Test Reddit API connection and subreddit access."""
    try:
        # Initialize Reddit client
        reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent=REDDIT_USER_AGENT,
            username=REDDIT_USERNAME,
            password=REDDIT_PASSWORD
        )
        
        # Test authentication
        me = reddit.user.me()
        logger.info(f"Successfully authenticated as: {me.name}")
        
        # Test subreddit access
        test_subreddits = ['nursing', 'StudentNurse', 'nursingstudents']
        for sub in test_subreddits:
            try:
                subreddit = reddit.subreddit(sub)
                # Try to fetch a few posts
                posts = list(subreddit.new(limit=5))
                logger.info(f"Successfully accessed r/{sub} - found {len(posts)} recent posts")
            except Exception as e:
                logger.error(f"Error accessing r/{sub}: {str(e)}")
        
        return True
        
    except Exception as e:
        logger.error(f"Error testing Reddit connection: {str(e)}")
        return False

if __name__ == "__main__":
    test_reddit_connection() 