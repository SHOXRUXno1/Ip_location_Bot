from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
location_keys = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🍽",callback_data='mylocation'),
        ],
])