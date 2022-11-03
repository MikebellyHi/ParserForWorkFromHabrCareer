
import telebot
from HabrParserJuPy import GetLinks
# Указываем токен
bot = telebot.TeleBot('5514669511:AAGHJhHXh0mY8DYZmPrezOct7TFP60BPyhE')
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types


# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Hi':
        links = []
        links += GetLinks()
        for i in range (0, len(links)):
            bot.send_message(message.from_user.id, links[i])
    
       
# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)