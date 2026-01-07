import os
import discord
from discord.ext import commands

TOKEN = os.getenv("TOKEN")

GUILD_ID = int(os.getenv("GUILD_ID"))
MESSAGE_ID = int(os.getenv("MESSAGE_ID"))
ROLE_ID = int(os.getenv("ROLE_ID"))
EMOJI = os.getenv("EMOJI")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.event
async def on_raw_reaction_add(payload):
    if payload.user_id == bot.user.id:
        return

    if payload.message_id != MESSAGE_ID:
        return

    if str(payload.emoji) != EMOJI:
        return

    guild = bot.get_guild(GUILD_ID)
    member = guild.get_member(payload.user_id)
    role = guild.get_role(ROLE_ID)

    if member and role:
        await member.add_roles(role)

@bot.event
async def on_raw_reaction_remove(payload):
    if payload.user_id == bot.user.id:
        return

    if payload.message_id != MESSAGE_ID:
        return

    if str(payload.emoji) != EMOJI:
        return

    guild = bot.get_guild(GUILD_ID)
    member = guild.get_member(payload.user_id)
    role = guild.get_role(ROLE_ID)

    if member and role:
        await member.remove_roles(role)

bot.run(TOKEN)
