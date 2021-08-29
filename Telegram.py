import telebot

bot = telebot.TeleBot('1819048696:AAEPk_T3sDr4mimemdk_HZ6tyjI_A6gch18')



def sendMessage(id, message):
    pass


def botListener():
    global bot

    print("bot started")

    @bot.message_handler(commands=['help', 'start'])
    def send_welcome(message):
        print("start message")
        msg = bot.send_message(message.chat.id, 'Hello world')

    @bot.message_handler(commands=['auth'])
    def send_auth(message):
        pass

    bot.polling()