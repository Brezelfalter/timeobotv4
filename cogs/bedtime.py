import discord
import json
import asyncio
import time

from __main__ import BASE_DIRECTORY, PREFIX
from discord.ext import commands, tasks
from datetime import datetime
from datetime import timedelta
from discord_components import DiscordComponents, ComponentsBot, Button



# getting bot version from json file
with open(f"{BASE_DIRECTORY}data/system/settings.json", "r") as file:
    data = json.load(file)
    BOT_VERSION = data["bot_info"]["version"]
    OWNERID = data["bot_info"]["owner-id"]




class Bedtime(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._batch = []
        self.lock = asyncio.Lock()
        self.bulker.start()

    @tasks.loop(seconds=45.0)
    async def bulker(self):
        async with self.lock:
            time_now = str(datetime.now())[:-10][11:]

            if time_now == "20:00":
                channel = await self.client.fetch_channel(967650418043785246)
                
                await channel.send(f"**AB INS BETTCHEN FLAUSCHI** <@{702250034879791115}> <@{771010949565120552}>")

                time.sleep(60)
                
    @commands.command()
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def remindFlauschi(self, ctx):
        await ctx.channel.purge(limit=1)

        await ctx.send(f"**AB INS BETTCHEN FLAUSCHI** <@{702250034879791115}> <@{771010949565120552}>")





async def setup(client):
    await client.add_cog(Bedtime(client))