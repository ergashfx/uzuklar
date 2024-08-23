from aiogram import types
from aiogram.dispatcher import FSMContext

from handlers.user.admin import create_user
from loader import dp
from keyboards.inline.main import main

from data.config import texts
@dp.message_handler(text=["/start", "Ortga qaytish"])
async def welcome(msg: types.Message, state: FSMContext):
    name = msg.from_user.full_name
    await msg.answer(texts["main_menu"], reply_markup=main,parse_mode="markdown")
    await state.finish()
