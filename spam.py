import discord
from discord.ext import commands
import asyncio
import json
import os

# Load configuration from config.json
with open("config.json") as f:
    config = json.load(f)
    guild_id = int(config["spam_guild_id"])
    role_id = int(config["ping_role_id"])
    bot_token = config["bot_token"]

# Initialize the bot
bot = commands.Bot(command_prefix="!", help_command=None)

# Define the ping task
async def ping_task(channel_id):
    while True:
        guild = bot.get_guild(guild_id)
        channel = guild.get_channel(channel_id)
        if channel:
            await channel.send(f"@everyone AHHAHAH DUMP!")
        await asyncio.sleep(0.01)  # Adjust the interval as needed

# Event handler for bot ready
@bot.event
async def on_ready():
    print(f"Bot is ready. Guild ID: {guild_id}")
    channel_id = int(input("Enter the channel ID where you want to ping everyone: "))
    bot.loop.create_task(ping_task(channel_id))

# Run the bot
bot.run(bot_token)
