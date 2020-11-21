import logging
import telegram.ext
from telegram import Update

import telegram
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, DispatcherHandlerStop
import time
from datetime import date



# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def unknown_command(update, context):
    update.message.reply_text(text="Sorry, I didn't understand that command.")

def greetings(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /ciao is issued."""
    update.message.reply_text('Ciao! I am Squanchy, your sex slave. Stefano is playing with me!')

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help! We all need help. It would be nice to have some other bots to count on.')

def trash_alarm(bot: telegram.Bot) -> None:
    context.bot.send_message(job.context, text='Sunday! Bring the garbage OUT please and update me when you are done')


def call_stop(update: Update, context: CallbackContext):
    update.message.reply_text('Thanks, I feel relieved.')
    raise DispatcherHandlerStop(trash_alarm)




def main():

    #updater = Updater('1269026033:AAEhLjwfUXgxZgCeBn_760qTE_lFYC2I2AY', use_context=True)
    bot = telegram.Bot('1269026033:AAEhLjwfUXgxZgCeBn_760qTE_lFYC2I2AY')
    chat_id = update.message.chat_id

    today = date.today()

    if today.weekday() == 5:
        bot.send_message(chat_id, text = "Sunday! Bring the garbage OUT please and update me when you are done")






    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher


    done_handler = CommandHandler("done", call_stop)
    help_handler = CommandHandler("help", help_command)
    dispatcher.add_handler(CommandHandler("trashout", trash_alarm))
    dispatcher.add_handler(CommandHandler("ciao", greetings))
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(done_handler)
    dispatcher.add_handler(MessageHandler(Filters.command, unknown_command))


    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
   main()


#job_minute.enabled = False  # Temporarily disable this job
#job_minute.schedule_removal()  # Remove this job completely
# userid 802610057
