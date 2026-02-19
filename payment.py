from aiogram.types import LabeledPrice, Message  
from aiogram.types import PreCheckoutQuery
from klava_oplata import payment_keyboard, payment_keyboard2 , payment_keyboard3 , payment_keyboard4   



async def low_price_handler(message: Message):  
    prices = [LabeledPrice(label="XTR", amount=100)]  
    await message.answer_invoice(  
        title="Покупка ключа",  
        description="Купить ключ доступа за 100 звёзд!",  
        prices=prices,  
        provider_token="",  
        payload="channel_support",  
        currency="XTR",  
        reply_markup=payment_keyboard(),  
    )



async def cheap_price_handler(message: Message):  
    prices = [LabeledPrice(label="XTR", amount=200)]  
    await message.answer_invoice(  
        title="Покупка ключа",  
        description="Купить ключ доступа за 200 звёзд!",  
        prices=prices,  
        provider_token="",  
        payload="channel_support",  
        currency="XTR",  
        reply_markup=payment_keyboard2(),  
    )



async def medium_price_handler(message: Message):  
    prices = [LabeledPrice(label="XTR", amount=300)]  
    await message.answer_invoice(  
        title="Покупка ключа",  
        description="Купить ключ доступа за 300 звёзд!",  
        prices=prices,  
        provider_token="",  
        payload="channel_support",  
        currency="XTR",  
        reply_markup=payment_keyboard3(),  
    )



async def rich_price_handler(message: Message):  
    prices = [LabeledPrice(label="XTR", amount=500)]  
    await message.answer_invoice(  
        title="Покупка ключа",  
        description="Купить ключ доступа за 500 звёзд!",  
        prices=prices,  
        provider_token="",  
        payload="channel_support",  
        currency="XTR",  
        reply_markup=payment_keyboard4(),  
    )



async def pre_checkout_handler(pre_checkout_query: PreCheckoutQuery):  
    await pre_checkout_query.answer(ok=True)



async def success_payment_handler(message: Message):  
    await message.answer(text="🥳Спасибо за вашу поддержку!🤗")



async def pay_support_handler(message: Message):  
    await message.answer(  
        text="Добровольные пожертвования не подразумевают возврат средств, "  
        "однако, если вы очень хотите вернуть средства - свяжитесь с нами."    )