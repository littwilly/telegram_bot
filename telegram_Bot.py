import telebot

bot = telebot.TeleBot('1475810870:AAGu0Lpt5EsEqxBJ7zohbmVddhJ_AkoyyO0')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    msg = f"Привет я бот! Приятно познакомиться { message.chat.username }!, напиши мне привет что бы посмотреть что я могу"  
    bot.reply_to(message, msg)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет! Что бы посмотреть список FAQ набери /command и выбери команду')
    elif message.text == "/command1":
        bot.send_message(message.from_user.id, "Network by Consensus - это сообщество активных молодых людей и форум для укрепления молодежного диалога. Оно служит платформой для обмена идеями и достижениями молодых людей, их знаниями и опытом, а также для содействия во взаимном обучении и развитии.")
    elif message.text == "/command2":
        bot.send_message(message.from_user.id, "Для участия в мероприятиях OSCE сделедите за новостями на официальной странице в Facebook \n https://www.facebook.com/networkbyconsensus/") 
    elif message.text == "/command3":
        bot.send_message(message.from_user.id, " Это телеграм канал Network by consensus на котором публикуются различные новости. Присоединяйся! \n https://t.me/networkbyconsensus")
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит. Напиши мне привет :)')

bot.polling(none_stop=True)
