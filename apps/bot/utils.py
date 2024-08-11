from telegram import Bot
from config import TOKEN
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo


async def send_telegram_message(chat_id: str, message: str, reply_markup=None):
    if TOKEN is None:
        raise Exception("Token bot can not be none")
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=chat_id, text=message, reply_markup=reply_markup)


async def create_game_link(link: str | None) -> InlineKeyboardMarkup | None:
    if link is None:
        return None
    buttons = [
        [
            InlineKeyboardButton(
                "open the game",
                web_app=WebAppInfo(link),
            )
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    return reply_markup
