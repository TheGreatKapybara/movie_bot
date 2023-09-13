from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[KeyboardButton(text='Начинаем')]])


randomizer = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(text='В меню'),
        KeyboardButton(text='Далее')]])
