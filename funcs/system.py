# this file has commands stop and restart


import discord
from discord.ext import commands
import os
import sys
import bot

class System(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def restart(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        print("restarting bot...")
        await self.bot.close()
        os.execv(sys.executable, ['python'] + sys.argv)

    @commands.command()
    async def stop(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        print("stopping bot...")
        await self.bot.close()

async def setup(bot):
    await bot.add_cog(System(bot))