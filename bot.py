#!/usr/bin/env python
import telebot
TOKEN = '798979267:AAEWbRlo36GcdtkvhM7AQ8psNpnx041nWUk'
bot = telebot.TeleBot(TOKEN)
inputfile = 'errorcode.txt'
myfile = open(inputfile, mode='r', encoding='UTF-8')
@bot.message_handler(commands=['start'])
def command_handler(message):
	bot.reply_to(message, 'Здравствуйте! Этот Бот создан для помощи ннженерам АТМ_Альянс')
	pass
@bot.message_handler(commands=['help'])
def command_handler(message):
	bot.reply_to(message, 'Помощь')
	pass
@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_digits(message):
	text = message.text.lower()
	for line in myfile:
		if text in line:
			bot.reply_to(message, ('Ошибка ' + line.strip()))
			pass
bot.infinity_polling(True)