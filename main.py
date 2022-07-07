from extensions import Converter
from extensions import ApiException
import telebot
from config import *
import traceback


bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start', 'help', 'cho_delat'])
def start(message: telebot.types.Message):
    text = "Здравствуйте! Я спец бот по конвертации! Вводите сообщение в виде <конвертируемая валюта>, <валюта в" \
           "которую конвертируем> и количество!"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in exchanges.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):

        values = message.text.split(' ')
        try:
            if len(values) != 3:
                raise ApiException('Неверное количество параметров!')

            resultation1 = Converter.get_price(*values)
        except ApiException as e:
            bot.reply_to(message, f"Ошибка в команде:\n{e}")
        except Exception as e:
            traceback.print_tb(e.__traceback__)
            bot.reply_to(message, f"Неизвестная ошибка:\n{e}")
        else:
            bot.reply_to(message, f'Стоимость ваших {values[2]} {values[0]} в {values[1]} составляет {resultation1}! Приятной конвертации!')



bot.polling()
