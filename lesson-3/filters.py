from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, CallbackQuery


class Button(BoundFilter):
    def __init__(self, key, contains=False):
        self.key = key
        self.contains = contains

    async def check(self, message) -> bool:
        if isinstance(message, Message):
            if self.contains:
                return self.key in message.text
            else:
                return message.text == self.key
        elif isinstance(message, CallbackQuery):
            if self.contains:
                return self.key in message.data
            else:
                return self.key == message.data

