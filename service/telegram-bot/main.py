from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

#initialize API token - Telegram
telegram_token = env("BOT_API_TOKEN")
#creating objects to perform a task
updater = Updater(telegram_token, use_context=True)
dispatcher = updater.dispatcher

#

def start(update, context):
  update.message.reply_text('Hello! Welcome to VocalShift BOT! Enjoy your ride!')
  update.message.reply_text('Type /help for the content to display!')
  update.message.reply_text('Happy Learning!')

def help(update, context):
  update.message.reply_text("HELP! I NEED SOMEBODY HELP, NOT JUST ANYBODY")
  update.message.reply_text('Just joking, here is list of command you can use:')



updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))

updater.start_polling()  # Start the bot
updater.idle()  # Wait for the script to be stopped; this will stop the bot