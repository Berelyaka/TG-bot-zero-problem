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
        "Добро пожаловать в Zero Problem VPN.\n\n"
        "Сервис обеспечивает стабильное и защищённое соединение.\n\n"
        "• Быстрое подключение\n"
        "• Поддержка Android / iOS / Windows / MAC \n"
        "• Мгновенная выдача ключа после оплаты\n\n"
        "Для начала выберите действие ниже.",
        reply_markup=start_inline_menu()
    )



@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Привет",
        reply_markup=platform_menu()
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
async def show_help_menu(message: Message):
    await message.answer(
        "Привет",
        reply_markup=platform_menu()
    )

