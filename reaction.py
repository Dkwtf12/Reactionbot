import asyncio
from pyrogram import Client
from pyrogram.raw.functions.messages import SendReaction
from pyrogram.raw.types import ReactionEmoji  # ✅ required for correct reaction type

async def add_reactions(bot: Client, chat_id: int, msg_id: int, emoji: str, count: int):
    try:
        peer = await bot.resolve_peer(chat_id)
        for _ in range(count):
            await bot.invoke(SendReaction(
                peer=peer,
                msg_id=msg_id,
                reaction=[ReactionEmoji(emoticon=emoji)]  # ✅ correct type
            ))
            await asyncio.sleep(0.3)  # Prevent floodwait
    except Exception as e:
        raise Exception(f"Error sending reactions: {e}")
    return True
