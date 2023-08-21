from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

menu = [
    [InlineKeyboardButton(text="😊 Просмотр selfie", callback_data="watch_selfie"),
    InlineKeyboardButton(text="🔥 Мое главное увлечение", callback_data="main_passion")],
    [InlineKeyboardButton(text="🎵  Услышать мой голос", callback_data="check_voice")],
    [InlineKeyboardButton(text="❔ Source code", url='https://github.com/nah990/simple-introduction-tg-bot')],
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])