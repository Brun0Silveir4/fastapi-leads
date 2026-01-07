from motor.motor_asyncio import AsyncIOMotorClient
import os 
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("MONGO_DB_NAME")


if not MONGO_URI:
    raise RuntimeError("MONGO_URI is not defined")

if not DB_NAME:
    raise RuntimeError("DB_NAME is not defined")

client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]