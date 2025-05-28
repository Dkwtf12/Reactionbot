from pyrogram import Client, filters
from pyrogram.types import Message
from config import OWNER_ID
import json

@Client.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast_handler(client: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply("Usage: /broadcast <message>")
    text = message.text.split(None, 1)[1]
    with open("users.json", "r") as f:
        users = json.load(f)

    success, failed = 0, 0
    for uid in users:
        try:
            await client.send_message(int(uid), text)
            success += 1
        except:
            failed += 1
    await message.reply(f"✅ Broadcast done.\nSuccess: {success}\nFailed: {failed}")
