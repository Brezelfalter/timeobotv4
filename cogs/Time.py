import discord
import json

from __main__ import BASE_DIRECTORY, PREFIX
from discord.ext import commands
from datetime import datetime
from datetime import timedelta
from discord_components import DiscordComponents, ComponentsBot, Button



# getting bot version from json file
with open(f"{BASE_DIRECTORY}data/system/settings.json", "r") as file:
    data = json.load(file)
    BOT_VERSION = data["bot_info"]["version"]
    OWNERID = data["bot_info"]["owner-id"]




class Time(commands.Cog):
    def __init__(self, client):
        self.client = client

    
    @commands.Cog.listener()
    async def on_message(self, message):
        DiscordComponents(self.client)
        OFFSET = data["time"]["offset"]
        wordsList = []
        charListFront = []
        charListBack = []

        owner_id = self.client.get_user(OWNERID)

        for word in message.content:
            word.lower()
            wordsList.append(word)
            
        if message.content.startswith(f"{PREFIX}"):
            return
        if message.author == self.client.user:
            return
        elif ":" in wordsList:
            index = wordsList.index(":")

            count = 0    
            tempIndex = index

            while count < 2:
                count += 1
                tempIndex -= 1

                try:
                    character = int(wordsList[tempIndex])
                    charListFront.append(character)
                except:
                    return
                
            count = 0
            tempIndex = index

            while count < 2:
                count += 1
                tempIndex += 1

                try:
                    character = int(wordsList[tempIndex])
                    charListBack.append(character)
                except:
                    return 
        else:
            pass

        try:
            first = charListFront[1]*10
            second = charListFront[0]
            third = charListBack[0]*10
            fourth = charListBack[1]

            hour = first + second
            minute = third + fourth

            cur_time = f"{hour}:{minute}"
        except:
            return

        if len(wordsList) <= 5:
                await message.delete()
        else:
            pass



        if message.author.id == 531068649532817416:
            new_time = str(get_time(cur_time, float(f"-{OFFSET}"), message))
            new_time = new_time[11:][:-3]

            timeEmb = discord.Embed(
                title = f"Deutschland: {new_time} Uhr",
                colour = discord.Colour.blue()
            )
            await message.channel.send(
                embed=timeEmb, 
                components = [
                    Button(style="2", emoji="❗", custom_id="germanTime")
                ],
                delete_after=10
            )
            interaction = await self.client.wait_for("button_click", check = lambda i: i.custom_id == "germanTime")
            await interaction.send(content="Incorrect time has been reported.", ephemeral=True)
            
            await owner_id.send(
                f"REPORT: `{interaction.user}` has reported incorrect time. "
                f"\n\nguild: `{interaction.guild}` \nchannel: `{interaction.channel}` \nmsg ID: `{interaction.message.id}`"
                f"\n\ngiven time: `{cur_time}` \nrecieved time: `{new_time}` \noffset: `-{OFFSET}h`"
            )
        else:
            new_time = str(get_time(cur_time, OFFSET, message))
            new_time = new_time[11:][:-3]

            timeEmb = discord.Embed(
                title = f"Australien: {new_time} Uhr",
                colour = discord.Colour.orange()
            )         
            # timeEmb.set_footer(text="report wrong time:")
            await message.channel.send(
                embed=timeEmb, 
                components = [
                    Button(style="2", emoji="❗", custom_id="australianTime")
                ],
                delete_after=10
            )
            interaction = await self.client.wait_for("button_click", check = lambda i: i.custom_id == "australianTime")
            await interaction.send(content="Incorrect time has been reported.", ephemeral=True)
            
            await owner_id.send(
                f"REPORT: `{interaction.user}` has reported incorrect time. "
                f"\n\nguild: `{interaction.guild}` \nchannel: `{interaction.channel}` \nmsg ID: `{interaction.message.id}`"
                f"\n\ngiven time: `{cur_time}` \nrecieved time: `{new_time}` \noffset: `{OFFSET}h`"
            )

            
    @commands.command(brief="Get a time of Germany in the current Australian time")
    async def ga(self, ctx, cur_time):
        await ctx.channel.purge(limit=1)

        OFFSET = data["time"]["offset"]
        owner_id = self.client.get_user(OWNERID)
        try: 
            new_time = str(get_time(cur_time, float(f"{OFFSET}"), ctx))
            new_time = new_time[11:][:-3]
    
            timeEmb = discord.Embed(
                title = f"Australien: {new_time} Uhr",
                colour = discord.Colour.orange()
            )
            await ctx.channel.send(
                embed=timeEmb, 
                components = [
                    Button(style="2", emoji="❗", custom_id="germanTime")
                ],
                delete_after=10
            )
        except:
            await ctx.send("An error occured. Please make sure to use following time format: `hh:mm`", delete_after=10)
            
        interaction = await self.client.wait_for("button_click", check = lambda i: i.custom_id == "germanTime")
        await interaction.send(content="Incorrect time has been reported.", ephemeral=True)
        
        await owner_id.send(
            f"REPORT: `{interaction.user}` has reported incorrect time. "
            f"\n\nguild: `{interaction.guild}` \nchannel: `{interaction.channel}` \nmsg ID: `{interaction.message.id}`"
            f"\n\ngiven time: `{cur_time}` \nrecieved time: `{new_time}` \noffset: `-{OFFSET}h`"
        )


    @commands.command(brief="Get a time of Australia in the current German time")
    async def ag(self, ctx, cur_time):
        await ctx.channel.purge(limit=1)

        OFFSET = data["time"]["offset"]
        owner_id = self.client.get_user(OWNERID)
        try: 
            new_time = str(get_time(cur_time, float(f"-{OFFSET}"), ctx))
            new_time = new_time[11:][:-3]

            timeEmb = discord.Embed(
                title = f"Deutschland: {new_time} Uhr",
                colour = discord.Colour.blue()
            )
            await ctx.channel.send(
                embed=timeEmb, 
                components = [
                    Button(style="2", emoji="❗", custom_id="germanTime")
                ],
                delete_after=10
            )
        except:
            await ctx.send("An error occured. Please make sure to use following time format: `hh:mm`", delete_after=10)
            
        interaction = await self.client.wait_for("button_click", check = lambda i: i.custom_id == "germanTime")
        await interaction.send(content="Incorrect time has been reported.", ephemeral=True)
        
        await owner_id.send(
            f"REPORT: `{interaction.user}` has reported incorrect time. "
            f"\n\nguild: `{interaction.guild}` \nchannel: `{interaction.channel}` \nmsg ID: `{interaction.message.id}`"
            f"\n\ngiven time: `{cur_time}` \nrecieved time: `{new_time}` \noffset: `-{OFFSET}h`"
        )


    '''
    ///////////////////////////// OWNER ONLY COMMANDS //////////////////////////
    '''
    @commands.is_owner()
    @commands.command()
    async def offset(self, ctx, offset_change: float):
        await ctx.channel.purge(limit=1)
        update_data = {
            "time": {
                "offset": offset_change
            }
        }
        with open(f"{BASE_DIRECTORY}data/system/settings.json", "r+") as file:
            file_data = json.load(file)

            file_data.update(update_data)
            file.seek(0)

            json.dump(file_data, file, indent=4)



def get_time(input_str: str, offset : int, message):
    if offset == 9.5:
        logTime(f"User <{message.author}> asked for: {input_str} (Germany)")
    else:
        logTime(f"User <{message.author}> asked for: {input_str} (Australian)")


    parsed_time = datetime.strptime(input_str, "%H:%M")
    parsed_date = datetime.combine(datetime.today(), parsed_time.time())

    offset = timedelta(hours=offset)


    if offset == 9.5:
        logTime(f"User <{message.author}> recieved: {str(parsed_date + offset)[11:][:-3]} (Germany)")
    else:
        logTime(f"User <{message.author}> recieved: {str(parsed_date + offset)[11:][:-3]} (Australian)")
    return parsed_date + offset
        
def logTime(ctx):
    timestamp = datetime.now()

    with open(f"{BASE_DIRECTORY}data/time/requests.txt", "a")as file:
        file.write(f"{timestamp} --- {ctx}\n")




def setup(client):
    client.add_cog(Time(client))