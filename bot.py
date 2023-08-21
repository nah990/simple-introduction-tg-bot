from aiogram import Dispatcher, Bot, types
from aiogram.dispatcher import filters
from config import TELEGRAM_BOT_TOKEN
from random import shuffle

import kb
import text


bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer(text.greet.format(name=message.from_user.full_name), reply_markup=kb.menu)


@dp.message_handler(commands=['watch_selfie'])
async def selfie_answer(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="https://i.ibb.co/12q4BMk/1.jpg",
                         caption="Моё последнее селфи")
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="https://i.ibb.co/FqDVxmr/2.jpg",
                         caption="А так я выглядел в старшей школе😊")
    

@dp.callback_query_handler()
async def selfie_callback(callback: types.CallbackQuery):
    if callback.data == 'watch_selfie':
        await bot.send_photo(chat_id=callback.message.chat.id,
                         photo="https://i.ibb.co/12q4BMk/1.jpg",
                         caption="Моё последнее селфи")
        await bot.send_photo(chat_id=callback.message.chat.id,
                         photo="https://i.ibb.co/FqDVxmr/2.jpg",
                         caption="А так я выглядел в старшей школе😊")
        await callback.message.answer(text.menu, reply_markup=kb.menu)
    
MENU_PHRASES = [
    'Меню',
    'Выйти в меню',
    '◀️ Выйти в меню'
]

@dp.message_handler(filters.Text(equals=MENU_PHRASES, ignore_case=True))
async def menu(message: types.Message):
    await message.answer_photo(photo = "https://i.ibb.co/12q4BMk/1.jpg")
    await message.answer(text.menu, reply_markup=kb.menu)

