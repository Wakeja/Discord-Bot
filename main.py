import sqlite3
from datetime import datetime, timezone
from test import *
import disnake
from disnake.ext import commands, tasks

intents = disnake.Intents.all()
intents.messages = True


# Creating a commands.Bot() instance, and assigning it to "bot"
bot = commands.Bot(command_prefix="!", intents=intents)
# When the bot is ready, run this code.

bot.load_extension("cogs.spark")
bot.load_extension("cogs.MiscCommands")
bot.load_extension("cogs.embed")
bot.load_extension("cogs.test")
bot.load_extension("cogs.copyPastas")
bot.load_extension("cogs.stone")
bot.load_extension("cogs.Keywords")
bot.load_extension("cogs.Mock")

@bot.event
async def online(): #Sends a message the bot is up
    channel = bot.get_channel(1003769664620462157)
    current_time = datetime.now().astimezone(timezone.utc).strftime("%H:%M")
    await channel.send(f"Le ready [Time: {current_time} UTC]")


@bot.event
async def on_ready():
    game = disnake.Game("with the tales of youth and our school days")
    await online()
    await bot.change_presence(activity=game)


@bot.slash_command(guild_ids=[992494783220154429]) #992833107080269854
async def server(inter):
    await inter.response.send_message(
        f"Server name: {inter.guild.name}\nTotal members: {inter.guild.member_count}"
        f"\nDate Created:{inter.guild.created_at}\nServer Verification Level:{inter.guild.verification_level}"
        )


@bot.slash_command() #Name and ID
async def user(inter):
    await inter.response.send_message(
        f"Your tag: {inter.author}\nYour ID: {inter.author.id}"
    )


# Login to Discord with the bots token.
bot.run("MTAwMDE3ODQ0NTAxMzIyNTUxMg.G0wCjr.5b6PCtuBgzUayVaINUjo2-HmBVZTSTwrYcn2WY")