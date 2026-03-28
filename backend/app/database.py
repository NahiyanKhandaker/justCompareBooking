import os
from pathlib import Path
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load .env file from backend directory
ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")

# Get database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise EnvironmentError("DATABASE_URL is not set. Check backend/.env and make sure it defines DATABASE_URL.")

# Create connection
engine = create_engine(DATABASE_URL)

# Test connection (optional)
try:
    connection = engine.connect()
    print("✅ Connected to database!")
    connection.close()
except Exception as e:
    print("❌ Database connection failed:", e)