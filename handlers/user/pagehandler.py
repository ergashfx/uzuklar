from time import sleep

from data.states import User

sonlar = [325]
from random import randint
from aiogram import types
from aiogram.dispatcher import FSMContext
# from data.config import texts
# from handlers.user.admin import create_user
from loader import dp
from aiogram.types import CallbackQuery
# from keyboards.inline.main import main
from keyboards.inline.pages import page1, page2, page3, bet1, bet3, bet2, page4, page5, page6, page7, page01, page02, \
    page03, page04, page8, page9, bet4, bet5, page10, page11, page12
from states.NameCollection import Ismlar, Ismlar2


@dp.callback_query_handler(text="one")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://t.me/testiszlar/245",
                                    caption="Kerakli rasmni tanlang", reply_markup=page01)


@dp.callback_query_handler(text="next01")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://t.me/testiszlar/246",
                                    caption="Kerakli rasmni tanlang", reply_markup=page02)


@dp.callback_query_handler(text="next02")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://t.me/testiszlar/247",
                                    caption="Kerakli rasmni tanlang", reply_markup=page03)


@dp.callback_query_handler(text="next03")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://t.me/testiszlar/248",
                                    caption="Kerakli rasmni tanlang", reply_markup=page04)


@dp.callback_query_handler(text="back04")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://t.me/testiszlar/247",
                                    caption="Kerakli rasmni tanlang", reply_markup=page03)


@dp.callback_query_handler(text="back03")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://t.me/testiszlar/246",
                                    caption="Kerakli rasmni tanlang", reply_markup=page02)


@dp.callback_query_handler(text="back02")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://t.me/testiszlar/245",
                                    caption="Kerakli rasmni tanlang", reply_markup=page01)


@dp.callback_query_handler(text="back1")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://t.me/testiszlar/248",
                                    caption="Kerakli rasmni tanlang", reply_markup=page04)


@dp.callback_query_handler(text="two")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://telegra.ph//file/bdfcc2dc951b7de244fb8.jpg",
                                    caption="Kerakli rasmni tanlang", reply_markup=bet1)


#
#
@dp.callback_query_handler(text="next04")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://telegra.ph//file/cdbe155c6986cf3d67522.jpg",
                                    caption="Kerakli rasmni tanlang", reply_markup=page1)


@dp.callback_query_handler(text="next1")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://telegra.ph//file/13dea56aeda2d35e8057b.jpg",
                                    caption="Kerakli rasmni tanlang", reply_markup=page2)


@dp.callback_query_handler(text="next2")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://telegra.ph//file/42b791e3b30cfe94f2809.jpg",
                                    caption="Kerakli rasmni tanlang", reply_markup=page3)


@dp.callback_query_handler(text="next3")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://t.me/testiszlar/241",
                                    caption="Kerakli rasmni tanlang", reply_markup=page4)


@dp.callback_query_handler(text="next4")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://t.me/testiszlar/242",
                                    caption="Kerakli rasmni tanlang", reply_markup=page5)


@dp.callback_query_handler(text="next5")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://t.me/testiszlar/243",
                                    caption="Kerakli rasmni tanlang", reply_markup=page6)


@dp.callback_query_handler(text="next6")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://t.me/testiszlar/244",
                                    caption="Kerakli rasmni tanlang", reply_markup=page7)


@dp.callback_query_handler(text="next7")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://t.me/testiszlar/249",
                                    caption="Kerakli rasmni tanlang", reply_markup=page8)


@dp.callback_query_handler(text=["next8", "back10"])
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://t.me/testiszlar/251",
                                    caption="Kerakli rasmni tanlang", reply_markup=page9)


photos = {
    '01': "https://grabus.uz/image1.php?text=",
    '02': "https://grabus.uz/image2.php?text=",
    '03': "https://grabus.uz/image3.php?text=",
    '04': "https://grabus.uz/image4.php?text=",
    '1': "https://grabus.uz/boyin.php?text=",
    '2': "https://grabus.uz/gold.php?text=",
    '3': "https://grabus.uz/kumush.php?text=",
    '4': "https://grabus.uz/taqinchoq1.php?text=",
    '5': "https://grabus.uz/taqinchoq2.php?text=",
    '6': "https://grabus.uz/taqinchoq4.php?text=",
    '7': "https://grabus.uz/taqinchoq5.php?text=",
    '8': "https://grabus.uz/braslet1.php?text=",
    '9': "https://grabus.uz/braslet2.php?text=",
    '10': "https://grabus.uz/t1.php?text=",
    '11': "https://grabus.uz/t2.php?text=",
    '12': "https://grabus.uz/t3.php?text=",
}


