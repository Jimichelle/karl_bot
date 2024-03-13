import os
import random
from dotenv import load_dotenv

import discord
from discord import app_commands
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="|",intents=intents)

intents.message_content = True
intents.guilds = True
intents.members = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)



@bot.event
async def on_ready():
    print(f"{bot.user.name} est connecté")
    print("Username : ", bot.user.name) 
    print("User ID : ", bot.user.id)

    try:
        synced = await bot.tree.sync(guild=discord.Object(id=1138070170129149994))
        print(f"Synced {len(synced)} commands")

    except Exception as e:
        print(f"Failed to sync commands: {e}")


@bot.tree.command(guild=discord.Object(id=1138070170129149994), name="test", description="Test command")
async def test_slash(interaction: discord.Interaction):
    await interaction.response.send_message("TEST!", ephemeral=True)

@bot.tree.command(guild=discord.Object(id=1138070170129149994), name="bonjour", description="Test command")
async def test_slash(interaction: discord.Interaction):
    await interaction.response.send_message("bonjour", ephemeral=True)

@bot.tree.command(guild=discord.Object(id=1138070170129149994), name="random", description="Random")
async def test_slash(interaction: discord.Interaction):
    rand = random.randint(1, 100)
    if rand < 50:
        await interaction.response.send_message("Perdu", ephemeral=True)
    else:
        await interaction.response.send_message("Gagné", ephemeral=True)

@bot.command(name="sympatique", description="La commande trop sympatique")
async def sympa_command(ctx):
    await ctx.send("Va manger du caca")
    
bot.run(TOKEN)