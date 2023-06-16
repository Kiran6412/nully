# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "22313424"))
API_HASH = os.environ.get("API_HASH", "2cbd9a90ac99583580d9ad6150701045")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5802403990:AAEXvxnGO-_sCg81zYhm67x63d2ghKTby2w")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1700238703")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Dhggg")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://kiranu:kirankabot@cluster0.k5tx2bb.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1700238703")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(1700238703)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001946243122")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "tulinks_official") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
