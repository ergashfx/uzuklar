from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

cancel = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Bekor qilish",callback_data="cancel"),
    ],
])