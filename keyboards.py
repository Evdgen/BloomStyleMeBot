from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    buttons = [
        [KeyboardButton(text="🌸 Подобрать образ")],
        [KeyboardButton(text="👗 Мои сохранения")],
        [KeyboardButton(text="📞 Связаться со стилистом")],
        [KeyboardButton(text="❓ Помощь")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def skin_type_menu():
    buttons = [
        [KeyboardButton(text="Светлая кожа")],
        [KeyboardButton(text="Смуглая кожа")],
        [KeyboardButton(text="Оливковая кожа")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

def budget_menu():
    buttons = [
        [KeyboardButton(text="До 3000 ₽")],
        [KeyboardButton(text="3000-10000 ₽")],
        [KeyboardButton(text="От 10000 ₽")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
