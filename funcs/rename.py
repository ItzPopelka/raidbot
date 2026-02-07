# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
import asyncio

class RenameALL(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rename_all(self, ctx, *, new_name="ez raid"):
        try:
            await ctx.message.delete()
        except:
            pass
    
        guild = ctx.guild
    
        for member in guild.members:
            try:
                await member.edit(nick=new_name)
                print(f"renamed {member.name} to {new_name}")
                await asyncio.sleep(0.5)
            except Exception as e:
                print(f"failed to rename {member.name}: {e}")

async def setup(bot):
    await bot.add_cog(RenameALL(bot))