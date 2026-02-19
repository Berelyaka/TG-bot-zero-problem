from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder



def start_inline_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="Купить ключ", callback_data="buy_key")
    return builder.as_markup()



def region_menu():
    builder = InlineKeyboardBuilder()

    builder.button(text="Регион 1", callback_data="region_1")
    builder.button(text="Регион 2", callback_data="region_2")
    builder.button(text="Регион 3", callback_data="region_3")
    builder.button(text="🔙 Назад", callback_data="back_to_main")

    builder.adjust(1)  # по одной кнопке в строке

    return builder.as_markup()



def platform_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Купить ключ")],
            [KeyboardButton(text="Тестовый период"),
             KeyboardButton(text="Промо доступ"),
             ],
            [KeyboardButton(text="Изменить протокол"),
             KeyboardButton(text="Изменить локацию")],
            [KeyboardButton(text="FAQ")]
        ],
        resize_keyboard=True
    )   



def help_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="IOS"),
            KeyboardButton(text="Android"),
            KeyboardButton(text="Windows/MAC")],
            [KeyboardButton(text="Написать в поддержку")],
            [KeyboardButton(text="Назад")]
        ],
        resize_keyboard=True
    )



def buy_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Stars"),
            KeyboardButton(text="Назад")]
        ],
        resize_keyboard=True
    )



def price_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="1 мес - 1$"),
             KeyboardButton(text="3 мес - 2$"),
             KeyboardButton(text="6 мес - 3$")],
             [KeyboardButton(text="12 мес - 5$")]
        ],
        resize_keyboard=True
    )