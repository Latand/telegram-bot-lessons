import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN
from sql import create_pool

# from aiogram.contrib.fsm_storage.redis import RedisStorage2

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)
# loop = asyncio.get_event_loop()
# Поток нам не нужен, т.к. он и так создается в диспатчере.

# Set up storage (either in Redis or Memory)
storage = MemoryStorage()
# storage = RedisStorage2()

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)

db = dp.loop.run_until_complete(create_pool())
