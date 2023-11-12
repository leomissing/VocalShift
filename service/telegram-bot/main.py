import environ
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

env = environ.Env(BOT_API_TOKEN=((str, "")))
#initialize API token - Telegram
telegram_token = env("BOT_API_TOKEN")



async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token(telegram_token).build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()