from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_inline_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="Купить ключ", callback_data="buy_menu")
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
