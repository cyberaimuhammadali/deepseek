from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()
supabase: Client = None

def init_supabase():
    global supabase
    supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

def get_supabase():
    return supabase