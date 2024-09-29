from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def product_plus_minus(number=1):
    menu = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='➕', callback_data='plus'),
                InlineKeyboardButton(text=f'{number}', callback_data=f'number.{number}'),
                InlineKeyboardButton(text='➖', callback_data='minus')
            ],
            [
                InlineKeyboardButton(text='🛒 Savatga qo\'shish', callback_data='add_to_cart')
            ]
        ]
    )

    return menu
