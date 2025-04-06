import telebot
import sqlite3
from telebot import types
from HackCaesar import hackcaesar
from Caesar import caesar
from Vernam import vernam
from Viegener import viegener

methods = 0
languages = ''
type = 0
key = ''
messages = ''
data = dict()

bot = telebot.TeleBot('6338986593:AAEL7iPoeftAHb9gQpSD1RTZRZASyWXA1CQ')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     'Чтобы начать работу с ботом введите капчу "QWERTY123"',)
    bot.register_next_step_handler(message, next)
def next(message):
    if message.text == "QWERTY123":
         bot.send_message(message.chat.id,'Введите /menu чтобы войти в главное меню пользователя')
    elif message.text != "QWERTY123":
        markup1 = types.ReplyKeyboardMarkup(row_width=2)
        itembtn3 = types.KeyboardButton('Неправильный ввод, ввести капчу еще раз (Нажмите на кнопку, чтобы ввести капчу еще раз)')
        markup1.add(itembtn3)
        bot.send_message(message.chat.id,
                         'Введите капчу еще раз',
                         reply_markup=markup1)


@bot.message_handler(commands=['menu'])
def menu(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    itembtn1 = types.InlineKeyboardButton('Все зашифрованные сообщения', callback_data='info')
    markup.add(itembtn1)
    photomessage = bot.get_user_profile_photos(message.chat.id)
    bot.send_photo(message.chat.id, photomessage.photos[0][0].file_id, caption=f"{message.from_user.first_name}, это главное меню пользователя, здесь вы можете посмотреть информацию"
                                                                              f" о зашифрованных сообщениях",reply_markup=markup)
    markup1 = types.ReplyKeyboardMarkup(row_width=2)
    itembtn3 = types.KeyboardButton('Начать работу с ботом')
    markup1.add(itembtn3)
    bot.send_message(message.chat.id,
                     'Чтобы начать работу с ботом нажмите на кнопку "Начать работу с ботом"',
                     reply_markup=markup1)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'info':
            bot.send_message(call.message.chat.id, 'Ваши закодированные сообщения:')
            con1 = sqlite3.connect('info.sql')
            cur1 = con1.cursor()
            cur1.execute('CREATE TABLE IF NOT EXISTS info (key varchar(30), code varchar(30))')
            cur1.execute('SELECT * FROM info')
            info = ''
            for i in cur1.fetchall():
                info += f'Ключ: {i[0]}, Зашифрованое сообщение: {i[1]}\n'
            bot.send_message(call.message.chat.id, info)
            con1.commit()
            cur1.close()
            con1.close()
        if call.data == 'users':
            con = sqlite3.connect('users.sql')
            cur = con.cursor()
            cur.execute('SELECT * FROM usernames')
            userinfo = ''
            for i in cur.fetchall():
                userinfo += f'Имя пользователя: {i[0]}, пароль: {i[1]}\n'
            bot.send_message(call.message.chat.id, userinfo)
            cur.close()
            con.close()

@bot.message_handler()
def start(message):
    if message.text == 'Неправильный ввод, ввести капчу еще раз (Нажмите на кнопку, чтобы ввести капчу еще раз)':
        bot.register_next_step_handler(message, nod)
    if message.text == 'Начать работу с ботом':
        con1 = sqlite3.connect('info.sql')
        cur1 = con1.cursor()
        cur1.execute('CREATE TABLE IF NOT EXISTS info (key varchar(30), code varchar(30))')
        cur1.execute('SELECT * FROM info')
        con1.commit()
        cur1.close()
        con1.close()
        bot.send_message(message.chat.id,'Введите язык')
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('English (Английский язык)')
        itembtn2 = types.KeyboardButton('Russian (Русский язык)')
        markup.add(itembtn1, itembtn2)
        bot.send_message(message.chat.id,f'Для начала работы выберите язык сообщения, которое вы хотите'
                                     f' зашифровать, дешифровать', reply_markup=markup)
        bot.register_next_step_handler(message, language)
def nod(message):
    if message.text == "QWERTY123":
        bot.send_message(message.chat.id, 'Введите /menu чтобы войти в главное меню пользователя')
    elif message.text != "QWERTY123":
        bot.send_message(message.chat.id, 'Введите капчу еще раз')
        bot.register_next_step_handler(message, start)
def language(message):
    global languages
    if message.text == 'English (Английский язык)':
        languages = 'EU'
    elif message.text == 'Russian (Русский язык)':
        languages = 'RU'
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('encryption (Шифрование)')
    itembtn2 = types.KeyboardButton('decryption (Дешифрование)')
    itembtn3 = types.KeyboardButton('hack (Взлом шифра Цезаря)')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id,
                     'Теперь выбери тип работы шифровальщика)', reply_markup=markup)
    bot.register_next_step_handler(message, typer)
