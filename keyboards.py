from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


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
