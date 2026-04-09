from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# --- Главное меню ---
def main_menu():
    buttons = [
        [KeyboardButton(text="🌸 Подобрать образ")],
        [KeyboardButton(text="👗 Мои сохранения")],
       KeyboardButton(text="📞 Связаться со стилистом"),
        [KeyboardButton(text="❓ Помощь")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

# --- Меню типа кожи ---
def skin_type_menu():
    buttons = [
        [KeyboardButton(text="Светлая кожа")],
        [KeyboardButton(text="Смуглая кожа")],
        [KeyboardButton(text="Оливковая кожа")],
        [KeyboardButton(text="🔙 Назад")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

# --- Меню бюджета ---
def budget_menu():
    buttons = [
        [KeyboardButton(text="До 3000 ₽")],
        [KeyboardButton(text="3000-10000 ₽")],
        [KeyboardButton(text="От 10000 ₽")],
        [KeyboardButton(text="🔙 Назад")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

# --- Меню Bloom ---
def bloom_menu():
    buttons = [
        [KeyboardButton(text="🌸 Цветотип")],
        [KeyboardButton(text="👤 Форма лица")],
        [KeyboardButton(text="💼 Подбор стиля")],
        [KeyboardButton(text="🔙 Назад")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

# --- Меню поиска товаров ---
def product_search_menu():
    buttons = [
        [KeyboardButton(text="👕 Футболки")],
        [KeyboardButton(text="👖 Джинсы")],
        [KeyboardButton(text="👗 Платья")],
        [KeyboardButton(text="🧥 Куртки")],
        [KeyboardButton(text="👟 Обувь")],
        [KeyboardButton(text="🔙 Назад")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

# --- Меню путешествий ---
def travel_menu():
    buttons = [
        [KeyboardButton(text="✈️ Лёгкий гардероб")],
        [KeyboardButton(text="🏖️ Пляжный образ")],
        [KeyboardButton(text="🏔️ Горный трекинг")],
        [KeyboardButton(text="🌆 Городской тур")],
        [KeyboardButton(text="🔙 Назад")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

# --- Меню стилей ---
def style_menu():
    buttons = [
        [KeyboardButton(text="👔 Деловой")],
        [KeyboardButton(text="👖 Кэжуал")],
        [KeyboardButton(text="🎉 Вечерний")],
        [KeyboardButton(text="🏃 Спортивный")],
        [KeyboardButton(text="🔙 Назад")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

# --- Меню макияжа и причёсок ---
def makeup_scene_menu():
    buttons = [
        [KeyboardButton(text="💄 Дневной макияж")],
        [KeyboardButton(text="✨ Вечерний макияж")],
        [KeyboardButton(text="💇 Причёски")],
        [KeyboardButton(text="🔙 Назад")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

# --- Меню знаний (knowledge) ---
def knowledge_menu():
    buttons = [
        [KeyboardButton(text="📚 Цветотипы")],
        [KeyboardButton(text="👤 Формы лица")],
        [KeyboardButton(text="👗 Стили одежды")],
        [KeyboardButton(text="🔙 Назад")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

# --- Меню настроек ---
def settings_menu():
    buttons = [
        [KeyboardButton(text="👤 Мой профиль")],
        [KeyboardButton(text="📍 Город")],
        [KeyboardButton(text="🎨 Цветотип")],
        [KeyboardButton(text="🔙 Главное меню")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)

# --- Меню помощи ---
def help_menu():
    buttons = [
        [KeyboardButton(text="📖 О боте")],
        [KeyboardButton(text="❓ Частые вопросы")],
        [KeyboardButton(text="📞 Контакты")],
        [KeyboardButton(text="🔙 Назад")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
