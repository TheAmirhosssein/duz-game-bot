import logging

from config import TOKEN
from database.engine import Base, engine
from handlers import start
from telegram.ext import ApplicationBuilder, CommandHandler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


if __name__ == "__main__":
    if TOKEN is None:
        raise ValueError("bot token can not be none")

    Base.metadata.create_all(bind=engine)
    application = ApplicationBuilder().token(TOKEN).build()
    start_handler = CommandHandler("start", start.start)
    application.add_handler(start_handler)

    application.run_polling()
