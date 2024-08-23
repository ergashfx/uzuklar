from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

main = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🧍‍♂️🧍‍♀️ 1 kishilik",callback_data="one"),
        InlineKeyboardButton(text="👩‍❤️‍👨 Juftliklar uchun",callback_data="two")
    ]
])