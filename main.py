from telebot import TeleBot
from telebot.types import Message, CallbackQuery
from config import Config
from excatcher import error_handler
from static import BotStrings

import commands


config = Config('.env', config_format='env')
bot = TeleBot(config.API_TOKEN, parse_mode=config.PARSE_MODE)

strings = BotStrings(parse_mode=bot.parse_mode)
c = commands.BotCommands(bot, strings)


@bot.message_handler(commands=['start'])
def start(message: Message):
    c.start(message)


@bot.message_handler(commands=['appeal'])
def test(message: Message):
    c.appeal(message)


# example of callback query handling
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call: CallbackQuery):
    if call.data == "appeal":
        c.appeal(call)


@error_handler(exits=False)
def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()
