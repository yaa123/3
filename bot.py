#!@atm72bot python
import telebot
from datetime import datetime
TOKEN = '798979267:AAEWbRlo36GcdtkvhM7AQ8psNpnx041nWUk'
bot = telebot.TeleBot(TOKEN)
inputfile = 'errorcode.txt'
sticker_id = 'CAADAgADAQAD0VrUCH5Dfvp5fahZAg'
sp_id=[148134609,205821042,229932251]
isRunning=False

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

def log(a,id):
	with open('log.txt','a') as f:
		a[0]=str(datetime.now())
		a[1]=id
		f.write(str(a)+'\n')

@bot.message_handler(commands=['start'])	
def command_handler(message):
	bot.reply_to(message, 'Здравствуйте! Этот Бот создан для помощи ннженерам АТМ-Альянс')

@bot.message_handler(commands=['add'])	
def command_handler_add(message):
	id = message.from_user.id
	text = message.text.lower()
	text = text[4:]
	if id == 148134609:
		myfile = open(inputfile, mode='a')
		myfile.write('\n' + text)
		myfile.close()
		bot.reply_to(message, 'Ошибка добавлена:' + text)
	else:
		bot.reply_to(message, 'Вы не можете добавлять ошибки!' )

@bot.message_handler(commands=['ot'])
def start_handler(message):
    global isRunning
    if not isRunning:
		id = message.from_user.id
        chat_id = message.chat.id
        text = message.text
		if id in sp_id:
			msg = bot.send_message(chat_id, 'Введите кличество полученных заявок')
			bot.register_next_step_handler(msg, ask1)
			isRunning = True
		else:
		bot.reply_to(message, 'Иди нахуй!' )
			isRunning = False

def ask1(message):
    chat_id = message.chat.id
    text = message.text
    if not text.isdigit():
        msg = bot.send_message(chat_id, 'Должно быть число, введите ещё раз.')
        bot.register_next_step_handler(msg, ask1)
        return
    msg = bot.reply_to(chat_id, 'Принято')
	a[2]=text
    isRunning = True
	bot.register_next_step_handler(msg, ask2)

def ask2(message):
    chat_id = message.chat.id
    text = message.text
    if not text.isdigit():
        msg = bot.send_message(chat_id, 'Должно быть число, введите ещё раз.')
        bot.register_next_step_handler(msg, ask2)
        return
    msg = bot.reply_to(chat_id, 'Принято')
	a[3]=text
    isRunning = True
	bot.register_next_step_handler(msg, ask1)

def ask3(message):
    chat_id = message.chat.id
    text = message.text
    if not text.isdigit():
        msg = bot.send_message(chat_id, 'Должно быть число, введите ещё раз.')
        bot.register_next_step_handler(msg, ask2)
        return
    msg = bot.reply_to(chat_id, 'Принято')
	a[4]=text
    isRunning = False
	x=log(a,id)

@bot.message_handler(commands=['ot'])	
def command_handler_otchet(message):
	id = message.from_user.id
	text = message.text.lower()
	text = text[4:]
	if id in sp_id:
		x=log(text,id)
		bot.reply_to(message, 'Принято' )
	else:
		bot.reply_to(message, 'Иди нахуй!' )

@bot.message_handler(commands=['get'])	
def command_handler_get(message):
	id = message.from_user.id
	if id == 148134609:
		doc = open('log.txt', 'rb')
		bot.send_document(message.chat.id, doc)
	else:
		bot.reply_to(message, 'Вы не можете добавлять ошибки!' )

@bot.message_handler(commands=['help'])
def command_handler_hel(message):
	bot.reply_to(message, 'Отправьте мне код ошибки, чтобы получить описание')

@bot.message_handler(commands=['edik'])
def command_handler_ed(message):
	bot.send_sticker(message.chat.id, sticker_id)

@bot.message_handler(content_types=['sticker'])
def sti(message):
	bot.reply_to(message, message)



@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def err(message):
	text = file(message.text.lower())
	bot.reply_to(message, ('Ошибка ' + text))

bot.polling(none_stop=True)