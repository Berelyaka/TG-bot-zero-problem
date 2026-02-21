from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


# =========================
# INLINE КЛАВИАТУРЫ (сценарии)
# =========================

def start_inline_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="🔑 Купить доступ", callback_data="buy_start")
    return builder.as_markup()


def region_menu():
    builder = InlineKeyboardBuilder()

    # Активный регион
    builder.button(text="🇨🇿 Чехия", callback_data="region_cz")

    # Заглушки
    builder.button(text="🇩🇪 Германия (скоро)", callback_data="region_locked")
    builder.button(text="🇳🇱 Нидерланды (скоро)", callback_data="region_locked")

    builder.button(text="🔙 Назад", callback_data="back_main")

    builder.adjust(1)
    return builder.as_markup()


def price_menu(region: str):
    builder = InlineKeyboardBuilder()

    builder.button(text="1 месяц — 100 ⭐", callback_data=f"price_{region}_1m")
    builder.button(text="3 месяца — 200 ⭐", callback_data=f"price_{region}_3m")
    builder.button(text="6 месяцев — 300 ⭐", callback_data=f"price_{region}_6m")
    builder.button(text="12 месяцев — 500 ⭐", callback_data=f"price_{region}_12m")

    builder.button(text="🔙 Назад", callback_data="back_region")

    builder.adjust(1)
    return builder.as_markup()


def after_payment_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="🏠 В главное меню", callback_data="back_main")
    return builder.as_markup()


# =========================
# REPLY ПАНЕЛЬ (постоянное меню)
# =========================

def platform_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🔑 Купить доступ")],
            [KeyboardButton(text="📦 Мой доступ")],
            [KeyboardButton(text="🆓 Тестовый период"),
             KeyboardButton(text="🎁 Промо доступ")],
            [KeyboardButton(text="🔄 Изменить протокол"),
             KeyboardButton(text="🌍 Изменить локацию")],
            [KeyboardButton(text="❓ Помощь")]
        ],
        resize_keyboard=True
    )


def help_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📱 iOS"),
             KeyboardButton(text="🤖 Android")],
            [KeyboardButton(text="💻 Windows / macOS")],
            [KeyboardButton(text="✉️ Написать в поддержку")],
            [KeyboardButton(text="🔙 Назад")]
        ],
        resize_keyboard=True
    )