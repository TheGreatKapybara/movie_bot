from aiogram.client.session.aiohttp import AiohttpSession
from aiogram import Bot, types, Dispatcher, F
from functions import hello_message, random_movies, main_menu
from aiogram.filters import Command
import asyncio

token = "6635995222:AAHvMY-zWePIV7S-3HQMn9OcCqft3kDvIiE"

bot = Bot(token=token)

dp = Dispatcher()

dp.message.register(hello_message, Command(commands="start"))
dp.message.register(random_movies, F.text == 'Начинаем')
dp.message.register(random_movies, F.text == 'Далее')
dp.message.register(main_menu, F.text == 'В меню')

async def on_startup():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(on_startup())