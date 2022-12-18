from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

location = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
location.add(KeyboardButton("📍 Geo-joylashuvni jo'nating", request_location=True))
