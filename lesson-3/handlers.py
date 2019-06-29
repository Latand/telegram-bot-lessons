from main import bot, dp
from aiogram.types import Message
from config import admin_id
from filters import *
from aiogram.dispatcher.storage import FSMContext
from states import Form


async def send_to_admin(*args):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")


@dp.message_handler(commands=["start"])
async def start(message: Message, state: FSMContext):
    await message.answer("Привет, Введи пожалуйста свое Имя.")
    await Form.Name.set()
    # Или можно еще сделать так await Form.next()


@dp.message_handler(state=Form.Name)
async def name_func(message: Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer("Теперь введите свою Фамилию")
    await Form.Surname.set()
    # Или можно еще сделать так await Form.next()


@dp.message_handler(state=Form.Surname)
async def surname_func(message: Message, state: FSMContext):
    surname = message.text
    await state.update_data(surname=surname)
    await message.answer("Теперь введите свою дату рождения")
    await Form.DOB.set()
    # Или можно еще сделать так await Form.next()


@dp.message_handler(state=Form.DOB)
async def dob_func(message: Message, state: FSMContext):
    dob = message.text
    await state.update_data(dob=dob)
    await message.answer("Теперь введите свой город")
    await Form.City.set()
    # Или можно еще сделать так await Form.next()


@dp.message_handler(state=Form.City)
async def city_func(message: Message, state: FSMContext):
    city = message.text
    await state.update_data(city=city)
    await message.answer("Спасибо, вот ваша информация!")
    data = await state.get_data()
    text = """
Вас зовут: {name} {surname}
Вы родились {dob} в городе {city}.
""".format(
        name=data.get("name"),
        surname=data.get("surname"),
        dob=data.get("dob"),
        city=data.get("city"),
    )
    await state.reset_state(with_data=False)
    await message.answer(text=text)


@dp.message_handler()
async def e_else(message, state):
    data = await state.get_data()

    await message.answer("Вы прошли регистрацию. Вас зовут {name}".format(**data))
