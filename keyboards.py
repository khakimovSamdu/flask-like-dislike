from telegram import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton,
)

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👍"),KeyboardButton(text="👎")],
        [KeyboardButton(text="🆑")]
    ],
    resize_keyboard=True

)
