import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Логи
logging.basicConfig(level=logging.INFO)

# Токен
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден в переменных окружения!")

# Бот и диспетчер (НОВЫЙ синтаксис для aiogram 3.7+)
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# --- Импорты хендлеров ---
from handlers.start import router as start_router
from handlers.survey import router as survey_router
from handlers.style import router as style_router
from handlers.premium_commands import router as premium_router
from handlers.settings import router as settings_router

# --- Импорты тестов ---
try:
    from colortype_test import router as colortype_router
    dp.include_router(colortype_router)
except ImportError:
    pass

try:
    from face_shape_test import router as faceshape_router
    dp.include_router(faceshape_router)
except ImportError:
    pass

# --- Регистрируем роутеры ---
dp.include_router(start_router)
dp.include_router(survey_router)
dp.include_router(style_router)
dp.include_router(premium_router)
dp.include_router(settings_router)

# --- Запуск ---
async def main():
    print("🚀 Бот BloomStyle запускается...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
