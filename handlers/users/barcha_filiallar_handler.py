from aiogram import F
from aiogram.types import Message

from loader import dp


@dp.message(F.text == 'MAX WAY ALAYSKIY')
async def get_branch1(message: Message):
    text = '📍 Filial:  MAX WAY ALAYSKIY \n\n🗺 Manzil:  проспект Амира Темура, 25\n\n🏢 Orientir:\n\n☎️ Telefon raqami:  +998712005400\n\n🕙 Ish vaqti : 10:00 - 03:00'
    
    await message.answer(text)
    await message.answer_location(
        latitude=41.318379,
        longitude=69.280708
    )



