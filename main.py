import logging
import telebot

from src.screener import Screener, UrlDoesNotExist
from src.storage import ScreenStorage

from settings import TOKEN

bot = telebot.TeleBot(TOKEN)

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)


storage = ScreenStorage()


@bot.message_handler(content_types=['text'])
def send_welcome(message):
	url = message.text

	bot.send_chat_action(message.from_user.id, 'upload_photo')

	path = storage.get_file_path_by_url(url)

	if path is None:

		try:
			path = Screener.do_screen_by_url(url)
		except UrlDoesNotExist:
			return

		storage.save_file_path(url, path)

	with open(path, 'rb') as doc:
		bot.send_document(message.from_user.id, doc)


bot.polling()
