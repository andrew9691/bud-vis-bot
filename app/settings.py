import logging
import os

from dotenv import load_dotenv


# load env vars
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_file_path = os.path.join(BASE_DIR, '.env')
load_dotenv(env_file_path)

# logging settings
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO,
)

# database settings
PG_HOST = os.getenv('PG_HOST', 'localhost')
PG_PORT = int(os.getenv('PG_PORT', 5432))
PG_DB = os.getenv('PG_DB')
PG_USER = os.getenv('PG_USER')
PG_PASSWORD = os.getenv('PG_PASSWORD')

BOT_TOKEN = os.getenv('BOT_TOKEN')

BOT_ADMIN_ID = int(os.getenv('BOT_ADMIN_ID', 0))
