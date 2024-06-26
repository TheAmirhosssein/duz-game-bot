from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat is not None:
        start_message = (
            "🎮 Welcome to Duz! 🎲\n\n"
            "Introducing Duz, a captivating Telegram app/game inspired by the traditional Persian game 'Duz.' "
            "This project leverages the power of Python and PostgreSQL to deliver a more enjoyable experience "
            "than the classic game of Tic-Tac-Toe (XO).\n\n"
            "Are you ready to embark on this exciting gaming adventure? Let's play Duz!"
            "\n(Please Excuse Me VANIA)"
        )
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text=start_message
        )
