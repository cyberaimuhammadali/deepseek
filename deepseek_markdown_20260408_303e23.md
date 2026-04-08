# Beauty Lab avtomatlashtirilgan Telegram boti

## O'rnatish

1. `.env` faylini yarating va tokenlarni kiriting.
2. Supabase da yuqoridagi SQL skriptni ishlating.
3. `docker-compose up --build` bilan ishga tushiring.
4. Render.com da:
   - Backend: `uvicorn backend.main:app --host 0.0.0.0 --port 10000`
   - Frontend: statik fayllarni hosting (Netlify yoki Render static)
   - Bot webhook: `https://your-backend.onrender.com/webhook` (agar siz webhook sozlagan bo'lsangiz)

## Xususiyatlar
- AI asosida tavsiyalar (transformers kutubxonasi bilan)
- Real vaqtda bron
- Mini app orqali chiroyli interfeys
- Scraper orqali ma'lumotlarni yangilash

## Kelajakdagi yaxshilanishlar
- Click / Payme to'lov integratsiyasi
- Telefon raqam orqali tasdiqlash
- Kengaytirilgan admin panel