import telegram
from datetime import date



bot = telegram.Bot(token='1269026033:AAEhLjwfUXgxZgCeBn_760qTE_lFYC2I2AY')
#bot.send_photo(chat_id=-443613216, photo=open("gio.jpg", "rb"))
bot.send_message(chat_id=-443613216, text="Some more testing")
#bot.send_document(chat_id=-443613216, document="calendar.pdf")
