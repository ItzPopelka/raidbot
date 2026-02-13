# dont change anything in imports or you can (90% sure) break the bot
import discord
from discord.ext.commands import *
from discord.ext import commands
import asyncio
import os
import json

# =======================================
# ========== DISCORD BOT TOKEN ==========
# =======================================
# 1. Create a file named "token.json" in the same directory as this script.

# 2. Add the following content to "token.json":
# {"TOKEN": "YOUR_BOT_TOKEN"}

# 3. Replace "YOUR_BOT_TOKEN" with your actual Discord bot token.

# 4. Make sure to add "token.json" to your .gitignore file to prevent it from being uploaded to version control.
token = json.load(open("token.json", "r"))["TOKEN"]

# =======================================
# ============ BOT SETTINGS =============
# =======================================
# intents are required for the bot to function properly, especially if you want to access certain events or data.
intents = discord.Intents.all()

# choose a command prefix for your bot (just make sure its not too common to avoid conflicts with other bots; it uses like "r?[command]")
bot = commands.Bot(command_prefix='r?', intents=intents)

# just a simple way to remove the default help command so you can create your own custom one later if you want
bot.remove_command('help')

# =======================================
# ============= BOT EVENTS ==============
# =======================================
# on ready event is triggered when the bot has successfully connected to Discord and is ready to start receiving events and commands
@bot.event
async def on_ready():
    print(f"logged in as {bot.user} (ID: {bot.user.id})")
    await bot.change_presence(
        status=discord.Status.invisible,  # online, idle, dnd, invisible || i use invisible for stealth
        activity=discord.Game(name="popelka is boss")
    )


# =======================================
# ============ FUNCS LOADER =============
# =======================================
# just a semi-simple way to load all the command files in the "funcs" directory without having to import them manually one by one
async def load_extensions():
    funcs_dir = "funcs"
    
    extensions = [f[:-3] for f in os.listdir(funcs_dir)
                if f.endswith('.py') and f != '__init__.py' and not f.startswith('__')]

    if "update" in extensions:
        extensions.remove("update")
        try:
            await bot.load_extension(f"{funcs_dir}.update")
            print("priority loaded: update")
        except Exception as e:
            print(f"critical error loading update: {e}")

    for ext in extensions:
        try:
            await bot.load_extension(f"{funcs_dir}.{ext}")
            print(f"loaded: {ext}")
        except Exception as e:
            print(f"error while loading {ext}: {e}")

# =======================================
# ============= BOT START ===============
# =======================================
# dont change anything here, this is just the code to start the bot and use the loaded extensions
async def main():
    async with bot:
        await load_extensions()
        await bot.start(token)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())