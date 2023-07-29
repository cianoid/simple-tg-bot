from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.filters.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from utils import handle_amount
import texts
import mortgage


router = Router()


class GetMortgage(StatesGroup):
    mortgage_amount = State()
    initial_mortgage_fee = State()


@router.message(Command("start"))
async def start_handler(msg: Message) -> None:
    await msg.answer(texts.START)


@router.message(Command("mortgage"))
async def mortgage_start_handler(msg: Message, state: FSMContext) -> None:
    await msg.answer(texts.MORTGAGE_START)
    await state.set_state(GetMortgage.mortgage_amount)


@router.message(GetMortgage.mortgage_amount)
async def mortgage_handler(msg: Message, state: FSMContext) -> None:
    mortgage_amount = handle_amount(msg.text)

    if mortgage_amount is False:
        await msg.answer(texts.NOT_A_NUMBER)
        return

    minimal_mortgage_amount = mortgage.get_minimal_mortgage_amount()

    if mortgage_amount < minimal_mortgage_amount:
        await msg.answer(
            texts.MORTGAGE_AMOUNT_FAIL.format(MINIMAL_MORTGAGE=minimal_mortgage_amount)
        )
        return

    await state.update_data(mortgage_amount=mortgage_amount)
    await msg.answer(texts.INITIAL_FEE_START.format(MORTGAGE_AMOUNT=mortgage_amount))
    await state.set_state(GetMortgage.initial_mortgage_fee)
    return


@router.message(GetMortgage.initial_mortgage_fee)
async def initial_fee_handler(msg: Message, state: FSMContext) -> None:
    initial_mortgage_fee = handle_amount(msg.text)

    if initial_mortgage_fee is False:
        await msg.answer(texts.NOT_A_NUMBER)
        return

    mortgage_data = await state.get_data()
    mortgage_amount = mortgage_data.get("mortgage_amount")
    minimal_initial_mortgage_fee = mortgage.get_initial_fee(mortgage_amount)

    if initial_mortgage_fee < minimal_initial_mortgage_fee:
        await msg.answer(
            texts.MORTGAGE_INITIAL_FEE_FAIL.format(
                MINIMAL_INITIAL_FEE=minimal_initial_mortgage_fee
            )
        )
        return

    minimal_mortgage_amount = mortgage.get_minimal_mortgage_amount()

    if mortgage_amount - initial_mortgage_fee < minimal_mortgage_amount:
        await msg.answer(
            texts.MORTGAGE_AMOUNT_FAIL.format(
                MINIMAL_MORTGAGE=minimal_mortgage_amount
            )
        )
        return

    await state.update_data(initial_mortgage_fee=initial_mortgage_fee)
    await msg.answer(texts.MORTGAGE_INITIAL_FEE_SUCCESS)
    await state.clear()
    return


@router.message()
async def any_message(msg: Message) -> None:
    await msg.answer(texts.FAIL)
    return
