from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from static import ClassList


class MessageMarkups:
    button_back = InlineKeyboardButton('Назад', callback_data='go_back')

    main: InlineKeyboardMarkup = InlineKeyboardMarkup()
    main_appeal = InlineKeyboardButton('Обращение', callback_data='appeal')
    main_inform = InlineKeyboardButton('Информация', callback_data='inform')
    main_subscribe = InlineKeyboardButton('Рассылки', callback_data='subscribe')
    main.add(main_appeal, main_inform, main_subscribe, button_back)

    appeal: InlineKeyboardMarkup = InlineKeyboardMarkup()
    appeal_anon = InlineKeyboardButton('Анонимно', callback_data='appeal_anon')
    appeal_nanon = InlineKeyboardButton('Не анонимно', callback_data='appeal_nanon')
    appeal.add(appeal_anon, appeal_nanon, button_back)

    inform: InlineKeyboardMarkup = InlineKeyboardMarkup()
    inform_resources = InlineKeyboardButton('Ресурсы', callback_data='inform_resources')
    inform_class = InlineKeyboardButton('Проход к аудитории', callback_data='inform_class')
    inform_pin = InlineKeyboardButton('Поиск ПИН', callback_data='inform_pin')  # web app in future
    # inform_other = InlineKeyboardButton('Прочая информация', callback_data='inform_other')
    inform.add(inform_resources, inform_class, inform_pin, button_back)

    resources = InlineKeyboardMarkup()
    resources_web = InlineKeyboardButton('Сайт МБИ', url='https://ibispb.ru/')
    resources_channels = InlineKeyboardButton('Ссылки на медиа', callback_data='resources_channels')
    resources_ibi_s_it = InlineKeyboardButton('Удобства', callback_data='ibi_s_it')
    resources.add(button_back)

    resources_channels_ = InlineKeyboardMarkup()
    resources_channels_.add(button_back)

    resources_ibi_s_it_ = InlineKeyboardMarkup()
    resources_ibi_s_it_.add(button_back)

    class_ = InlineKeyboardMarkup()
    # callback_data can be changed to web_app argument to integrate web app
    class_buttons_MC = [InlineKeyboardButton(f'МС-{i}', callback_data=f'class_{i}') for i in ClassList['МС']]
    class_buttons_H = [InlineKeyboardButton(f'Н-{i}', callback_data=f'class_{i}') for i in ClassList['Н']]
    class_buttons = class_buttons_MC + class_buttons_H
    class_buttons.append(button_back)
    class_.add(class_buttons)

    subscribe = InlineKeyboardMarkup()
    subscribe_media = InlineKeyboardButton('Подслушано студсовет')
    subscribe_decan = InlineKeyboardButton('Подслушано МБИ')
    # other...
    subscribe.add(subscribe_media, subscribe_decan, button_back)
