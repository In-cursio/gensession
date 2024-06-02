from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "29922662"))
API_HASH = getenv("API_HASH", "fabd9f89368de7cc31357522a0089a56")

BOT_TOKEN = getenv("BOT_TOKEN", "7209509711:AAFgCugkXL7NgDt__CFvFsPpJyK_jd4eEsU")
#OWNER_ID = int(getenv("6752444356"))
OWNER_ID = int(getenv("OWNER_ID", "6047510747"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://animebot:animebot@cluster0.h0ix44k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUST_JOIN = getenv("MUST_JOIN", "Cv_official_channel")
