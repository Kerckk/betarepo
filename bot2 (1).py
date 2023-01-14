import telebot
token = "5919501544:AAE3axlbO_9sOkvqea4w2TaypCJlyYZYv9o"
from telebot import types
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    btn3 = types.KeyboardButton('Расскажи рассказ')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот ".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет.. Спасибо что общаешься со мной!)")
    elif(message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как тебя зовут?")
        btn2 = types.KeyboardButton("Что ты можешь?")
        btn3 = types.KeyboardButton('Ссылки на сотсети')
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, back)
        
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
    
    elif(message.text == "Как тебя зовут?"):
        bot.send_message(message.chat.id, "Меня зовут Katrin")
    
    elif (message.text == "Что ты можешь?"):
        bot.send_message(message.chat.id, text="Поздороваться с читателями,поделиться ссылками на сотсети, рассказать рассказы")

    elif (message.text == "Ссылки на сотсети"):
        bot.send_message(message.chat.id, text="Подпишись пожалуйста!🥰 : https://pin.it/h0nrYrc ; Instagram : https://instagram.com/kerckkk?igshid=YmMyMTA2M2Y= ;")
    if(message.text == "Расскажи рассказ"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("«И грянул гром», Рэй Бредбери:")
        btn2 = types.KeyboardButton("«Я искал тебя, искал», Ирвин Шоу")
        btn3 = types.KeyboardButton('«Шоколадный зайчик», Андрей Рубанов:')
        btn4 = types.KeyboardButton("«Генезис и катастрофа», Роальд Даль")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3,btn4, back)
    
        bot.send_message(message.chat.id, text="Выбери рассказ", reply_markup=markup)
    if (message.text == "«И грянул гром», Рэй Бредбери:"):
        bot.send_message(message.chat.id, text=" Самое приключенческое приключение, о каком только может мечтать настоящий охотник — путешествие на шестьдесят миллионов лет назад и величайшая добыча. Только правила жесткие, а их нарушение может разрушить мир." )
    elif (message.text == "«Я искал тебя, искал», Ирвин Шоу"):
        bot.send_message(message.chat.id, text=" Самые пронзительные сюжеты всегда короткие. Помните тот самый сборник Хемингуэя из рассказов в три слова? Этот рассказ Ирвина Шоу о том, что настоящую любовь можно лишь отодвинуть на время, но она никогда не уйдет навсегда.")
    elif (message.text == "«Шоколадный зайчик», Андрей Рубанов:"):
        bot.send_message(message.chat.id, text=" Когда они поженились, ей было восемнадцать, а ему — двадцать два. А на дворе безденежный девяносто первый год, и даже приличные джинсы в семье были одни на двоих. И вот любимая жена захотела небольшой подарок на Новый год...")
    elif (message.text == "«Генезис и катастрофа», Роальд Даль"):
        bot.send_message(message.chat.id, text=" У женщины — четвертые роды за четыре года. Недаром роженица беспокоится за новорожденного, ведь трое детей, родившихся раньше, — мертвы. Роальд Даль заставит вас вместе с главной героиней молиться за жизнь младенца. Хотя в конце вы обязательно пожалеете об этом. Но только не о том, что прочли этот рассказ.")

    elif(message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        button3 = types.KeyboardButton("Расскажи рассказ")
        markup.add(button1, button2, button3)
    
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="🥰")
   
bot.infinity_polling()
