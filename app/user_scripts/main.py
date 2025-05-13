from pyrogram import filters
from pyrogram.types.messages_and_media import Message

from app import Client, get_bot


TARGET = [-1002343015438, -1002662489774]


@Client.on_message(filters.chat(TARGET))
async def bot_trans(client: Client, message: Message):
    bot = get_bot()
    await bot.send_message(
        chat_id=-1002622414580,
        text=message.caption if message.caption else message.text,
    )