def typer(message):
    global type
    if message.text == 'encryption (Шифрование)':
        type = 1
    elif message.text == 'decryption (Дешифрование)':
        type = -1
    elif message.text == 'hack (Взлом шифра Цезаря)':
        type = 3
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Метод Цезаря')
    itembtn2 = types.KeyboardButton('Метод Вернама')
    itembtn3 = types.KeyboardButton('Метод Виженера')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id,
                     'Теперь выбери метод шифрования (Цезарь/Вернам/Виженера)',
                     reply_markup=markup)
    bot.register_next_step_handler(message, method)
def method(message):
    global methods
    if message.text == 'Метод Цезаря':
        methods = 1
    elif message.text == 'Метод Вернама':
        methods = 2
    elif message.text == 'Метод Виженера':
        methods = 3
    bot.send_message(message.chat.id, 'Теперь введи сообщение для шифрования/дешифрования:')
    bot.register_next_step_handler(message, mess)
def mess(message):
    global messages, methods, type
    messages = message.text
    if methods == 1:
        if type == 3:
            markup = types.ReplyKeyboardMarkup(row_width=2)
            itembtn1 = types.KeyboardButton('Начать взлом')
            markup.add(itembtn1)
            bot.send_message(message.chat.id,
                             'Сообщение готово ко взлому',
                             reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Теперь введи ключ для шифрования/дешифрования (В методе Цезаря ключами являются числа):')
    if methods == 2:
        if type == 1:
            markup = types.ReplyKeyboardMarkup()
            itembtn1 = types.KeyboardButton('ok')
            markup.add(itembtn1)
            bot.send_message(message.chat.id,
                             'Для шифрования методом Вернама не требуется вводить пользовательский ключ',
                             reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Теперь введи ключ для шифрования/дешифрования')
    if methods == 3:
        bot.send_message(message.chat.id,
                         'Теперь введи ключ для шифрования/дешифрования (В методе Виженера ключами являются различные слова)')
    bot.register_next_step_handler(message, shifr)
def shifr(message):
    global key, messages, methods, type, languages
    key = message.text
    if methods == 1:
        if type == 3:
            bot.send_message(message.chat.id, 'Взломанный текст:')
            bot.send_message(message.chat.id,hackcaesar(messages,languages))
        else:
            bot.send_message(message.chat.id,'Зашифрованный/Дешифрованный текст')
            bot.send_message(message.chat.id,caesar(messages,int(key) * type,languages))
            data[key] = caesar(messages,int(key) * type,languages)
    if methods == 2:
        if type == 1:
            bot.send_message(message.chat.id, 'Зашифрованный/Дешифрованный текст')
            ans2,ans1 = vernam(languages,messages,type)
            bot.send_message(message.chat.id, ans1)
            bot.send_message(message.chat.id, 'Ваш код:')
            bot.send_message(message.chat.id, ans2)
            key = ans2
            data[key] = ans1
        else:
            bot.send_message(message.chat.id, 'Зашифрованный/Дешифрованный текст')
            bot.send_message(message.chat.id, viegener(languages,key,messages,type))
    if methods == 3:
        bot.send_message(message.chat.id, 'Зашифрованный/Дешифрованный текст')
        bot.send_message(message.chat.id, viegener(languages,key,messages,type))
        data[key] = viegener(languages,key,messages,type)
    if type == 1:
        con1 = sqlite3.connect('info.sql')
        cur1 = con1.cursor()
        cur1.execute('INSERT INTO info (key, code) VALUES("%s","%s")' % (key, data[key]))
        con1.commit()
        cur1.close()
        con1.close()
    bot.send_message(message.chat.id,'Чтобы посмотреть информацию о пользователе или о закодированном тексте, введите команду /menu')
    markup1 = types.ReplyKeyboardMarkup(row_width=2)
    itembtn3 = types.KeyboardButton('Начать работу с ботом')
    markup1.add(itembtn3)
    bot.send_message(message.chat.id,
                     'Чтобы начать работу с ботом нажмите на кнопку "Начать работу с ботом"',
                     reply_markup=markup1)

bot.infinity_polling()