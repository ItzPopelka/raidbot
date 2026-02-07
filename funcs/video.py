# this file has commands for spamming czech meme music and video of epstien dancing


import discord
from discord.ext.commands import *
from discord.ext import commands

class Video(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def spam_muzik1(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        while True:
            try:
                await ctx.send("https://www.youtube.com/watch?v=731b3l-9KOI&list=OLAK5uy_k6Z-HR97OYUjeJ3C8-AYLNfiCBs4-20qk")
                print("music sent")
            except Exception as e:
                print(f"failed to send music: {e}")

    @commands.command()
    async def spam_muzik2(self,ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        while True:
            try:
                await ctx.send("https://www.youtube.com/watch?v=Wd8LmGIjojI&list=RDWd8LmGIjojI&start_radio=1")
                print("music sent")
            except Exception as e:
                print(f"failed to send music: {e}")

    @commands.command()
    async def spam_video(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        while True:
            try:
                await ctx.send("https://cdn.discordapp.com/attachments/1467480445586509937/1467873798757023937/K7KelLL.mov?ex=6981f781&is=6980a601&hm=3d0e1b11a5c412373e2c8853ef682c7bf41efd1d3b41042e656428d3695fe068&")
                print("video sent")
            except Exception as e:
                print(f"failed to send video: {e}")

async def setup(bot):
    await bot.add_cog(Video(bot))