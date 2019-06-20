from aiogram.dispatcher.filters.state import StatesGroup, State


class Form(StatesGroup):
    Name = State()
    Surname = State()
    DOB = State()
    City = State()
