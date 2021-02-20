import discord
from discord.ext import commands
from googlesearch import search


client = discord.Client()

@client.event
async def on_ready():
    print("Bot is ready")


@client.event
async def on_message(message):
    if message.content.startswith('a/ google'):
        searchContent = ""
        text = str(message.content).split(' ')
        for i in range(2, len(text)):
            searchContent = searchContent + text[i]
        for j in search(searchContent, tld="co.in", num=1, stop=1, pause=4):
            await message.channel.send(j)

client.run("NzgwNzM0MDYwMjQ2MDczMzc0.X7zZQQ.XO0sNCFFH5sXCo7ZMnRP87L3hWM")