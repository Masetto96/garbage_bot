import schedule
import time
from telegram.ext import Updater, CommandHandler
import logging

from secrets import token

garbage_status = False

updater = Updater(token, use_context=True)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
def done():
    global garbage_status
    updater.bot.send_message(chat_id=-443613216, text="thanks next time do it a bit quicker")
    garbage_status = True

garbage_is_out_handler = CommandHandler('done', done)

updater.dispatcher.add_handler(garbage_is_out_handler)

def job():
    global garbage_status
    updater.start_polling()
    updater.bot.send_message(chat_id=-443613216, text="it is sunday get your shit together and put out the garbage")

    while not garbage_status:
        updater.bot.send_message(chat_id=-443613216, text="lazy ass take out the garbage")
        time.sleep(10)

    updater.stop()
    garbage_status = False






    updater.stop()
schedule.every().sunday.at("16:41").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
