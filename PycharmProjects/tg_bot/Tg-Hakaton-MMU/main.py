import types
import telebot
from telebot import types
import webbrowser


bot = telebot.TeleBot('7486383790:AAHKlMrGIKGuzcM_GpLtqVFVgf8CUHI_XGM')
bot.delete_webhook()

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    btn3 = types.KeyboardButton("экстреная помощь!!!")
    btn4 = types.KeyboardButton("открыть доступ")
    back = types.KeyboardButton("Вернуться в главное меню")
    markup.add(btn1, btn2, btn3, btn4, back)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я тестовый бот для "
                          "https://idivergent.ru/"
                     .format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, f'Здравствуйте! {message.from_user.first_name}'
        f' {message.from_user.last_name} Поздравляем, <b>Вы</b> были приняты на работу в нашу '
        f'компанию! на должность Стажёра. В Вашу работу входит  присутствовать на рабочем месте,'
        f' ответственно относиться к работе, соблюдать дедлайны. В нашей компании проходят встречи '
        f'2 раза в неделю. А в течение испытательного срока Вам будут высылаться небольшие опросы по'
        f' сбору основных сведений. Наша компании заботится о качестве работы наших сотрудников,  '
        f'поэтому просим Вас дать нам обратную связь, чтобы мы могли стать лучше',
        parse_mode='html')
    elif (message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2 = types.KeyboardButton("Что я могу у тебя спросить?")
        btn3 = types.KeyboardButton("экстреная помощь!!!")
        btn4 = types.KeyboardButton("открыть доступ")
        btn5 = types.KeyboardButton("график работы")
        btn6 = types.KeyboardButton("место работы")
        btn7 = types.KeyboardButton("где находиться обеденная зона?")
        btn8 = types.KeyboardButton("К кому обратиться при небольшой проблеме")
        btn9 = types.KeyboardButton("сайт компании")
        back1 = types.KeyboardButton("Вернуться в главное меню")
        markup.add( btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, back1)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    elif message.text == "Что я могу у тебя спросить?":
        bot.send_message(message.chat.id, text="/site - перейти на сайт, /website - тоже перейт на сайт, /help - экстрен помощь.")
    elif message.text == "открыть доступ":
        bot.send_message(message.chat.id, f'Доступ открыт')
    elif message.text == "график работы":
        bot.send_message(message.chat.id, f'Понедельник-Пятница с 9:00 до 17:00')
    elif message.text == "место работы":
        bot.send_message(message.chat.id, f' приходи в Саратовскую область, г.Саратов, '
        f'ул.Им Рахова В.Г., д.108 кв 18, 16 этаж, кабинет 1863, место 4')
    elif message.text == "где находиться обеденная зона?":
        bot.send_message(message.chat.id, f'на 3 этаже ')
    elif message.text == ("К кому обратиться при небольшой проблеме"):
        bot.send_message(message.chat.id, f'@FBI_RF_77')
    elif message.text == ("сайт компании"):
        webbrowser.open('https://idivergent.ru/')
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        button3 = types.KeyboardButton("экстреная помощь!!!")
        button4 = types.KeyboardButton("открыть доступ")
        button5 = types.KeyboardButton("график работы")
        button6 = types.KeyboardButton("место работы")
        button7 = types.KeyboardButton("где находиться обеденная зона?")
        button8 = types.KeyboardButton("К кому обратиться при небольшой проблеме")
        button9 = types.KeyboardButton("сайт компании")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, back)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню",
        reply_markup=markup)
    elif (message.text == "экстреная помощь!!!"):
        bot.send_message(message.chat.id, '+7-495-215-05-95, sales@idivergent.ru')
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")


@bot.message_handler(commands=['start', 'поехали', 'go', 'hello', 'hi'])
def main(message):
    bot.send_message(message.chat.id, f'Здравствуйте! {message.from_user.first_name}'
    f' {message.from_user.last_name} Поздравляем, <b>Вы</b> были приняты на работу в нашу'
    f' компанию! на должность Стажёра. В Вашу работу входит [перечисление]. В нашей '
    f'компании проходят встречи [частота встеч] А в течение испытательного срока Вам'
    f' будут высылаться небольшие опросы по сбор основных сведений. Наша компании '
    f'заботится о качестве работы наших сотрудников,  поэтому просим Вас дать нам '
    f'обратную связь, чтобы мы могли стать лучше',
    parse_mode='html')


bot.infinity_polling()