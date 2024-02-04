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
inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='👍', callback_data='inline_like'), InlineKeyboardButton(text='👎', callback_data='inline_dislike')],
        [InlineKeyboardButton(text='🆑', callback_data='inline_clear')]
    ]
)