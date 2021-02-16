import os
import discord

from dotenv import load_dotenv
from discord.ext import commands

## IMPORT COGS ##
from Cogs.Edit import EditCog
from Cogs.Logger import LoggerCog
from Cogs.Permissions import PermissionsCog
from Cogs.View import ViewCog

## INITIALIZE BOT ##
bot = commands.Bot(command_prefix="!")

## ADD COGS ##
bot.add_cog(EditCog(bot))
bot.add_cog(LoggerCog(bot))
bot.add_cog(PermissionsCog(bot))
bot.add_cog(ViewCog(bot))

## RUN BOT ##
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)