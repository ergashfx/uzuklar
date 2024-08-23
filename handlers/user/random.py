from random import randint

from aiogram import types
from aiogram.dispatcher import FSMContext
sonlar = [325]
from handlers.user.admin import create_user
from loader import dp

@dp.message_handler(text="/random")
async def send_rendom(msg:types.Message):
    son = sonlar[0]
    num = randint(253,son)
    await msg.answer_photo(f"https://t.me/testiszlar/{num}")