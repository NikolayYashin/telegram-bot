import telebot



chatID = -1001420169796

print("Бот запущен. Нажмите Ctrl+C для завершения")

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Для помощи наберите команду /help и будет помощь')

@bot.message_handler(commands=["help"])
def start(message):
    bot.send_message(message.chat.id, 'Тут сообщение о помощи')


@bot.message_handler(content_types=['text'])
def all_messages(message):
    if 'входящий платеж:' in message.text.lower():
        bot.forward_message(chatID, message.chat.id, message.message_id)
    if 'перевод от' in message.text.lower():
        bot.forward_message(chatID, message.chat.id, message.message_id)

if __name__ == '__main__':
    bot.polling(none_stop = True)
