import discord
import time
import asyncio
import random

client = discord.Client()
token = "ODE4NTAwMzU5MDMzOTc4OTQx.YEY93A.oKtI5Rbk_dG7rdskKAzx_HuWfgE"


@client.event
async def on_ready():
    print("Ready Boss!!")


@client.event
async def on_message(message):
    global messages
    ig = 0
    if (message.content.startswith("=create") or message.content.startswith("=new") or message.content.startswith(
            "=ticket")) and str(message.channel.id) == "818499321611026492":
        if message.content == ("=create") or message.content == ("=new") or message.content == ("=ticket"):
            await message.channel.send(
                embed=discord.Embed(title="Syntax Error", description="Enter a Reason to create a ticket!!"))
        else:
            n = message.content.split(" ")
            msg = ""
            for i in range(2, len(n)):
                msg += n[i]
            doms = message.author
            overwrites = {
                message.guild.default_role: discord.PermissionOverwrite(read_messages=False),
                message.author: discord.PermissionOverwrite(read_messages=True),
                doms.author: discord.PermissionOverwrite(send_messages=True)
            }
            astrl = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            aid = random.choice(astrl)
            bid = random.choice(astrl)
            cid = random.choice(astrl)
            did = random.choice(astrl)
            eid = random.choice(astrl)
            dataid = f"{aid}{bid}{cid}{did}{eid}"
            await message.guild.create_text_channel(f'Ticket-{dataid}', overwrites=overwrites)
            await message.channel.send(embed=discord.Embed(title="Ticket Created !!"))

    if str(message.channel.id) == "806906773268332581"and not str(message.author.id) == "818500359033978941":
        mos = message.content
        await message.delete()
        rs = await message.channel.send(embed=discord.Embed(title=f"{message.author}'s Suggestion!", description=f"`{mos}`", color=0x01FD14))
        await rs.add_reaction("<:upvote:816324827908014139>")
        await rs.add_reaction("<:downvote:816324896262324276>")


client.run(token)