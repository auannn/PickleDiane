import telebot
import random
import os

TOKEN = none

# Создайте бота
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ["start"])
def start_cmd(message):
    bot.send_message(message.chat.id,"Привет я твой бот!")

@bot.message_handler(commands = ["info"])
def start_cmd(message):
    bot.send_message(message.chat.id,"Бот создан @vloov_q")

@bot.message_handler(commands = ["funfact"])
def funfacts(message):
    facts = [
        "На самом деле Даен не огурец, а морковь",
        "Рик с-137 искал Рика Прайма 24 лет",
        "Морти считается аутистом"
    ]
    fact = random.choice(facts)
    bot.send_message(message.chat.id, "Интересный факт:\n " + fact)




print("Бот работает ...")
bot.infinity_polling() # Запуск бота
