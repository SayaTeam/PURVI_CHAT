import importlib
from pyrogram import idle
import os

from SonaliChat import app
from SonaliChat.modules import ALL_MODULES

# Get port from environment variable, default to 8000 for Render/Railway
port = int(os.environ.get("PORT", 8000))

async def boot():
    await app.start()

    for module in ALL_MODULES:
        importlib.import_module(f"SonaliChat.modules.{module}")

    await idle()
    await app.stop()

if __name__ == "__main__":
    app.run(boot())
