import random

from aiogram import types
from load_all import db, dp

@dp.message_handler(commands=["start"])
async def register_user(message: types.Message):
    chat_id = message.from_user.id
    referral = message.get_args()
    id = await db.add_new_user(referral=referral)
    count_users = await db.count_users()

    text = ""
    if not id:
        id = await db.get_id()
    else:
        text += "Записал в базу! "

    bot_username = (await dp.bot.me).username
    bot_link = f"https://t.me/{bot_username}?start={id}"
    balance = await db.check_balance()
    text += f"""
Сейчас в базе {count_users} человек!

Ваша реферальная ссылка: {bot_link}
Проверить рефералов можно по команде: /referrals

Ваш баланс: {balance} монет.

Добавить монет: /add_money
"""

    await dp.bot.send_message(chat_id, text)


@dp.message_handler(commands=["referrals"])
async def check_referrals(message: types.Message):
    referrals = await db.check_referrals(dp)
    text = f"Ваши рефералы:\n{referrals}"

    await message.answer(text)


@dp.message_handler(commands=["add_money"])
async def add_money(message: types.Message):
    random_amount = random.randint(1, 100)
    await db.add_money(random_amount)
    balance = await db.check_balance()

    text = f"""
Вам было добавлено {random_amount} монет.
Теперь ваш баланс: {balance}
    """
    await message.answer(text)

