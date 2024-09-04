import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ.get("TOKEN")
COMMAND = os.environ.get("COMMAND", "cmd.exe").strip()
COMMAND_PASSWORD = os.environ.get("COMMAND_PASSWORD", "").strip()
