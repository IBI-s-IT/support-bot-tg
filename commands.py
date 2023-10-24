from telebot.types import Message
from telebot import TeleBot

from strings import BotStrings


class BotCommands:
    def __init__(self, bot: TeleBot, strings: BotStrings):
        self.bot = bot
        self.strings = strings

    def start(self, message: Message):
        self.bot.send_message(message.chat.id, self.strings.hello)

    def test(self, message: Message):
        self.bot.send_message(message.chat.id, self.strings.test)
        self.bot.send_message(message.chat.id, f'<b>Hi, {message.from_user.first_name}</b>\n'
                                               'Your API token is <i>secret</i>', parse_mode='HTML')
        self.bot.send_message(message.chat.id, 'This is a <a href="https://t.me/cullfy">link</a>', parse_mode='HTML')
        self.bot.reply_to(message, 'This is a reply')
