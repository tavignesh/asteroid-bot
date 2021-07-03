import discord
import discord.utils
import asyncio
import math
import random
import psutil
import json
import requests
import wikipedia
import time
from time import perf_counter
import uptime
import string
import pymongo
from pymongo import MongoClient
import bs4
import urllib
import urllib.request
import urllib3
import googlesearch
from googlesearch import search
from discord.ext import commands
import pplpcl
import csv
import platform
import gc
import os
import qrcode
from PIL import Image
import play_scraper
import google_play_scraper
import pprint
# import pyzbar.pyzbar
import io
  
version = "1.9.0"
botingscheme = "main" # beta or main

# strtuptime = int(uptime.uptime())

client = discord.Client()

cluster = MongoClient("mongodb+srv://bot:1234@cluster0.5bkqm.mongodb.net/discord?retryWrites=true&w=majority")
db = cluster["discord"]
collection = db["bot"]

#
acrackerfile = open("cracker.py", "rb")
toktokdic = pplpcl.load(acrackerfile)
toktok = toktokdic[botingscheme]

wthapikey = "b79ac8eaa95ac8f6d9248eeee1fd3f08"
srakey = "8H8tuaCZeMpJgVc5EaXtOR7sM"
# ag srvr id      = 708329597141385229
# id support srvr = 780625655657791518

messages = joined = 0
mtlist = []


# PRE DECLARE

# \n<a:ag_arrowgif:781395494127271947> Premium`but free` :gift_heart: (premium) \n<a:ag_arrowgif:781395494127271947> Music :notes: (music)
# \n<a:ag_arrw_hrt:781410692321640530> [Invite Asteroid Music](https://discord.com/oauth2/authorize?client_id=836830093644791809&scope=bot&permissions=37088576) :notes:

helpmbd = discord.Embed(title="Hey !! I am **Asteroid**!!\nMy Prefix is `a/`\n▬▬▬▬▬▬▬▬▬▬\n Make sure to leave a space between `a/` and command\n▬▬▬▬▬▬▬▬▬▬", description="Use `a/ <module id> help` for More Info!\nIn the Place of <module id> put the text in (Brackets) After each Module\n\n**Modules** :control_knobs: \n▬▬▬▬▬▬▬▬▬▬\n<a:ag_arrowgif:781395494127271947> Moderati\
on :tools: (mod)\n<a:ag_arrowgif:781395494127271947> Invite <a:ag_flyn_hrts_red:781395643134115852>\n\n<a:ag_arrowgif:781395494127271947> Calculation :1234: (calculate)\n<a:ag_arrowgif:781395494127271947> Converters :thermometer: (convert)\n<a:ag_arrowgif:781395494127271947> TAX <:ag_tax:807893601244676116> (tax)\n<a:ag_arrowgif:781395494127271947> Ticket System :tickets: (ticket)\n<a:ag_arrowgif:781395494127271947> Embed Creation :card_index: (embed)\n<a:ag_arrowgif:781395494127271947>\
 Say :love_letter: (say)\n<a:ag_arrowgif:781395494127271947> Random :game_die: (random)\n<a:ag_arrowgif:781395494127271947> Random Joke :joy: (joke)\n<a:ag_arrowgif:781395494127271947> Random Facts :scream: (fact)\n<a:ag_arrowgif:781395494127271947> Weather :white_sun_rain_cloud: (weather)\n<a:ag_arrowgif:781395494127271947> AI Chat :speech_balloon: (chat)\n<a:ag_arrowgif:781395494127271947> Poll :man_raising_hand: (poll)\n<a:ag_arrowgif:781395494127271947> Suggestion :pencil: (suggest)\n<a:ag_arrowgif:781395494127271947>\
  Google,Wiki, +more :satellite: <a:ag_book_pgs:781410721397080084> (web)\
\n<a:ag_arrowgif:781395494127271947> QR Utility (qr)\n<a:ag_arrowgif:781395494127271947> Image generation :frame_photo:(image)\n<a:ag_arrowgif:781395494127271947> AFK :zzz: (afk)\n<a:ag_arrowgif:781395494127271947> Quizz :interrobang: (quiz)\n<a:ag_arrowgif:781395494127271947> Statistics :level_slider: (stats)\n▬▬▬▬▬▬▬▬▬▬\n**Example:**\n`a/ chat help`", color=0x01FD14)
helpmbd.set_image(url="https://tavignesh.github.io/imhost/asteroid1.gif")

