from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

from filters import IsUser
from keyboards.inline.user_buttons import main_menu_btn_uz, main_menu_btn_ru, main_menu_btn_en
from loader import dp, bot, db


@dp.message_handler(IsUser(), content_types=types.ContentTypes.ANY)
async def bot_start(message: types.Message):
    lang_code = db.select_user(id=message.from_user.id)[3]
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
    location_user = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
    location_user.add(KeyboardButton("📍 Geo-joylashuvni jo'nating", request_location=True))
    location_user.add(KeyboardButton("🔙 Orqaga"))
    await call.message.answer("Yetkazib berish uchun geo-joylashuvni jo'nating",
                              reply_markup=location_user)
    await state.set_state("get_location")


@dp.message_handler(IsUser(), content_types=types.ContentType.LOCATION, state="get_location")
async def location(message: types.Message, state: FSMContext):
    await message.answer("📍 Geo-joylashuv jo'natildi", reply_markup=ReplyKeyboardRemove())
    await state.update_data()
    await state.finish()


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
