from aiogram import types, Dispatcher
from config import bot, dp


# @dp.message_handler()
async def echo_message(message: types.Message):
    if message.text.isdigit():
        a = int(message.text)
        await message.answer(a ** 2)
    else:
        await message.answer(message.text)


def register_hendlers_notification(dp: Dispatcher):
    dp.register_message_handler(echo_message)
