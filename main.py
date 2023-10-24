from telebot import TeleBot
from telebot.types import Message, CallbackQuery
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


@bot.message_handler(commands=['test_markup'])
def test_markup(message: Message):
    c.test_markup(message)


# example of callback query handling
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call: CallbackQuery):
    if call.data == "test":
        c.test(call.message, callback=call)


@error_handler
def main():
    bot.polling()


if __name__ == '__main__':
    main()
