from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text="🍭 Locatsiyani yuborish",
                                                      request_location=True)
                                   ],
                               ])
