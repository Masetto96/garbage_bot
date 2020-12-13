from telegram import Update
import time
from datetime import date
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


#bot = telegram.Bot(token='')


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def garbage_flag(optio=False):
    if optio:
        return True
    return False

def garbage_out(update: Update, context: CallbackContext) -> None:
    garbage_flag(optio=True)
    update.message.reply_text("I thank you for the collaboration")


def help(update: Update, context: CallbackContext) -> None:
    #update.reply_text("If you dont know how this works go ask Jakob")
    update.message.reply_text("If you dont know how this works go ask Jakob")





updater = Updater("", use_context=True)
bot = updater.bot

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(CommandHandler("done", garbage_out))
today = date.today()
print(garbage_flag())
if today.weekday() == 0:
    while garbage_flag() == False:
        print("looping again")
        updater.start_polling()
        time.sleep(20)
        print("sending reminder")
        bot.send_message(chat_id=-443613216, text="Please bring the garbage out (I know its not Sunday, this is just a test ;)")
print("FINITO")







updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
updater.idle()
