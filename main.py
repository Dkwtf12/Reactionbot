import logging
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
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

# Register handlers properly
app.add_handler(MessageHandler(start_handler, filters.command("start") & filters.private))
app.add_handler(MessageHandler(broadcast_handler, filters.command("broadcast") & filters.user(OWNER_ID)))
app.add_handler(MessageHandler(reaction_flow_handler, filters.text & filters.private))
app.add_handler(CallbackQueryHandler(callback_handler))  # Correct usage

logger.info("Bot is running...")
app.run()
