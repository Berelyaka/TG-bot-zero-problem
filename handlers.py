from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

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
    await message.answer(
        "🚀 <b>Zero Problem VPN</b>\n\n"
        "Быстрый и стабильный доступ к сети без ограничений.\n\n"
        "• ⚡ Высокая скорость\n"
        "• 🔐 Защищённое соединение\n"
        "• 📱 Android, iOS, Windows, macOS\n"
        "• 🔑 Мгновенная выдача ключа\n\n"
        "Выберите действие ниже 👇",
        reply_markup=start_inline_menu(),
        parse_mode="HTML"
    )

    # Постоянная панель
    await message.answer(
        "Главное меню:",
        reply_markup=platform_menu()
    )


# =========================
# REPLY КНОПКИ (ПАНЕЛЬ)
# =========================

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
    region = callback.data.split("_")[1]

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