from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types, Dispatcher
from config import bot, dp, ADMIN
import random


# @dp.message_handler(commands=['mem'])
async def mem_1(message: types.Message):
    photo = open("Media/images.jpg", 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)


# @dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f"Салам хозяин {message.from_user.full_name}")


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):

    murkup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "NEXT",
        callback_data="button_call_1"
    )
    murkup.add(button_call_1)

    photo = open("media/problem1.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=photo)

    question = "Output:"
    answers = ["[2, 4]", '[2, 4, 6]', '[2]', '[4]', '[0]', "Error"]
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answers,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=0,
                        open_period=5,
                        reply_markup=murkup
                        )


# @dp.message_handler(commands=["pin"], commands_prefix="!/")
async def pin(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Команда должна быть ответом на сообщение!")
    else:
        await message.bot.delete_message(message.chat.id, message.message_id)
        await message.bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)


# @dp.message_handler(content_types=["text"])
async def echo_message(message: types.Message):
    if message.text.startswith("game"):
        if message.from_user.id != ADMIN:
            await bot.send_message(message.chat.id, "Permission denied!")
        else:
            emoji_list = ["⚽", "🏀", "🎲", "🎯", "🎳", "🎰"]
            emoji = random.choices(emoji_list)
            await bot.send_dice(message.chat.id, emoji=emoji)


def register_hendlers_client(dp: Dispatcher):
    dp.register_message_handler(mem_1, commands=["mem"])
    dp.register_message_handler(hello, commands=["start"])
    dp.register_message_handler(quiz_1, commands=["quiz"])
    dp.register_message_handler(echo_message, content_types=["text"])
    dp.register_message_handler(pin, commands=["pin"], commands_prefix="!/")
