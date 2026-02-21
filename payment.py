from aiogram.types import LabeledPrice, Message, PreCheckoutQuery
from keyboards import after_payment_menu
from klava_oplata import payment_keyboard
from database import add_subscription
from vpn_manager import create_vless_client

async def success_payment_handler(message: Message):
    user_id = message.from_user.id
    payload = message.successful_payment.invoice_payload

    _, region, period = payload.split("_")

    period_map = {
        "1m": 30,
        "3m": 90,
        "6m": 180,
        "12m": 365,
    }

    days = period_map.get(period, 30)

    # создаём клиента на сервере
    uuid_value, link = create_vless_client()

    # сохраняем подписку в БД
    add_subscription(user_id, region, days)

    await message.answer(
        "🎉 Оплата подтверждена!\n\n"
        "Ваш персональный VPN доступ готов:\n\n"
        f"{link}\n\n"
        "Сохраните ссылку."
    )

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


