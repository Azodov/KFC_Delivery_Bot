from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     validate_data = "19/02/2022"
#     year = validate_data.split("/")[-1]
#     month = validate_data.split("/")[-2]
#     day = validate_data.split("/")[-3]
#     if int(year) > 2021:
#         await message.answer("Bot is active")
#         return
#     await message.answer(f"Salom, {message.from_user.full_name}!")
