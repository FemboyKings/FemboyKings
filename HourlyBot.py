import telegram
from telegram.ext.dispatcher import run_async
from telegram.utils.request import Request
from telegram.ext import Updater, Dispatcher
import datetime
import toml
import time
from random import choice


config = toml.load('config.toml')
bot = telegram.Bot(config.get('token'), request=Request(con_pool_size=70, connect_timeout=120))
image_urls = [
    'https://i.imgur.com/72oDVSW.jpg',
    'https://i.imgur.com/4xBs4JD.png',
    'https://i.imgur.com/L3KOxC1.png',
]


@run_async
def hourly():
    while True:
        while datetime.datetime.utcnow().minute == 0 and datetime.datetime.utcnow().second == 0:
            image_url = choice(image_urls)
            bot.send_photo(config.get('channel'), image_url)
            time.sleep(1)
        time.sleep(1)


def main():
    updater = Updater(bot=bot, workers=66, use_context=True)
    updater.start_polling()
    print(f'Signed in as {bot.name}')
    hourly()
    updater.idle()


if __name__ == '__main__':
    main()
