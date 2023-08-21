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
    await message.answer(text.menu, reply_markup=kb.menu)
    
    
@dp.message_handler(commands=['check_voice'])
async def check_voice_answer(message: types.Message):
    await bot.send_audio(chat_id = message.from_user.id,
                         audio = "https://dl.sndup.net/y79j/1.mp3",
                         caption = "Объясняю, что такое GPT")
    await bot.send_audio(chat_id = message.from_user.id,
                         audio = "https://dl.sndup.net/s2p9/2.mp3",
                         caption = "Объясняю разницу между SQL и NoSQL")
    await bot.send_audio(chat_id = message.from_user.id,
                         audio = "https://dl.sndup.net/mdn7/3.mp3",
                         caption = "История первой любви ❤️")
    await message.answer(text.menu, reply_markup=kb.menu)


@dp.message_handler(commands=['main_passion'])
async def main_passion_answer(message: types.Message):
    await bot.send_message(chat_id= message.from_user.id,
                           text = text.my_passion)
    await message.answer(text.menu, reply_markup=kb.menu)
    


@dp.callback_query_handler()
async def button_callback(callback: types.CallbackQuery):
    if callback.data == 'watch_selfie':
        await bot.send_photo(chat_id=callback.message.chat.id,
                         photo="https://i.ibb.co/12q4BMk/1.jpg",
                         caption="Моё последнее селфи")
        await bot.send_photo(chat_id=callback.message.chat.id,
                         photo="https://i.ibb.co/FqDVxmr/2.jpg",
                         caption="А так я выглядел в старшей школе😊")
    if callback.data == 'check_voice':
        await bot.send_audio(chat_id = callback.message.chat.id,
                         audio = "https://dl.sndup.net/y79j/1.mp3",
                         caption = "Объясняю, что такое GPT")
        await bot.send_audio(chat_id = callback.message.chat.id,
                         audio = "https://dl.sndup.net/s2p9/2.mp3",
                         caption = "Объясняю разницу между SQL и NoSQL")
        await bot.send_audio(chat_id = callback.message.chat.id,
                         audio = "https://dl.sndup.net/mdn7/3.mp3",
                         caption = "История первой любви ❤️")
    if callback.data == 'main_passion':
        await bot.send_message(chat_id= callback.message.chat.id,
                           text = text.my_passion)
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

