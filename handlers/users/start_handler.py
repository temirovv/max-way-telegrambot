from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import html

from loader import dp, db

from config.config import LANG
from keyboards.default.level1_kb import menu_buttons


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    text = '''Buyurtma berishni boshlash uchun 🛍 Buyurtma berish tugmasini bosing\n\nShuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin'''
    await message.answer(text, reply_markup=menu_buttons())


    db.add_user(
        tg_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name
    )