##Yangilar
@dp.callback_query_handler(text=["next9", "back11"])
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://t.me/testiszlar/348",
                                    caption="Kerakli rasmni tanlang", reply_markup=page10)


@dp.callback_query_handler(text=["next10", "back12"])
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://t.me/testiszlar/350",
                                    caption="Kerakli rasmni tanlang", reply_markup=page11)


@dp.callback_query_handler(text=["next11","back01"])
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://t.me/testiszlar/349",
                                    caption="Kerakli rasmni tanlang", reply_markup=page12)


@dp.callback_query_handler(lambda query: 'stil' in query.data)
async def handle_specific_word(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("*Ismingizni bosh harfini kiriting*", parse_mode="markdown")
    await state.set_state(call.data)


# Yangilar oxiri
@dp.callback_query_handler(text="back3")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://telegra.ph//file/13dea56aeda2d35e8057b.jpg",
                                    caption="Kerakli rasmni tanlang", reply_markup=page2)


@dp.callback_query_handler(text="back7")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://t.me/testiszlar/243",
                                    caption="Kerakli rasmni tanlang", reply_markup=page6)


@dp.callback_query_handler(text="back8")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://t.me/testiszlar/244",
                                    caption="Kerakli rasmni tanlang", reply_markup=page7)


@dp.callback_query_handler(text="back9")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://t.me/testiszlar/249",
                                    caption="Kerakli rasmni tanlang", reply_markup=page8)


@dp.callback_query_handler(text="back6")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://t.me/testiszlar/242",
                                    caption="Kerakli rasmni tanlang", reply_markup=page5)


@dp.callback_query_handler(text="back5")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://t.me/testiszlar/241",
                                    caption="Kerakli rasmni tanlang", reply_markup=page4)


@dp.callback_query_handler(text="back4")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://telegra.ph//file/42b791e3b30cfe94f2809.jpg",
                                    caption="Kerakli rasmni tanlang", reply_markup=page3)


@dp.callback_query_handler(text="back2")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://telegra.ph//file/cdbe155c6986cf3d67522.jpg",
                                    caption="Kerakli rasmni tanlang", reply_markup=page1)


@dp.callback_query_handler(text="ortga3")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://telegra.ph////file/c7902b93fcf0680dc615b.jpg",
                                    caption="Kerakli rasmni tanlang", reply_markup=bet2)


@dp.callback_query_handler(text="ortga4")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://telegra.ph/////file/772ec047a80d465ac11ce.jpg",
                                    caption="Kerakli rasmni tanlang", reply_markup=bet3)


@dp.callback_query_handler(text="ortga5")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://t.me/testiszlar/250",
                                    caption="Kerakli rasmni tanlang", reply_markup=bet4)


@dp.callback_query_handler(text="ortga2")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://telegra.ph//file/bdfcc2dc951b7de244fb8.jpg",
                                    caption="Kerakli rasmni tanlang", reply_markup=bet1)


@dp.callback_query_handler(text="oldinga1")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://telegra.ph////file/c7902b93fcf0680dc615b.jpg",
                                    caption="Kerakli rasmni tanlang", reply_markup=bet2)


@dp.callback_query_handler(text="oldinga2")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://telegra.ph/////file/772ec047a80d465ac11ce.jpg",
                                    caption="Kerakli rasmni tanlang", reply_markup=bet3)


@dp.callback_query_handler(text="oldinga3")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://t.me/testiszlar/250",
                                    caption="Kerakli rasmni tanlang", reply_markup=bet4)


