from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


class Form(StatesGroup):
    tg_id = State()
    name = State()
    email = State()
    phone = State()
