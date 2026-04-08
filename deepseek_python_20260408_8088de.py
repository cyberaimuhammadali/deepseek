from backend.utils.supabase_client import get_supabase
from datetime import datetime, timedelta

def get_free_slots(service_id, date=None):
    if not date:
        date = datetime.now().date()
    # Soat 9:00 dan 20:00 gacha, 30 daqiqalik intervallar
    slots = []
    start = datetime(date.year, date.month, date.day, 9, 0)
    for i in range(22):  # 9:00 dan 20:00 gacha
        slot = start + timedelta(minutes=30*i)
        if slot.time() <= datetime.strptime("20:00", "%H:%M").time():
            slots.append(slot.strftime("%H:%M"))
    # DB da band bo'lganlarni olib tashlash (real implementatsiya)
    return slots[:10]

def create_booking(user_id, service_id, master_id, booking_time):
    supabase = get_supabase()
    data = {
        "user_id": user_id,
        "service_id": service_id,
        "master_id": master_id,
        "booking_time": booking_time,
        "status": "confirmed"
    }
    result = supabase.table("bookings").insert(data).execute()
    return result.data[0] if result.data else None