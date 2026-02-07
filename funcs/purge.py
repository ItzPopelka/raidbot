# -*- coding: utf-8 -*-
import discord
from discord.ext import commands

class PurgeALL(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def purge_all(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass
    
        guild = ctx.guild
    
        for channel in guild.text_channels:
            try:
                await channel.purge(limit=None)
                print(f"purged {channel.name}")
            except:
                pass

async def setup(bot):
    await bot.add_cog(PurgeALL(bot))