import asyncio
import logging
from random import randrange

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from app.config import BOT_TOKEN
from app.handlers import router, logger


async def bot() -> None:
    logger.info("Trying to connect")
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())

    if router.parent_router is None:
        dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

    return


async def main():
    while True:
        try:
            await bot()
        except Exception as e:
            logger.critical("%s: %s", e.__class__.__name__, e)
            sleep_s = randrange(4_000, 8_000, 1) * 0.001
            logger.warning("Sleep for %f seconds", sleep_s)
            await asyncio.sleep(sleep_s)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    logger.info("Starting")
    asyncio.run(main())
