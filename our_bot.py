from telegram import update
from datetime import date, time
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def start(context) -> None:
    """Send a message when the command /start is issued."""
    context.bot.send_message(chat_id=-443613216, text="Hi, I am back bitches")
    bot.send_photo(chat_id=-443613216, photo=open("squanchy.png", "rb"))






def main():
    today = date.today()
    updater = Updater("", use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("ciao", start))
    #dispatcher.add_handler(CommandHandler("help", help_command))

    if today.weekday() == 6:
        bot.send_message(chat_id=-443613216, text="More and more bullshit coming")

        #bot.send_message(chat_id=-, text="Today is Sunday. Bring out the trash please")
        #bot.send_document(chat_id=-, document=open("calendar.pdf", "rb"))
        #bot.send_dice(chat_id=-)
        #bot.pin_chat_mupdater = Updater("TOKEN", use_context=True)essage(chat_id=-443613216, message_id=)


    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
