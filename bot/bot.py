import telebot
import random
from telebot import types
import setup


f = open('data/regim.txt', 'r', encoding='UTF-8')
regim = f.read().split('\n')
f.close()

f = open('data/orders.txt', 'r', encoding='UTF-8')
orders = f.read().split('\n')
f.close()

f = open('data/ask.txt', 'r', encoding='UTF-8')
ask = f.read().split('\n')
f.close()

photo = open('data/march.JPG', 'rb')

bot = telebot.TeleBot(setup.token)


# @bot.message_handler(commands=['start'])
# def start(m, res=False):
#     bot.send_message(m.chat.id, 'Howdy!')

@bot.message_handler(commands=['start'])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('📝 Оперативная работа')
    item2 = types.KeyboardButton('📕 Приказы')
    item3 = types.KeyboardButton('👮‍ Атемий попросил')
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    # bot.send_photo(m.chat.id, photo)
    bot.send_message(m.chat.id, f'Howdy! <b><i>{m.chat.username}</i></b>!\nВыбери, тчо тебе нужно!', reply_markup=markup, parse_mode='html')


# @bot.message_handler(content_types=['text'])
# def handly_text(message):
#     bot.send_message(message.chat.id, 'I said: ' + message.text)

@bot.message_handler(content_types=['text'])
def handly_text(message):
    if message.text.strip() == '📝 Оперативная работа':
        # answer = regim

        markup = types.InlineKeyboardMarkup(row_width=2)
        itm1 = types.InlineKeyboardButton('Режимные', callback_data='regim')
        itm2 = types.InlineKeyboardButton('График', callback_data='schedule')
        markup.add(itm1, itm2)

        bot.send_message(message.chat.id, 'fine!', reply_markup=markup)
    elif message.text.strip() == '📕 Приказы':
        bot.send_message(message.chat.id, orders)
    elif message.text.strip() == '👮‍ Атемий попросил':
        bot.send_message(message.chat.id, random.choice(ask))
        # answer = ask


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'regim':
                bot.send_message(call.message.chat.id, regim)
            elif call.data == 'schedule':
                bot.send_photo(call.message.chat.id, photo)

    except Exception as e:
        print(repr(e))


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
