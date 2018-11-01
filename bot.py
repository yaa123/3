#!/usr/bin/env python
import telebot
from telebot import types
from telebot.types import Message
TOKEN = '798979267:AAEWbRlo36GcdtkvhM7AQ8psNpnx041nWUk'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def echo_digits(message: Message):
bot.reply_to(message, 'test')
	return


bot.polling(timeout=60)
