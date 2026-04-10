from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import F

from keyboards import (
    main_menu, skin_type_menu, budget_menu,
    bloom_menu, product_search_menu, travel_menu,
    style_menu, makeup_scene_menu, settings_menu, help_menu
)
from texts import WELCOME, DISCLAIMER, SAFETY_TIPS, HELP
from database import (
    set_user_city, get_user_city, set_user_skin_type,
    set_user_budget, init_user_stats
)

router = Router()

# --- Команда /start ---
@router.message(CommandStart())
async def start(message: Message):
    user_id = message.from_user.id
    init_user_stats(user_id)
    await message.answer(WELCOME, reply_markup=main_menu())

# --- Команда /help ---
@router.message(F.text == "❓ Помощь")
async def help_command(message: Message):
    await message.answer(HELP, reply_markup=help_menu())

# --- Кнопка "Подобрать образ" ---
@router.message(F.text == "🌸 Подобрать образ")
async def choose_style(message: Message):
    await message.answer(
        "Давай подберем твой идеальный образ!\n\nСначала выбери тип кожи:",
        reply_markup=skin_type_menu()
    )

# --- Кнопка "Мои сохранения" ---
@router.message(F.text == "👗 Мои сохранения")
async def my_saves(message: Message):
    await message.answer(
        "Мои сохранения\n\nЗдесь будут храниться твои любимые образы.\nПока что тут пусто — сохрани первый образ!",
        reply_markup=main_menu()
    )

# --- Кнопка "Связаться со стилистом" ---
@router.message(F.text == "📞 Связаться со стилистом")
async def contact_stylist(message: Message):
    await message.answer(
        "Связь со стилистом\n\nНапиши нам: @evd_gen\nИли отправь сообщение прямо сюда — я передам!",
        reply_markup=main_menu()
    )

# --- Обработчики выбора типа кожи ---
@router.message(F.text == "Светлая кожа")
async def light_skin(message: Message):
    user_id = message.from_user.id
    set_user_skin_type(user_id, "светлая")
    await message.answer(
        "Сохранила: Светлая кожа\n\nТеперь выбери свой бюджет:",
        reply_markup=budget_menu()
    )

@router.message(F.text == "Смуглая кожа")
async def dark_skin(message: Message):
    user_id = message.from_user.id
    set_user_skin_type(user_id, "смуглая")
    await message.answer(
        "Сохранила: Смуглая кожа\n\nТеперь выбери свой бюджет:",
        reply_markup=budget_menu()
    )

@router.message(F.text == "Оливковая кожа")
async def olive_skin(message: Message):
    user_id = message.from_user.id
    set_user_skin_type(user_id, "оливковая")
    await message.answer(
        "Сохранила: Оливковая кожа\n\nТеперь выбери свой бюджет:",
        reply_markup=budget_menu()
    )

# --- Обработчики выбора бюджета ---
@router.message(F.text == "До 3000 ₽")
async def budget_low(message: Message):
    user_id = message.from_user.id
    set_user_budget(user_id, "до 3000")
    await message.answer(
        "Сохранила бюджет: до 3000 ₽\n\nПодбор стиля завершён!\nСкоро я покажу тебе подходящие образы.",
        reply_markup=main_menu()
    )

@router.message(F.text == "3000-10000 ₽")
async def budget_mid(message: Message):
    user_id = message.from_user.id
    set_user_budget(user_id, "3000-10000")
    await message.answer(
        "Сохранила бюджет: 3000-10000 ₽\n\nПодбор стиля завершён!\nСкоро я покажу тебе подходящие образы.",
        reply_markup=main_menu()
    )

@router.message(F.text == "От 10000 ₽")
async def budget_high(message: Message):
    user_id = message.from_user.id
    set_user_budget(user_id, "от 10000")
    await message.answer(
        "Сохранила бюджет: от 10000 ₽\n\nПодбор стиля завершён!\nСкоро я покажу тебе подходящие образы.",
        reply_markup=main_menu()
    )

# --- Кнопка "Назад" ---
@router.message(F.text == "🔙 Назад")
async def back_button(message: Message):
    await message.answer("Возвращаюсь в главное меню", reply_markup=main_menu())

# --- Кнопка "Назад в главное меню" ---
@router.message(F.text == "🔙 Главное меню")
async def back_to_main(message: Message):
    await message.answer("Возвращаюсь в главное меню", reply_markup=main_menu())

# --- Заглушка на любое другое сообщение ---
@router.message()
async def unknown_message(message: Message):
    await message.answer(
        "Пожалуйста, используй кнопки меню для навигации.\n\nЕсли нужна помощь — нажми 'Помощь'",
        reply_markup=main_menu()
    )
