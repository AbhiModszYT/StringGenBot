import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "12227067").strip()
API_HASH = os.getenv("API_HASH", "b463bedd791aa733ae2297e6520302fe").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "postgres://citus:AbhiModszYT12@c-yone.2iti2yet5lss6l.postgres.cosmos.azure.com:5432/yone").strip()
MUST_JOIN = os.getenv("MUST_JOIN", "AMBOTYT")

if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit

try:
    API_ID = int(API_ID)
except ValueError:
    print("API_ID is not a valid integer. Exiting...")
    raise SystemExit

if "postgres" in DATABASE_URL and "postgresql" not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
