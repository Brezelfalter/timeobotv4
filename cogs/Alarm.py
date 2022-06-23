import discord
import json
import asyncio
import time
import requests
import youtube_dl 

from __main__ import BASE_DIRECTORY, PREFIX
from discord.ext import commands, tasks
from datetime import datetime
from datetime import timedelta



# getting bot version from json file
with open(f"{BASE_DIRECTORY}data/system/settings.json", "r") as file:
    data = json.load(file)
    BOT_VERSION = data["bot_info"]["version"]
    OWNERID = data["bot_info"]["owner-id"]




class Alarm(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._batch = []
        self.lock = asyncio.Lock()
        self.bulker.start()

    @tasks.loop(seconds=1.0)
    async def bulker(self):
        async with self.lock:
            pass
                
    @commands.command(brief="Sets an alarm for a specified time an a url to play a song from.")
    async def alarm(self, ctx, alarm_time : str, url : str):
        # alarm_time in format HH:MM
        # url as string

        await ctx.channel.purge(limit=1)
        
        if int(alarm_time[:-3]) > 23: 
            await ctx.send(f"Give a valid time in format HH:MM. \n\nCause of error: __{alarm_time[:-3]}__:{alarm_time[3:]}") 
            return

        if int(alarm_time[3:]) > 59: 
            await ctx.send(f"Give a valid time in format HH:MM. \n\nCause of error: {alarm_time[:-3]}:__{alarm_time[3:]}__")
            return

        try:
            if int(requests.get(url).status_code) >= 400:
                error_code = int(requests.get(url).status_code)
                error_message = requests.status_codes._codes[int(requests.get(url).status_code)]

                await ctx.send(f"The give url is not valid or unreachable. \n\n Error `{error_code}`: `{error_message}`", delete_after=5)
        except:
            await ctx.send(f"Fatal error. Can not get error code from url. Please try again with different url.", delete_after=5)

        update_data = {
            f"{ctx.user.id}": {
                "time": f"{alarm_time}",
                "url": f"{url}"
            }
        }
        self.json_update(f"{BASE_DIRECTORY}data/alarm/alarms.json", update_data)

        await ctx.send(f"Set an alarm for `<{alarm_time}>` playing from `<{url}>`.", delete_after=5)


    def json_update(filename, push_data, keys=None):
        # keys as list in order
        # push_data as dict

        with open(filename, "r+") as file:
            data = json.load(file)
            
            if keys != None:
                for item in keys: 
                    data = data[f"{keys[keys.index(item)]}"]

            data.update(push_data)
            file.seek(0)
            json.dump(data, file, indent=4)
        





def setup(client):
    client.add_cog(Alarm(client))
