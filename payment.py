from aiogram.types import LabeledPrice, Message, PreCheckoutQuery
from keyboards import after_payment_menu
from klava_oplata import payment_keyboard


# Соответствие тарифов
TARIFFS = {
    "1m": {"stars": 100, "label": "1 месяц"},
    "3m": {"stars": 200, "label": "3 месяца"},
    "6m": {"stars": 300, "label": "6 месяцев"},
    "12m": {"stars": 500, "label": "12 месяцев"},
}


async def send_invoice(message: Message, region: str, period: str):
    """
    Универсальная отправка инвойса
    region — выбранный регион (de, pl и т.п.)
    period — срок подписки (1m, 3m и т.д.)
    """

    if period not in TARIFFS:
        await message.answer("Ошибка тарифа.")
        return

    tariff = TARIFFS[period]
    stars_amount = tariff["stars"]

    prices = [LabeledPrice(label="VPN Access", amount=stars_amount)]

    await message.answer_invoice(
        title="Покупка доступа к VPN",
        description=f"Регион: {region.upper()}\n"
                    f"Тариф: {tariff['label']}\n\n"
                    f"Стоимость: {stars_amount} ⭐",
        prices=prices,
        provider_token="",  # для Telegram Stars должен быть пустым
        payload=f"vpn_{region}_{period}",
        currency="XTR",
        reply_markup=payment_keyboard(stars_amount),
    )


async def pre_checkout_handler(pre_checkout_query: PreCheckoutQuery):
    await pre_checkout_query.answer(ok=True)


async def success_payment_handler(message: Message):
    """
    Обработка успешной оплаты
    Здесь позже можно добавить выдачу ключа
    """

    await message.answer(
        "✅ Оплата прошла успешно!\n\n"
        "Ваш ключ будет выдан в ближайшее время.",
        reply_markup=after_payment_menu()
    )