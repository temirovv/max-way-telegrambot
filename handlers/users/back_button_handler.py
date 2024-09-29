from aiogram import F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from loader import dp
from keyboards.default.level1_kb import menu_buttons
from keyboards.default.level2_kb import for_buyurtma_berish_kb
from states.states_level import BuyurtmaBerishState


@dp.message(F.text == '⬅️ Orqaga', BuyurtmaBerishState.yetkazib_berish)
async def back_to_buyurtma_berish(message: Message, state: FSMContext):
    await message.answer(
        text='Yetkazib berish turini tanlang', 
        reply_markup=for_buyurtma_berish_kb())
    await state.clear()


@dp.message(F.text == '⬅️ Orqaga')
async def main_back_btn_handler(message: Message):
    text = '''Buyurtma berishni boshlash uchun 🛍 Buyurtma berish tugmasini bosing\n\nShuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin'''
    await message.answer(text, reply_markup=menu_buttons())

