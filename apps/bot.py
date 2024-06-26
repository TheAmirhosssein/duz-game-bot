import logging

from dotenv import dotenv_values
from telegram.ext import ApplicationBuilder, CommandHandler

from handlers import start

config = dotenv_values(".env")

TOKEN = config.get("BOT_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


if __name__ == "__main__":
    if TOKEN is None:
        raise ValueError("bot token can not be none")

    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler("start", start.start)
    application.add_handler(start_handler)

    application.run_polling()
