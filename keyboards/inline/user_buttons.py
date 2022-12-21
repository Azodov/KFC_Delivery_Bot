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


order_menu_btn_uz = InlineKeyboardMarkup(row_width=2)

order_menu_btn_uz.add(InlineKeyboardButton(text="🍔 BURGERLAR", callback_data="burgers"))
order_menu_btn_uz.add(InlineKeyboardButton(text="🍗 TOVUQ", callback_data="chickens"))
order_menu_btn_uz.add(InlineKeyboardButton(text="🌯 TWISTERLAR", callback_data="twisters"))
order_menu_btn_uz.add(InlineKeyboardButton(text="🥡 BASKETLAR", callback_data="baskets"))
order_menu_btn_uz.add(InlineKeyboardButton(text="🍟🍔🥤 LANCHBOXLAR", callback_data="lunchboxes"))
order_menu_btn_uz.add(InlineKeyboardButton(text="🍦🥮 DESSERTLAR", callback_data="desserts"))
order_menu_btn_uz.add(InlineKeyboardButton(text="🍟 KARTOFEL VA SNEKLAR", callback_data="fries_and_snacks"))
order_menu_btn_uz.add(InlineKeyboardButton(text="🥫 SOUSLAR", callback_data="souces"))
order_menu_btn_uz.add(InlineKeyboardButton(text="🥤 SALQIN ICHIMLIKLAR", callback_data="drinks"))
order_menu_btn_uz.add(InlineKeyboardButton(text="☕️ KOFE / CHOY", callback_data="coffee__and_tea"))

order_menu_btn_ru = InlineKeyboardMarkup(row_width=2)

order_menu_btn_ru.add(InlineKeyboardButton(text="🍔 БУРГЕРЫ", callback_data="burgers"))
order_menu_btn_ru.add(InlineKeyboardButton(text="🍗 КУРИЦА", callback_data="chickens"))
order_menu_btn_ru.add(InlineKeyboardButton(text="🌯 ТВИСТЕРЫ", callback_data="twisters"))
order_menu_btn_ru.add(InlineKeyboardButton(text="🥡 БАСКЕТЫ", callback_data="baskets"))
order_menu_btn_ru.add(InlineKeyboardButton(text="🍟🍔🥤 ЛАНЧБОКСЫ", callback_data="lunchboxes"))
order_menu_btn_ru.add(InlineKeyboardButton(text="🍦🥮 ДЕСЕРТЫ", callback_data="desserts"))
order_menu_btn_ru.add(InlineKeyboardButton(text="🍟 КАРТОФЕЛЬ И СНЭКИ", callback_data="fries_and_snacks"))
order_menu_btn_ru.add(InlineKeyboardButton(text="🥫 СОУСЫ", callback_data="souces"))
order_menu_btn_ru.add(InlineKeyboardButton(text="🥤 НАПИТКИ", callback_data="drinks"))
order_menu_btn_ru.add(InlineKeyboardButton(text="☕️ КОФЕ / ЧАЙ", callback_data="coffee__and_tea"))

order_menu_btn_en = InlineKeyboardMarkup(row_width=2)

order_menu_btn_en.add(InlineKeyboardButton(text="🍔 BURGERS", callback_data="burgers"))
order_menu_btn_en.add(InlineKeyboardButton(text="🍗 CHICKEN", callback_data="chickens"))
order_menu_btn_en.add(InlineKeyboardButton(text="🌯 TWISTERS", callback_data="twisters"))
order_menu_btn_en.add(InlineKeyboardButton(text="🥡 BASKETS", callback_data="baskets"))
order_menu_btn_en.add(InlineKeyboardButton(text="🍟🍔🥤 LUNCHBOXES", callback_data="lunchboxes"))
order_menu_btn_en.add(InlineKeyboardButton(text="🍦🥮 DESSERTS", callback_data="desserts"))
order_menu_btn_en.add(InlineKeyboardButton(text="🍟 FRIES AND SNACKS", callback_data="fries_and_snacks"))
order_menu_btn_en.add(InlineKeyboardButton(text="🥫 SOUCES", callback_data="souces"))
order_menu_btn_en.add(InlineKeyboardButton(text="🥤 DRINKS", callback_data="drinks"))
order_menu_btn_en.add(InlineKeyboardButton(text="☕️ COFFEE / TEA", callback_data="coffee__and_tea"))

