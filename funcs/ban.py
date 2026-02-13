# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
import asyncio

class BanALL(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban_all(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass
    
        guild = ctx.guild
        banned_count = 0
    
        for member in guild.members:
            try:
            
                if member == ctx.author:
                    continue
            
                await member.ban(reason="popelka is boss")
                banned_count += 1
                print(f"banned: {member.name}")
            
                await asyncio.sleep(1)
            
            except discord.Forbidden:
                print(f"no permission to ban: {member.name}")
            except Exception as e:
                print(f"error banning {member.name}: {e}")
    
        await ctx.send(f"banned {banned_count} members")

async def setup(bot):
    await bot.add_cog(BanALL(bot))