import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN
from language_middleware import setup_middleware

#######################
# Если у вас РКН блокирует запросы к Телеграму, можете перезаписать адрес по которому делаются запросы
# И раскомментите следующие строки
# from aiogram.bot import api
# PATCHED_URL = "https://telegg.ru/orig/bot{token}/{method}"
# setattr(api, "API_URL", PATCHED_URL)
#######################


logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)
# loop = asyncio.get_event_loop()
# Поток нам не нужен, т.к. он и так создается в диспатчере.

storage = MemoryStorage()

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)

# Настроим i18n middleware для работы с многоязычностью
i18n = setup_middleware(dp)
# Создадим псевдоним для метода gettext
_ = i18n.gettext
