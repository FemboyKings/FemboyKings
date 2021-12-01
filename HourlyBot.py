import telegram
from telegram.ext.dispatcher import run_async
from telegram.utils.request import Request
from telegram.ext import Updater
import datetime
import toml
import time
import os
from random import choice

image_urls = [
    'https://drive.google.com/drive/folders/1q0UcKmWTBVLdzaYgrDf3VT3BUAPXFoTd?usp=sharing',
    'https://drive.google.com/drive/folders/1q0UcKmWTBVLdzaYgrDf3VT3BUAPXFoTd?usp=sharing',
    ]

config = toml.load('config.toml')

bot = telegram.Bot(config.get('token'), request = Request(con_pool_size = 70, connect_timeout = 120))

run_async
def hourly():
    while True:
        while datetime.datetime.utcnow().minute == 0 and datetime.datetime.utcnow().second == 0:
            image_url = choice(image_urls)
            bot.send_photo(config.get('channel'), image_url)
        time.sleep(1)

def main():
    updater = Updater(bot=bot, workers=66, use_context=True)
    updater.start_polling()
    print(f'Signed in as {bot.name}')
    hourly()
    updater.idle()


if __name__ == '__main__':
    main()
