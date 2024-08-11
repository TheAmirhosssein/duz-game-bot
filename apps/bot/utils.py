from telegram import Bot
from config import TOKEN


async def send_telegram_message(chat_id: str, message: str, reply_markup=None):
    if TOKEN is None:
        raise Exception("Token bot can not be none")
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=chat_id, text=message, reply_markup=reply_markup)
