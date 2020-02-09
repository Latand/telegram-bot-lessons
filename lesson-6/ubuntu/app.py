import asyncio

from aiogram import executor

from ubuntu.config import admin_id
from ubuntu.database import create_db
from ubuntu.load_all import bot


async def on_shutdown(dp):
    await bot.close()


async def on_startup(dp):
    # Подождем пока запустится база данных...
    await asyncio.sleep(5)
    await create_db()
    await bot.send_message(admin_id, "Я запущен!")


if __name__ == '__main__':
    from ubuntu.admin_panel import dp
    from ubuntu.handlers import dp

    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=on_startup)
