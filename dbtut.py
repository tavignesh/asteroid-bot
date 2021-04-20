import discord
import time
import asyncio
import random

client = discord.Client()
token = "ODMzOTE1ODA5Nzk3MzczOTcy.YH5Sng.hdOnulgCR0w9Ea2f1MKgyBqMKd8"


@client.event
async def on_ready():
    print("Bot is Ready Boss!!")


@client.event
async def on_message(message):
    global messages
    ig = 0
    if str(message.channel.id) == "806906773268332581"and not (str(message.author.id) == "818500359033978941" or str(message.author.id) == "833915809797373972"):
        mos = message.content
        await message.delete()
        rs = await message.channel.send(embed=discord.Embed(title=f"{message.author}'s Suggestion!", description=f"`{mos}`", color=0x01FD14))
        await rs.add_reaction("<:upvote:816324827908014139>")
        await rs.add_reaction("<:downvote:816324896262324276>")


client.run(token)