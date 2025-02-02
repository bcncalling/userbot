import os
import asyncio
from sys import exit as SystemExit 
from userbot.logger import LOGGER
from userbot import user 
from pyrogram import idle

try:
    from config import API_ID, API_HASH, BOT_TOKEN, SESSION
except ImportError:
    LOGGER.error("config.py not found or missing required variables!")
    raise SystemExit("Please ensure `config.py` exists and contains API_ID, API_HASH, BOT_TOKEN, and SESSION.")

from userbot.modules import load_modules
load_modules()

async def check_userbot_status():
    if user._is_running:
        LOGGER.info("userbot has started successfully.")
        print("userbot started successfully.")
    else:
        LOGGER.error("userbot failed to start.")
        print("userbot failed to start.")

async def main():
    LOGGER.info("Starting user Bot...")
    await user.start()
    
    try:
        await user.start()
        await check_userbot_status()
    except Exception as e:
        LOGGER.error(f"Failed to start userbot: {e}")
        print(f"Error: {e}")
        raise SystemExit("userbot failed to start.")

    LOGGER.info("user Bot has started successfully!")
    print("Bot started successfully.")
    await idle()
    await user.stop()
    LOGGER.info("user Bot has stopped.")

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        LOGGER.error("Bot stopped manually.")
    except SystemExit:
        LOGGER.error("System exit encountered.")
    except Exception as e:
        LOGGER.error(f"An unexpected error occurred: {e}")
        import sys
        sys.exit(1)