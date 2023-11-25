import os.path

import segno
import telebot
from telebot import types
from data.input.settings import PATH, BOT_API


bot = telebot.TeleBot(BOT_API)

def make_qr(text):
    qrcode = segno.make_qr(text)
    qrcode.save(PATH, scale=7)
    file_name = os.path.split(PATH)[-1]
    print(file_name)
    return PATH


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'Привет ✌️ {message.chat.first_name} я умею делать куар коды\n'
                                      f'Просто пришли мне нужный текст', parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_qr(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Get my QR-code')
    markup.add(item1)
    print(message.text)
    # if message.text.strip() == 'Get my QR-code':
    #     bot.send_message(message.chat.id, f'Получи {tmp}', reply_markup=start_message())
    #     # bot.send_photo(message.chat.id, )

    file = make_qr(message.text)
    qr = open(file, 'rb')
    bot.send_message(message.chat.id, f'Вот твой куар код, {message.chat.username}:')
    bot.send_photo(message.chat.id, qr)
    start_message(message)


bot.infinity_polling()


# if __name__ == "__main__":
#     make_qr(input('Your prompt here: '))