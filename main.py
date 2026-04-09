import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден!")

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Импорты из папки handlers
from handlers.start import router as start_router
from handlers.bloom import router as bloom_router
from handlers.style import router as style_router
from handlers.settings import router as settings_router
from handlers.knowledge import router as knowledge_router
from handlers.premium_commands import router as premium_commands_router

# Регистрация роутеров
dp.include_router(start_router)
dp.include_router(bloom_router)
dp.include_router(style_router)
dp.include_router(settings_router)
dp.include_router(knowledge_router)
dp.include_router(premium_commands_router)

async def main():
    print("🚀 Бот BloomStyleMe запускается...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
