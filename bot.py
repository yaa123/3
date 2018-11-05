#!/usr/bin/env python
import telebot
TOKEN = '798979267:AAEWbRlo36GcdtkvhM7AQ8psNpnx041nWUk'
bot = telebot.TeleBot(TOKEN)
inputfile = 'errorcode.txt'
myfile = open(inputfile, mode='r', encoding='UTF-8')

@bot.message_handler(commands=['start'])
def command_handler(message):
	bot.reply_to(message, 'Здравствуйте! Этот Бот создан для помощи ннженерам АТМ_Альянс')

@bot.message_handler(commands=['help'])
def command_handler(message):
	bot.reply_to(message, 'Помощь')


@bot.message_handler(content_types=['text'])
def error (message):
	text = message.text.lower()
	for line in myfile:
		if text in line:
			bot.reply_to(message, 'ошибка' + line.strip())

@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_digits(message):
	bot.reply_to(message, 'test')	

bot.polling(timeout=60)
