from os import getenv
import os

from dotenv import load_dotenv
load_dotenv()

API_ID = int(getenv("API_ID", None))
API_HASH = getenv("API_HASH", None)
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", None))
MONGO_URL = getenv("MONGO_URL", None)

API_KEY = getenv("API_KEY", None)
# Get a Fresh Api Key from https://aistudio.google.com/app/apikey
# Then set it as environment variable API_KEY

if not API_KEY:
    raise ValueError("API_KEY environment variable is not set. Get a fresh key from https://aistudio.google.com/app/apikey")

AUTH_CHANNEL = int(getenv("AUTH_CHANNEL", None)) # Fsub Channel Id
FSUB = getenv("FSUB", True) # Promote Bot Admin on Your Channel (Fsub Channel Id Channel ) 

LOGGER_GROUP_ID = -1003951821704 # Bot Events Logs

SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "SAYAPROJECT")
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "SHNWAZX")


STICKER = [
    "CAACAgUAAxkBAAIGpGp-VJ-6cZFAaeyhxyCLjPYtYE8fAAIlGAACKI6wVVNEvN-6z3Z7HgQ",
    "CAACAgUAAxkBAAIGpWp-VKJF8N-4rcnqFxHwzaYRUQGHAAK4GQAC_SsIVhGA75QnH5eeHgQ",
    "CAACAgUAAxkBAAIGpmp-VKP13V0vDwp1viybZeTqgqzfAAI4FwACDDexVVp91U_1BZKFHgQ",
    "CAACAgUAAxkBAAIGp2p-VKZV-sQvGudORSv3he6HYnkAA4wVAAKlaghW3OVYVMaWLLAeBA",
    "CAACAgUAAxkBAAIGqGp-VKvdNZXSTdVX31pnlCPJArVoAALdGwACYXsIVp5U_CAhCyEfHgQ"
]

IMG = [
"https://files.catbox.moe/4q7c4w.jpg",
"https://files.catbox.moe/90z6sq.jpg",
"https://files.catbox.moe/rdfi4z.jpg",
"https://files.catbox.moe/6f9rgp.jpg",
"https://files.catbox.moe/99wj12.jpg",
"https://files.catbox.moe/ezpnd2.jpg",
"https://files.catbox.moe/e7q55f.jpg",
"https://files.catbox.moe/qyfsi7.jpg",
"https://files.catbox.moe/kbke7s.jpg",
"https://files.catbox.moe/7icvpu.jpg",
"https://files.catbox.moe/4hd77z.jpg",
"https://files.catbox.moe/yn7wje.jpg",
"https://files.catbox.moe/kifsir.jpg",
"https://files.catbox.moe/zi21kc.jpg",
]
