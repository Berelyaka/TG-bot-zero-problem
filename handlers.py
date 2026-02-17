from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards import platform_menu, help_menu
from aiogram.filters import Command
from payment import (
    send_invoice_handler,
    pre_checkout_handler,
    success_payment_handler,
    pay_support_handler
)

router = Router()

router.message.register(send_invoice_handler, Command("donate"))
router.pre_checkout_query.register(pre_checkout_handler)
router.message.register(success_payment_handler, F.successful_payment)
router.message.register(pay_support_handler, Command("paysupport"))

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Привет",
        reply_markup=platform_menu()
    )


@router.message(F.text == "📎 Android")
async def android_handler(message: Message):
    await message.answer("Инструкция для Android: ")


@router.message(F.text == "📎 IOS")
async def ios_handler(message: Message):
    await message.answer("Инструкция для IOS ")


@router.message(F.text == "💻 Windows/MAC")
async def windows_handler(message: Message):
    await message.answer("Инструкция для Windows/MAC ")


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


@router.message(F.text == "🚀 Купить доступ")
async def buy_handler(message: Message):
    await message.answer("Раздел покупки (пока заглушка)")


@router.message(F.text == "📄 Мой аккаунт")
async def account_handler(message: Message):
    await message.answer("Раздел аккаунта (пока заглушка)")


@router.message(F.text == "ℹ️ Поддержка")
async def support_handler(message: Message):
    await message.answer("Поддержка: @your_support_username")
