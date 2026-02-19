from aiogram.utils.keyboard import InlineKeyboardBuilder  
  
  
  
def payment_keyboard():  
    builder = InlineKeyboardBuilder()  
    builder.button(text=f"Оплатить 100 ⭐️", pay=True)  
  
    return builder.as_markup()



def payment_keyboard2():  
    builder = InlineKeyboardBuilder()  
    builder.button(text=f"Оплатить 200 ⭐️", pay=True)  
  
    return builder.as_markup()



def payment_keyboard3():  
    builder = InlineKeyboardBuilder()  
    builder.button(text=f"Оплатить 300 ⭐️", pay=True)  
  
    return builder.as_markup()



def payment_keyboard4():  
    builder = InlineKeyboardBuilder()  
    builder.button(text=f"Оплатить 500 ⭐️", pay=True)  
  
    return builder.as_markup()