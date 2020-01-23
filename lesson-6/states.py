from aiogram.dispatcher.filters.state import StatesGroup, State


class Purchase(StatesGroup):
    EnterQuantity = State()
    Approval = State()
    Payment = State()


class NewItem(StatesGroup):
    Name = State()
    Photo = State()
    Price = State()
    Confirm = State()


class Mailing(StatesGroup):
    Text = State()
    Language = State()
