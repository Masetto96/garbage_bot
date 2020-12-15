import schedule
import time
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update
import logging

from secrets import token


def done(update: Update, context: CallbackContext) -> None:
    global garbage_status
    garbage_status = True
    updater.bot.send_message(chat_id=-443613216, text="thanks (Y)")



def job():
    global garbage_status
    updater.start_polling()
    #updater.bot.send_message(chat_id=-443613216, text="it is sunday get your shit together and put out the garbage")

    while not garbage_status:
        updater.bot.send_message(chat_id=-443613216, text="lazy ass take out the garbage")
        time.sleep(200)







garbage_status = False


updater = Updater(token)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


garbage_is_out_handler = CommandHandler('done', done)
updater.dispatcher.add_handler(garbage_is_out_handler)


schedule.every().sunday.at("19:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
