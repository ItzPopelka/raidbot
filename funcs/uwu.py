import discord
from discord.ext import commands

class Uwu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def uwu(self, ctx):
        try:
            await ctx.message.delete()
            try:
                await ctx.send("https://cdn.discordapp.com/attachments/1430965413289656501/1469122405652893828/ajdub0.gif?ex=6986825c&is=698530dc&hm=3626a9bf362c84471af8a8d618c550fc9c3827b1c4a0c24a5a6990096debaef6&")
                print(f"uwu command used")
            except Exception as e:
                print(f"failed to send uwu gif: {e}")
        except:
            pass

async def setup(bot):
    await bot.add_cog(Uwu(bot))