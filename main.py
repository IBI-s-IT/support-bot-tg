import telebot
from config import Config
from excatcher import error_handler
from strings import BotStrings


config = Config('.env', config_format='env')
bot = telebot.TeleBot(config.API_TOKEN, parse_mode=config.parse_mode)
strings = BotStrings(parse_mode=bot.parse_mode)


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    bot.send_message(message.chat.id, strings.hello)


@bot.message_handler(commands=['test'])
def test(message: telebot.types.Message):
    bot.send_message(message.chat.id, strings.test)
    bot.send_message(message.chat.id, f'<b>Hi, {message.from_user.first_name}</b>\n'
                                      f'Your API token is <i>secret</i>', parse_mode='HTML')
    bot.send_message(message.chat.id, 'This is a <a href="https://t.me/cullfy">link</a>', parse_mode='HTML')
    bot.reply_to(message, 'This is a reply')


@error_handler
def main():
    bot.polling()


if __name__ == '__main__':
    main()
