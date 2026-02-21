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

    builder.button(text="🇩🇪 Германия", callback_data="region_de")
    builder.button(text="🇵🇱 Польша", callback_data="region_pl")
    builder.button(text="🇳🇱 Нидерланды", callback_data="region_nl")

    builder.button(text="🔙 Назад", callback_data="back_main")

    builder.adjust(1)
    return builder.as_markup()


def price_menu(region: str):
    """
    region передаём, чтобы сохранить его в callback_data
    """
    builder = InlineKeyboardBuilder()

    builder.button(
        text="1 месяц — 100 ⭐",
        callback_data=f"price_{region}_1m"
    )
    builder.button(
        text="3 месяца — 200 ⭐",
        callback_data=f"price_{region}_3m"
    )
    builder.button(
        text="6 месяцев — 300 ⭐",
        callback_data=f"price_{region}_6m"
    )
    builder.button(
        text="12 месяцев — 500 ⭐",
        callback_data=f"price_{region}_12m"
    )

    builder.button(
        text="🔙 Назад",
        callback_data="back_region"
    )

    builder.adjust(1)
    return builder.as_markup()


def after_payment_menu():
    builder = InlineKeyboardBuilder()
    builder.button(text="🏠 В главное меню", callback_data="back_main")
    return builder.as_markup()


# =========================
# REPLY КЛАВИАТУРА (постоянная панель)
# =========================

def platform_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🔑 Купить доступ")],
            [KeyboardButton(text="📦 Мой доступ")],
            [KeyboardButton(text="⚙️ Настройки")],
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