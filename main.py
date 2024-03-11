import os
from dotenv import load_dotenv
import discord

from discord import app_commands

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!k",intents=intents)

intents.message_content = True
intents.guilds = True
intents.members = True

@bot.event
async def on_ready():
    print(f"{bot.user.name} est connecté")

bot.run(TOKEN)