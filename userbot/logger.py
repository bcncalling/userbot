import logging
import os

if not os.path.exists("logs"):
    os.makedirs("logs")

LOG_FILE = "userbotlog.txt"

logging.basicConfig(
    level=logging.INFO,  
    format="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),  
        logging.StreamHandler()  
    ]
)

LOGGER = logging.getLogger("userbot")

logging.getLogger("pyrogram").setLevel(logging.WARNING)  
 