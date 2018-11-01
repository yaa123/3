#!/usr/bin/env python
import telebot


TOKEN = '798979267:AAEWbRlo36GcdtkvhM7AQ8psNpnx041nWUk'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
	pass


bot.polling(timeout=60)
