from discord.ext import commands

class LoggerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_connect(self):
        print(f"{self.bot.user} connected")

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.bot.user} ready")

    @commands.Cog.listener()
    async def on_disconnected(self):
        print(f"{self.bot.user} disconnected")