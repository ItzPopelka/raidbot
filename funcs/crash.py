import discord
from discord.ext import commands

class CrashSpam(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def crash(self, ctx):
        try:
            await ctx.message.delete()
        except:
            pass

        file_path = "assets/crash.gif"
        
        try:
            with open(file_path, 'rb') as f:
                discord_file = discord.File(f, filename="crash.gif")
                await ctx.send(file=discord_file)
                print("crash gif send")
        except FileNotFoundError:
            print(f"{file_path} wasnt found")
        except Exception as e:
            print(f"error: {e}")

async def setup(bot):
    await bot.add_cog(CrashSpam(bot))