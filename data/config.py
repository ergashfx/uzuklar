BOT_TOKEN = '5228072940:AAGsiauvXSLfxm3PwgyHCcp_bairGg0YB6I'
from utils.db_api.sqlite import db

admins = db.select_all_adminss()
channels = db.select_all_channel()
id_list = [id[0] for id in channels]
CHANNELS = list(map(lambda x: x[0], channels))

ids = [id[0] for id in admins]
ADMINS = list(map(lambda x: x[0], admins))
texts = db.select_all_from_texts()

Button_text = [texts[0][1]]
Text_caption = [texts[0][0]]
btns = {
    "accept": "Tekshirish",
    "back": "Ortga qaytish",
}

texts = {
    "text_to_start": f"Assalomu alaykum! Botimizdan foydalanish uchun quyidagi quyidagi kanalga obuna bo'lishingiz kerak",
    "main_menu": "[🌸](https://telegra.ph/file/06bef4a756add9b85d451.jpg) *Salom \n\nMen orqali o'z imsingiz bosh harfi yozilgan taqinchoqlar rasmini tayyorlay olasiz\n\nQuyidagi menyulardan birini tanlang*",
    "notaccepted": "❌<b> Quyidagi kanallarga a'zo bo'lmadingiz</b>, iltimos botdan foydalanish uchun kanalga a'zo bo'ling!",
    "accepted": "[🌸](https://telegra.ph/file/06bef4a756add9b85d451.jpg) *Salom \n\nMen orqali o'z imsingiz bosh harfi yozilgan taqinchoqlar rasmini tayyorlay olasiz\n\nQuyidagi menyulardan birini tanlang*",
}