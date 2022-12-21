from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from filters import IsUser
from keyboards.inline.user_buttons import main_menu_btn_uz, main_menu_btn_ru, main_menu_btn_en, order_menu_btn_uz, \
    order_menu_btn_ru, order_menu_btn_en
from loader import dp, bot, db


@dp.message_handler(IsUser(), content_types=types.ContentTypes.ANY)
async def bot_start(message: types.Message, state: FSMContext):
    lang_code = db.select_user(id=message.from_user.id)[3]
    await state.update_data(lang_code=lang_code)
    if lang_code == "uz":
        await message.answer("👋 Assalom alaykum!\n"
                             "☺️ O'zingizga kerakli xizmatni tanlang.", reply_markup=main_menu_btn_uz)
    elif lang_code == "ru":
        await message.answer("👋 Здраствуйте!\n"
                             "☺️ Выберите нужный сервис.", reply_markup=main_menu_btn_ru)
    elif lang_code == "en":
        await message.answer("👋 Hi!\n"
                             "☺️ Choose the service you need.", reply_markup=main_menu_btn_en)


@dp.callback_query_handler(IsUser(), text="order", state="*")
async def order(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=1)
    await call.message.delete()
    lang_code = await state.get_data()
    lang_code = lang_code.get("lang_code")
    location_user = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
    if lang_code == "uz":
        location_user.add(KeyboardButton("📍 Geo-joylashuvni jo'nating", request_location=True))
        location_user.add(KeyboardButton("🔙 Orqaga"))
        await call.message.answer("Yetkazib berish uchun geo-joylashuvni jo'nating",
                                  reply_markup=location_user)
    elif lang_code == "ru":
        location_user.add(KeyboardButton("📍 Отправить гео-локацию", request_location=True))
        location_user.add(KeyboardButton("🔙 Назад"))
        await call.message.answer("Отправьте гео-локацию для доставки",
                                  reply_markup=location_user)
    else:
        location_user.add(KeyboardButton("📍 Send geo-location", request_location=True))
        location_user.add(KeyboardButton("🔙 Back"))
        await call.message.answer("Send a geo-location for delivery",
                                  reply_markup=location_user)
    await state.set_state("get_location")


@dp.message_handler(IsUser(), content_types=types.ContentType.LOCATION, state="get_location")
async def location(message: types.Message, state: FSMContext):
    await state.update_data(location=message.location)
    lang_code = await state.get_data()
    lang_code = lang_code.get("lang_code")
    order_menu_btn_uz = order_menu_btn_uz
    if lang_code == "uz":
        await message.answer("👌 Geo-joylashuvingiz muvaffaqiyatli jo'natildi.", reply_markup=ReplyKeyboardRemove())
        await message.answer("Quydagilardan birini tanlang:", reply_markup=order_menu_btn_uz)
    elif lang_code == "ru":
        await message.answer("👌 Ваша гео-локация успешно отправлена.", reply_markup=ReplyKeyboardRemove())
        await message.answer("Выберите один из следующих:", reply_markup=order_menu_btn_ru)
    else:
        await message.answer("👌 Your geo-location was successfully sent.", reply_markup=ReplyKeyboardRemove())
        await message.answer("Choose one of the following:", reply_markup=order_menu_btn_en)

    await state.finish()


@dp.callback_query_handler(IsUser(), text="back", state="*")
async def back(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=1)
    await call.message.delete()
    lang_code = await state.get_data()
    lang_code = lang_code.get("lang_code")
    if lang_code == "uz":
        await call.message.answer("👋 Assalom alaykum!\n"
                                  "☺️ O'zingizga kerakli xizmatni tanlang.", reply_markup=main_menu_btn_uz)
    elif lang_code == "ru":
        await call.message.answer("👋 Здраствуйте!\n"
                                  "☺️ Выберите нужный сервис.", reply_markup=main_menu_btn_ru)
    elif lang_code == "en":
        await call.message.answer("👋 Hi!\n"
                                  "☺️ Choose the service you need.", reply_markup=main_menu_btn_en)


@dp.message_handler(IsUser(), content_types=types.ContentType.TEXT, state="get_location", text="🔙 Orqaga")
async def back_to_main_menu_method(message: types.Message):
    lang_code = db.select_user(id=message.from_user.id)[3]
    await message.answer("👋 Sizni yana korganimdan xursandman...\n", reply_markup=ReplyKeyboardRemove())
    if lang_code == "uz":
        await message.answer("👋 Assalom alaykum!\n"
                             "☺️ O'zingizga kerakli xizmatni tanlang.", reply_markup=main_menu_btn_uz)
    elif lang_code == "ru":
        await message.answer("👋 Здраствуйте!\n"
                             "☺️ Выберите нужный сервис.", reply_markup=main_menu_btn_ru)
    elif lang_code == "en":
        await message.answer("👋 Hi!\n"
                             "☺️ Choose the service you need.", reply_markup=main_menu_btn_en)
