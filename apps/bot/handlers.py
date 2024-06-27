from database.match_up import create_match_up
from database.users import create_user, get_user
from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("na")
    if update.effective_chat is not None:
        if (
            update.message is not None
            and (user_info := update.message.from_user) is not None
        ):
            user = await get_user(str(user_info.id))
            if user is None:
                await create_user(name=user_info.full_name, username=str(user_info.id))

            start_message = (
                f"🎮 Welcome to Duz Dear {user_info.full_name}! 🎲\n\n"
                "Introducing Duz, a captivating Telegram app/game inspired by the traditional Persian game 'Duz.' "
                "This project leverages the power of Python and PostgreSQL to deliver a more enjoyable experience "
                "than the classic game of Tic-Tac-Toe (XO).\n\n"
                "Are you ready to embark on this exciting gaming adventure? Let's play Duz!"
                "\n(Please Excuse Me VANIA)"
            )
            await context.bot.send_message(
                chat_id=update.effective_chat.id, text=start_message
            )


async def match_up(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("na")
    if update.effective_chat is not None:
        if (
            update.message is not None
            and (user_info := update.message.from_user) is not None
        ):
            user = await get_user(str(user_info.id))
            assert user is not None
            await create_match_up(user)
            message = "until 30 seconds later we will find you a match! 🎲\n\n"
            await context.bot.send_message(
                chat_id=update.effective_chat.id, text=message
            )
