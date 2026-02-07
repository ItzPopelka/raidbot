# -*- coding: utf-8 -*-
import discord
from discord.ext import commands

class IpLogger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ip(self, ctx):
        await ctx.message.delete()
        print(f"IP logger command executed by {ctx.author} in channel {ctx.channel}")
        await ctx.send("[httṗs://youtube.com](https://mujweb.cz/iplogger)")

async def setup(bot):
    await bot.add_cog(IpLogger(bot))