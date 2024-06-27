import logging

from config import TOKEN
from database.engine import Base, engine
from bot import handlers
from telegram.ext import ApplicationBuilder, CommandHandler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


if __name__ == "__main__":
    if TOKEN is None:
        raise ValueError("bot token can not be none")

    Base.metadata.create_all(bind=engine)
    application = ApplicationBuilder().token(TOKEN).build()
    start_handler = CommandHandler("start", handlers.start)
    application.add_handler(start_handler)
    matchup_handler = CommandHandler("match_up", handlers.match_up)
    application.add_handler(matchup_handler)

    application.run_polling()
