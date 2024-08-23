from aiogram import types

from data.config import texts
from handlers.user.admin import create_user
from loader import dp, bot
from keyboards.inline.main import main
from data.config import CHANNELS
from keyboards.inline.group import group
from utils.misc.subscription import check
from filters.private import IsPrivate


@dp.message_handler(IsPrivate())
async def test(msg: types.Message):
    user = msg.from_user.id
    text_request_text = texts["text_to_start"]
    result = f"{text_request_text}:\n"
    final_status = True
    chs = []
    for channel in CHANNELS:
        status = await check(
            user_id=user,
            channel=channel
        )
        final_status *= status
        channel = await bot.get_chat(channel)
        if not status:
            await msg.answer(texts["text_to_start"], reply_markup=group, parse_mode="markdown")
        else:
            await msg.answer(texts['accepted'], reply_markup=main, parse_mode="markdown")
