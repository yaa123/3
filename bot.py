#!/usr/bin/env python
import telebot
from telebot import types
from telebot.types import Message
TOKEN = '798979267:AAEWbRlo36GcdtkvhM7AQ8psNpnx041nWUk'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def command_handler(message):
    bot.reply_to(message, 'Здравствуйте! Этот Бот создан для помощи ннженерам АТМ_Альянс')

@bot.message_handler(commands=['help'])
def command_handler(message):
    bot.reply_to(message, 'Помощь')
	
@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_digits(message: Message):
	bot.reply_to(message, 'test')	

@bot.message_handler(commands=['ошибка'])
def error (message):
	bot.reply_to(message, 'ошибка')
	
	
bot.polling(timeout=60)
