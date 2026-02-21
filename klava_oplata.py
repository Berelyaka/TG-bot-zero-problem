from aiogram.utils.keyboard import InlineKeyboardBuilder


def payment_keyboard(stars: int):
    """
    Универсальная кнопка оплаты через Telegram Stars.
    stars — количество звёзд для отображения на кнопке.
    """

    builder = InlineKeyboardBuilder()
    builder.button(
        text=f"Оплатить {stars} ⭐",
        pay=True
    )

    return builder.as_markup()