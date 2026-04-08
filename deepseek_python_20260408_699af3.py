from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

def main_menu_keyboard():
    web_app = WebAppInfo(url="https://your-frontend-url.onrender.com")  # Mini app URL
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💇‍♀️ Xizmatlar va Bron", web_app=web_app)],
        [InlineKeyboardButton(text="📅 Mening bronlarim", callback_data="my_bookings")],
        [InlineKeyboardButton(text="⭐ Ustalar", callback_data="masters")],
        [InlineKeyboardButton(text="🎁 Aksiyalar", callback_data="promos")],
        [InlineKeyboardButton(text="☎️ Admin bilan bog'lanish", callback_data="contact_admin")]
    ])

def services_keyboard(services):
    buttons = []
    for s in services:
        buttons.append([InlineKeyboardButton(text=f"{s['name']} - {s['price']} so'm", callback_data=f"service_{s['id']}")])
    buttons.append([InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_main")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)