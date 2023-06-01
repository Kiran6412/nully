# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "25562244"))
API_HASH = os.environ.get("API_HASH", "afa60b3fd1ba44e46851f534177a9161")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6225190414:AAEOCnW2cBFgGjb0tul7h4BM5AUI02BM3Jw")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5790359537")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Dhggg")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://ciros42580:omprtngslb@cluster0.phrmyvu.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5790359537")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(5790359537)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001795283531")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "popcornpanda") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
