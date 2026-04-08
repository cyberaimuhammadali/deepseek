from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from bot.keyboards.inline import main_menu_keyboard

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    user = message.from_user
    # Foydalanuvchini DB ga qo'shish (supabase orqali)
    await message.answer(
        f"Assalomu alaykum, {user.full_name}!\n"
        "Beauty Lab avtomatlashtirilgan tizimiga xush kelibsiz.\n"
        "Quyidagi menyu orqali bron qilishingiz mumkin:",
        reply_markup=main_menu_keyboard()
    )

@router.message(Command("menu"))
async def cmd_menu(message: Message):
    await message.answer("Asosiy menyu:", reply_markup=main_menu_keyboard())
