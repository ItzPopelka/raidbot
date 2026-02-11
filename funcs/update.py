import discord
from discord.ext import commands
import random
import string
import subprocess
import os

pending_updates = {}


class Update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def update(self, ctx, os_type: str):
        os_type = os_type.lower()
        if os_type not in ['win', 'linux']:
            print("Specify whether ```win``` or ```linux```")
            return

        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        pending_updates[ctx.guild.id] = {'code': code, 'os': os_type}
        print(f"New update code: {code} for {os_type}")

    @commands.command()
    async def update_code(self, ctx, code: str):
        guild_id = ctx.guild.id

        if guild_id not in pending_updates or pending_updates[guild_id]['code'] != code:
            print("Wrong code")
            return

        os_type = pending_updates[guild_id]['os']

        del pending_updates[guild_id]

        try:
            if os_type == 'win':
                subprocess.Popen(['scripts/update.bat'], shell=True)
            else:
                subprocess.Popen(['bash', '.scripts/update.sh'])
            print(f"Update script for {os_type} was executed")
        except Exception as e:
            print(f"Error: {e}")

async def setup(bot):
    await bot.add_cog(Update(bot))