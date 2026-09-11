import shopping
import asyncio
import os

from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

async def main():
    shopping.check_and_create_file()
    bot = Bot(token=TOKEN)

    dp = Dispatcher()

    dp.include_router(router)

    await dp.start_polling(bot)


# Загружаем переменные из .env
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


# Создаём экземпляр Router
router = Router()


# Handler команды /start
@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привет, я первая версия персонального помощника.")


# Handler конкретного текста
@router.message(F.text == "список покупок")
async def show_shopping_list_handler(message: Message):
    text = shopping.shop_list

    await message.answer(f"твой список покупок: {text}")



# Fallback: любой другой текст
@router.message(F.text)
async def unknown_handler(message: Message):
    await message.answer("Я пока не знаю такой команды.")


# Запуск приложения



if __name__ == "__main__":
    asyncio.run(main())