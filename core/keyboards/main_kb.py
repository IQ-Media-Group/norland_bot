from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder, KeyboardButton, ReplyKeyboardMarkup
from core.db.scripts import get_user


def main_kb_as_markup(tg_id: int) -> ReplyKeyboardMarkup:
    main_kb = ReplyKeyboardBuilder()
    main_kb.add(KeyboardButton(text='Пройти тест'))

    if not get_user(tg_id):
        main_kb.add(KeyboardButton(text='Регистрация'))

    main_kb.max_width = 2

    return main_kb.as_markup(resize_keyboard=True)