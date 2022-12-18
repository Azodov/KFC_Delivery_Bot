from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu_btn_uz = InlineKeyboardMarkup(row_width=1)

main_menu_btn_uz.add(InlineKeyboardButton(text="📝 Buyurtma berish", callback_data="order"))
main_menu_btn_uz.add(InlineKeyboardButton(text="📦 Buyurtmalarim", callback_data="my_orders"))
main_menu_btn_uz.add(InlineKeyboardButton(text="✍️ Fikr bildirish", callback_data="feedback"))
main_menu_btn_uz.add(InlineKeyboardButton(text="📞 Aloqa", callback_data="contact"))

main_menu_btn_ru = InlineKeyboardMarkup(row_width=1)

main_menu_btn_ru.add(InlineKeyboardButton(text="📝 Оформить заказ", callback_data="order"))
main_menu_btn_ru.add(InlineKeyboardButton(text="📦 Мои заказы", callback_data="my_orders"))
main_menu_btn_ru.add(InlineKeyboardButton(text="✍️ Оставить отзыв", callback_data="feedback"))
main_menu_btn_ru.add(InlineKeyboardButton(text="📞 Контакты", callback_data="contact"))

main_menu_btn_en = InlineKeyboardMarkup(row_width=1)

main_menu_btn_en.add(InlineKeyboardButton(text="📝 Order", callback_data="order"))
main_menu_btn_en.add(InlineKeyboardButton(text="📦 My orders", callback_data="my_orders"))
main_menu_btn_en.add(InlineKeyboardButton(text="✍️ Feedback", callback_data="feedback"))
main_menu_btn_en.add(InlineKeyboardButton(text="📞 Contact", callback_data="contact"))
