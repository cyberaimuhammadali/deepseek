# Bu real veb-saytdan ma'lumot olish uchun asos. 
# Sizga moslab o'zgartirishingiz mumkin.
from bs4 import BeautifulSoup
import aiohttp

async def fetch_beautylab_services():
    url = "https://beautylab.uz/services"  # misol
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            html = await resp.text()
    soup = BeautifulSoup(html, 'html.parser')
    # Sayt strukturasiga mos ravishda ma'lumotlarni ajratib oling
    services = []
    # ... parse qilish ...
    return services