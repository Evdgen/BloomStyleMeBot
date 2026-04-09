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

# Бот и диспетчер (новый синтаксис aiogram 3.7+)
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# --- Импорты из папки handlers ---
from handlers.start import router as start_router
from handlers.style import router as style_router
from handlers.premium_commands import router as premium_router
from handlers.settings import router as settings_router
from handlers.keyboards import router as keyboards_router
from handlers.database import router as database_router
from handlers.config import router as config_router
from handlers.texts import router as texts_router

# --- Дополнительные модули (если есть) ---
try:
    from handlers.colortype_test import router as colortype_router
    dp.include_router(colortype_router)
except ImportError:
    pass

try:
    from handlers.face_shape_test import router as faceshape_router
    dp.include_router(faceshape_router)
except ImportError:
    pass

try:
    from handlers.weather_api import router as weather_router
    dp.include_router(weather_router)
except ImportError:
    pass

try:
    from handlers.style_engine import router as style_engine_router
    dp.include_router(style_engine_router)
except ImportError:
    pass

try:
    from handlers.product_engine import router as product_router
    dp.include_router(product_router)
except ImportError:
    pass

# --- Регистрируем основные роутеры ---
dp.include_router(start_router)
dp.include_router(style_router)
dp.include_router(premium_router)
dp.include_router(settings_router)
dp.include_router(keyboards_router)
dp.include_router(database_router)
dp.include_router(config_router)
dp.include_router(texts_router)

# --- Запуск ---
async def main():
    print("🚀 Бот BloomStyleMe запускается...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
