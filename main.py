import logging
import telebot

from src.screener import Screener
from src.storage import ScreenStorage
from settings import TOKEN

bot = telebot.TeleBot(TOKEN)

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

storage = ScreenStorage()


def respond_screenshot(message, url, js_delay='0'):
    msg_to_delete = bot.reply_to(message, "Processing...\nPlease wait...")
    path = storage.get_file_path_by_url(url) if js_delay == '0' else None

    if path is None:

        try:
            path = Screener.do_screen_by_url(url, js_delay)
        except OSError as e:
            logging.error(e)
            bot.send_message(message.from_user.id, 'Bad URL...\nPlease correct and try again...')
            return

        storage.save_file_path(url, path)

    bot.send_chat_action(message.from_user.id, 'upload_photo')
    with open(path, 'rb') as doc:
        bot.send_document(message.from_user.id, doc)
    bot.delete_message(message.from_user.id, msg_to_delete.message_id)


@bot.message_handler(commands=['start', 'help'])
def handle_start(message):
    bot.send_message(message.from_user.id, "Hello, this bot can do screenshot by url\n"
                                           "Just send valid url to me as text\n"
                                           "Also if your site using lazy loading you can send url and "
                                           "JavaScript loading delay to handle this case using command:\n"
                                           "<code>/js_delay delay_in_sec url</code>", parse_mode='HTML')


@bot.message_handler(commands=['js_delay'])
def handle_js_delay(message):
    splited = message.text.split()

    if len(splited) == 3 and splited[1].isdigit():
        command, delay, url = message.text.split()
        respond_screenshot(message, url, js_delay=delay)
    else:
        bot.reply_to(message, "Wrong command usage.\nRead /help")


@bot.message_handler(content_types=['text'])
def handle_text(message):
    url = message.text
    respond_screenshot(message, url)


bot.polling()
