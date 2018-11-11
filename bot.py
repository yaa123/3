#!@atm72bot python
import telebot
TOKEN = '798979267:AAEWbRlo36GcdtkvhM7AQ8psNpnx041nWUk'
bot = telebot.TeleBot(TOKEN)
inputfile = 'errorcode.txt'
sticker_id = 'CAADAgADAQAD0VrUCH5Dfvp5fahZAg'

def file(text):
	myfile = open(inputfile, mode='r', encoding='UTF-8')
	for line in myfile:
		text=text.replace('/','')
		if text in line:
			err = line.strip()
			myfile.close()
			return err
	else:
			err = 'не найдена'
			return err

@bot.message_handler(commands=['start'])	
def command_handler(message):
	bot.reply_to(message, 'Здравствуйте! Этот Бот создан для помощи ннженерам АТМ-Альянс')

@bot.message_handler(commands=['add'])	
def command_handler(message):
	id = message.from_user.id
	text = file(message.text.lower())
	text = text[:2]
	if id == '148134609':
		bot.reply_to(message, 'Ошибка добавлена!', id, text)
	else:
		bot.reply_to(message, 'нет', id)

	
@bot.message_handler(commands=['help'])
def command_handler(message):
	bot.reply_to(message, 'Отправьте мне код ошибки, чтобы получить описание')

@bot.message_handler(commands=['edik'])
def command_handler(message):
	bot.send_sticker(message.chat.id, sticker_id)

@bot.message_handler(content_types=['sticker'])
def test(message):
	bot.reply_to(message, message)
	
@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_digits(message):
	text = file(message.text.lower())
	bot.reply_to(message, ('Ошибка ' + text))

bot.polling(none_stop=True)