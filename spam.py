import discord
from discord.ext import commands
import asyncio
import json
import os



filename = "config.json"
if os.path.isfile(filename):
    print(f"{filename} exists.")
else:
    print(f"{filename} does not exist.")


pingr = commands.Bot(command_prefix="!", help_command=None)



with open("config.json") as f:
    geb = json.load(f)
    guildid  =  int(geb["spam_guild_id"])
    roleid   =  int(geb["ping_role_id"])
    bottoken =  geb["bot_token"]

async def ping_task():
    while True:
        guild = pingr.get_guild(guildid)
        for channel in guild.channels:
            if isinstance(channel, discord.TextChannel):
                if channel.name.startswith('general'): #specify channel name
                    await channel.send(f"@everyone HI :)!!! AHAHHAHAHAHHa")
                    await asyncio.sleep(0.01)
                else:
                    pass
                  
@pingr.event
async def on_ready():
    pingr.loop.create_task(ping_task())

@pingr.slash_command(guild_ids=[guildid])
async def ping(ctx):
    await ctx.respond(f"{round(pingr.latency * 10)}ms")


pingr.run(bottoken)
