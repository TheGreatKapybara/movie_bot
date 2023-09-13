from aiogram import Bot, types
from movies import random_movie
import keyboards as kb


async def hello_message(message: types.Message, bot: Bot):
    await message.answer(text=f"Привет! Если не знаешь что посмотреть - жми на кнопку ниже! \n"
                              "Я пришлю тебе рандомный фильм и его краткое описание. \n"
                              "Если понравилось - перерходи к просмотру, если нет - нажимай далее и так "
                              "пока не найдешь что то интересное!",
                         reply_markup=kb.start_keyboard)
    await message.delete()

async def main_menu(message: types.Message, bot: Bot):
    await message.delete()
    await message.answer(text='До скорого😉', reply_markup=kb.start_keyboard)

async def random_movies(message: types.Message, bot: Bot):
    await message.delete()
    result = random_movie()
    await bot.send_photo(chat_id=message.chat.id, photo=f"{result[2]}")
    await message.answer(text=f"<b>{result[0]}</b>\n"
                              f"<i>Год - {result[4]}</i>\n"
                              f"<i>Жанр - {result[5]}</i>\n"
                              f"<i>Страна - {result[6]}</i>\n \n \n"
                              f"{result[1]}", parse_mode="HTML", reply_markup=kb.randomizer)