# EDIT TO FIELDS
invitembd = discord.Embed(title=" <a:ag_reddot:781410740619051008> **Usefull Links** <a:ag_reddot:781410740619051008> \n▬▬▬▬▬▬▬▬▬▬", description="<a:ag_arrw_hrt:781410692321640530> [Invite Me](https://discord.com/oauth2/authorize?client_id=780734060246073374&scope=applications.commands%20bot&permissions=809500159) <a:ag_tickop:781395575962599445>\n<a:ag_arrw_hrt:781410692321640530> [Vote Asteroid](https://top.gg/bot/780734060246073374/vote) :reminder_ribbon: \n<a:ag_arrw_hrt:781410692321640530> [Support Server](https://discord.gg/teszgSR9yK) <a:ag_discord:781395597277134869>\n<a:ag_arrw_hrt:781410692321640530> [Vote Support Server](https://top.gg/servers/780625655657791518/vote) :reminder_ribbon:", color=0x13FD03)
invitembd.set_image(url="https://tavignesh.github.io/imhost/asteroid1.gif")

tstmbd = discord.Embed(title="Your title\n___________", description="Your description\ndescreption2", color=000000)

badwrds =                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ["wtf", "fuck", "porn", "slut", "gangbang"]


global loggggg
rp = 0
loggggg = 0

global ncmnd
global prfx
global ld_prefix
ld_prefix = 1
ncmnd = 0



# nitro emoji nqn


def ncmnda():
    ncmnd = 1
    return ncmnd


def fetch_data(content):
    try:
        data = content.split(" ")
        rldata = ""
        if data[0] == "a/":
            if len(data) <= 2:
                return
            else:
                for i in range(2, len(data)):
                    rldata += f"{data[i]} "
            return rldata
        else:
            if len(data) <= 1:
                return
            else:
                for i in range(1, len(data)):
                    rldata += f"{data[i]} "
            return rldata
    except Exception as e:
        return "Error"

def randata(aisjd=5):
    aisjd = int(aisjd)
    astrl = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    dataid = ""
    for i in range(0,aisjd):
        aid = random.choice(astrl)
        dataid += aid
    return dataid

def reload_prefix():
    try:
        with open("prefixes.dat", "rb") as pxfile:
            prfx = pplpcl.load(pxfile)
        ld_prefix = 0
        return prfx
    except Exception as e:
        raise Exception (f"Failed to read prefixes.dat as : {e}")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Important, New Asteroid! Do a/help and see Very important"))


async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, Member Joined: {joined}\n")

            await asyncio.sleep(10)
        except Exception as e:
            print(e)
            await asyncio.sleep(10)

# @client.event
# async def on_member_join(member):
#     global joined
#     joined += 1
#     await client.send_messsage(f"""hi bro wlcome to my support server {member.mention}""")

@client.event
async def on_message(message):
    global messages, loggggg

    messages += 1
    ans = "none"
# serverid = client.get_guild(780625655657791518)
    a = 0
    rp = 0

# CRIETERIA FILTER
    if message.author == client.user:
        ncmnda()
        return
    if message.author.bot:
        ncmnda()
        return
# LOGS
    if message.content == ("logs enable") and str(message.author.id) == "641305773095387156":
        loggggg = 1

    if message.content == ("logs disable") and str(message.author.id) == "641305773095387156":
        loggggg = 0

    if loggggg == 1:
        print("The Message | ", message.content, " | Was sent in | ", message.channel, " | Channel by | ", message.author, "| in SERVER =>", message.guild)

# HELPS
    if message.content.startswith("A/"):
        ncmnda()
        await message.channel.send(embed=discord.Embed(description="Due to a Problem THIS bot has been Depriciated and will not work/n Invite The New Asteroid \nInvite Link: [ https://discord.com/oauth2/authorize?client_id=780734060246073374&scope=bot&permissions=809500159 ]", color=0x04FD03))
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
    if message.content == ("a/") or message.content == ("a/ "):
        ncmnda()
        await message.channel.send(embed=discord.Embed(description="Due to a Problem THIS bot has been Depriciated and will not work/n Invite The New Asteroid \nInvite Link: [ https://discord.com/oauth2/authorize?client_id=780734060246073374&scope=bot&permissions=809500159 ]"))
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
    if message.content == "<@!780734060246073374>":
        ncmnda()
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(description="My prefix is `a/`", color=0x04FD03))
    if message.content == "a/ help" or message.content == "a/help" or message.content == "A/help" or message.content == "A/ help" or message.content == "A/ info" or message.content == "a/info" or message.content == "a/ info":
        ncmnda()
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send("Due to a Problem THIS bot has been Depriciated and will not work/n Invite The New Asteroid \nInvite Link: [ https://discord.com/oauth2/authorize?client_id=780734060246073374&scope=bot&permissions=809500159 ]")
    if message.content.find("a/ invite") != -1 or message.content == "a/invite" or message.content == 'a/vote' or message.content == 'a/ vote' or message.content == "a/ support" or message.content == "a/support":
        ncmnda()
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=invitembd)
client.run("NzgwNDcyMDcwMDcyNjk2ODUy.X7vlQQ.g4uA0qtEOBw4xTFxsOweh2pySW0")
