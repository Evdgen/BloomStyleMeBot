from aiogram import Router
from aiogram.types import Message
from aiogram import F

from keyboards import main_menu, style_menu, makeup_scene_menu
from database import get_user_skin_type, get_user_budget
from product_engine import get_products_by_style
from style_engine import get_style_recommendations

router = Router()

# --- Обработчик меню стилей ---
@router.message(F.text == "💼 Подбор стиля")
async def style_recommendation(message: Message):
    user_id = message.from_user.id
    skin_type = get_user_skin_type(user_id)
    
    if not skin_type:
        await message.answer(
            "Сначала определи свой тип кожи!\n"
            "Нажми '🌸 Подобрать образ' и выбери тип кожи.",
            reply_markup=main_menu()
        )
        return
    
    await message.answer(
        "Выбери стиль, который тебе интересен:",
        reply_markup=style_menu()
    )

# --- Обработчики выбора стиля ---
@router.message(F.text == "👔 Деловой")
async def business_style(message: Message):
    user_id = message.from_user.id
    skin_type = get_user_skin_type(user_id)
    budget = get_user_budget(user_id)
    
    recommendations = get_style_recommendations("деловой", skin_type)
    products = get_products_by_style("деловой", budget)
    
    await message.answer(
        f"{recommendations}\n\n{products}",
        reply_markup=style_menu()
    )

@router.message(F.text == "👖 Кэжуал")
async def casual_style(message: Message):
    user_id = message.from_user.id
    skin_type = get_user_skin_type(user_id)
    budget = get_user_budget(user_id)
    
    recommendations = get_style_recommendations("кэжуал", skin_type)
    products = get_products_by_style("кэжуал", budget)
    
    await message.answer(
        f"{recommendations}\n\n{products}",
        reply_markup=style_menu()
    )

@router.message(F.text == "🎉 Вечерний")
async def evening_style(message: Message):
    user_id = message.from_user.id
    skin_type = get_user_skin_type(user_id)
    budget = get_user_budget(user_id)
    
    recommendations = get_style_recommendations("вечерний", skin_type)
    products = get_products_by_style("вечерний", budget)
    
    await message.answer(
        f"{recommendations}\n\n{products}",
        reply_markup=style_menu()
    )

@router.message(F.text == "🏃 Спортивный")
async def sport_style(message: Message):
    user_id = message.from_user.id
    skin_type = get_user_skin_type(user_id)
    budget = get_user_budget(user_id)
    
    recommendations = get_style_recommendations("спортивный", skin_type)
    products = get_products_by_style("спортивный", budget)
    
    await message.answer(
        f"{recommendations}\n\n{products}",
        reply_markup=style_menu()
    )

# --- Кнопка "Назад" ---
@router.message(F.text == "🔙 Назад")
async def back_to_style_menu(message: Message):
    await message.answer("Выбери стиль:", reply_markup=style_menu())
