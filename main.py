from telebot import TeleBot
from telebot.types import Message
from config import Config
from excatcher import error_handler
from strings import BotStrings

import commands


config = Config('.env', config_format='env')
bot = TeleBot(config.API_TOKEN, parse_mode=config.PARSE_MODE)

strings = BotStrings(parse_mode=bot.parse_mode)
c = commands.BotCommands(bot, strings)


@bot.message_handler(commands=['start'])
def start(message: Message):
    c.start(message)


@bot.message_handler(commands=['test'])
def test(message: Message):
    c.test(message)


@error_handler
def main():
    bot.polling()


if __name__ == '__main__':
    main()
