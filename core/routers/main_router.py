from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from core.keyboards.main_kb import main_kb_as_markup
from core.db.scripts import get_user
from core.routers.registration import start_reg


router = Router()


@router.message(CommandStart())
async def start(mes: Message, state: FSMContext):
    await mes.answer(text="""Привет! 👋  Это бот помощник Norland Academy! 

Хотите  освоить новую профессию  и  кардинально  изменить  свою  жизнь? 💫

Здесь вы можете получить информацию об обучении  по  самым  востребованным  направлениям 📦

Получать бесплатные гайды и чек-листы 📜

Проходить полезные тестирования 📊

Давайте начнем!  😉""", reply_markup=ReplyKeyboardRemove())
    await mes.delete()
    await start_reg(mes, state)
