import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
CASHCOW_CHAT_ID = os.getenv("CASHCOW_CHAT_ID")

# Other configuration settings can be added here