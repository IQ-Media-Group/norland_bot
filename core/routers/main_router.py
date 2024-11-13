from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from core.keyboards.main_kb import main_kb_as_markup
from core.db.scripts import get_user
from core.routers.registration import start_reg


router = Router()


@router.message(CommandStart())
async def start(mes: Message, state: FSMContext):
    await mes.answer(text="""Привет! 👋  Рада приветствовать вас в чате  Norland Academy! 

Хотите  освоить новую профессию  и  кардинально  изменить  свою  жизнь? 💫

Мы  предлагаем  обучение  по  самым  востребованным  направлениям на рынке:

- Воспитатель дошкольной организации
с дополнительной специализацией «гувернантка»
- HR - менеджер с нуля.
Рекрутер
- Рекрутер в подборе домашнего персонала
- Специалист по раннему развитию детей
- Педагог по ментальной арифметике
- Графический дизайн с нуля
- Ведущий мероприятий
- Аниматор, игропрактик
- Продюсер образовательных программ
- Методист образовательных программ
- Ассистент, персональный помощник руководителя
- Специалист по профиориентации
- Коррекционный специалист по работе с детьми с ОВ3

С  нашим  обучением  вы:

- Получите  практические  знания  от  опытных  преподавателей.
- Освоите  современные  программы  и  инструменты.
- Создадите портфолио  и  готов  к  успешной  карьере.

Напишите  мне  свою  мечту,  и  я  помогу  ее  воплотить!  ✨

Если вы еще не выбрал (а) свою нишу, мы разработали  короткий тест, который подскажет ваши сильные стороны и предложит профессию по душе! 

Давайте начнем!  😉""", reply_markup=main_kb_as_markup(mes.from_user.id))
    await mes.delete()
    await start_reg(mes, state)
