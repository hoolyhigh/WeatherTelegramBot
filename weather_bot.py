import telebot
import sys

TOKEN = '213675554:AAEHHFkB-NCFt0evRhfoodeL3SOIIEfDGNQ'
dest = '@clima_rio'

bot = telebot.TeleBot(TOKEN)

bot.send_message(dest, "I'M ALIVE!!") # dest and msg
