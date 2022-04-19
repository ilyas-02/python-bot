from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cancel_button = KeyboardButton("Cencel")
cancel_murkup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

cancel_murkup.add(cancel_button)
