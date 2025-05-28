import os

# Debugging prints (remove after testing)
print("API_ID:", os.getenv("API_ID"))
print("API_HASH:", os.getenv("API_HASH"))
print("BOT_TOKEN:", os.getenv("BOT_TOKEN"))
print("OWNER_ID:", os.getenv("OWNER_ID"))

# Convert and assign
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))
