import asyncio
from pyrogram import Client
from pyrogram.raw.functions.messages import SendReaction

async def add_reactions(bot: Client, chat_id: int, msg_id: int, emoji: str, count: int):
    try:
        peer = await bot.resolve_peer(chat_id)
        for _ in range(count):
            await bot.invoke(SendReaction(
                peer=peer,
                msg_id=msg_id,
                reaction=[emoji]
            ))
            await asyncio.sleep(0.3)  # Prevent FloodWait
    except Exception as e:
        raise Exception(f"Error sending reactions: {e}")
    return True
