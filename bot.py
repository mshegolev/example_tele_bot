import os
import time

import telebot

token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token=token, num_threads=1)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, interval=5, timeout=20)
        except Exception as e:
            telebot.logger.error(e)
            time.sleep(60)
