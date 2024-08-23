from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

group = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Guruhga kirish",url="https://t.me/+yS41sUjfl-szMTc0"),
        InlineKeyboardButton(text="Tekshirish",callback_data="check_subs"),
    ],
])