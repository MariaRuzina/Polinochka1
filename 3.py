import telebot
import random
from telebot import types
from PIL import Image
sl={
    '1':'путь к фото1',
    '2':'путь к фото2'
    }
sk ={
    '1':'текст1',
    '2':'текст2',
    '3':'текст3',
    '4':'текст4',
    '5':'текст5',
    '6':'текст6',
    '7':'текст7',
    '8':'текст8',
    '9':'текст9'
}
bot = telebot.TeleBot('TOKEN');
def ds (message):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton('Фото', callback_data='yes')
    item2 = types.InlineKeyboardButton('Милые слова', callback_data='no')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, text='Выбрать действие:', reply_markup=markup)
@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'yes':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=sk[str(random.randint(1, 9))])
            bot.send_photo(message.chat.id, open(sl[str(random.randint(1, 9))]))
        elif call.data == 'no':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text= sk[str(random.randint(1,9))])
bot.polling(none_stop=True, interval=0)