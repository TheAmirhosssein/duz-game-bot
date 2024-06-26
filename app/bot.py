import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import dotenv_values

config = dotenv_values(".env")

TOKEN = config.get("BOT_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat is not None:
        start_message = (
            "🎮 Welcome to Duz! 🎲\n\n"
            "Introducing Duz, a captivating Telegram app/game inspired by the traditional Persian game 'Duz.' "
            "This project leverages the power of Python and PostgreSQL to deliver a more enjoyable experience "
            "than the classic game of Tic-Tac-Toe (XO).\n\n"
            "Are you ready to embark on this exciting gaming adventure? Let's play Duz!"
        )
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text=start_message
        )


if __name__ == "__main__":
    if TOKEN is None:
        raise ValueError("bot token can not be none")

    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    application.run_polling()
