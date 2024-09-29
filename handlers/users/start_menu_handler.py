from aiogram import F
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.fsm.context import FSMContext

from loader import dp, db
from keyboards.default.level2_kb import for_buyurtma_berish_kb, for_yetkazib_berish_kb
from keyboards.default.barcha_filiallar_kb import get_barcha_filiallar
from keyboards.default.categories_kb import get_categories_kb
from keyboards.inline.vacancy_kb import make_vacancy_kb
from keyboards.default.products_kb import make_product_keyboard, make_cart_sub_keyboard
from keyboards.inline.product_inline import product_plus_minus
# states
from states.states_level import BuyurtmaBerishState



@dp.message(F.text == '🛍 Buyurtma berish')
async def buyurtma_berish(message: Message, state: FSMContext):
    await message.answer('Yetkazib berish turini tanlang', reply_markup=for_buyurtma_berish_kb())

@dp.message(F.text == '🎉 Aksiya')
async def aksiya(message: Message, state: FSMContext):
    pass

@dp.message(F.text == '🏘 Barcha filiallar')
async def barcha_filiallar(message: Message, state: FSMContext):
    await message.answer('Bizning filiallarimiz :', reply_markup=get_barcha_filiallar())

@dp.message(F.text == '💼 Vakansiyalar')
async def vakansiyalar(message: Message, state: FSMContext):
    vacancies = db.get_vacancies()
    await message.answer('💼 Vakansiyalar:')

    for title in vacancies:
        await message.answer(text=title[0], reply_markup=make_vacancy_kb(title[0]))


@dp.message(F.text == '🚖 Yetkazib berish')
async def yetkazib_berish(message: Message, state: FSMContext):
    await message.answer('Buyurtmani davom ettirish uchun iltimos lokatsiyangizni yuboring',
                         reply_markup=for_yetkazib_berish_kb())
    
    await state.set_state(BuyurtmaBerishState.yetkazib_berish)


@dp.message(BuyurtmaBerishState.yetkazib_berish)
async def get_user_location_handler(message: Message, state: FSMContext):
    if message.location:
        '''
        Shu yerda foydalanuvchi manzili bazaga saqlash kodi bo'lishi kerak
        '''
        await message.answer('kategoriyalardan birini tanlang', reply_markup=get_categories_kb())
        await state.set_state(BuyurtmaBerishState.select_category)
    else:
        await message.answer('Iltimos lokatsiya yuboring!')


@dp.message(BuyurtmaBerishState.select_category)
async def get_product_category_handler(message: Message, state: FSMContext):
    category_name = message.text
    await state.update_data(category_name=category_name)

    await message.answer('Mahsulotni tanlang:', reply_markup=make_product_keyboard(category_name))
    await state.set_state(BuyurtmaBerishState.product)


async def calculate_price(price, quantity = 1):
    return price * quantity    


@dp.message(F.text == '🛒 savat', BuyurtmaBerishState.product)
async def show_cart_handler(message: Message, state: FSMContext):
    tg_id = message.from_user.id
    carts = db.get_user_cart(tg_id)

    main_text = ''
    for cart in carts:
        name, price, quantity = cart
        main_text += f"{name} x {quantity} = {price*quantity}\n"
    
    await message.answer(main_text)

@dp.message(BuyurtmaBerishState.product)
async def get_product_handler(message: Message, state: FSMContext):
    product_name = message.text
    name, description, price, image = db.get_product_by_name(product_name)
   
    data = await state.get_data()
    quantity = data.get('quantity')
    if not quantity:
        quantity = 1

    jami = await calculate_price(price, quantity)
    await state.update_data(
        quantity=quantity, 
        price=price,
        description=description,
        name=name
        )

    caption = F"{name}\n{description}\n\n{name} {price} x {quantity} = {jami}\numumiy: {jami}"

    photo_file = FSInputFile(path=image)

    

    await message.answer_photo(
        photo=photo_file,
        caption=caption,
        reply_markup=product_plus_minus()
    )



@dp.callback_query(F.data == "plus", BuyurtmaBerishState.product)
async def product_plus_handler(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    quantity = data.get('quantity')
    price = data.get('price')
    name = data.get('name')
    description = data.get('description')
    quantity += 1

    await call.answer('😃')
    await state.update_data(quantity=quantity)
    
    jami = await calculate_price(price, quantity)
    caption = F"{name}\n{description}\n\n{name} {price} x {quantity} = {jami}\numumiy: {jami}"

    await call.message.edit_caption(
        caption=caption, 
        reply_markup=product_plus_minus(quantity))
 

@dp.callback_query(F.data == "minus", BuyurtmaBerishState.product)
async def product_plus_handler(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    quantity = data.get('quantity')
    price = data.get('price')
    name = data.get('name')
    description = data.get('description')

    if quantity != 1:
        quantity -= 1
        await call.answer('😢')
        await state.update_data(quantity=quantity)
    

    jami = await calculate_price(price, quantity)
    caption = F"{name}\n{description}\n\n{name} {price} x {quantity} = {jami}\numumiy: {jami}"

    await call.message.edit_caption(
        caption=caption, 
        reply_markup=product_plus_minus(quantity))


@dp.callback_query(F.data == 'add_to_cart', BuyurtmaBerishState.product)
async def add_to_cart_handler(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    name = data.get('name')
    quantity = data.get('quantity')
    tg_id = call.from_user.id
    
    db.add_to_cart(name, quantity, tg_id)

    await call.message.answer('Mahsulot savatga qo\'shildi', reply_markup=make_cart_sub_keyboard())
    
    await call.message.delete()


