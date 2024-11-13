from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import F

from core.states.registration import Form
from core.validators.phone import validate_phone_number
from core.validators.email import email_validator
from core.db.scripts import create_user, get_user
from core.keyboards.main_kb import main_kb_as_markup

router = Router()


async def show_form(mes: Message, state: FSMContext):
    data = await state.get_data()
    create_user(data.get('tg_id'), data.get('name'), data.get('email'), data.get('phone'))
    await mes.answer(text="Супер! Теперь я смогу делиться с вами скидками и присылать подарки.",
                     reply_markup=main_kb_as_markup(mes.from_user.id))
    await state.clear()


@router.message(Form.phone)
async def get_phone(mes: Message, state: FSMContext):
    status, phone = validate_phone_number(mes.text)
    if status:
        await state.update_data(phone=mes.text)
        await state.set_state(Form.phone)
        await show_form(mes, state)
    else:
        await mes.answer(text="Неверный формат номера. Попробуйте ещё раз. Номер телефона должен содержать 11 цифр и\
 начинаться с 7 или 8. Например, +79999999999")
        await state.set_state(Form.phone)


@router.message(Form.email)
async def get_email(mes: Message, state: FSMContext):
    if email_validator(mes.text):
        await mes.answer(text="Отличная почта! Теперь мне нужен ваш телефон, он нужен для того, чтобы отправлять вам\
     подарки и скидки.")
        await state.update_data(email=mes.text)
        await state.set_state(Form.phone)
    else:
        await mes.answer(text="Неверный формат почты. Попробуйте ещё раз. Например, example@example.com")
        await state.set_state(Form.email)


@router.message(Form.name)
async def get_name(mes: Message, state: FSMContext):
    await mes.answer(text="Приятно познакомиться, " + mes.text + "! Какая у вас почта?")
    await state.update_data(name=mes.text)
    await state.set_state(Form.email)


# @router.message(F.text == "Регистрация")
async def start_reg(mes: Message, state: FSMContext):
    if get_user(mes.from_user.id):
        return
    await mes.answer(text="Давайте знакомиться! Как вас зовут? Напишите свое ФИО")
    await state.update_data(tg_id=mes.from_user.id)
    await state.set_state(Form.name)
