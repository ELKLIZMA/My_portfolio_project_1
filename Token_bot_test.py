import asyncio
import os

from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv


# Загружаем переменные из .env
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


# Создаём экземпляр Router
router = Router()


# Handler команды /start
@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привет! Бот работает.")


# Handler конкретного текста
@router.message(F.text == "тест")
async def test_handler(message: Message):
    text = message.text

    await message.answer(f"Я получил: {text}")


# Fallback: любой другой текст
@router.message(F.text)
async def unknown_handler(message: Message):
    await message.answer("Я пока не знаю такой команды.")


# Запуск приложения
async def main():
    bot = Bot(token=TOKEN)

    dp = Dispatcher()

    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())