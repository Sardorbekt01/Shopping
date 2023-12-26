import shopapp
import telebot 
from telebot.types import Message


BOT_TOKEN = '6862950696:AAEfrSDX1k1KFkgVRsHZRQ54u4cWmqk6FkE'

bot = telebot.TeleBot(BOT_TOKEN)
bot.message_handler(commands=['start'])
def start_handler(msg:Message):
    bot.send_message(msg.chat.id,"Shop botga xush kelibsiz")
