import discord
import json
import duden

from __main__ import BASE_DIRECTORY, PREFIX
from discord.ext import commands

# getting bot version from json file
with open(f"{BASE_DIRECTORY}data/system/settings.json", "r") as file:
    data = json.load(file)
    BOT_VERSION = data["bot_info"]["version"]
    COMMAND_BLACKLIST = data["bot_info"]["command_blacklist"]


class Duden(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    
    @commands.command(brief="Lookup any word in the Duden and get information about it.")
    async def d(self, ctx, word=None):
        '''
        uses the "duden" module to lookup words in german, then 
        puts everything together in an Embed
        '''
        await ctx.channel.purge(limit=1)

        if any([word == "Brust", word == "brust", word == "Brüste", word == "brüste"]):
            duden_embed = discord.Embed(
                title="[d][duden] --- [Duden]",
                description="** **",
                colour=discord.Colour.gold()
            )

            duden_embed.add_field(name="Brust, die", value="Substantiv, feminin")
            duden_embed.add_field(name="Häufigkeit", value="3/5")
            duden_embed.add_field(name="** **", value="** **", inline=False)
            duden_embed.add_field(name="** **", value="** **", inline=False)
            duden_embed.add_field(name="Bedeutung", value="paariges, halbkugelförmiges Organ (an der Vorderseite des weiblichen Oberkörpers), das die Milchdrüsen enthält und das in der Stillzeit Milch bildet", inline=False)
            
            await ctx.send(embed=duden_embed, delete_after=30)
            return

        if word == None:
            word = duden.get_word_of_the_day
        else:
            word = duden.get(word)
        
        duden_embed = discord.Embed(
            title="[d][duden] --- [Duden]",
            description="** **",
            colour=discord.Colour.gold()
        )

        if word.title != None:
            duden_embed.add_field(name=word.title, value=word.part_of_speech)
        if word.frequency != None:
            duden_embed.add_field(name="Häufigkeit", value=f"{word.frequency}/5")
        if word.word_separation != None:
            duden_embed.add_field(name="Trennung", value=self.replace_max_chars(word.word_separation))
        if word.usage != None: 
            duden_embed.add_field(name="Benutzung", value=self.replace_max_chars(word.usage), inline=False)
            
        duden_embed.add_field(name="** **", value="** **", inline=False)
        if word.origin != None: 
            duden_embed.add_field(name="Herkunft", value=self.replace_max_chars(word.origin))
        duden_embed.add_field(name="** **", value="** **", inline=False)
        if word.meaning_overview != None: 
            duden_embed.add_field(name="Bedeutung", value=self.replace_max_chars(word.meaning_overview), inline=False)

        await ctx.send(embed=duden_embed, delete_after=30)

    def replace_max_chars(self, data):
        data = str(data).replace("[", "").replace("]", "").replace("'", "")

        if len(data) > 196:
            data = f"{data[:196]}[...]"
        return data



def setup(client):
    client.add_cog(Duden(client))