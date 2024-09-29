from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from loader import db


def make_product_keyboard(category_name: str):
    products = db.get_products_by_category_name(category_name)
    buttons = []

    menu = ReplyKeyboardBuilder()
    menu.max_width = 2

    for product in products:
        buttons.append(
            KeyboardButton(text=product[0])
        )

    menu.row(*buttons)

    return menu.as_markup()

def make_cart_sub_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='◀️ orqaga'),
                KeyboardButton(text="🛒 savat")
            ]
        ],
        resize_keyboard=True
    )