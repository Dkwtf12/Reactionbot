from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client
from users import get_user_data, update_user_data, increment_reaction
from reaction import add_reactions

EMOJIS = [
    "👏", "😁", "🎉", "🤩", "🙏", "👌", "🕊", "😍",
    "🐳", "❤", "🔥", "💯", "⚡", "🏆"
]

user_state = {}

async def start_handler(client: Client, message: Message):
    kb = InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Add me to your Channel", url=f"https://t.me/{client.me.username}?startchannel=true")],
        [InlineKeyboardButton("Give Reaction", callback_data="give_reaction")]
    ])
    await message.reply_text(
        f"Hi Sir 👋\nI am your Reaction Assistant! ❤️",
        reply_markup=kb
    )

async def callback_handler(client: Client, callback_query: CallbackQuery):
    data = callback_query.data
    if data == "give_reaction":
        buttons = [InlineKeyboardButton(e, callback_data=f"emoji_{e}") for e in EMOJIS]
        kb = InlineKeyboardMarkup([buttons[i:i + 4] for i in range(0, len(buttons), 4)])
        await callback_query.message.reply("Choose your emoji:", reply_markup=kb)
    elif data.startswith("emoji_"):
        emoji = data.split("_", 1)[1]
        user_state[callback_query.from_user.id] = {"emoji": emoji}
        await callback_query.message.reply("Send me the message link to react to:")

async def reaction_flow_handler(client: Client, message: Message):
    uid = message.from_user.id
    if uid not in user_state:
        return await message.reply("Use 'Give Reaction' first.")

    state = user_state[uid]

    if "link" not in state:
        state["link"] = message.text
        await message.reply("How many reactions to add?")
    else:
        try:
            count = int(message.text)
            link = state["link"]
            emoji = state["emoji"]
            parts = link.split("/")
            chat_username = parts[-2]
            msg_id = int(parts[-1])
            chat = await client.get_chat(chat_username)
            result = await add_reactions(client, chat.id, msg_id, emoji, count)
            if result:
                increment_reaction(uid, emoji, count)
                await message.reply("✅ Reaction added! Check your channel.")
            else:
                await message.reply("❌ Failed to add reactions.")
        except:
            await message.reply("Invalid input. Start again.")
        finally:
            user_state.pop(uid, None)
