import telebot

TOKEN = "5473022753:AAE85Vdaluw_a6VzWbAa1F-2wq9Jegd8kTQ"

bot = telebot.TeleBot(token=TOKEN)

@bot.message_handler(commands=['start']) 
def bot_starting(message):
    bot.send_message(message.chat.id,"Привет!")


