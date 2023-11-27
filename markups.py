from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from static import ClassList


class MessageMarkups:
    button_back = InlineKeyboardButton('Назад', callback_data='go_back')

    main: InlineKeyboardMarkup = InlineKeyboardMarkup()
    main_ss = InlineKeyboardButton('Структура студсовета', callback_data='ss_info')
    main_appeal = InlineKeyboardButton('Обращение', callback_data='appeal')
    main_inform = InlineKeyboardButton('Информация', callback_data='inform')
    # main_subscribe = InlineKeyboardButton('Рассылки', callback_data='subscribe')
    # main_kb = [[main_ss], [main_appeal], [main_inform], [main_subscribe]]
    main_kb = [[main_ss], [main_appeal], [main_inform]]
    main.keyboard = main_kb

    ss_info: InlineKeyboardMarkup = InlineKeyboardMarkup()
    ss_info.keyboard = [[button_back]]

    appeal: InlineKeyboardMarkup = InlineKeyboardMarkup()
    appeal_anon = InlineKeyboardButton('Анонимно', callback_data='appeal_anon')
    appeal_nanon = InlineKeyboardButton('Не анонимно', callback_data='appeal_nanon')
    appeal_kb = [[appeal_anon], [appeal_nanon], [button_back]]
    appeal.keyboard = appeal_kb

    inform: InlineKeyboardMarkup = InlineKeyboardMarkup()
    inform_resources_btn = InlineKeyboardButton('Ресурсы', callback_data='inform_resources')
    # inform_class_btn = InlineKeyboardButton('Проход к аудитории', callback_data='inform_class')
    # inform_pin = InlineKeyboardButton('Поиск ПИН', callback_data='inform_pin')  # web app in future
    # inform_other = InlineKeyboardButton('Прочая информация', callback_data='inform_other')
    # inform_kb = [[inform_resources_btn, inform_pin], [inform_class_btn], [button_back]]
    inform_kb = [[inform_resources_btn], [button_back]]
    inform.keyboard = inform_kb

    inform_resources = InlineKeyboardMarkup()
    resources_web = InlineKeyboardButton('Сайт МБИ', url='https://ibispb.ru/')
    resources_channels_btn = InlineKeyboardButton('Ссылки на медиа', callback_data='resources_channels')
    resources_ibi_s_it_btn = InlineKeyboardButton('Другие удобства от студсовета', callback_data='resources_ibi_s_it')
    resources_kb = [[resources_web, resources_channels_btn], [resources_ibi_s_it_btn], [button_back]]
    inform_resources.keyboard = resources_kb

    resources_channels = InlineKeyboardMarkup()
    resources_channels.keyboard = [[button_back]]

    resources_ibi_s_it = InlineKeyboardMarkup()
    resources_ibi_s_it.keyboard = [[button_back]]

    inform_class = InlineKeyboardMarkup()
    # callback_data can be changed to web_app argument to integrate web app
    class_buttons_MC = [InlineKeyboardButton(f'МС-{i}', callback_data=f'class_{i}') for i in ClassList['МС']]
    class_buttons_H = [InlineKeyboardButton(f'Н-{i}', callback_data=f'class_{i}') for i in ClassList['Н']]
    class_buttons = class_buttons_MC + class_buttons_H

    class_kb = []
    _c_t = []
    for i in class_buttons:
        _c_t.append(i)
        if len(_c_t) == 5:
            class_kb.append(_c_t)
            _c_t = []
    else:
        class_kb.append(_c_t)

    class_kb.append([button_back])
    inform_class.keyboard = class_kb

    # subscribe = InlineKeyboardMarkup()
    # subscribe_media = InlineKeyboardButton('Подслушано студсовет', url='https://cullfy.ru')
    # subscribe_decan = InlineKeyboardButton('Подслушано МБИ', url='https://cullfy.ru')
    # # other...
    # subscribe_kb = [[subscribe_media], [subscribe_decan], [button_back]]
    # subscribe.keyboard = subscribe_kb
