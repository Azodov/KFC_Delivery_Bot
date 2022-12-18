from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

lang = InlineKeyboardMarkup(row_width=1)

lang.add(InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="lang_uz"),
         InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru"),
         InlineKeyboardButton(text="🇺🇸 English", callback_data="lang_en"))

request_phone_uz = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
request_phone_uz.add(KeyboardButton(text="📲 Telefon raqamni yuborish", request_contact=True))

request_phone_ru = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
request_phone_ru.add(KeyboardButton(text="📲 Отправить номер телефона", request_contact=True))

request_phone_en = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
request_phone_en.add(KeyboardButton(text="📲 Send phone number", request_contact=True))


confirm_phone_uz = InlineKeyboardMarkup(row_width=2)
confirm_phone_uz.add(InlineKeyboardButton(text="✅ Tasdiqlash", callback_data="phone_confirm"),
                        InlineKeyboardButton(text="❌ Bekor qilish", callback_data="phone_cancel"))

confirm_phone_ru = InlineKeyboardMarkup(row_width=2)
confirm_phone_ru.add(InlineKeyboardButton(text="✅ Подтвердить", callback_data="phone_confirm"),
                        InlineKeyboardButton(text="❌ Отмена", callback_data="phone_cancel"))

confirm_phone_en = InlineKeyboardMarkup(row_width=2)
confirm_phone_en.add(InlineKeyboardButton(text="✅ Confirm", callback_data="phone_confirm"),
                        InlineKeyboardButton(text="❌ Cancel", callback_data="phone_cancel"))


