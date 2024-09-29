from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def for_buyurtma_berish_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='🚖 Yetkazib berish'), KeyboardButton(text='🏃 Olib ketish')],
            [KeyboardButton(text='⬅️ Orqaga')]
        ],
        resize_keyboard=True
    )


def for_yetkazib_berish_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Lokatsiya yuborish', request_location=True)],
            [KeyboardButton(text='⬅️ Orqaga')]
        ],
        resize_keyboard=True
    )
