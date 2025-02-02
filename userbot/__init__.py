# created by santhu
# created on: 2-2-2025

#pyrogram imports
from pyrogram import Client
from pyrogram import idle

#manual imports 
import asyncio 
import os
from config import API_ID, API_HASH, SESSION


user = Client(
          ":memory:", 
          api_id=API_ID, 
          api_hash=API_HASH, 
          session_string=str(SESSION), 
          in_memory=True, 
) 