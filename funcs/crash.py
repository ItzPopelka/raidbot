import discord
from discord.ext import commands

class CrashSpam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def spam_crash(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        for _ in range(100):
            #TODO: add discord-crashing gif
            await ctx.send("---")

async def setup(bot):
    await bot.add_cog(CrashSpam(bot))