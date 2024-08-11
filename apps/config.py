from dotenv import dotenv_values

config = dotenv_values(".env")

TOKEN = config.get("BOT_TOKEN")
DATABASE_URL = config.get("DATABASE_URL")
GAME_LINK = config.get("GAME_LINK")
