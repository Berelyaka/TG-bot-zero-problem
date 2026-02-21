from database import add_user
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from database import add_user, get_active_subscription
from database import has_used_promo, mark_promo_used, add_subscription
from vpn_manager import create_vless_client

waiting_for_promo = set()
promo_flow_users = set()


from keyboards import (
    platform_menu,
    help_menu,
    start_inline_menu,
    region_menu,
    price_menu,
    after_payment_menu
)

from payment import (
    send_invoice,              # новый универсальный метод (мы его добавим далее)
    pre_checkout_handler,
    success_payment_handler
)

router = Router()

# =========================
# PAYMENT SYSTEM
# =========================

router.pre_checkout_query.register(pre_checkout_handler)
router.message.register(success_payment_handler, F.successful_payment)


# =========================
# START
# =========================



@router.message(CommandStart())
async def start_handler(message: Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name or "друг"

    add_user(user_id)

    await message.answer(
        f"👋 Привет, {first_name}!\n\n"
        "🚀 <b>Zero Problem VPN</b>\n\n"
        "Быстрый и стабильный доступ без ограничений.\n\n"
        "• ⚡ Высокая скорость\n"
        "• 🔐 Защищённое соединение\n"
        "• 📱 Android, iOS, Windows, macOS\n"
        "• 🔑 Мгновенная выдача ключа\n\n"
        "Выберите действие ниже 👇",
        reply_markup=start_inline_menu(),
        parse_mode="HTML"
    )

    await message.answer(
        "Главное меню:",
        reply_markup=platform_menu()
    )


# =========================
# REPLY КНОПКИ (ПАНЕЛЬ)
# =========================
@router.message(F.text == "🎁 Промо доступ")
async def promo_start(message: Message):
    user_id = message.from_user.id

    if has_used_promo(user_id):
        await message.answer("❌ Вы уже использовали промо-доступ.")
        return

    waiting_for_promo.add(user_id)

    await message.answer(
        "Введите кодовое слово для активации промо-доступа:"
    )


@router.message(F.text == "📦 Мой доступ")
async def my_access_handler(message: Message):
    user_id = message.from_user.id
    subscription = get_active_subscription(user_id)

    if not subscription:
        await message.answer(
            "❌ У вас нет активной подписки.\n\n"
            "Оформите доступ через кнопку «Купить доступ»."
        )
        return

    region, expires_at = subscription

    await message.answer(
        "✅ <b>Подписка активна</b>\n\n"
        f"🌍 Регион: {region.upper()}\n"
        f"⏳ Действует до: {expires_at}\n\n"
        "Спасибо, что используете Zero Problem VPN 🚀",
        parse_mode="HTML"
    )


@router.message(F.text == "🔑 Купить доступ")
async def reply_buy_handler(message: Message):
    await message.answer(
        "🌍 Выберите регион:",
        reply_markup=region_menu()
    )


@router.message(F.text == "❓ Помощь")
async def reply_help_handler(message: Message):
    await message.answer(
        "Раздел помощи:",
        reply_markup=help_menu()
    )


@router.message(F.text == "🔙 Назад")
async def reply_back_handler(message: Message):
    await message.answer(
        "Главное меню:",
        reply_markup=platform_menu()
    )


# =========================
# INLINE СЦЕНАРИЙ ПОКУПКИ
# =========================

@router.callback_query(F.data == "buy_start")
async def buy_start_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "🌍 Выберите регион:",
        reply_markup=region_menu()
    )
    await callback.answer()


@router.callback_query(F.data.startswith("region_"))
async def region_selected(callback: CallbackQuery):
    user_id = callback.from_user.id
    region = callback.data.split("_")[1]

    # Если это промо-сценарий
    if user_id in promo_flow_users:
        promo_flow_users.remove(user_id)

        # создаём клиента на сервере
        uuid_value, link = create_vless_client()

        # добавляем подписку на 30 дней
        add_subscription(user_id, region, 30)
        mark_promo_used(user_id)

        await callback.message.edit_text(
            "🎉🎉🎉 ПРОМО ДОСТУП АКТИВИРОВАН! 🎉🎉🎉\n\n"
            f"🌍 Регион: {region.upper()}\n"
            "⏳ Срок: 30 дней\n\n"
            "Вот ваша персональная ссылка:\n\n"
            f"{link}\n\n"
            "Сохраните её."
        )

        await callback.answer()
        return

    # Обычный режим покупки
    await callback.message.edit_text(
        f"🌍 Регион выбран: {region.upper()}\n\n"
        "Выберите тариф:",
        reply_markup=price_menu(region)
    )

    await callback.answer()


@router.callback_query(F.data.startswith("price_"))
async def price_selected(callback: CallbackQuery):
    _, region, period = callback.data.split("_")

    await send_invoice(callback.message, region, period)

    await callback.answer()


@router.callback_query(F.data == "region_locked")
async def region_locked_handler(callback: CallbackQuery):
    await callback.answer("Этот регион скоро будет доступен.", show_alert=True)

# =========================
# INLINE НАВИГАЦИЯ
# =========================

@router.callback_query(F.data == "back_main")
async def back_main_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "🚀 <b>Zero Problem VPN</b>\n\n"
        "Выберите действие ниже 👇",
        reply_markup=start_inline_menu(),
        parse_mode="HTML"
    )
    await callback.answer()


@router.callback_query(F.data == "back_region")
async def back_region_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "🌍 Выберите регион:",
        reply_markup=region_menu()
    )
    await callback.answer()


###ПРОМО###

@router.message()
async def promo_code_handler(message: Message):
    user_id = message.from_user.id

    if user_id not in waiting_for_promo:
        return

    waiting_for_promo.remove(user_id)

    if message.text.strip().upper() == "ШКИБИДИТЬ":
        promo_flow_users.add(user_id)

        await message.answer(
            "🎉 Промо активировано!\n\n"
            "Выберите регион для подключения:",
            reply_markup=region_menu()
        )
    else:
        await message.answer("❌ Неверное кодовое слово.")