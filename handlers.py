from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards import platform_menu, help_menu, buy_menu, region_menu, price_menu
from aiogram.filters import Command
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from keyboards import start_inline_menu
from payment import (
    low_price_handler,
    cheap_price_handler,
    medium_price_handler,
    rich_price_handler,
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
        "Hi",
        reply_markup=platform_menu()
)
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



@router.callback_query(F.data == "buy_key")
async def buy_key_handler(callback: CallbackQuery):
    await callback.message.edit_text(
        "🌍 Выберите регион для подключения:",
        reply_markup=region_menu()
    )
    await callback.answer()



@router.message(F.text == "Купить ключ")
async def show_region_menu(message: Message):
    await message.answer(
        "🌍 Выберите регион для подключения:",
        reply_markup=region_menu()
    )



@router.callback_query(F.data.startswith("region_"))
async def region_selected(callback: CallbackQuery):
    region = callback.data.split("_")[1]

    await callback.message.delete()

    
    await callback.message.answer(
        f"🌍 Регион выбран: {region.upper()}\n\n"
        "Выберите тариф:",
        reply_markup=price_menu()
    )

    await callback.answer()





router.message.register(
    low_price_handler,
    F.text == "1 мес - 1$"
)



router.message.register(
    cheap_price_handler,
    F.text == "3 мес - 2$"
)



router.message.register(
    medium_price_handler,
    F.text == "6 мес - 3$"
)



router.message.register(
    rich_price_handler,
    F.text == "12 мес - 5$"
)


@router.callback_query(F.data == "back_to_main")
async def back_to_main(callback: CallbackQuery):
    await callback.message.edit_text(
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
    await callback.answer()




@router.message(F.text == "FAQ")
async def show_help_menu(message: Message):
    await message.answer(
        "Меню поддержки:",
        reply_markup=help_menu()
    )



@router.message(F.text == "Назад")
async def show_main_menu(message: Message):
     await message.answer(
        "Hi",
        reply_markup=platform_menu()
    )
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