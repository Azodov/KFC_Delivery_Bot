import re

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart

from filters.users import *
from keyboards.universal.guest_buttons import request_phone_uz, lang, request_phone_ru, request_phone_en, \
    confirm_phone_uz, confirm_phone_ru, confirm_phone_en

from keyboards.inline.user_buttons import main_menu_btn_uz, main_menu_btn_ru, main_menu_btn_en
from loader import dp, db, bot


@dp.message_handler(IsGuest(), CommandStart(), state="*")
async def bot_start(message: types.Message):
    bot_username = (await bot.me).full_name

    await message.answer(f"👋 Assalom alaykum {message.from_user.full_name} "
                         f"{bot_username} ga xush kelibsiz!\n\n"
                         f"👋 Здраствуйте {message.from_user.full_name} "
                         f"добро пожаловать в {bot_username}!\n\n"
                         f"👋 Hi {message.from_user.full_name} "
                         f"welcome to {bot_username}!\n\n"
                         f"🇺🇿 Tilni tanlang...\n"
                         f"🇷🇺 Выберите язык...\n"
                         f"🇺🇸 Choose language...", reply_markup=lang)


@dp.callback_query_handler(text_contains="lang_", state="*")
async def choose_language(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.delete()
    lang_code = call.data.split("_")[1]
    await state.update_data(lang=lang_code)
    if lang_code == "uz":
        await call.message.answer(f"Botdan foydalanish uchun Telefon raqamingizni yuboring.\n"
                                  f"Masalan: +998 90 123 45 67", reply_markup=request_phone_uz)
    elif lang_code == "ru":
        await call.message.answer(f"Отправьте свой номер телефона для использования бота.\n"
                                  f"Пример: +998 90 123 45 67", reply_markup=request_phone_ru)
    elif lang_code == "en":
        await call.message.answer(f"Send your phone number to use the bot.\n"
                                  f"Example: +998 90 123 45 67", reply_markup=request_phone_en)


@dp.message_handler(IsGuest(), content_types=types.ContentTypes.CONTACT, state="*")
@dp.message_handler(IsGuest(), state="*", content_types=types.ContentTypes.TEXT)
async def get_phone_number(message: types.Message, state: FSMContext):
    data = await state.get_data()
    lang_code = data.get("lang")
    match_number = r'''^(\+998|998)(90|91|99|77|94|93|95|97|98|88|33){1}\d{7}$'''
    phone_number = ""

    if message.contact and re.match(match_number, message.contact.phone_number):
        phone_number = message.contact.phone_number
    elif message.text and re.match(match_number, message.text):
        phone_number = message.text
    else:
        if lang_code == "uz":
            await message.answer(f"❌ Telefon raqam xato kiritildi!\n"
                                 f"Masalan: +998 90 123 45 67", reply_markup=request_phone_uz)
        elif lang_code == "ru":
            await message.answer(f"❌ Отправьте правильный номер телефона!\n"
                                 f"Пример: +998 90 123 45 67", reply_markup=request_phone_ru)
        elif lang_code == "en":
            await message.answer(f"❌ Send the correct phone number!\n"
                                 f"Example: +998 90 123 45 67", reply_markup=request_phone_en)
        return

    if phone_number:
        if lang_code == "uz":
            await message.answer(f"📲 {phone_number} raqamni tasdiqlaysizmi?", reply_markup=confirm_phone_uz)
        elif lang_code == "ru":
            await message.answer(f"📲 Вы уверены что хотите подтвердить {phone_number}?", reply_markup=confirm_phone_ru)
        elif lang_code == "en":
            await message.answer(f"📲 Are you sure you want to confirm {phone_number}?", reply_markup=confirm_phone_en)
        await state.update_data(phone_number=phone_number)


@dp.callback_query_handler(text_contains="phone_", state="*")
async def confirm_phone(call: types.CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    await call.message.delete()
    data = await state.get_data()
    lang_code = data.get("lang")
    phone_number = data.get("phone_number")
    status = call.data.split("_")[-1]
    if status == "confirm":
        if lang_code == "uz":
            await call.message.answer(f"✅ Siz muvaffaqiyatli ro'yxatdan o'tdingiz!\n"
                                      f"☺️ O'zingizga kerakli xizmatni tanlang.", reply_markup=main_menu_btn_uz)
        elif lang_code == "ru":
            await call.message.answer(f"✅ Вы успешно зарегистрировались!\n"
                                      f"☺️ Выберите необходимую услугу.", reply_markup=main_menu_btn_ru)
        elif lang_code == "en":
            await call.message.answer(f"✅ You have successfully registered!\n"
                                      f"☺️ Choose the service you need.", reply_markup=main_menu_btn_en)
        await state.finish()
        db.add_user(id=call.from_user.id, full_name=call.from_user.full_name, phone_number=phone_number, lang=lang_code)
    elif status == "cancel":
        if lang_code == "uz":
            await call.message.answer(f"📲 {phone_number} raqamni tasdiqlamadingiz!")
        elif lang_code == "ru":
            await call.message.answer(f"📲 Вы не подтвердили {phone_number}!")
        elif lang_code == "en":
            await call.message.answer(f"📲 You did not confirm {phone_number}!")
        await state.finish()
        await state.reset_data()
        await call.message.answer(f"🇺🇿 Tilni tanlang...\n"
                                  f"🇷🇺 Выберите язык...\n"
                                  f"🇺🇸 Choose language...", reply_markup=lang)
