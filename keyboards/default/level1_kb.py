from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def language_buttons():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='O’zbekcha'), 
                KeyboardButton(text='Русский'), 
                KeyboardButton(text='English')]
        ]
    )

def menu_buttons():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='🛍 Buyurtma berish')],
            [KeyboardButton(text='🎉 Aksiya'), KeyboardButton(text='🏘 Barcha filiallar')]
        ],
        resize_keyboard=True
    )
