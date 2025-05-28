import os

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = os.getenv("OWNER_ID")

# Validate environment variables
missing = []
if not API_ID:
    missing.append("API_ID")
if not API_HASH:
    missing.append("API_HASH")
if not BOT_TOKEN:
    missing.append("BOT_TOKEN")
if not OWNER_ID:
    missing.append("OWNER_ID")

if missing:
    raise EnvironmentError(f"Missing required environment variables: {', '.join(missing)}")

# Convert to correct types
API_ID = int(API_ID)
OWNER_ID = int(OWNER_ID)
