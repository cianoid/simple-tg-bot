from logging import getLogger

from aiogram import Router
from aiogram.filters.command import Command
from aiogram.types import Message

from app import texts
from app.config import COMMAND, COMMAND_PASSWORD
from app.utils import launch

logger = getLogger(__name__)


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message) -> None:
    await msg.answer(texts.START)


async def command_launcher(msg: Message) -> None:
    await msg.answer(texts.COMMAND_STARTED)

    try:
        for text in launch(COMMAND, logger):
            logger.debug("%s", text)
            if isinstance(text, bool):
                if text is True:
                    await msg.answer(texts.COMMAND_STOPPED)
                    logger.info(texts.COMMAND_STOPPED)
                else:
                    await msg.answer(texts.COMMAND_FAILED)
                    logger.error(texts.COMMAND_FAILED)
            else:
                if len(text) > 0:
                    await msg.answer(f"<code>{text.strip()}</code>")
    except Exception as e:
        await msg.answer(texts.COMMAND_FAILED)
        logger.exception(e)

    return


@router.message()
async def command_handler(msg: Message) -> None:
    try:
        if msg.text.strip() == COMMAND_PASSWORD:
            return await command_launcher(msg)
        await msg.answer(texts.FAIL)
    except Exception as e:
        logger.critical(e)
    return
