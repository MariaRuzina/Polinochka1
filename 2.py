import csv

import datetime
import telebot
from telebot import types
import requests
import wikipedia, re
from random import randrange

wikipedia.set_lang("ru")
f = open('wiki.txt', mode='r+', encoding='utf8')
print('0', file=f)
bot = telebot.TeleBot('5343779719:AAFHPugoByNf_ywQ_BcXL89kccpElOmTihw')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Просто интересно")
    btn2 = types.KeyboardButton("Не могу разобраться в себе")
    btn3 = types.KeyboardButton("Дневник")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text="Приветики, меня зовут Полина, всегда готова помочь своим друзьям поддержать ментальное равновесие^^\nЯ учусь на психологическом факультете нашего города, всей душой люблю своё дело!!\nО чём хочешь поговорить?".format(
                         message.from_user), reply_markup=markup)


def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not ('==' in x):
                if (len((x.strip())) > 3):
                    wikitext2 = wikitext2 + x + '.'
            else:
                break
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return 'В энциклопедии нет информации об этом'


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Просто интересно"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Что есть что?")
        btn2 = types.KeyboardButton("Основы психологии")
        btn3 = types.KeyboardButton("Самоанализ")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Тааак, давай-ка я расскажу тебе поподробнее", reply_markup=markup)

    elif (message.text == "Что есть что?"):
        bot.send_message(message.chat.id, 'Отправь мне любое слово, и я найду его значение на Wikipedia')
        f = open('wiki.txt', mode='r+', encoding='utf8')
        print('1', file=f)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Завершить")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Что именно тебя интересует?", reply_markup=markup)

    elif (message.text == "Основы психологии"):
        markup1 = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Мифы о психологии и психологах",
                                             url='https://www.paracels.ru/populjarnaja-psihologija/mify-o-psihologii-i-psihologah.html')
        button2 = types.InlineKeyboardButton("Арт-терапия в России: пройденный путь и векторы дальнейшего развития",
                                             url='https://www.paracels.ru/populjarnaja-psihologija/art-terapiya-v-rossii.html')
        button3 = types.InlineKeyboardButton(
            "О защитных механизмах психики, их роли в сопротивлении природным процессам и движению",
            url='https://www.paracels.ru/populjarnaja-psihologija/o-zashhitnyh-mehanizmah-psihiki.html')
        button4 = types.InlineKeyboardButton("Психологическое присутствие и психотерапия",
                                             url='https://www.paracels.ru/populjarnaja-psihologija/psihologicheskoe-prisutstvie-i-psihoterapija.html')
        button5 = types.InlineKeyboardButton(
            "Психосоматика", url='https://www.paracels.ru/populjarnaja-psihologija/psihosomatika.html')
        button6 = types.InlineKeyboardButton("Всё дело в голове",
                                             url='https://www.paracels.ru/populjarnaja-psihologija/vsjo-delo-v-golove.html')
        markup1.add(button1, button2, button3, button4, button5, button6)
        bot.send_message(message.chat.id, text="Вот несколько интересных статей, если интересно, можешь обратиться к ним", reply_markup=markup1)


    elif (message.text == "Самоанализ"):
        markup1 = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("16 типов личности по MBTI",
                                             url='https://www.16personalities.com/ru/test-lichnosti')
        button2 = types.InlineKeyboardButton("Формула темперамента Белова",
                                             url='https://testometrika.com/personality-and-temper/the-formula-of-temperament-a-belov/')
        button3 = types.InlineKeyboardButton(
            "Тест Айзенка EPQ-R: узнайте свой темперамент",
            url='https://testometrika.com/personality-and-temper/questionnaire-eysenck-pen/')
        button4 = types.InlineKeyboardButton("Протестируй свою психику!",
                                             url='https://testometrika.com/personality-and-temper/test-your-psyche/')
        markup1.add(button1, button2)
        markup1.add(button3, button4)
        bot.send_message(message.chat.id, text="Вот несколько интересных тестов на тип личности и темперамент, быть может это прояснит некоторые моменты",
                         reply_markup=markup1)



    elif (message.text == "Не могу разобраться в себе"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Давай пройдем тест")
        btn2 = types.KeyboardButton("Просто отдохнем")
        btn3 = types.KeyboardButton("Может сразу обратимся к специалисту?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif (message.text == "Давай пройдем тест"):
        markup1 = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Много разных вариантов",
                                             url='https://elementarno.center/tests#popup:karantin')
        button2 = types.InlineKeyboardButton("Тест по картинкам",
                                             url='https://www.playbuzz.com/kzrsbv10/7-10-2017-12-06-05-pm')
        button3 = types.InlineKeyboardButton(
            "Тест эмоционального самочувствия",
            url='https://alkoinfo.ee/ru/enesetunde-test/')
        markup1.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Смотри какие прикольные я нашла!!", reply_markup=markup1)

    elif message.text == "Просто отдохнем":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Котики")
        btn2 = types.KeyboardButton("Собачки")
        btn3 = types.KeyboardButton("Словесная поддержка")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id,
                         text="Тебе больше нравятся котики или песики? Или может я поддержу тебя словами?",
                         reply_markup=markup)

    elif message.text == "Котики":
        response = requests.get('https://api.thecatapi.com/v1/images/search')
        file = response.json()
        bot.send_photo(message.chat.id, file[0]['url'])

    elif message.text == "Собачки":
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        file1 = response.json()
        bot.send_photo(message.chat.id, file1['message'])

    elif message.text == "Словесная поддержка":
        f = open('support.txt', mode='r', encoding='utf8').readlines()
        t = f[randrange(len(f) - 1)]
        bot.send_message(message.chat.id, t)

    elif message.text == "Может сразу обратимся к специалисту?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("По телефону и желательно прямо сейчас")
        btn2 = types.KeyboardButton("По видеосвязи")
        btn3 = types.KeyboardButton("Вживую")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id,
                         text="Как тебе будет удобнее поговорить?",
                         reply_markup=markup)

    elif message.text == "По телефону и желательно прямо сейчас":
        q = '\n'.join(open('phones.txt', mode='r', encoding='utf8').readlines())
        bot.send_message(message.chat.id, text=q)

    elif message.text == "По видеосвязи":
        markup1 = types.InlineKeyboardMarkup()
        f = open('sites.csv', encoding='utf8')
        reader = list(csv.reader(f, delimiter=',', quotechar='"'))
        for i in reader:
            print(i)
            n, m = i[0], i[1]
            button1 = types.InlineKeyboardButton(n, url=m)
            markup1.add(button1)
        bot.send_message(message.chat.id, text="Вот пара сайтов, на которых ты можешь найти специалиста",
                         reply_markup=markup1)

    elif message.text == "Вживую":
        markup1 = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('Список действующих специалистов города',
                                             url='https://prodoctorov.ru/saratov/psihoterapevt/')
        markup1.add(button1)
        f = open('adress.csv', encoding='utf8')
        q = ''
        reader = list(csv.reader(f, delimiter=',', quotechar='"'))
        for i in reader:
            q += ' '.join(i) + '\n'
        bot.send_message(message.chat.id, text=f"Вот пара клиник, в которые можно обратиться\n{q}",
                         reply_markup=markup1)

    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Просто интересно")
        btn2 = types.KeyboardButton("Не могу разобраться в себе")
        btn3 = types.KeyboardButton("Дневник")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Хочешь еще что-то спросить?", reply_markup=markup)

    elif message.text == "Завершить":
        f = open('wiki.txt', mode='r+', encoding='utf8')
        print('0', file=f)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Просто интересно")
        btn2 = types.KeyboardButton("Не могу разобраться в себе")
        btn3 = types.KeyboardButton("Дневник")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Хочешь еще что-то спросить?", reply_markup=markup)

    elif message.text == "Дневник":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Новая запись")
        btn2 = types.KeyboardButton("Перечитать все прошлые записи")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2)
        markup.add(back)
        bot.send_message(message.chat.id, text="Хочешь поделиться новым секретом? Или может освежить память?))",
                         reply_markup=markup)
    elif message.text == "Новая запись":
        bot.send_message(message.chat.id,
                         text="В первой строке введи свой логин, во второй пароль, а со следующей начинай свое письмо))")
        f = open('wiki.txt', mode='r+', encoding='utf8')
        print('2', file=f)

    elif message.text == "Перечитать все прошлые записи":
        bot.send_message(message.chat.id, text="Вводи свой логин и пароль построчно, так мне будет проще найти тебя")
        f = open('wiki.txt', mode='r+', encoding='utf8')
        print('3', file=f)

    else:
        w = int(open('wiki.txt', encoding='utf8').readlines()[-1])
        print(w)
        if w == 0:
            bot.send_message(message.chat.id, text="Прости, на такую команду я не запрограммирована..")
        elif w == 1:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Завершить")
            markup.add(btn1)
            bot.send_message(message.chat.id, getwiki(message.text), reply_markup=markup)
        elif w == 2:
            t = message.text.split('\n')
            if len(t) != 3:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Новая запись")
                btn2 = types.KeyboardButton("Перечитать все прошлые записи")
                back = types.KeyboardButton("Вернуться в главное меню")
                markup.add(btn1, btn2)
                markup.add(back)
                bot.send_message(message.chat.id,
                                 text="Прости, я не могу внести запись, ты не последовал(а) инструкциям",
                                 reply_markup=markup)
            else:
                x = datetime.datetime.now()
                t.append(x.strftime("%x"))
                with open('diary.csv', 'a', newline='', encoding='utf8') as f:
                    writer = csv.writer(f)
                    writer.writerow(t)
                    f.close()
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Завершить")
                markup.add(btn1)
                bot.send_message(message.chat.id, text='Запись добавлена', reply_markup=markup)
        elif w == 3:
            t = message.text.split()
            w = []
            with open('diary.csv', encoding="utf8") as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                for i in enumerate(reader):
                    log, pas, texxt, time = i[1]
                    print(log, pas, texxt)
                    if log == t[0] and pas == t[1]:
                        w.append(time+' '+texxt)
            if len(w) == 0:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Новая запись")
                btn2 = types.KeyboardButton("Перечитать все прошлые записи")
                back = types.KeyboardButton("Вернуться в главное меню")
                markup.add(btn1, btn2)
                markup.add(back)
                bot.send_message(message.chat.id, text='Где-то в данных допущена ошибка, перепроверь',
                                 reply_markup=markup)
            else:
                for i in w:
                    bot.send_message(message.chat.id, text=i)


bot.polling(none_stop=True)