@dp.callback_query_handler(text="oldinga4")
async def one(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo("https://t.me/testiszlar/252",
                                    caption="Kerakli rasmni tanlang", reply_markup=bet5)


from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from keyboards.inline.pages import page1, page2, page3
from loader import dp

@dp.callback_query_handler(text="usul1")
async def stil1(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("*Ikki insonning ismini + belgisi bilan qo'shib yozib jo'nating\n\nMasalan E+M*",
                              parse_mode="markdown")
    await state.set_state('usul4')


@dp.callback_query_handler(text="usul2")
async def stil1(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("*Ikki insonning ismini + belgisi bilan qo'shib yozib jo'nating\n\nMasalan E+M*",
                              parse_mode="markdown")
    await state.set_state('usul5')


@dp.callback_query_handler(text="usul3")
async def stil1(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("*Ikki insonning ismini + belgisi bilan qo'shib yozib jo'nating\n\nMasalan E+M*",
                              parse_mode="markdown")
    await state.set_state('usul6')


@dp.callback_query_handler(text="usul4")
async def stil1(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("*Avval o'zingizni ismingizni kiriting*",
                              parse_mode="markdown")
    await Ismlar.ism1.set()


@dp.callback_query_handler(text="usul5")
async def stil1(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("*Avval o'zingizni ismingizni kiriting*",
                              parse_mode="markdown")
    await Ismlar2.ism1.set()


@dp.message_handler(state='stil1')
async def send_stil1(msg: types.Message, state: FSMContext):
    print("Working")
    add_text_to_image1(msg.text)
    # await msg.answer_photo(f"https://grabus.uz/boyin.php?text={msg.text}",
    #                        caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
    #                        parse_mode="markdown")
    await msg.answer(
        "*Rasmdagi yozuvlarni konspekt qilib qo'lda yozilgandek qilib beurvchi bot* \n\n👉 *@OsonYozamiz_bot*",
        parse_mode="Markdown")
    await state.finish()

from .add_text_image import add_text_to_image_1, add_text_to_image_2, add_text_to_image_3, add_text_to_image_4, \
    add_text_to_image1


@dp.message_handler(state='stil01')
async def send_stil1(msg: types.Message, state: FSMContext):
    add_text_to_image_1(msg.text)
    with open('images/saved/image1.png', 'rb') as image:
        await msg.answer_photo(image,
                           caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                           parse_mode="markdown")
    await msg.answer(
        "*Rasmdagi yozuvlarni konspekt qilib qo'lda yozilgandek qilib beurvchi bot* \n\n👉 *@OsonYozamiz_bot*",
        parse_mode="Markdown")
    await state.finish()


@dp.message_handler(state='stil02')
async def send_stil1(msg: types.Message, state: FSMContext):
    add_text_to_image_2(msg.text)
    with open('images/saved/image2.png', 'rb') as image:
        await msg.answer_photo(image,
                           caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                           parse_mode="markdown")
    await msg.answer(
        "*Rasmdagi yozuvlarni konspekt qilib qo'lda yozilgandek qilib beurvchi bot* \n\n👉 *@OsonYozamiz_bot*",
        parse_mode="Markdown")
    await state.finish()


@dp.message_handler(state='stil03')
async def send_stil1(msg: types.Message, state: FSMContext):
    add_text_to_image_3(msg.text)
    with open('images/saved/image3.png', 'rb') as image:
        await msg.answer_photo(image,
                           caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                           parse_mode="markdown")
    await msg.answer(
        "*Rasmdagi yozuvlarni konspekt qilib qo'lda yozilgandek qilib beurvchi bot* \n\n👉 *@OsonYozamiz_bot*",
        parse_mode="Markdown")
    await state.finish()


@dp.message_handler(state='stil04')
async def send_stil1(msg: types.Message, state: FSMContext):
    add_text_to_image_4(msg.text)
    with open('images/saved/image4.png', 'rb') as image:
        await msg.answer_photo(image,
                           caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                           parse_mode="markdown")
    await msg.answer(
        "*Rasmdagi yozuvlarni konspekt qilib qo'lda yozilgandek qilib beurvchi bot* \n\n👉 *@OsonYozamiz_bot*",
        parse_mode="Markdown")
    await state.finish()


@dp.message_handler(state='stil2')
async def send_stil1(msg: types.Message, state: FSMContext):
    await msg.answer_photo(f"https://grabus.uz/gold.php?text={msg.text}",
                           caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                           parse_mode="markdown")
    await msg.answer(
        "*Rasmdagi yozuvlarni konspekt qilib qo'lda yozilgandek qilib beurvchi bot* \n\n👉 *@OsonYozamiz_bot*",
        parse_mode="Markdown")
    await state.finish()


@dp.message_handler(state='stil3')
async def send_stil1(msg: types.Message, state: FSMContext):
    await msg.answer_photo(f"https://grabus.uz/kumush.php?text={msg.text}",
                           caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                           parse_mode="markdown")
    await msg.answer(
        "*Rasmdagi yozuvlarni konspekt qilib qo'lda yozilgandek qilib beurvchi bot* \n\n👉 *@OsonYozamiz_bot*",
        parse_mode="Markdown")
    await state.finish()


@dp.message_handler(state='stil4')
async def send_stil1(msg: types.Message, state: FSMContext):
    await msg.answer_photo(f"https://grabus.uz/taqinchoq1.php?text={msg.text}",
                           caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                           parse_mode="markdown")
    await msg.answer(
        "*Rasmdagi yozuvlarni konspekt qilib qo'lda yozilgandek qilib beurvchi bot* \n\n👉 *@OsonYozamiz_bot*",
        parse_mode="Markdown")
    await state.finish()


@dp.message_handler(state='stil5')
async def send_stil1(msg: types.Message, state: FSMContext):
    await msg.answer_photo(f"https://grabus.uz/taqinchoq2.php?text={msg.text}",
                           caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                           parse_mode="markdown")
    await msg.answer(
        "*Rasmdagi yozuvlarni konspekt qilib qo'lda yozilgandek qilib beurvchi bot* \n\n👉 *@OsonYozamiz_bot*",
        parse_mode="Markdown")
    await state.finish()


@dp.message_handler(state='stil6')
async def send_stil1(msg: types.Message, state: FSMContext):
    await msg.answer_photo(f"https://grabus.uz/taqinchoq4.php?text={msg.text}",
                           caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                           parse_mode="markdown")
    await msg.answer(
        "*Rasmdagi yozuvlarni konspekt qilib qo'lda yozilgandek qilib beurvchi bot* \n\n👉 *@OsonYozamiz_bot*",
        parse_mode="Markdown")
    await state.finish()


@dp.message_handler(state='stil7')
async def send_stil1(msg: types.Message, state: FSMContext):
    await msg.answer_photo(f"https://grabus.uz/taqinchoq5.php?text={msg.text}",
                           caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                           parse_mode="markdown")
    await msg.answer(
        "*Rasmdagi yozuvlarni konspekt qilib qo'lda yozilgandek qilib beurvchi bot* \n\n👉 *@OsonYozamiz_bot*",
        parse_mode="Markdown")
    await state.finish()


@dp.message_handler(state='stil8')
async def send_stil1(msg: types.Message, state: FSMContext):
    await msg.answer_photo(f"https://grabus.uz/braslet1.php?text={msg.text}",
                           caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                           parse_mode="markdown")
    await msg.answer(
        "*Rasmdagi yozuvlarni konspekt qilib qo'lda yozilgandek qilib beurvchi bot* \n\n👉 *@OsonYozamiz_bot*",
        parse_mode="Markdown")
    await state.finish()


@dp.message_handler(state='stil9')
async def send_stil1(msg: types.Message, state: FSMContext):
    await msg.answer_photo(f"https://grabus.uz/braslet2.php?text={msg.text}",
                           caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                           parse_mode="markdown")
    await msg.answer(
        "*Rasmdagi yozuvlarni konspekt qilib qo'lda yozilgandek qilib beurvchi bot* \n\n👉 *@OsonYozamiz_bot*",
        parse_mode="Markdown")
    await state.finish()


@dp.message_handler(state='stil10')
async def send_stil1(msg: types.Message, state: FSMContext):
    link = photos["10"]
    await msg.answer_photo(link + msg.text,
                           caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                           parse_mode="markdown")
    await msg.answer(
        "*Rasmdagi yozuvlarni konspekt qilib qo'lda yozilgandek qilib beurvchi bot* \n\n👉 *@OsonYozamiz_bot*",
        parse_mode="Markdown")
    await state.finish()


@dp.message_handler(state='stil11')
async def send_stil1(msg: types.Message, state: FSMContext):
    link = photos["11"]
    await msg.answer_photo(link + msg.text,
                           caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                           parse_mode="markdown")
    await msg.answer(
        "*Rasmdagi yozuvlarni konspekt qilib qo'lda yozilgandek qilib beurvchi bot* \n\n👉 *@OsonYozamiz_bot*",
        parse_mode="Markdown")
    await state.finish()


@dp.message_handler(state='stil12')
async def send_stil1(msg: types.Message, state: FSMContext):
    link = photos["12"]
    await msg.answer_photo(link + msg.text,
                           caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                           parse_mode="markdown")
    await msg.answer(
        "*Rasmdagi yozuvlarni konspekt qilib qo'lda yozilgandek qilib beurvchi bot* \n\n👉 *@OsonYozamiz_bot*",
        parse_mode="Markdown")
    await state.finish()


@dp.message_handler(state='usul4')
async def send_stil1(msg: types.Message, state: FSMContext):
    await msg.answer("*Biroz kutib turing*", parse_mode="markdown")
    harflar = ["h", "H"]
    if msg.text[1] in harflar:
        one = msg.text[0]
        two = msg.text[1]
        three = msg.text[3]
        await msg.answer_photo(f"https://grabus.uz/final.php?text1={one + two}&text2={three}",
                               caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                               parse_mode="markdown")
        await state.finish()
    else:
        one = msg.text[0]
        two = msg.text[2]
        await msg.answer_photo(f"https://grabus.uz/final.php?text1={one}&text2={two}",
                               caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                               parse_mode="markdown")
    await msg.answer(
        "*Rasmdagi yozuvlarni konspekt qilib qo'lda yozilgandek qilib beurvchi bot* \n\n👉 *@OsonYozamiz_bot*",
        parse_mode="Markdown")
    await state.finish()


@dp.message_handler(state='usul5')
async def send_stil1(msg: types.Message, state: FSMContext):
    await msg.answer("*Biroz kutib turing*", parse_mode="markdown")
    harflar = ["h", "H"]
    if msg.text[1] in harflar:
        one = msg.text[0]
        two = msg.text[1]
        three = msg.text[3]
        await msg.answer_photo(f"https://grabus.uz/ta.php?text1={one + two}&text2={three}",
                               caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                               parse_mode="markdown")
        await state.finish()
    else:
        one = msg.text[0]
        two = msg.text[2]
        await msg.answer_photo(f"https://grabus.uz/ta.php?text1={one}&text2={two}",
                               caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                               parse_mode="markdown")
    await msg.answer(
        "*Rasmdagi yozuvlarni konspekt qilib qo'lda yozilgandek qilib beurvchi bot* \n\n👉 *@OsonYozamiz_bot*",
        parse_mode="Markdown")
    await state.finish()


@dp.message_handler(state='usul6')
async def send_stil1(msg: types.Message, state: FSMContext):
    await msg.answer("*Biroz kutib turing*", parse_mode="markdown")
    harflar = ["h", "H"]
    if msg.text[1] in harflar:
        one = msg.text[0]
        two = msg.text[1]
        three = msg.text[3]
        await msg.answer_photo(f"https://grabus.uz/uzuk.php?text1={one + two}&text2={three}",
                               caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                               parse_mode="markdown")
        await state.finish()
    else:
        one = msg.text[0]
        two = msg.text[2]
        await msg.answer_photo(f"https://grabus.uz/uzuk.php?text1={one}&text2={two}",
                               caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                               parse_mode="markdown")
    await msg.answer(
        "*Rasmdagi yozuvlarni konspekt qilib qo'lda yozilgandek qilib beurvchi bot* \n\n👉 *@OsonYozamiz_bot*",
        parse_mode="Markdown")
    await state.finish()


@dp.message_handler(state=Ismlar.ism1)
async def send_stil4(msg: types.Message, state: FSMContext):
    await state.update_data({'ism1': f"{msg.text}"})
    await msg.answer(f"*Endi ikkinchi odamni ismini kiriting*",
                     parse_mode="markdown")
    await Ismlar.next()


@dp.message_handler(state=Ismlar.ism2)
async def send_stil1(msg: types.Message, state: FSMContext):
    await state.update_data({'ism2': f"{msg.text}"})
    await msg.answer("Qabul qilindi \n\nTayyorlayapman kutib turing..")
    data = await state.get_data()
    name = data.get("ism1")
    name2 = data.get("ism2")
    await msg.answer_photo(f"https://grabus.uz/bras3.php?text={name}&&ism={name2}",
                           caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                           parse_mode="markdown")
    await msg.answer(
        "*Rasmdagi yozuvlarni konspekt qilib qo'lda yozilgandek qilib beurvchi bot* \n\n👉 *@OsonYozamiz_bot*",
        parse_mode="Markdown")
    await state.finish()


@dp.message_handler(state=Ismlar2.ism1)
async def send_stil4(msg: types.Message, state: FSMContext):
    await state.update_data({'ism1': f"{msg.text}"})
    await msg.answer(f"*Endi ikkinchi odamni ismini kiriting*",
                     parse_mode="markdown")
    await Ismlar2.next()


@dp.message_handler(state=Ismlar2.ism2)
async def send_stil1(msg: types.Message, state: FSMContext):
    await state.update_data({'ism2': f"{msg.text}"})
    await msg.answer("Qabul qilindi \n\nTayyorlayapman kutib turing..")
    data = await state.get_data()
    name = data.get("ism1")
    name2 = data.get("ism2")
    await msg.answer_photo(f"https://grabus.uz/braslet4.php?text={name}&&ism={name2}",
                           caption="*Buyurtmangiz tayyor boldi.\n\nQayta ishlatish uchun /start bosing*",
                           parse_mode="markdown")
    await msg.answer(
        "*Rasmdagi yozuvlarni konspekt qilib qo'lda yozilgandek qilib beurvchi bot* \n\n👉 *@OsonYozamiz_bot*",
        parse_mode="Markdown")
    await state.finish()
