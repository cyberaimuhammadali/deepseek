from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from bot.states.booking_states import BookingStates
from backend.services.booking_service import get_free_slots, create_booking
from bot.keyboards.inline import services_keyboard

router = Router()

@router.callback_query(F.data == "masters")
async def show_masters(callback: CallbackQuery):
    # Supabase dan ustalar ro'yxati
    await callback.message.edit_text("Ustalar ro'yxati...")
    await callback.answer()

@router.callback_query(F.data.startswith("service_"))
async def select_service(callback: CallbackQuery, state: FSMContext):
    service_id = int(callback.data.split("_")[1])
    await state.update_data(service_id=service_id)
    await callback.message.edit_text("Vaqtni tanlang:", reply_markup=await time_slots_keyboard(service_id))
    await state.set_state(BookingStates.select_time)

async def time_slots_keyboard(service_id):
    # Backend orqali bo'sh vaqtlarni olish
    slots = get_free_slots(service_id)
    buttons = [[InlineKeyboardButton(text=slot, callback_data=f"slot_{slot}")] for slot in slots]
    return InlineKeyboardMarkup(inline_keyboard=buttons)