from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from core.states.registration import Form
from core.validators.phoen import validate_phone_number


router = Router()


async def show_form(state: FSMContext):
    data = await state.get_data()
    print(data)


@router.message(Form.phone)
async def get_phone(mes: Message, state: FSMContext):
    status, phone = validate_phone_number(mes.text)
    if status:
        await mes.answer(text="Супер! Теперь я смогу делиться с вами скидками и присылать подарки.")
        await state.update_data(phone=mes.text)
        await state.set_state(Form.phone)
        await show_form(state)
    else:
        await mes.answer(text="Неверный формат номера. Попробуйте ещё раз. Номер телефона должен содержать 11 цифр и\
 начинаться с 7 или 8. Например, +79999999999")
        await state.set_state(Form.phone)


@router.message(Form.email)
async def get_email(mes: Message, state: FSMContext):
    await mes.answer(text="Отличная почта! Теперь мне нужен ваш телефон, он нужен для того, чтобы отправлять вам\
 подарки и скидки.")
    await state.update_data(email=mes.text)
    await state.set_state(Form.phone)


@router.message(Form.name)
async def get_name(mes: Message, state: FSMContext):
    await mes.answer(text="Приятно познакомиться, " + mes.text + "! Какая у вас почта?")
    await state.update_data(name=mes.text)
    await state.set_state(Form.email)


@router.message(Command('reg'))
async def start(mes: Message, state: FSMContext):
    await mes.answer(text="Давайте знакомиться! Как вас зовут? Напишите свое ФИО")
    await state.set_state(Form.name)
