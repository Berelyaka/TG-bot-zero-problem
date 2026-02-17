from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards import platform_menu, help_menu, buy_menu
from aiogram.filters import Command
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import F
from keyboards import start_inline_menu
from payment import (
    send_invoice_handler,
    pre_checkout_handler,
    success_payment_handler,
    pay_support_handler
)

router = Router()


router.pre_checkout_query.register(pre_checkout_handler)
router.message.register(success_payment_handler, F.successful_payment)
router.message.register(pay_support_handler, Command("paysupport"))


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
    "🚀 <b>Zero Problem VPN</b>\n\n"
    "Быстрый и стабильный доступ к сети без ограничений.\n\n"
    "Подключение занимает меньше минуты:\n"
    "• ⚡ Высокая скорость без просадок\n"
    "• 🔐 Защищённое соединение\n"
    "• 📱 Поддержка Android, iOS Windows и MAC\n"
    "• 🔑 Мгновенная выдача ключа после оплаты\n\n"
    "Никаких сложных настроек — вы получаете готовый доступ и простую инструкцию.\n\n"
    "Нажмите кнопку ниже, чтобы получить ключ и начать пользоваться сервисом.",
    reply_markup=start_inline_menu(),
    parse_mode="HTML"
)

@router.message(F.text == "Купить ключ")
async def show_buy_menu(message: Message):
    await message.answer(
        "Выберите метод оплаты: ",
        reply_markup=buy_menu()
    )

router.message.register(
    send_invoice_handler,
    F.text == "Stars"
)



@router.message(F.text == "FAQ")
async def show_help_menu(message: Message):
    await message.answer(
        "Меню поддержки:",
        reply_markup=help_menu()
    )

@router.message(F.text == "Назад")
async def show_main_menu(message: Message):
    await message.answer(
        reply_markup=platform_menu()
    )

@router.message(F.text == "Назад")
async def show_main_menu(message: Message):
     await message.answer(
    "🚀 <b>Zero Problem VPN</b>\n\n"
    "Быстрый и стабильный доступ к сети без ограничений.\n\n"
    "Подключение занимает меньше минуты:\n"
    "• ⚡ Высокая скорость без просадок\n"
    "• 🔐 Защищённое соединение\n"
    "• 📱 Поддержка Android, iOS Windows и MAC\n"
    "• 🔑 Мгновенная выдача ключа после оплаты\n\n"
    "Никаких сложных настроек — вы получаете готовый доступ и простую инструкцию.\n\n"
    "Нажмите кнопку ниже, чтобы получить ключ и начать пользоваться сервисом.",
    reply_markup=start_inline_menu(),
    parse_mode="HTML"
)