from aiogram import executor

from config import admin_id
from database import run_db
from load_all import bot


async def on_shutdown(dp):
    await bot.close()


async def on_startup(dp):
    await bot.send_message(admin_id, "Я запущен!")
    await run_db()


if __name__ == '__main__':
    from admin_panel import dp
    from handlers import dp

    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=on_startup)
