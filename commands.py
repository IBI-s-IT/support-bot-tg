from telebot.types import Message, CallbackQuery
from telebot import TeleBot
from markups import MessageMarkups
from static import BotStrings


class BotCommands:
    def __init__(self, bot: TeleBot, strings: BotStrings):
        self.bot = bot
        self.strings = strings

    def start(self, message: Message):
        self.bot.send_message(message.chat.id, self.strings.hello, reply_markup=MessageMarkups.main)

    def appeal(self, data: Message | CallbackQuery):
        if data.inline_message_id:
            markup = MessageMarkups.appeal
            self.bot.edit_message_text(
                'Если у вас возник вопрос, вы можете задать его студсовету:',
                data.message.chat.id,
                data.message.message_id,
                reply_markup=markup
            )

    # def test(self, message: Message, callback: CallbackQuery = None):
    #     if callback:  # example of reaction to callback query
    #         markup = MessageMarkups.main
    #         self.bot.answer_callback_query(callback.id, 'Test')
    #         self.bot.edit_message_text('Edited text', message.chat.id, message.message_id, reply_markup=markup)
    #     else:
    #         self.bot.send_message(message.chat.id, self.strings.test)
    #         self.bot.send_message(message.chat.id, f'<b>Hi, {message.from_user.first_name}</b>\n'
    #                                                'Your API token is <i>secret</i>', parse_mode='HTML')
    #         self.bot.send_message(message.chat.id, 'This is a <a href="https://t.me/cullfy">link</a>',
    #                               parse_mode='HTML')
    #         self.bot.reply_to(message, 'This is a reply')

    # def test_markup(self, message: Message):
    #     markup = MessageMarkups.main
    #     self.bot.send_message(message.chat.id, 'Test message', reply_markup=markup)
