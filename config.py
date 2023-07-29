import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get("TOKEN")
MINIMAL_MORTGAGE = int(os.environ.get("MINIMAL_MORTGAGE", "300_000"))
INITIAL_FEE_PERCENT = int(os.environ.get("INITIAL_FEE_PERCENT", "15"))
