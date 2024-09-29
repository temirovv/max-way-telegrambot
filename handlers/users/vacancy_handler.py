from aiogram import F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from loader import dp

from states.states_level import VacancyState


@dp.callback_query(F.data.startswith('vacancy'))
async def vacancy_callback_query_handler(call: CallbackQuery, state: FSMContext):
    data = call.data.split(":")[-1]
    # statega o'tkazasila
    # saqlash
    # await state.update_data(vacancy=data)
    await call.message.answer()


@dp.message(VacancyState.fio)
async def get_fio(message: Message, state: FSMContext):
    fio = message.text

    await state.update_data(fio=fio)
