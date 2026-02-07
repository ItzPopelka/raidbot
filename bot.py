import discord
from discord.ext.commands import *
from discord.ext import commands
import asyncio
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='r?', intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f"logged in as {bot.user} (ID: {bot.user.id})")
    await bot.change_presence(
        status=discord.Status.invisible,  # online, idle, dnd, invisible || i use invisible for stealth
        activity=discord.Game(name="popelka je boss")
    )

import base64
def encrypt_token(token):
    return base64.b64encode(token.encode()).decode()
def decrypt_token(encrypted):
    return base64.b64decode(encrypted.encode()).decode()

async def load_extensions():
    funcs_dir = "funcs"
    extensions = [f[:-3] for f in os.listdir(funcs_dir)
                if f.endswith('.py') and f != '__init__.py' and not f.startswith('__')]
    
    for ext in extensions:
        try:
            await bot.load_extension(f"{funcs_dir}.{ext}")
            print(f"loaded: {ext}")
        except Exception as e:
            print(f"error while loading {ext}: {e}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start("token")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())