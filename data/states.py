from aiogram.dispatcher.filters.state import StatesGroup, State


class PersonalData(StatesGroup):
    ID = State()
    answer = State()


class Texts(StatesGroup):
    caption = State()
    button = State()

class User(StatesGroup):
    num = State()
    name = State()