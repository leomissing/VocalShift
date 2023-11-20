import environ
import logging

from telegram import ForceReply, Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (Application, CommandHandler,
                          ContextTypes, MessageHandler,
                          filters,     ConversationHandler, CallbackQueryHandler)

env = environ.Env(BOT_API_TOKEN=(str, ""))


# initialize API token - Telegram
telegram_token = env("BOT_API_TOKEN")


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

BEGIN, AUDIO, RUN = range(3)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hello {user.mention_html()}! Send me audio"
    )
    return AUDIO


async def begin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """"""
    await update.message.reply_text("Send me Audio!")
    return AUDIO


async def run_model(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """"""
    logger.info(f"I got {update.message.text}")
    await update.message.reply_text(f"You choose {update.message.text}. I will do all work now! Just chill and wait")
    await update.message.reply_text(f"Some results from our model!")
    await update.message.reply_text("Send me anoter Audio!")
    return AUDIO


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """"""
    await update.message.reply_text("Help! I need somebody HELP!")


async def echo_audio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Echo the user message."""
    if not update.message.audio or not update.message.audio.file_id:
        await update.message.reply_text("Please, send me valid audio")
        return AUDIO

    # if update.message.audio and update.message.audio.file_id:
    await update.message.reply_audio(update.message.audio.file_id)

    reply_keyboard = [["Sexy", "Angry", "Lovely"]]

    await update.message.reply_text(
        "Please choose voice for shifting",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder="What type of voice you want?"
        ),
    )
    return RUN


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    logger.info(f"I got {update.message.text}")
    await update.message.reply_text(update.message.text)
    return RUN


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        "Bye! I hope we can talk again some day.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(telegram_token).build()

    # on different commands - answer in Telegram
    # application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    # application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    # application.add_handler(MessageHandler(filters.ATTACHMENT, echo_audio))

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start), ],
        states={
            BEGIN: [MessageHandler(filters.ALL, begin)],
            AUDIO: [MessageHandler(filters.ATTACHMENT, echo_audio)],
            RUN: [MessageHandler(filters.Regex("^(Sexy|Angry|Lovely)$"), run_model)],
        },
        fallbacks=[CommandHandler("cancel", cancel), MessageHandler(filters.ALL, begin)],
    )
    application.add_handler(conv_handler)
    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
