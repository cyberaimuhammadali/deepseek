from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.api import endpoints
from backend.utils.supabase_client import init_supabase

app = FastAPI(title="Beauty Salon Bot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(endpoints.router, prefix="/api")

@app.on_event("startup")
async def startup():
    init_supabase()

@app.get("/")
def root():
    return {"status": "Beauty Lab Bot API ishlayapti"}