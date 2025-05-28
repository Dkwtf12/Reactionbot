import logging
from pyrogram import Client, filters
from pyrogram.types import Message
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID
from handlers import start_handler, callback_handler, reaction_flow_handler
from admin import broadcast_handler

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = Client("reaction-bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Handlers
app.add_handler(filters.command("start") & filters.private, start_handler)
app.add_handler(filters.command("broadcast") & filters.user(OWNER_ID), broadcast_handler)
app.add_handler(filters.text & filters.private, reaction_flow_handler)
app.add_handler(filters.callback_query, callback_handler)

logger.info("Bot is running...")
app.run()
