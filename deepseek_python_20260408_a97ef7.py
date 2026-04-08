import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
import os

from bot.handlers import start, booking, profile, admin
from bot.utils.helpers import setup_commands

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

async def main():
    dp.include_router(start.router)
    dp.include_router(booking.router)
    dp.include_router(profile.router)
    dp.include_router(admin.router)

    await setup_commands(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    # Webhook (Render) yoki polling
    webhook_url = os.getenv("WEBHOOK_URL")
    if webhook_url:
        await bot.set_webhook(webhook_url)
        logging.info(f"Webhook set to {webhook_url}")
    else:
        logging.info("Start polling...")
        await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())