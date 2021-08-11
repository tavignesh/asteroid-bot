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
from discordTogether import DiscordTogether
from server import keep_alive
from discord_components import DiscordComponents, Button, Select, SelectOption

  
version = "1.9.2"
botingscheme = "main" # beta or main

# strtuptime = int(uptime.uptime())

client = discord.Client()
togetherControl = DiscordTogether(client)

cluster = MongoClient("mongodb+srv://bot:1234@cluster0.5bkqm.mongodb.net/discord?retryWrites=true&w=majority")
db = cluster["discord"]
collection = db["bot"]

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

helpmbd = discord.Embed(title="Hey !! I am **Asteroid**!!\nMy Prefix is `a/`\n▬▬▬▬▬▬▬▬▬▬", description="Use `a/ <module id> help` for More Info!\nIn the Place of <module id> put the text in (Brackets) After each Module\n\n**Modules** :control_knobs: \n▬▬▬▬▬▬▬▬▬▬\n<a:ag_arrowgif:781395494127271947> Moderati\
on :tools: (mod)\n<a:ag_arrowgif:781395494127271947> Invite <a:ag_flyn_hrts_red:781395643134115852>\n<a:ag_arrowgif:781395494127271947> Party Games (game) <:ag_poker:854976463962636339>\n<a:ag_arrowgif:781395494127271947> Calculation :1234: (calculate)\n<a:ag_arrowgif:781395494127271947> Converters :thermometer: (convert)\n<a:ag_arrowgif:781395494127271947> TAX <:ag_tax:807893601244676116> (tax)\n<a:ag_arrowgif:781395494127271947> Ticket System :tickets: (ticket)\n<a:ag_arrowgif:781395494127271947> Embed Creation :card_index: (embed)\n<a:ag_arrowgif:781395494127271947>\
 Say :love_letter: (say)\n<a:ag_arrowgif:781395494127271947> Random :game_die: (random)\n<a:ag_arrowgif:781395494127271947> Random Joke :joy: (joke)\n<a:ag_arrowgif:781395494127271947> Random Facts :scream: (fact)\n<a:ag_arrowgif:781395494127271947> Weather :white_sun_rain_cloud: (weather)\n<a:ag_arrowgif:781395494127271947> AI Chat :speech_balloon: (chat)\n<a:ag_arrowgif:781395494127271947> Poll :man_raising_hand: (poll)\n<a:ag_arrowgif:781395494127271947> Suggestion :pencil: (suggest)\n<a:ag_arrowgif:781395494127271947>\
  Google,Wiki, +more :satellite: <a:ag_book_pgs:781410721397080084> (web)\
\n<a:ag_arrowgif:781395494127271947> QR Utility (qr)\n<a:ag_arrowgif:781395494127271947> Image generation :frame_photo:(image)\n<a:ag_arrowgif:781395494127271947> AFK :zzz: (afk)\n<a:ag_arrowgif:781395494127271947> Quizz :interrobang: (quiz)\n<a:ag_arrowgif:781395494127271947> Statistics :level_slider: (stats)\n▬▬▬▬▬▬▬▬▬▬\n**Example:**\n`a/ game help`", color=0x01FD14)
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


newpath = './imgcache'
if not os.path.exists(newpath):
    os.makedirs(newpath)

#make chat channel file from db

dbdic = collection.find_one({"_id": 4322})
dblist = dbdic["ids"]
chnlfile = open("chatchannellist.dat", "wb")
try:
    pplpcl.dump(dblist, chnlfile)
except Exception as e:
    print(f"Chat wont work :( Error: {e}")
chnlfile.close() 
print("done")
  
  
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
    DiscordComponents(client)
    if botingscheme != "main":
        game = discord.Game("with v1.9.0 and Having Fun Testing New Features")
        # await client.change_presence(status=discord.Status.idle, activity=game)
        # await client.change_presence(status=discord.Status.online, activity=game)
        # await client.change_presence(status=discord.Status.invisible, activity=game)
        await client.change_presence(status=discord.Status.do_not_disturb, activity=game)
    else:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a/ help in v1.9.0 with AI Chat !! Invite Me a/ invite"))
        # await client.change_presence(status=discord.Status.online, activity=game)
        # await client.change_presence(status=discord.Status.invisible, activity=game)
        # await client.change_presence(status=discord.Status.do_not_disturb, activity=game)
    print("{} is ONLINE!!".format(client.user))

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
        await message.channel.send(embed=discord.Embed(description="My prefix is `a/`", color=0x04FD03))
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
    if message.content == ("a/") or message.content == ("a/ "):
        ncmnda()
        await message.channel.send(embed=discord.Embed(title="Yes? , How May i Help You?",description=("Use `a/ help` for More!\n Make sure there is a space between `a/` and `help`"), color=0x04FD03))
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
    if message.content == "<@!780734060246073374>":
        ncmnda()
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(description="My prefix is `a/`", color=0x04FD03))
    if message.content == "a/ help" or message.content == "a/help" or message.content == "A/help" or message.content == "A/ help" or message.content == "A/ info" or message.content == "a/info" or message.content == "a/ info":
        ncmnda()
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=helpmbd, components = [Button(label = "Website", disabled=False, style=5, url="https://asteroidbot.xyz"),Button(label = "INVITE", disabled=False, style=5, url="https://discord.com/oauth2/authorize?client_id=780734060246073374&scope=applications.commands%20bot&permissions=809500159")])
    if message.content.find("a/ invite") != -1 or message.content == "a/invite" or message.content == 'a/vote' or message.content == 'a/ vote' or message.content == "a/ support" or message.content == "a/support":
        ncmnda()
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=invitembd, components = [Button(label = "Website", disabled=False, style=5, url="https://asteroidbot.xyz"),Button(label = "INVITE", disabled=False, style=5, url="https://discord.com/oauth2/authorize?client_id=780734060246073374&scope=applications.commands%20bot&permissions=809500159")])
    if message.content == "a/ delete" or message.content == "a/delete":
        ncmnda()
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(description="Use `a/ delete help` for Help Regarding Delete messges"))
    if message.content.startswith("a/ mod ") or message.content.startswith("a/mod"):
        ncmnda()
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title=":tools: Moderation <a:ag_book_pgs:769053582472642561>\n▬▬▬▬▬▬▬▬▬▬", description="All moderation Commands Needs You and Me to have Specific **Permissions** to perform Moderation!\n\n**Commands:**\n<a:ag_arrowgif:781395494127271947> <:ag_ban:774867115529469992> - `a/ ban <mention user> for <reason optional>`\n<a:ag_arrowgif:781395494127271947> Kick - `a/ kick <mention user> for <reason optional>`\n<a:ag_arrowgif:781395494127271947> Warn - `a/ warn <mention user> =<reason optional>`\n<a:ag_arrowgif:781395494127271947> Ticketing System - Use `a/ ticket help` for more info \n<a:ag_arrowgif:781395494127271947> DEcancer Names :microbe: - Use `a/ decan @mention` to change their nickname!\n<a:ag_arrowgif:781395494127271947> Delete - Use `a/ delete help` For more!\n<a:ag_arrowgif:781395494127271947> Pls Use `a/ pref help` for Chat and BadWord (Customisable) Moderation\n<a:ag_arrowgif:781395494127271947> Member Count - `a/ members`", color=0xFDDE01))
    if message.content == "a/ delete help" or message.content == "a/ help delete" or message.content == "a/delete help" or message.content == "a/help delete":
        ncmnda()
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="**Delete Messages** :x:\n▬▬▬▬▬▬▬▬▬▬", description="Maximum of 500 Messages can be Deleted at a Time <a:ag_reddot:781410740619051008>\nYou need to Have Manage Messages Permisiion \n\nSyntax : `a/ delete <Number of msges in number>`\n\nExample:\n`a/ delete 15`", color=0x04FD03))
    if message.content == "a/ suggest help" or message.content == "a/ help suggest" or message.content == "a/suggest help" or message.content == "a/help suggest":
        ncmnda()
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="**Suggesions on Me** <a:ag_discord:781395597277134869> \n▬▬▬▬▬▬▬▬▬▬", description="Your Suggesions are Really Valuable to us(me) , It helps in Improving The Bot! <a:ag_reddot:781410740619051008> \n▬▬▬▬▬▬▬▬▬▬\n\nSyntax : `a/ suggest <your suggesion>`\n\nExample:\n`a/ suggest plz include multiplayer`",color=0x04FD03))
    if message.content == "a/ calculate help" or message.content == "a/ help calculate" or message.content == "a/ calculate" or message.content == "a/ calculator" or message.content == "a/calculate help" or message.content == "a/help calculate" or message.content == "a/calculate" or message.content == "a/calculator":
        ncmnda()
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="**Basic Calculator** :1234:\n▬▬▬▬▬▬▬▬▬▬", description="**Mathematical Operators**\n▬▬▬▬▬▬▬▬▬▬\n`add` => Addition\n `sub` => Subtraction\n `mult` => Multiplication \n `div` => Division\n\nSyntax: `a/ <mathamatical operator>  <1st number>  <2nd number>`\nExample : `a/ add 13 2`\n\n**LCM and HCF**\n▬▬▬▬▬▬▬▬▬▬\n`lcm` => Least Common Multiple\n `hcf` => Highest Common Factor\n\n**Complex Calculations**\n▬▬▬▬▬▬▬▬▬▬\n For More Use `a/ ccalculator help`", color=0x05FCF1))
    if message.content == "a/ ccal help" or message.content == "a/ help ccal" or message.content == "a/ccal help" or message.content == "a/help ccal":
        ncmnda()
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="**Complex Calculation**:1234:\n▬▬▬▬▬▬▬▬▬▬", description="I can do a lot of **Complex Calculations**!\nThere are 2 types of Complex Calculations\n\n <a:ag_arrowgif:781395494127271947> Single input Calculation\nUse `a/ ccalculate 1 help`\n\n <a:ag_arrowgif:781395494127271947> Double Input Calculation\n Use `a/ ccalculate 2 help`", color=0xD705FC))
    if message.content == "a/ ccal 1 help" or message.content == "a/ccal 1 help":
        ncmnda()
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="**Complex Calculator #1** :1234:\n▬▬▬▬▬▬▬▬▬▬", description="Single Input Functions\n All single Input variable = `a`\n▬▬▬▬▬▬▬▬▬▬\n`ceil` => Gives the Nearest Integer Greater than `a`\nExample: `a/ ceil 2.4` Gives `3`\n\n`pi` => Gives the Value of `Pi`\n`e` => Gives the Value of `e`\n\n\n`floor` => Gives the Nearest Integer\
         Lessser than `a`\nExample : `a/ floor 3.9` Gives `3`\n\n `sqrt` => Gives the Square Root of `a`\nExample : `a/ sqrt 9` Gives `3`\n\n `facto` => Gives the Factorial of `a`\nExample : `a/ facto 5` Gives `120`\n\n`exp` Gives the Value of `e^a`\nExample : `a/ exp 4` Gives `54.598150033144236`\n\n`log` => Gives the Natural Log of `a`\nExample : `a/ log 2` Gives `0.6931471805599453`\n\n`log10` => Gives the Log to the Base 10 of `a`\nExample : `a/ log10 2` Gives\
         `0.3010299956639812`\n\n`sin, cos, tan` => Gives the Trigonometric (sin or cos or tan as Specified) Values\nExample : `a/ sin 30` Gives `0.5`\n\nCommon\
         Syntax: `a/ <operator> <value(a)>`\n\n▬▬▬▬▬▬▬▬▬▬\n**More Calculations in `a/ complex 2 help`**\n\n If your Preffered Calculation is not available then plz Suggest using `a/ suggest help`", color=0xD705FC))
    if message.content == "a/ convert help" or message.content == "a/ help convert" or  message.content == "a/convert help" or message.content == "a/help convert":
        ncmnda()
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="**Converter** :scales:\n▬▬▬▬▬▬▬▬▬▬", description="**__Temperature__**\n__Radians to Degrees__\nConverts `a` in Radians to Degrees\n Example : `a/ degrees 5` Gives `286.4788975654116`\n\n__Degrees to Radians__\nConverts `a` in Degrees to Radians\nExample : `a/ radians 90` Gives `1.5707963267948966`\n\n__Farenheit to Celcius__\nConverts Tempereture `a`\
        in Farenheit to Celcius\nExample : `a/ far 32` Gives `0`\n\n**Celcius to Farenheit**\nConverts Tempereture `a` in Celcius to Farenheit\nExample : `a/ cel 0` Gives `32`\n\n__Celcius to Kelvin__\nConverts Tempereture `a` in Celcius to Kelvin\nExample : `a/ cel 0` Gives `273`\n\n__Farenheit to Kelvin__\nConverts Tempereture `a` in Celcius to Farenheit\nExample : `a/ cel 0` Gives `32`\n\n**__CURRENCY__**\nConverts or returns value of any curency from any to any currency.\n Available Currency:\n \
        AED AFN ALL AMD ANG AOA ARS AUD AWG AZN BAM BBD BDT BGN BHD BIF BMD BND BOB BRL BSD BTC BTN BWP CRC CUC CUP CVE CZK DJF DKK DOP DZD EEK EGP ERN ETB EUR FJD FKP GBP GEL GGP GHS GIP GMD GNF GTQ GYD HKD HNL HRK HTG HUF IDR ILS IMP INR IQD IRR ISK JEP JMD JOD JPY KES KGS KHR KMF KPW KRW KWD KYD KZT LAK LBP LKR LRD LSL LTL LVL LYD MAD MDL MGA MKD MMK MNT MOP MRO MUR MVR MWK MXN MYR MZN NAD NGN NIO NOK NPR NZD OMR PAB PEN PGK PHP PKR PLN PYG QAR RON RSD RUB RWF SAR SBD SCR SDG SEK SGD SHP SLL SOS SRD STD SVC SYP SZL THB TJS TMT TND TOP TRY TTD TWD TZS UAH UGX USD UYU UZS VEF VND VUV WST XAF XAG XAU XCD XDR XOF XPF YER ZAR ZMK ZMW ZWL BYN BYR BZD CAD CDF CHF CLF CLP CNY COP\n Syntax: `a/ USD`", color=0xD705FC))
    if message.content == "a/ ccal 2 help" or message.content == "a/ccal 2 help":
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="**Complex Calculator #2** :1234:\n▬▬▬▬▬▬▬▬▬▬", description="Single Input Functions\n All Double Input variable = `a` and `b`\n▬▬▬▬▬▬▬▬▬▬\n`bilog` => Gives the Value of Log `a` to the Base `b`\nExample: `a/ bilog 100 2` Gives `6.643856189774725`\n\n`pow` => Gives the Value of `a` to the Power `b`\nExample: `a/ pow 5 2` Gives `25`\n\n▬▬▬▬▬▬▬▬▬▬\n**TAX**\n`tax` => Gives tax amount and Amount after tax, `a` is tax% and `b` is amount\nExample: `a/ tax 12 1000`\n\n`danktax` => Gives tax that DankMemer(bot) put on transferres\nExample: `a/ danktax 150000`", color=0xD705FC))
    if message.content == "a/ afk help" or message.content == "a/ help afk" or message.content == "a/ afk" or message.content == "a/afk help":
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="AFK Status :zzz:\n▬▬▬▬▬▬▬▬▬▬", description="If you set afk status all the Messages that Ping you will be responded with a msg you gave!\n\n**Syntax:**\n<a:ag_arrowgif:781395494127271947> Set AFK - `a/ afk =<reason>`\n<a:ag_arrowgif:781395494127271947> Remove AFK - `a/ afk remove`", color=0xA205FC))
    if message.content == "a/ say help" or message.content == "a/ help say" or message.content == "a/ say":
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="SAY :speech_balloon: \n▬▬▬▬▬▬▬▬▬▬", description="This Command Makes Me to Say or Delete and Say What you say!!\n\n**Syntax:**\n`a/ say = <text>` or `a/ delsay = <text>`\n\n**Example:**\n`a/ say =text this you bot!`", color=0x4805FC))
    if message.content == "a/ random help" or message.content == "a/ help random":
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="Random :game_die: \n▬▬▬▬▬▬▬▬▬▬", description="This Chooses a number from 1 to `a` randomly.\n\n**Syntax:** \n`a/ random <Number>`\n\n**Example:**\n`a/ random 3`", color=0xFC058C))
    if message.content == 'a/ stats help' or message.content == "a/ help stats" or message.content == 'a/stats help' or message.content == "a/help stats":
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="My Statistics :level_slider:\n▬▬▬▬▬▬▬▬▬", description="**Syntax**\n`a/ <id>` The `id` is in (brackets)\n\n**Commands**\n<a:ag_arrowgif:781395494127271947> Version Updates (updates)\n<a:ag_arrowgif:781395494127271947> CPU Usage (cpu)\n<a:ag_arrowgif:781395494127271947> Server Count (server)\n<a:ag_arrowgif:781395494127271947> My Ping or Latency (ping)\n<a:ag_arrowgif:781395494127271947> Server ID (serverid)\n\n**Example:**\n`a/ cpu`", color=0x04FD03))
    if message.content == "a/ setup chat" or message.content == "a/setup chat":
        if message.author.guild_permissions.administrator:
            ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
            try:
                chtcnnl = await message.guild.create_text_channel('asteroid-chat')
                dbdic = collection.find_one({"_id": 4322})
                dblist = dbdic["ids"]
                dblist.append(chtcnnl.id)
                collection.update_one({"_id": 4322}, {"$set": {"ids": dblist}})
                chnlfile = open("chatchannellist.dat", "wb")
                try:
                    pplpcl.dump(dblist, chnlfile)
                except Exception as e:
                    print(e)
                chnlfile.close()
                await message.channel.send(embed=discord.Embed(title="Chat Channel Created", description="You can Chat with Me in that channel without my Prefix!", color=0x01FD14))
                await message.channel.send(embed=discord.Embed(title="<a:ag_exc:781410611366985748> Note: ", description="You **CAN** freely rename, move or edit permissions of this channel!", color=0x01FD14))
            except Exception as e:
                print(e)
                await message.channel.send(embed=discord.Embed(title="An error Occured", description="If this occures again and again Please Report the below info to "))
            await message.channel.send(embed=discord.Embed(title="Chat Channel Created", description="You can Chat with Me in that channel without my Prefix!", color=0x01FD14))
            await message.channel.send(embed=discord.Embed(title="<a:ag_exc:781410611366985748> Note: ", description="You can freely change, move or edit permissions of this channel!", color=0x01FD14))
        else:
            await message.channel.send(embed=discord.Embed(title="You Don't have Permission to Manage Channels <a:ag_exc:781410611366985748>"))
    if message.content.startswith("a/ owner") or message.content.startswith("a/owner"):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="**Vignesh_x64ᴰᵉᵛ#8351** <a:ag_flyn_hrts_cyn:781395468978356235>\nCreated me on 23th Nov 2020",color=0x04FD03))
    if message.content.find("a/ chat help") != -1 or message.content == "a/ help chat" or message.content.find("a/chat help") != -1 or message.content == "a/help chat" or message.content.find("a/ AI help") != -1 or message.content == "a/ ai chat" or message.content.find("a/AI help") != -1 or message.content == "a/ai chat":
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="CHAT :speech_balloon:\n▬▬▬▬▬▬▬▬▬▬", description="<a:ag_arrowgif:781395494127271947> `a/ setup chat` will Create a New Channel to Chat mith Meee!\n<a:ag_arrowgif:781395494127271947> <More To be added here>", color=0xFC058C))
    if message.content.find("a/ today help") != -1 or message.content == "a/ help today" or message.content.find("a/today help") != -1 or message.content.find("a/today help") != -1 or message.content == "a/help today" or message.content.find("a/ today help") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="Today :date:\n▬▬▬▬▬▬▬▬▬▬", description="**Commands:**\n<a:ag_arrowgif:781395494127271947> `a/ time` :clock3: Shows the Time Now\n<a:ag_arrowgif:781395494127271947> `a/ date` :date: Shows the Date Today\n<a:ag_arrowgif:781395494127271947> <More to be added here>", color=0x6E05FC))
    if message.content == "a/ wiki help" or message.content == "a/ help wiki" or message.content == "a/ wiki" or message.content == "a/wiki help" or message.content == "a/wiki help" or message.content == "a/help wiki" or message.content == "a/wiki" or message.content == "a/ wiki help":
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="Wikipedia Search :mag:\n▬▬▬▬▬▬▬▬▬▬", description="This commands Fetches Descreption about the Keyword you give.\n**Syntax:**\n`a/ wiki =keyword`\n\n**Example:**\n`a/ wiki =bot making`", color=0x05B5FC))
    if message.content == "a/ help weather" or message.content == "a/ weather help" or message.content == "a/help weather" or message.content == "a/ weather" or message.content == "a/help weather" or message.content == "a/weather help" or message.content == "a/ help weather" or message.content == "a/weather":
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="Weather Reports\n▬▬▬▬▬▬▬▬▬▬", description="This Feature allows You to Get a weather Report Of your Preffered Location\n\n**Syntax:**\n`a/ weather =<location>`\n\n**Example:**\n`a/ weather =Chennai`", color=0x0527FC))
    if message.content == "a/ quiz help" or message.content == "a/quiz help" or message.content == "a/ help quiz" or message.content == "a/help quiz":
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title=":speech_balloon: QUIZ <a:ag_book_pgs:769053582472642561>\n▬▬▬▬▬▬▬▬▬▬", description="Type `a/ quiz start <level> <topic id>`\n**For Topic ID Type** `a/ list topic` (Default - General Knowledge) \nLevels :\nEasy: 1\nMedium: 2\nHard: 3\nExample: `a/ quiz start 2 10`\nTo start a quiz and after answering react with a :thumbsup: for next question\nMark Counting Feature Under Development Sorry..", color=0xFDDE01))
    if message.content == "a/ list topic" or message.content == "a/ topic list" or message.content == "a/list topic" or message.content == "a/ list topic" or message.content == "a/topic list" or message.content == "a/ list topic":
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="**Topic List**", description="ID |       TOPIC\n1  <a:ag_arrw_hrt:781410692321640530> General Knowledge\n2  <a:ag_arrw_hrt:781410692321640530> Entertainment: Books\n3  <a:ag_arrw_hrt:781410692321640530> Entertainment: Film\n4  <a:ag_arrw_hrt:781410692321640530> Entertainment: Music\n5  <a:ag_arrw_hrt:781410692321640530> Entertainment: Musicals &\
         Theatres\n6  <a:ag_arrw_hrt:781410692321640530> Entertainment: Television\n7  <a:ag_arrw_hrt:781410692321640530> Entertainment: Video Games\n8  <a:ag_arrw_hrt:781410692321640530> Entertainment: Board Games\n9  <a:ag_arrw_hrt:781410692321640530> Science & Nature\n10 <a:ag_arrw_hrt:781410692321640530> Science: Computers\n11 <a:ag_arrw_hrt:781410692321640530> Science: Mathematics\n12\
          <a:ag_arrw_hrt:781410692321640530> Mythology\n13 <a:ag_arrw_hrt:781410692321640530> Sports\n14 <a:ag_arrw_hrt:781410692321640530> Geography\n15 <a:ag_arrw_hrt:781410692321640530> History\n16 <a:ag_arrw_hrt:781410692321640530> Politics\n17 <a:ag_arrw_hrt:781410692321640530> Art\n18 <a:ag_arrw_hrt:781410692321640530> Celebrities\n19 <a:ag_arrwhrt:781410692321640530> Animals\n20\
           <a:ag_arrw_hrt:781410692321640530> Vehicles\n21 <a:ag_arrw_hrt:781410692321640530> Entertainment: Comics\n22 <a:ag_arrw_hrt:781410692321640530> Science: Gadgets\n23 <a:ag_arrw_hrt:781410692321640530> Entertainment: Japanese Anime & Manga\n24 <a:ag_arrw_hrt:781410692321640530> Entertainment: Cartoon & Animations\n", color=0xFDDE01))
    if message.content == "a/ help set" or message.content == "a/ set help" or message.content == "a/ pref help" or message.content == "a/ help pref" or message.content == "a/help set" or message.content == "a/set help" or message.content == "a/pref help" or message.content == "a/help pref" :
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="Chat Moderation Preferences\n▬▬▬▬▬▬▬▬▬▬", description="<a:ag_arrowgif:781395494127271947> Chat Moderation Enable or Disable `a/ set chatmod true(or)false`\n<a:ag_arrowgif:781395494127271947> Deletion of Blacklisted Words `a/ set delmod true(or)false`\n<a:ag_arrowgif:781395494127271947> Add badwords to Blacklisted words `a/ badword=<word here>` Example : `a/ badword=die`\n<a:ag_arrowgif:781395494127271947> \
        Remove Blacklisted word `a/ remove badword=<word>`\n<a:ag_arrowgif:781395494127271947> Add some Default Badwords `a/ badword defaults`\n<a:ag_arrowgif:781395494127271947> Clear All badwords `a/ badwords clear`", color=0xBCFC09))
    if message.content == 'a/ tax' or message.content == 'a/ tax help' or message.content == 'a/ help tax' or message.content == 'a/tax' or message.content == 'a/tax help' or message.content == 'a/help tax':
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="TAX\n▬▬▬▬▬▬▬▬▬▬", description="**TAX**\n`tax` => Gives tax amount and Amount after tax.\nSyntax : `a/ tax <tax rate> <amt>`\nExample: `a/ tax 12 1000` or `a/ t 12 1000`", color=0xD705FC))
    if message.content == 'a/ poll' or message.content == 'a/ poll help' or message.content == 'a/ help poll' or message.content == 'a/poll' or message.content == 'a/poll help' or message.content == 'a/help poll':
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="POLL\n▬▬▬▬▬▬▬▬▬▬", description="This command is usefull For conducting Yes or No Questions or Voting\nTwo types of polls:\n1. :thumbsup: , :thumbsdown: (`a/ poll1 =<qn>` or just `a/ poll =<qn>`)\n2. <:ag_upvote:816330395506180107>, <:ag_downvote:816330463937167391> (`a/ poll2 =<qn>`)\nSyntax : `a/ poll1 =<question>`\nExample: `a/ poll1 =How is This Bot?`\nLot of features like custom emoji reaction custom color to be added soon!", color=0xBCFC09))
    if message.content == 'a/ google' or message.content == 'a/ google help' or message.content == 'a/ help google' or message.content == 'a/google' or message.content == 'a/google help' or message.content == 'a/help google':
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="Google Search <a:ag_ggl:781410701327335445>\n▬▬▬▬▬▬▬▬▬▬", description="You can search for almost anything in google with me!!\nSyntax:`a/ google <search terms>`\nExample:`a/ google asteroid bot`", color=0xBCFC09))
    if message.content == 'a/ dictionary' or message.content == 'a/ def help' or message.content == 'a/ dic help' or message.content == 'a/ help def' or message.content == 'a/ help dic' or message.content == 'a/dictionary' or message.content == 'a/def help' or message.content == 'a/dic help' or message.content == 'a/help def' or message.content == 'a/help dic':
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="Dictionary 📔\n▬▬▬▬▬▬▬▬▬▬", description="You can search for definition with examples in this dictionary with me!!\nSyntax:`a/ dic =<search terms>` or `a/ def =<search term>`\nExample:`a/ def =asteroid`", color=0xBCFC09))
    if message.content == 'a/ ticket help' or message.content == 'a/ help ticket' or message.content == 'a/ ticket' or message.content == 'a/ticket help' or message.content == 'a/help ticket' or message.content == 'a/ticket':
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="Ticket System <a:ag_ggl:781410701327335445>\n▬▬▬▬▬▬▬▬▬▬", description="You can Create ticket to contact staff and discuss personally!!\nTo create a ticket use `a/ new ticket =reason`\nTo enable Ticketing system feature use `a/ ticket enable`\nTo disable Ticketing system use `a/ ticket disable`\nTo Close a single ticket use `a/ close`\nTo close all tickets use `a/ close all`", color=0xBCFC09))
    if message.content == 'a/ embed help' or message.content == 'a/ help embed' or message.content == 'a/ embed' or message.content == 'a/embed help' or message.content == 'a/help embed' or message.content == 'a/embed':
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        adasss = r"\n"
        await message.channel.send(embed=discord.Embed(title="Embed Creation :card_index:\n▬▬▬▬▬▬▬▬▬▬", description=f"Embed is very usefull message type for creating beautifully arranged and ordered formal messages. But sadly Normal users cannot create or send embed messages. Don't worry! Asteroid is here with a new very user friendly Embed Creator!\nTo create an embed Just type `a/ embed create` and follow the instructions!\n\n**IMPORTANT INFO**\nYou can add external, default and animated emojis BUT the limitation is you can ONLY use emojis from servers I am a Member of (ie. our mutual servers, which can be viewed in my profile).\nTo jump to next line use {adasss} in the correct place where you want to jump.\nYou can ping or tag someone in the message description but NOT in the title\n The above given limitation are not limited wantedly made but are the limitations of Discord Embeds\n\n**Syntax**: `a/ embed create`", color=0xBCFC09))
    if message.content == 'a/ fact help' or message.content == 'a/ help fact' or message.content == 'a/fact help' or message.content == 'a/help fact':
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="Random Facts :scream:\n▬▬▬▬▬▬▬▬▬▬", description="This shows you an interesting random fact chosen from a huge list of facts. Every care has been taken to provide good and quality facts but if some error or inapropriate or unwanted or nsfw content had crept in, just remember the fact id and send a suggsetion(`a/ suggest help`) or send a message in our [Support Server](https://discord.gg/teszgSR9yK). Sorry for the inconvinience.\n\n**Syntax**: `a/ fact`", color=0xBCFC09))
    if message.content == 'a/ website' or message.content == 'a/website':
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="Make sure to check out our website!!", description="__Website:__ https://asteroidbot.xyz \n__Email:__ support@asteroidbot.xyz", color=0xBCFC09))
    if message.content == 'a/ imgen' or message.content == 'a/imgen' or message.content == 'a/ imgen help' or message.content == 'a/imgen help' or message.content == 'a/ help imgen' or message.content == 'a/help imgen':
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="Image Generation :frame_photo:", description=f"Generates Modifyed images based on your Avatar!\nTypes:\nGlass, Pixel, Red, Blue, Green, YTComment, rainbow, wasted, triggered, bw, invert, bright, sepia, threshold... more will be added\nSyntax: `a/ <variety> @mention`\nExample: a/ red {message.author.mention} \nLooking for QR Code generator And Reader? Try `a/ qr help`", color=0xBCFC09))
    if message.content == 'a/ qr' or message.content == 'a/qr' or message.content == 'a/ qr help' or message.content == 'a/qr help' or message.content == 'a/ help qr' or message.content == 'a/help qr':
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="QR Code Generator & Reader", description="__Generation:__\nGenerates a QR Code based on give data or link.\nSyntax: `a/ qr <data or link>`\nExample: `a/ qr https://asteroidbot.xyz` \n\n__QR Code Reader:__\nReads the qr code from the given image! It need NOT be an image Generated by me it can even be a photo!\n Syantax: `a/ qrread <direct image link>` or `a/ qrread`+attachment", color=0xBCFC09))
    if message.content == 'a/ web' or message.content == 'a/web' or message.content == 'a/ web help' or message.content == 'a/web help' or message.content == 'a/ help web' or message.content == 'a/help web':
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="WEB Searches!!", description="This command searches the web using a range of web places listed below:\n<a:ag_multiarr:853185161839771648> YouTube <a:ag_yt:781395515526348801> - `a/ yt <search word>`\n<a:ag_multiarr:853185161839771648> Google <:ag_gglsym:817776047315091459> - `a/ google <search word>` \n<a:ag_multiarr:853185161839771648> Reddit <:ag_reddit:853191906770419724> - `a/ reddit <subreddit>`\n<a:ag_multiarr:853185161839771648> GitHub <:ag_github:853186834339332106> - `a/ GitHub <account name>` \n<a:ag_multiarr:853185161839771648> Playstore <:ag_playstore:853187910077775883> - `a/ PlayStore <app name>`\n<a:ag_multiarr:853185161839771648> Disctionary <a:ag_book_pgs:781410721397080084> - `a/ def <word>`\n<a:ag_multiarr:853185161839771648> Image Search :frame_photo: - `a/ image <search term>`\n<a:ag_multiarr:853185161839771648> Song Lyrics :notes: - `a/ lyrics <song>`\n<a:ag_multiarr:853185161839771648> Weather :white_sun_rain_cloud: - `a/ weather <location>`", color=0xBCFC09))



    # if message.content.startswith('a/ music') or message.content == 'a/ help music' or message.content == 'a/ music help':
    #     await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
    #     await message.channel.send(embed=discord.Embed(title="Music :notes:\n▬▬▬▬▬▬▬▬▬▬", description="This feature allows you to listen to music by streaming music to a voice channel. To activate all commands join a voice channel and use `a/ play songname`. This also includes a lot of filters which can be applied to the song!!. Enjoy the music and kindly report any bugs or gliches to [Support Server](https://discord.gg/teszgSR9yK)\n__Music Commands (Usage: `a/ command`)__:\nplay, pause, clear-queue, filter, loop, nowplaying, queue, resume, search, shuffle, skip, stop, volume, w-filters\n__Filters (Usage: `a/ filter filtername`)__:\n`8D, gate, haas, phaser, treble, tremolo, vibrato, reverse, karaoke, flanger, mcompand, pulsator, subboost, bassboost, vaporwave, nightcore, normalizer, surrounding`\n\n **Introducing Asteroid Music!** \n [Invite Asteroid Music](https://discord.com/oauth2/authorize?client_id=836830093644791809&scope=bot&permissions=37088576)", color=0xBCFC09))

# PREMIUM
#     if message.content.startswith("a/ premium") or message.content.startswith("a/ help premium") or message.content.startswith("a/ premium help"):
#         ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
#         await message.channel.send(embed=discord.Embed(title="**PREMIUM for FREE!!**\n▬▬▬▬▬▬▬▬▬▬", description="__Premium Features__:\n__NOTE__: Premium features are not available yet, so pls do not ask or create ticket for it. It will be available in next(v1.9) or v2.0 update! the below details are only tentative and just for some idea about premium \n<a:ag_arrowgif:781395494127271947> A different animated emoji will be used instead of <a:ag_flyn_hrts_cyn:781395468978356235> while reacting to your messages\n\nPresently there are NO features to enjoy in premium but lots will be added to it in upcomming updates!\nAbout premium:\nPremium here does not mean any profit of any kind to me and you will NOT be asked to USE or PAY any money or related items. Premium can be obtained by redeeming AstroCash. Astrocash can be redeemed ony by creating a ticket in our [Support Server](https://discord.gg/teszgSR9yK) but soon there will be a feature to redeem using commands! To earn AstroCash use `a/ earn` or `a/ astrocash`. Also to check your profile use `a/ profile` (not available yet) You can see the redeemption price for each feature using `a/ redeem`."))

    # if message.content.startswith("a/ astrocash") or message.content.startswith("a/ earn"):
    #     await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
    #     await message.channel.send(embed=discord.Embed(title="AstroCash\n▬▬▬▬▬▬▬▬▬▬", description="AstroCash is currency for me! It can be redeemed into lots of usable features, commands or even premium. Presently you cannot transfer or trade AstroCash. To view redeemable items or Redeem AstroCash use `a/ redeem`\n\nAstroCash can be earned by:\n<a:ag_arrowgif:781395494127271947> Joining Support Server and other servers listed in a separate channel in Support Server\n<a:ag_arrowgif:781395494127271947> Finding bugs in the bot and reporting it in our [Support Server](https://discord.gg/teszgSR9yK) AstroCash will be given according to the size of the bug, you can even report typos!\n<a:ag_arrowgif:781395494127271947> Vote for me every 12hrs use `a/ vote`\n<a:ag_arrowgif:781395494127271947> Giving good suggestions using `a/ suggest help` AstroCash will be given accrding to the worthiness of suggestion ||Spamming will be dealt with punishment||\n<a:ag_arrowgif:781395494127271947> Inviteing me to servers\n<a:ag_arrowgif:781395494127271947> Gaining levels with Asteroid or Gaining levels in [Support Server](https://discord.gg/teszgSR9yK) - According to levels\n<a:ag_arrowgif:781395494127271947> Sending cool facts in a channel in [Support Server](https://discord.gg/teszgSR9yK) - 20 points\n<a:ag_arrowgif:781395494127271947> Helping creator to test the bot. Make sure you read rules in [Support Server](https://discord.gg/teszgSR9yK)\n<a:ag_arrowgif:781395494127271947> Playing Quiz - 10 points for correct and 2 points for wrong answer"))

    # if message.content.startswith("a/ redeem") or message.content.startswith("a/ help redeem") or message.content.startswith("a/ help reedeem") or message.content.startswith("a/ help reedem") or message.content.startswith("a/ reedeem") or message.content.startswith("a/ reedem"):
    #     await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
    #     await message.channel.send(embed=discord.Embed(title="Item List", description="File storage space - 500 AC\nbot space - 200 AC\n5 database space - 50 AC\n:SOME: Reaction - 100\n:another: Reaction - 120\n:another: Reaction - 10000\nLevel Mutiplyer - ###\nlotz to be added (suggestions welcomed with reward!)\n\nUse `a/ itemname redeem` to buy or `a/ info itemname` to get item info"))

# PREFERENCE

    if message.content.startswith("a/ add ticketmgr") or message.content.startswith("a/add ticketmgr") or message.content.startswith("a/ ticketmgr add") or message.content.startswith("a/ticketmgr add") or message.content.startswith("a/ add ticketmanager") or message.content.startswith("a/add ticketmanager") or message.content.startswith("a/ ticketmanager add") or message.content.startswith("a/ticketmanager add"):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.author.guild_permissions.administrator:
            tif = await message.channel.send(embed=discord.Embed(title="Adding... <a:ag_ldingwin:781410586138902529>", color=0x09BEFC))
            roleid = fetch_data(message.content)
            roleid = roleid.split(r"<@&")[1]
            roleid = roleid.split(r">")[0]

            srvdic = collection.find_one({"_id": int(message.guild.id)})
            try:
                rolelst = srvdic["ticketroleid"]
            except:
                rolelst = []

            if len(rolelst) >= 2:
                await tif.edit(embed=discord.Embed(title="Slots Full", description=f"Neither you nor your server is not Premium, so you can add maximum of 2 roles only. \n For help about premium and premium features Please use `a/ premium`", color=0x2AE717))
            elif (int(roleid) in rolelst) or (str(roleid) in rolelst):
                await tif.edit(embed=discord.Embed(title="Already Added", color=0x2AE717))
            else:
                rolelst.append(roleid)
                print(roleid)
                collection.update_one({"_id": int(message.guild.id)}, {"$set": {"ticketroleid": rolelst}})
                await tif.edit(embed=discord.Embed(title="Added", description=f"Role: <@&{roleid}> \nRequested By : {message.author.mention}", color=0x2AE717))
        else:
            await message.channel.send(embed=discord.Embed(title="You Don't have Administrator Permissions <a:ag_exc:781410611366985748>", color=0xFC4905))
    #     await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)

    if message.content.startswith("a/ remove ticketmgr") or message.content.startswith("a/remove ticketmgr") or message.content.startswith("a/ ticketmgr remove") or message.content.startswith("a/ticketmgr remove"):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.author.guild_permissions.administrator:
            tif = await message.channel.send(embed=discord.Embed(title="Removing... <a:ag_ldingwin:781410586138902529>", color=0x09BEFC))
            roleid = fetch_data(message.content)
            roleid = roleid.split(r"<@&")[1]
            roleid = roleid.split(r">")[0]

            srvdic = collection.find_one({"_id": int(message.guild.id)})
            try:
                rolelst = srvdic["ticketroleid"]
            except:
                rolelst = []

            if (int(roleid) in rolelst) or (str(roleid) in rolelst):
                for i in range(0, len(rolelst)):
                    if int(roleid) == rolelst[i]:
                        rolelst.pop(i)
                    elif str(roleid) == rolelst[i]:
                        rolelst.pop(i)
                    print(roleid)
                    print(rolelst)
                collection.update_one({"_id": int(message.guild.id)}, {"$set": {"ticketroleid": rolelst}})
                await tif.edit(embed=discord.Embed(title="Removed", description=f"Role: <@&{roleid}> \nRequested By : {message.author.mention}", color=0x2AE717))
            else:
                await tif.edit(embed=discord.Embed(title="Role not Found!", color=0x2AE717))
        else:
            await message.channel.send(embed=discord.Embed(title="You Don't have Administrator Permissions <a:ag_exc:781410611366985748>", color=0xFC4905))


    if message.content == "a/ ticket enable" or message.content == "a/ ticket true" or message.content == "a/ enable ticket":
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.author.guild_permissions.manage_channels:
            tif = await message.channel.send(embed=discord.Embed(title="Enabling... <a:ag_ldingwin:781410586138902529>", color=0x2AE717))
            srvdic = collection.find_one({"_id":1341})
            srvlst = srvdic["ids"]
            if int(message.guild.id) in srvlst:
                await tif.edit(embed=discord.Embed(title="Already Enabled", color=0x2AE717))
            else:
                strgid = int(message.guild.id)
                srvlst.append(strgid)
                collection.update_one({"_id":1341}, {"$set":{"ids":srvlst}})
                await tif.edit(embed=discord.Embed(title="Enabled", description=f"Requested By : {message.author.mention}", color=0x2AE717))
        else:
            await message.channel.send(embed=discord.Embed(title="You Don't have Permission to Manage Channels <a:ag_exc:781410611366985748>", color=0xFC4905))

    if message.content == "a/ ticket disable" or message.content == "a/ ticket false" or message.content == "a/ disable ticket":
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.author.guild_permissions.manage_channels:
            tif = await message.channel.send(embed=discord.Embed(title="Disabling... <a:ag_ldingwin:781410586138902529>", color=0x2AE717))
            srvdic = collection.find_one({"_id":1341})
            srvlst = srvdic["ids"]
            if int(message.guild.id) not in srvlst:
                await tif.edit(embed=discord.Embed(title="Already Disabled", color=0x2AE717))
            else:
                strgid = int(message.guild.id)
                srvlst.remove(strgid)
                collection.update_one({"_id": 1341}, {"$set": {"ids": srvlst}})
                await tif.edit(embed=discord.Embed(title="Disabled", description=f"Requested By: {message.author.mention}", color=0x2AE717))
        else:
            await message.channel.send(embed=discord.Embed(title="You Don't have Permission to Manage Channels <a:ag_exc:781410611366985748>", color=0xFC4905))

    if message.content.find("a/ set chatmod false") != -1 or message.content.find("a/set chatmod false") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.author.guild_permissions.manage_messages:
            tif = await message.channel.send(embed=discord.Embed(title="Disabling... <a:ag_ldingwin:781410586138902529>", color=0x2AE717))
            gid = int(message.guild.id)
            fin = collection.find_one({"_id":gid})
            if fin == None:
                collection.insert({"_id":gid,"chatmod":0,"badwords":[],"moddel":0})
                await tif.edit(embed=discord.Embed(title="Chat Moderation Diabled", description="Chat in this Server will **NOT** be moderated with a warn message for the words you have added using `a/ badword =<badword>`\n For more use `a/ mod help` or `a/ set help`", color=0x2AE717))
            else:
                collection.update_one({"_id":gid},{"$set":{"chatmod":0}})
            await tif.edit(embed=discord.Embed(title="Chat Moderation Diabled", description="Chat in this Server will **NOT** be moderated with a warn message for the words you have added using `a/ badword =<badword>`\n For more use `a/ mod help` or `a/ set help`", color=0x2AE717))
        else:
            await message.channel.send(embed=discord.Embed(title="You Don't have Permission to Manage Messages <a:ag_exc:781410611366985748>", color=0xFC4905))

    if message.content.find("a/ set chatmod true") != -1 or message.content.find("a/ set chatmod true") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.author.guild_permissions.manage_messages:
            tif = await message.channel.send(embed=discord.Embed(title="Enabling... <a:ag_ldingwin:781410586138902529>", color=0x2AE717))
            gid = int(message.guild.id)
            fin = collection.find_one({"_id":gid})
            if fin == None:
                collection.insert({"_id":gid,"chatmod":1,"badwords":[],"moddel":0})
                await tif.edit(embed=discord.Embed(title="Chat Moderation Enabled", description="Chat in this Server **WILL** be moderated with a warn message for the words you have added using `a/ badword =<badword>`\nIf you want to Delete AND warn pls type `a/ set delmod true`\n For more use `a/ mod help` or `a/ set help`"))
            else:
                collection.update_one({"_id":gid},{"$set":{"chatmod":1}})
                await tif.edit(embed=discord.Embed(title="Chat Moderation Enabled", description="Chat in this Server **WILL** be moderated with a warn message for the words you have added using `a/ badword =<badword>`\nIf you want to Delete AND warn pls type `a/ set delmod true`\n For more use `a/ mod help` or `a/ set help`", color=0x2AE717))
        else:
            await message.channel.send(embed=discord.Embed(title="You Don't have Permission to Manage Messages <a:ag_exc:781410611366985748>", color=0xFC4905))

    if message.content.find("a/ set delmod true") != -1 or message.content.find("a/ set delmod true") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.author.guild_permissions.manage_messages:
            gid = int(message.guild.id)
            fin = collection.find_one({"_id":gid})
            if fin == None:
                collection.insert({"_id":gid,"chatmod":1,"badwords":[], "moddel":1})
                await message.channel.send(embed=discord.Embed(title="DelMod and Chat Moderation Enabled", description="Blacklisted words in this Server **WILL** be Deleted with a warn message for the words you have added using `a/ badword =<badword>`\n For more use `a/ mod help` or `a/ set help`", color=0x2AE717))
            else:
                collection.update_one({"_id":gid},{"$set":{"chatmod":1,"moddel":1}})
            await message.channel.send(embed=discord.Embed(title="DelMod and Chat Moderation Enabled", description="Blacklisted words in this Server **WILL** be Deleted with a warn message for the words you have added using `a/ badword =<badword>`\n For more use `a/ mod help` or `a/ set help`", color=0x2AE717))
        else:
            await message.channel.send(embed=discord.Embed(title="You Don't have Permission to Manage Messages <a:ag_exc:781410611366985748>", color=0xFC4905))

    if message.content == ("a/ set delmod false") or message.content == ("a/ set delmod false"):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.author.guild_permissions.manage_messages:
            gid = int(message.guild.id)
            fin = collection.find_one({"_id": gid})
            if fin == None:
                collection.insert({"_id": gid, "chatmod": 0, "badwords": [], "moddel": 0})
                await message.channel.send(embed=discord.Embed(title="DelMod and Chat Modertion Disabled", description="Blacklisted words in this Server will **NOT** be deleted\nFor more use `a/ mod help` or `a/ set help`", color=0x2AE717))
            else:
                collection.update_one({"_id": gid}, {"$set": {"moddel": 0}})
            await message.channel.send(embed=discord.Embed(title="DelMod Disabled", description="Blacklisted words in this Server will **NOT** be deleted\nFor more use `a/ mod help` or `a/ set help`", color=0x2AE717))
        else:
            await message.channel.send(embed=discord.Embed(title="You Don't have Permission to Manage Messages <a:ag_exc:781410611366985748>", color=0xFC4905))

# WIKIPEDIA
    if message.content.find("a/ wiki ") != -1 or message.content.find("a/wiki ") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        edmsg = await message.channel.send(embed=discord.Embed(title="Searching... <a:ag_ldingwin:781410586138902529>", color=0x09BEFC))
        words = fetch_data(message.content)
        wordas = words
        wordas = str(wordas)
        topa = ""
        dups = list(words)
        for i in range(0,len(dups)):
            if dups[i] == " ":
                topa += "+"
            else:
                topa += dups[i]
        words = topa
        wordas = wordas.upper()
        def wiki_summary(arg):
            definition = wikipedia.summary(arg, sentences=5, chars=1000, auto_suggest=True, redirect=True)
            return definition
        try:
            desc = wiki_summary(words)
            serch = discord.Embed(title=f"{wordas}", description=f"**Defenition According to WikiPedia:**\n{desc}", color=0x05FCB1)
            await edmsg.edit(embed=serch)
        except Exception as e:
            await edmsg.edit(embed=discord.Embed(title="Page Not Found", description=f"**Possible Reasons:**\n<a:ag_arrowgif:781395494127271947> The Keyword **{words}** did not Match any Pages\n<a:ag_arrowgif:781395494127271947> My Ping or Latency is High, check using `a/ ping`\n<a:ag_arrowgif:781395494127271947> WikiPedia's Server is Down or not Responding", color=0xFC8C05))

# URBAN DICTIONARY
    if message.content.startswith('a/ dic ') or message.content.startswith("a/dic ") or message.content.startswith("a/ def ") or message.content.startswith("a/def "):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        eddic = await message.channel.send(embed=discord.Embed(title='Searching... <a:ag_ldingwin:781410586138902529>', color=0x09BEFC))
        dicsr = fetch_data(message.content)
        url = f"https://api.urbandictionary.com/v0/define?term={dicsr}"
        response = json.loads(requests.get(url).content)
        a = (response['list'])
        b = a[0]
        c = b['definition']
        d = b['example']
        thup = b['thumbs_up']
        thdo = b['thumbs_down']
        try:
            dicsr = dicsr.upper()
        except Exception as e:
            print(e)
        dicem = discord.Embed(title=f'{dicsr}', description=f'__Definition__: {c}\nExample: {d}', color=0x02BDFE)
        dicem.set_footer(text=f"👍 : {thup}, 👎 : {thdo}")
        await eddic.edit(embed=dicem)

# Image search
    if message.content.startswith("a/image ") or message.content.startswith("a/ image "):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        try:
            msgcontent = message.content.split(' ')
            imgsearchterm = ""
            try:
                for i in range(2,len(msgcontent)):
                    imgsearchterm += f"{msgcontent[i]} "
            except:
                pass

            if msgcontent != "":
                class AppURLopener(urllib.request.FancyURLopener):
                    version = "Mozilla/5.0"

                opener = AppURLopener()
                htmldata = opener.open(f'https://www.dogpile.com/serp?q={imgsearchterm}&sc=wUtDg1W2On4R20')
                imagesoup = bs4.BeautifulSoup(htmldata, 'html.parser')
                images = imagesoup.find_all('img')
                add = images[random.choice([1,2,3,4,5,6,7,8,9,0])]
                imgurl = add["src"]
                imgmbd = discord.Embed(title=f"Image for **{imgsearchterm}**", color=0x02BDFE)
                imgmbd.set_image(url=f"{imgurl}")
                imgmbd.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
                await message.channel.send(embed=imgmbd)
            else:
                await message.content.send(embed=discord.Embed(title="Enter a term to search!!", color=0xFB1F1F))
        except Exception as e:
            print(e)
            await message.channel.send(embed=discord.Embed(title="An error Occurred", description="If this occurs again and again Please Report to [Support Server](https://discord.gg/teszgSR9yK)", color=0xFB1F1F))

# RANDOM FACTS
    if message.content.startswith("a/ fact") or message.content.startswith("a/ random fact") or message.content.startswith("a/fact") or message.content.startswith("a/random fact"):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        factfile = open("fact.txt", "r", encoding="utf8")
        rndmfctlst = factfile.readlines()
        factfile.close()
        randnumf = random.randint(0, len(rndmfctlst))
        rndmfct = rndmfctlst[randnumf]
        await message.channel.send(embed=discord.Embed(title=f"{rndmfct} Fact ID: {randnumf}", description=f"Care has been taken to give a quality fact but If you find any inappropriate or unwanted or offensive or nsfw content above just remember the fact ID(Fact ID: **{randnumf}**) and please send it to us using a suggestion(`a/ suggest help`) or a message in our [Support Server](https://discord.gg/teszgSR9yK) and that sentence will be removed and you will be awarded AstroCash. Sorry for the inconvenience.", color=0x02BDFE))

# DeCAN
    if message.content.startswith("a/ decan") or message.content.startswith("a/decan"):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.author.guild_permissions.manage_nicknames:
            try:
                target = message.mentions[0]
                naaame = str(target)
                namelst = list(naaame)
                naaame = ""
                splchardic = {"ᴷ": "K", "ᴺ": "N", '『': '(', '』': ')', '𝑀': 'M', '𝒫': 'P', '𝒮': 'S', '𝒴': 'Y', '𝒞': 'C', '𝐻': 'H', '𝒪': 'O', "ᴅ": "D", "ᴇ": "E", 'Ｂ': 'B', 'Ｏ': 'O', 'Ｓ': 'S', "〃": ".", "м": "M", '◉': 'O', 'ᴳ': 'G', 'ˣ': 'X', 'ᵘ': 'u', 'Ｎ': 'N', 'Ａ': 'A', 'Ｒ': 'R', 'Ｈ': 'H', 'Ｃ': 'C', '🅼': 'M', '🅰': 'C', '🅻': 'L', '🆂': 'S', '🅷': 'H', '𝖎': 'i', '𝖍': 'h', '𝖘': 's', '𝖗': 'r', '𝑹': 'R', '𝑬': 'E', '𝑫': 'D', '𝑼': 'U', '𝑯': 'H', '𝑻': 'T', 'ɪ': 'I', 'ᴠ': 'V', 'ʜ': 'H', 'ᴛ': 'T', 'ʀ': 'R', 'ᴘ': 'P', 'Ｉ': 'I', 'Ｔ': 'T', 'Ｋ': 'K', 'є': 'e', 'я': 'R', 'α': 'a', 'ʑ': 'z', 'ℓ': 'l',"𝒄":"c", "𝒌":"k", 'ι': 'l', 'Z': 'Z', 'Ƭ': 'T', "𝒋":"j", "𝒂":"a", '~': '-', "Ѧ":"A", "₊":",", "⋆":".", "𒆜":"X","Ѵ":"V", "Ǥ":"G", "Л":"N", "Σ":"E", "$":"S","Ƕ":"H", "ᵉ":"e", "ᵛ":"v", "⎰":"/", "⎱":"\\", "⎝":"\\", "⧹":"\\", "⧸":"/", "⎠":"/", "™":"tm", "𝑩":"B", "𝑵":"N", "𝑮":"G", "ᴰ":"D", "ᴱ":"E", "ⱽ":"V", "Ξ":"E"}
                for i in range(0, len(namelst)-5):
                    if namelst[i] in ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '_', '`', '{', '|', '}', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
                        naaame += namelst[i]

                    elif namelst[i] in splchardic:
                        naaame += splchardic[namelst[i]]

                    else:
                        ranchn = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
                        naaame += ranchn
                await target.edit(nick=f"{naaame}")
                await message.channel.send(embed=discord.Embed(title="Name has been DEcancered :microbe:", description=f"{target.mention}", color=0xFD4201))
            except Exception as e:
                await message.channel.send(embed=discord.Embed(title="<a:ag_exc:781410611366985748> Error Occured <a:ag_exc:781410611366985748>", description=f"__Possible Reason__:\n<a:ag_arrowgif:781395494127271947> You Did not mention someone\n<a:ag_arrowgif:781395494127271947> I Don't have Manage Nickname Permissions\n<a:ag_arrowgif:781395494127271947> Person mentioned has a Higher Role than Me\n\nError:{e}", color=0xFD4201))

        else:
            await message.channel.send(embed=discord.Embed(title="You do not have Manage Nickname permissions"))

# WEATHER
    if (message.content.startswith("a/ weather ") or message.content.startswith("a/weather ")) and not (message.content.startswith("a/ weather help") or message.content.startswith("a/weather help")):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        wethd = await message.channel.send(embed=discord.Embed(title="Searching... <a:ag_ldingwin:781410586138902529>", color=0x09BEFC))
        location = fetch_data(message.content)
        if len(location) >= 2:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={wthapikey}&units=metric"
            data = json.loads(requests.get(url).content)
            data = str(data)
            # {'coord': {'lon': 80.28, 'lat': 13.09}, 'weather': [{'id': 301, 'main': 'Drizzle', 'description': 'drizzle', 'icon': '09d'},
            # {'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}],
            # 'base': 'stations', 'main': {'temp': 27, 'feels_like': 31.85, 'temp_min': 27, 'temp_max': 27, 'pressure': 1008, 'humidity': 94},
            # 'visibility': 3000, 'wind': {'speed': 3.1, 'deg': 40}, 'rain': {'1h': 0.27}, 'clouds': {'all': 90},
            # 'dt': 1607074808, 'sys': {'type': 1, 'id': 9218, 'country': 'IN', 'sunrise': 1607042849, 'sunset': 1607083870}, 'timezone': 19800,
            # 'id': 1264527, 'name': 'Chennai', 'cod': 200}
            if data.split("'")[-2] == "city not found":
                await message.channel.send(embed=discord.Embed(title=f"City {location} Not Found", description="Your Requested City Is not Found Sorry!", color=0xFC5F05))
            lon = data.split(":")[2]
            lon = lon.split(",")[0]

            lat = data.split(":")[3]
            lat = lat.split("}")[0]

            stat = data.split(":")[6]
            stat = stat.split("'")[1]

            emoj = ":sunny:"
            if stat == "Drizzle":
                emoj = ":white_sun_rain_cloud:"
            if stat == "Rain":
                emoj = ":cloud_rain:"
            if stat == "Clouds":
                emoj = ":cloud:"
            if stat == "Mist":
                emoj = "<:mistop:784711272369225728>"
            if stat == "Smoke":
                emoj = ":anger_right:"
            if stat == "Snow":
                emoj = ":snowflake:"
            if stat == "Haze":
                emoj = ":white_sun_cloud:"

            temp = data.split("temp")[1]
            temp = temp.split(",")[0]
            temp = temp.split(":")[1]

            feels = data.split("feels_like':")[1]
            feels = feels.split(",")[0]

            mintem = data.split("temp_min':")[1]
            mintem = mintem.split(",")[0]

            maxtem = data.split("temp_max':")[1]
            maxtem = maxtem.split(',')[0]

            press = data.split("pressure':")[1]
            press = press.split(',')[0]

            humid = data.split("humidity':")[1]
            humid = humid.split("}")[0]

            visib = data.split("visibility':")[1]
            visib = visib.split(',')[0]

            wndspd = data.split("speed':")[1]
            wndspd = wndspd.split(",")[0]

            snrtim = data.split("sunrise':")[1]
            snrtim = snrtim.split(",")[0]
            snrtim = datetime.datetime.utcfromtimestamp(int(snrtim)).strftime('%Y-%m-%d %H:%M:%S')

            snttim = data.split("sunset':")[1]
            snttim = snttim.split("}")[0]
            snttim = datetime.datetime.utcfromtimestamp(int(snttim)).strftime('%Y-%m-%d %H:%M:%S')

            await wethd.edit(embed=discord.Embed(title=f"{location} Weather Report\n▬▬▬▬▬▬▬▬▬▬", description=f"{emoj}{emoj}{emoj}{emoj}{emoj}{emoj}\n<a:ag_arrowgif:781395494127271947> Longitide : {lon}\n<a:ag_arrowgif:781395494127271947> Latitude\
            : {lat}\n<a:ag_arrowgif:781395494127271947> Status : {stat}\n<a:ag_arrowgif:781395494127271947> Temperature : {temp}\n<a:ag_arrowgif:781395494127271947> Feels Like : {feels}\n<a:ag_arrowgif:781395494127271947> Minimum Temperature : {mintem}\n<a:ag_arrowgif:781395494127271947> Maximum Temperature : {maxtem}\n<a:ag_arrowgif:781395494127271947> Pressure : {press}\n<a:ag_arrowgif:781395494127271947> Humidity : {humid}\n<a:ag_arrowgif:781395494127271947> Wind Speed : {wndspd}", color=0x057DFC))
        else:
            ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
            await wethd.edit(embed=discord.Embed(title="Invalid Location <a:ag_exc:781410611366985748>", description="Enter a Valid Location", color=0xFC5F05))

# SYSTEM STATS
    if message.content.startswith("a/ cpu") or message.content.startswith("a/cpu"):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")

        try:
            cpupert = "Error"
            cpun = "Error"
            cpusw = "Error"
            cpupers = "Error"
        except Exception as e:
            print(e)

        try:
            cpui = "Error"
            cpui = "Error"
            cpui = "Error"
            cpui = "Error"
            cpui = "Error"
            cpui = "Error"
            cpuppp = "Error"
        except Exception as e:
            print(e)

        try:
            cpusw = "Error"
            cpuswt = "Error"
            cpuswt = "Error"
            cpuswt = "Error"
            cpuswt = "Error"
            cpuswt = "Error"
            cpuswt = "Error"
        except Exception as e:
            print(e)

        try:
            cpusw = "Error"
            cpuswu = "Error"
            cpuswu = "Error"
            cpuswu = "Error"
            cpuswu = "Error"
            cpuswu = "Error"
            cpuswu = "Error"
        except Exception as e:
            print(e)

        try:
            cpusw = "Error"
            cpuswf = "Error"
            cpuswf ="Error"
            cpuswf = "Error"
            cpuswf = "Error"
            cpuswf = "Error"
            cpuswf = "Error"
        except Exception as e:
            print(e)

        try:
            cpusw = "Error"
            cpuswp = "Error"
            cpuswp = "Error"
        except Exception as e:
            print(e)

        try:
            sysarch = "Error"
            nodsds = "Error"
            sysmchn = "Error"
        except Exception as e:
            pass

        try:
            dist = "Error"
            dist = "Error"
        except Exception as e:
            print(e)

        try:
            lines = "Error"

            meminf1 = "Error"
            meminf2 = "Error"
            info = "Error"
        except Exception as e:
            print(e)

        try:
            syscpumo = "Error"
            cpuinfo = "Error"
            syscpumo = "Error"
        except Exception as e:
            print(e)

        try:
            uptime = "Error"
            uptime = "Error"
            uptime = "Error"
            uptime_hours = "Error"
            uptime_minutes = "Error"
            servuptime = "Error"
        except Exception as e:
            print(e)

        try:
            avgload = "Error"
            sysspd = "Error"
        except Exception as e:
            print(e)

        if str(platform.system()) != "":
            try:
                cpupert = psutil.cpu_percent()
                cpun = psutil.cpu_count()
                cpusw = psutil.swap_memory()
                cpupers = psutil.cpu_percent(percpu=1)
            except Exception as e:
                print(e)

            try:
                cpui = psutil.cpu_freq()
                cpui = str(cpui)
                cpui = cpui.split("=")[-1]
                cpui = cpui.split(")")[0]
                cpui = float(cpui)
                cpui = cpui / 1000
                cpuppp = ""
                print("printing hereeeeee: ", cpupers)
                for i in range(len(cpupers)):
                    cpuo = cpupers[int(i)]
                    cpuppp += f"Core{int(i)}: {cpuo}%\n"
            except Exception as e:
                print(e)

            try:
                cpusw = str(cpusw)
                cpuswt = cpusw.split("=")[1]
                cpuswt = cpuswt.split(",")[0]
                cpuswt = float(cpuswt)
                cpuswt = cpuswt/10000000
                cpuswt = math.floor(cpuswt)
                cpuswt = cpuswt/100
            except Exception as e:
                print(e)

            try:
                cpusw = str(cpusw)
                cpuswu = cpusw.split("=")[2]
                cpuswu = cpuswu.split(",")[0]
                cpuswu = float(cpuswu)
                cpuswu = cpuswu / 10000000
                cpuswu = math.floor(cpuswu)
                cpuswu = cpuswu / 100
            except Exception as e:
                print(e)

            try:
                cpusw = str(cpusw)
                cpuswf = cpusw.split("=")[3]
                cpuswf = cpuswf.split(",")[0]
                cpuswf = float(cpuswf)
                cpuswf = cpuswf / 10000000
                cpuswf = math.floor(cpuswf)
                cpuswf = cpuswf / 100
            except Exception as e:
                print(e)

            try:
                cpusw = str(cpusw)
                cpuswp = cpusw.split("=")[4]
                cpuswp = cpuswp.split(",")[0]
            except Exception as e:
                print(e)

            try:
                sysarch = platform.architecture()[0]
                nodsds = platform.node()
                sysmchn = platform.system()
            except Exception as e:
                pass

            try:
                dist = platform.dist()
                dist = " ".join(x for x in dist)
            except Exception as e:
                print(e)

            try:
                with open("/proc/meminfo", "r") as f:
                    lines = f.readlines()

                meminf1 = ("     " + lines[0].strip())
                meminf2 = ("     " + lines[1].strip())

                with open("/proc/cpuinfo", "r")  as f:
                    info = f.readlines()
            except Exception as e:
                print(e)

            try:
                syscpumo = "Error"
                cpuinfo = [x.strip().split(":")[1] for x in info if "model name" in x]
                for index, item in enumerate(cpuinfo):
                    syscpumo = ("    " + str(index) + ": " + item)
            except Exception as e:
                print(e)

            try:
                uptime = None
                with open("/proc/uptime", "r") as f:
                    uptime = f.read().split(" ")[0].strip()
                uptime = int(float(uptime))
                uptime_hours = uptime // 3600
                uptime_minutes = (uptime % 3600) // 60
                servuptime = ("Uptime: " + str(uptime_hours) + ":" + str(uptime_minutes) + " hours")
            except Exception as e:
                print(e)

            try:
                with open("/proc/loadavg", "r") as f:
                    avgload = ("Average Load: " + f.read().strip())
                sysspd = syscpumo.split(" ")[-1]
            except Exception as e:
                print(e)
            await message.channel.send(embed=discord.Embed(title="CPU STATS :tools:", description=f"\nNode: {nodsds}\nServer Load: {avgload}\n**Processor**\nArchitecture: {sysarch}\nModel: {syscpumo}\nCores = {cpun}\nSpeed = {sysspd} Ghz\nTotal Usage = {cpupert}%\n{cpuppp}\n\nOS: {sysmchn}\nDist: {dist}\n\nDisk:\nTotal: {meminf1}\nFree: {meminf2}\n\n**RAM**\nTotal = {cpuswt} Gb\nUsed = {cpuswu} Gb\nPercentage = {cpuswp}%\nFree = {cpuswf} Gb\n\nServer {servuptime}", color=0xFD9E01))

# DATE TIME
    if message.content.find("a/ time") != -1 or message.content.find("a/time") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        time = datetime.datetime.now()
        time = str(time)
        time = time.split()[-1]
        time = time.split('.')[0]
        await message.channel.send(embed=discord.Embed(title=f"{time}", description="The Time NOW According to My server", color=0x05ADFC))

    if message.content.find("a/ date") != -1 or message.content.find("a/date") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        date = datetime.datetime.now()
        date = str(date)
        date = date.split()[0]
        await message.channel.send(embed=discord.Embed(title=f"{date}", description="Date Today According to My server", color=0x05ADFC))

# EVAL
    if message.content.find("a/ eval ^") != -1 and message.author.id == 782624720989585409:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        ecol = message.content.split('^')[-1]
        opt = eval(ecol)
        await message.channel.send(embed=discord.Embed(title=f"{opt}", description=f"Evauated by {message.author}"))

# OWNER
    if message.content.find("a/ perm") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        owie = message.mentions[0].guild_permissions
        await message.channel.send(embed=discord.Embed(title=f"{message.author}'s Permissions in {message.guild}", description=f"{owie}"))

# MODERATION
    if message.content.find("a/ kick") != -1 or message.content.find("a/kick") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        try:
            if message.author.guild_permissions.kick_members:
                kikser = message.mentions[0]
                if int(kikser.id) == 641305773095387156:
                    raise Exception ("Owner")
                else:
                    kiksn = "no reason"
                    try:
                        kiksn = message.content.split("for")[1]
                    except Exception as e:
                        kiksn = "no reason"
                        print(e)
                    await kikser.kick(reason=f"{kiksn}")
                    kikbed = discord.Embed(title=f"<a:ag_exc:781410611366985748> KICKED {kikser}<a:ag_exc:781410611366985748>", description=f"{message.author} has Kicked {kikser} from {message.guild} for {kiksn}", color=0xFD0101)
                    await message.channel.send(embed=kikbed)
                    woks = message.mentions[0]
                    await woks.send(embed=kikbed)
            else:
                await message.channel.send(embed=discord.Embed(title="You Don't have Permission to Kick Members <a:ag_exc:781410611366985748>", color=0xFC4905))
        except Exception as exp:
            exp = str(exp)
            exp = exp.split(': ')[-1]
            if exp == ("Missing Permissions"):
                await message.channel.send(embed=discord.Embed(title="<a:ag_exc:781410611366985748> Missing Permissions <a:ag_exc:781410611366985748>", description="Possible Reasons:\n<a:ag_arrowgif:781395494127271947> I Don't have Kick Permissions\n<a:ag_arrowgif:781395494127271947> The Member You are trying to Kick has a Higher Role than Me", color=0xFD4201))
            elif exp == ("Owner"):
                await message.channel.send(embed=discord.Embed(title="<a:ag_exc:781410611366985748> Error! <a:ag_exc:781410611366985748>", description="Sorry! I can't Kick My Master!", color=0xFD4201))

    if message.content.find("a/ ban") != -1 or message.content.find("a/ban") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        try:
            if message.author.guild_permissions.ban_members:
                banser = message.mentions[0]
                if int(banser.id) == 641305773095387156:
                    raise Exception ("Owner")
                else:
                    bansn = "no reason"
                    try:
                        bansn = message.content.split("for")[1]
                    except Exception as e:
                        bansn = "no reason"
                    await banser.ban(reason=f"{bansn}")
                    await message.channel.send(embed=discord.Embed(title=f"<a:ag_exc:781410611366985748> BANNED {banser}<a:ag_exc:781410611366985748>", description=f"**{message.author}** has Banned **{banser}** from {message.guild} for {bansn}", color=0xFD0101))
            else:
                await message.channel.send(embed=discord.Embed(title="You Don't have Permission to Ban Members <a:ag_exc:781410611366985748>", color=0xFC4905))
        except Exception as exp:
            exp = str(exp)
            exp = exp.split(': ')[-1]
            if exp == ("Missing Permissions"):
                await message.channel.send(embed=discord.Embed(title="<a:ag_exc:781410611366985748> Missing Permissions <a:ag_exc:781410611366985748>", description="Possible Reasons:\n<a:ag_arrowgif:781395494127271947> I Don't have Ban Permissions\n<a:ag_arrowgif:781395494127271947> The Member You are trying to Ban has a Higher Role than Me", color=0xFD4201))
            elif exp == ("Owner"):
                await message.channel.send(embed=discord.Embed(title="<a:ag_exc:781410611366985748> Error! <a:ag_exc:781410611366985748>", description="Sorry! I can't Ban My Master!", color=0xFD4201))

    if message.content.find("a/ unban") != -1 or message.content.find("a/unban") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        try:
            if message.author.guild_permissions.ban_members:
                unbanser = message.mentions[0]
                await unbanser.pardon()
                await message.channel.send(embed=discord.Embed(title="<a:ag_exc:781410611366985748> UNBANNED <a:ag_exc:781410611366985748>", description=f"{message.author} has UNBANNED {unbanser} in {message.guild}", color=0xFD0101))

            else:
                await message.channel.send(embed=discord.Embed(title="You Don't have Permission to UNBAN Members <a:ag_exc:781410611366985748>", color=0xFC4905))
        except Exception as exp:
            exp = str(exp)
            exp = exp.split(': ')[-1]
            if exp == ("Missing Permissions"):
                await message.channel.send(embed=discord.Embed(title="<a:ag_exc:781410611366985748> Missing Permissions <a:ag_exc:781410611366985748>", description="Possible Reasons:\n<a:ag_arrowgif:781395494127271947> I Don't have Kick Permissions\n<a:ag_arrowgif:781395494127271947> The Member You are trying to Kick has a Higher Role than Me", color=0xFD4201))
            else:
                await message.channel.send(embed=discord.Embed(title="An Error Occured"), color=0xFD4201)

    if message.content.find("a/ mute") != -1 or message.content.find("a/mute") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.author.guild_permissions.administrator:
            mutser = message.mentions[0]
            await mutser.mute()
            await message.channel.send(embed=discord.Embed(title="<a:ag_exc:781410611366985748> MUTED <a:ag_exc:781410611366985748>", description=f"**{message.author}** has MUTED **{mutser}**", color=0xFD0101))

        else:
            await message.channel.send(embed=discord.Embed(title="You Don't have Permission to Mute Members <a:ag_exc:781410611366985748>", color=0xFC4905))

    if message.content.find("a/ warn") !=-1 or message.content.find("a/warn") !=-1:
        try:
            try:
                rsn = message.channel.split("for")[-1]
            except Exception as tods:
                rsn = "no reason"
            if message.author.guild_permissions.manage_messages:
                wrnser = message.mentions[0]
                await message.channel.send(embed=discord.Embed(title=f"<a:ag_exc:781410611366985748> {wrnser} YOU HAVE BEEN WARNED :warning: !!!", description=f"<@!{wrnser.id}> you have been warned by <@!{message.author.id}> for {rsn}", color=0xFD0101))
            else:
                await message.channel.send(embed=discord.Embed(title="You Don't have Permission to Warn Members <a:ag_exc:781410611366985748>", color=0xFC4905))
        except Exception as exp:
            exp = str(exp)
            exp = exp.split(': ')[-1]
            if exp == ("Missing Permissions"):
                await message.channel.send(embed=discord.Embed(title="<a:ag_exc:781410611366985748> Missing Permissions <a:ag_exc:781410611366985748>", description="Possible Reasons:\n<a:ag_arrowgif:781395494127271947> I Don't have Kick Permissions\n<a:ag_arrowgif:781395494127271947> The Member You are trying to Kick has a Higher Role than Me", color=0xFD4201))
            else:
                print(exp)

# EMOTIFY
    if message.content.find("a/ emotify ") !=-1 or message.content.find("a/emotify ") !=-1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        emo = fetch_data(message.content)
        emo = list(emo)
        emf = ""
        for i in emo:
            if i == "a" or i == "b" or i == "c" or i == "d" or i == 'e' or i == 'f'or i == 'g' or i == 'h' or i == 'i' or i == 'j' or i == 'k' or i == 'l' or i == 'm' or i == 'n' or i == 'o' or i == 'p' or i == 'q' or i == 'r' or i == 's' or i == 't' or i == 'u' or i == 'v' or i == 'w' or i == 'x' or i == 'y' or i == 'z':
               emf += f" :regional_indicator_{i}:"
            elif i == " ":
                emf += "  "
            elif i == "0":
                emf += ":zero:"
            elif i == "1":
                emf += ":one:"
            elif i == "2":
                emf += ":two:"
            elif i == "3":
                emf += ":three:"
            elif i == "4":
                emf += ":four:"
            elif i == "5":
                emf += ":five:"
            elif i == "6":
                emf += ":six:"
            elif i == "7":
                emf += ":seven:"
            elif i == "8":
                emf += ":eight:"
            elif i == "9":
                emf += ":nine:"
        await message.channel.send(embed=discord.Embed(title=f"{emf}", description=f"Requested By : {message.author}", color=0x02FE95))

# BASIC CALCULATOR
    if message.content.find('a/ div') != -1 or message.content.find('a/div') != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.content.split(' ')[-3] == 'divide' or message.content.split(' ')[-3] == 'div' or message.content.split(' ')[-3] == 'a/divide' or message.content.split(' ')[-3] == 'a/div':
            divv = message.content.split(' ')[-2]
            div = message.content.split(' ')[-1]
        divv = float(divv)
        div = float(div)
        divans = divv/div
        await message.channel.send(embed=discord.Embed(title=":1234: CALCULATOR :1234:", description=f"**{divv}** Divided by **{div}** =\n **{divans}** <a:ag_tickop:781395575962599445>\n\n{message.channel}", color=0x02FE95))

    if message.content.find('a/ add') != -1 or message.content.find('a/add') != -1:
        if message.content.find("ti"):
            pass
        else:
            ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
            if message.content.split(' ')[-3] == 'add' or message.content.split(' ')[-3] == 'addition' or message.content.split(' ')[-3] == 'a/add' or message.content.split(' ')[-3] == 'a/addition':
                addd = message.content.split(' ')[-2]
                adddd = message.content.split(' ')[-1]
            addd = float(addd)
            adddd = float(adddd)
            addans = addd + adddd
            await message.channel.send(embed=discord.Embed(title=":1234: CALCULATOR :1234:", description=f"**{addd}** Added to **{adddd}** =\n **{addans}** <a:ag_tickop:781395575962599445>", color=0x02FE95))

    if message.content.find('a/ sub') != -1 or message.content.find('a/sub') != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.content.split(' ')[-3] == 'sub' or message.content.split(' ')[-3] == 'subtract' or message.content.split(' ')[-3] == 'a/sub' or message.content.split(' ')[-3] == 'a/subtract':
            subb = message.content.split(' ')[-2]
            subbb = message.content.split(' ')[-1]
        subb = float(subb)
        subbb = float(subbb)
        subans = subb - subbb
        await message.channel.send(embed=discord.Embed(title=":1234: CALCULATOR :1234:", description=f"**{subbb}** Subtracted from **{subb}** =\n **{subans}** <a:ag_tickop:781395575962599445>", color=0x02FE95))

    if message.content.find('a/ mult') != -1 or message.content.find('a/mult') != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.content.split(' ')[-3] == 'mult' or message.content.split(' ')[-3] == 'multiply' or message.content.split(' ')[-3] == 'a/mult' or message.content.split(' ')[-3] == 'a/multiply':
            mult = message.content.split(' ')[-2]
            multt = message.content.split(' ')[-1]
        mult = float(mult)
        multt = float(multt)
        multans = mult * multt
        await message.channel.send(embed=discord.Embed(title=":1234: CALCULATOR :1234:", description=f"**{mult}** Multiplied by **{multt}** =\n **{multans}** <a:ag_tickop:781395575962599445>", color=0x02FE95))

    if message.content.find('a/ lcm') != -1 or message.content.find('a/lcm') != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.content.split(' ')[-3] == 'lcm' or message.content.split(' ')[-3] == 'a/lcm':
            aha1 = message.content.split(' ')[-2]
            aha2 = message.content.split(' ')[-1]
        aha1 = int(aha1)
        aha2 = int(aha2)
        if aha1 > aha2:
            gr = aha1
        else:
            gr = aha2
        while (True):
            if ((gr % aha1 == 0) and (gr % aha2 == 0)):
                lcm = gr
                break
            gr += 1
        await message.channel.send(embed=discord.Embed(title=":1234: CALCULATOR :1234:", description=f"LCM of **{aha1}** and **{aha2}** =\n **{lcm}** <a:ag_tickop:781395575962599445>", color=0x02FE95))

    if message.content.find('a/ hcf') != -1 or message.content.find('a/hcf') != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.content.split(' ')[-3] == 'hcf' or message.content.split(' ')[-3] == 'a/hcf':
            num1 = message.content.split(' ')[-2]
            num2 = message.content.split(' ')[-1]
        num1 = int(num1)
        num2 = int(num2)
        if num1 > num2:
            smaller = num2
        else:
            smaller = num1
        for i in range(1, smaller + 1):
            if ((num1 % i == 0) and (num2 % i == 0)):
                hcf = i
        await message.channel.send(embed=discord.Embed(title=":1234: CALCULATOR :1234:", description=f"HCF of **{num1}** and **{num2}** =\n **{hcf}** <a:ag_tickop:781395575962599445>", color=0x02FE95))

# TAX
    if message.content.find('a/ tax') != -1 or message.content.find('a/tax') != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.content.split(' ')[-3] == 'tax' or message.content.split(' ')[-2] == 't' or message.content.split(' ')[-3] == 'a/tax' or message.content.split(' ')[-2] == 'a/t':
            num1 = message.content.split(' ')[-2]
            num2 = message.content.split(' ')[-1]
            num1 = int(num1)
            num2 = int(num2)
            atxr = num2*num1
            atxr = atxr/100
            await message.channel.send(embed=discord.Embed(title=":1234: CALCULATOR :1234:", description=f"**{num2}** Amount\n**{num1}%** tax \nTax Amount = **{atxr}**\nBal Amount = **{num2-atxr}** <a:ag_tickop:781395575962599445>", color=0x02FE95))

# COMPLEX CALCULATOR 1
    if message.content.find("a/ ceil ") != -1 or message.content.find("a/ceil ") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        ceil = message.content.split(" ")[-1]
        ceil = float(ceil)
        cans = math.ceil(ceil)
        await message.channel.send(embed=discord.Embed(title=f"Ceil of {ceil} = {cans}", color=0x05FCE2))

    if message.content.find("a/ sqrt ") != -1 or message.content.find("a/sqrt ") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        sqrt = message.content.split(" ")[-1]
        sqrt = float(sqrt)
        cans = math.sqrt(sqrt)
        await message.channel.send(embed=discord.Embed(title=f"Square Root of {sqrt} = {cans}", color=0x05FCE2))

    if message.content.find("a/ exp ") != -1 or message.content.find("a/exp ") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        exp = message.content.split(" ")[-1]
        exp = float(exp)
        cans = math.exp(exp)
        await message.channel.send(embed=discord.Embed(title=f"Log `e` to the Power {exp} = {cans}", description="Use `a/ val e` for the Value of `e`", color=0x05FCE2))

    if message.content.find("a/ floor ") != -1 or message.content.find("a/floor ") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        floor = message.content.split(" ")[-1]
        floor = float(floor)
        cans = math.floor(floor)
        await message.channel.send(embed=discord.Embed(title=f"Floor Value of {floor} = {cans}", color=0x05FCE2))

    if message.content.find("a/ log ") != -1 or message.content.find("a/log ") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        log = message.content.split(" ")[-1]
        log = float(log)
        if log >= 0 :
            cans = math.log(log)
            await message.channel.send(embed=discord.Embed(title=f"Natural Log of {log} = {cans}", color=0x05FCE2))
        else:
            await message.channel.send(embed=discord.Embed(title=f"Natural Log of {log} is Not Defined", color=0xFC4905))

    if message.content.find("a/ log10 ") != -1 or message.content.find("a/log10 ") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        log = message.content.split(" ")[-1]
        log = float(log)
        if log >= 0:
            cans = math.log10(log)
            await message.channel.send(embed=discord.Embed(title=f"Log to the Base 10 of {log} = {cans}", color=0x05FCE2))
        else:
            await message.channel.send(embed=discord.Embed(title=f"The Log to the Base 10 of {log} is Not Defined", color=0xFC4905))

    if message.content.find("a/ sin ") != -1 or message.content.find("a/sin ") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        sin = message.content.split(" ")[-1]
        sin = float(sin)
        sin = math.radians(sin)
        cans = math.sin(sin)
        await message.channel.send(embed=discord.Embed(title=f"Sin of {sin} = {cans}", color=0x05FCE2))

    if message.content.find("a/ cos ") != -1 or message.content.find("a/cos ") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        cos = message.content.split(" ")[-1]
        cos = float(cos)
        cos = math.radians(cos)
        cans = math.cos(cos)
        await message.channel.send(embed=discord.Embed(title=f"Cos of {cos} = {cans}", color=0x05FCE2))

    if message.content.find("a/ tan ") != -1 or  message.content.find("a/tan ") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        tan = message.content.split(" ")[-1]
        tan = float(tan)
        tan = math.radians(tan)
        cans = math.tan(tan)
        await message.channel.send(embed=discord.Embed(title=f"Tan of {tan} = {cans}", color=0x05FCE2))

    if message.content.find("a/ factorial ") != -1 or message.content.find("a/ factorial ") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        fct = message.content.split(" ")[-1]
        fct = float(fct)
        cans = math.factorial(fct)
        await message.channel.send(embed=discord.Embed(title=f"Factorial of {fct} = {cans}", color=0x05FCE2))

# COMPLEX CALCULATOR 2

    if message.content.find("a/ bilog ") != -1 or message.content.find("a/bilog ") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        blga = message.content.split(" ")[-2]
        blga = float(blga)
        blgb = message.content.split(" ")[-1]
        blgb = float(blgb)
        cans = math.log(blga, blgb)
        await message.channel.send(embed=discord.Embed(title=f"The Value of {blga} to the Power {blgb} = {cans}", color=0x05FCE2))

    if message.content.find("a/ pow ") != -1 or message.content.find("a/pow ") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        powa = message.content.split(" ")[-2]
        powa = float(powa)
        powb = message.content.split(" ")[-1]
        powb = float(powb)
        cans = math.pow(powa, powb)
        await message.channel.send(embed=discord.Embed(title=f"The Value of {powa} to the Power {powb} = {cans}", color=0x05FCE2))

# CONVERTERS

    if (message.content.startswith("a/currency ") or message.content.startswith("a/ currency ")) and not (message.content.startswith("a/currency help") or message.content.startswith("a/ currency help") or message.content.startswith("a/ help currency") or message.content.startswith("a/help currency")):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        cnt = fetch_data(message.content)
        try:
            try:
                frm = cnt.split[" "](0)
                too = cnt.split[" "](1)
                amt = cnt.split[" "](2)
                url = f'https://free-currency-converter.herokuapp.com/list/convert?source={frm}&destination={too}'
                res = json.loads(requests.get(url).content)
                if res["success"] == False:
                    await message.channel.send(embed=discord.Embed(title="Invalid Syntax", description="Enter currencies only from the below list:\n AED AFN ALL AMD ANG AOA ARS AUD AWG AZN BAM BBD BDT BGN BHD BIF BMD BND BOB BRL BSD BTC BTN BWP CRC CUC CUP CVE CZK DJF DKK DOP DZD EEK EGP ERN ETB EUR FJD FKP GBP GEL GGP GHS GIP GMD GNF GTQ GYD HKD HNL HRK HTG HUF IDR ILS IMP INR IQD IRR ISK JEP JMD JOD JPY KES KGS KHR KMF KPW KRW KWD KYD KZT LAK LBP LKR LRD LSL LTL LVL LYD MAD MDL MGA MKD MMK MNT MOP MRO MUR MVR MWK MXN MYR MZN NAD NGN NIO NOK NPR NZD OMR PAB PEN PGK PHP PKR PLN PYG QAR RON RSD RUB RWF SAR SBD SCR SDG SEK SGD SHP SLL SOS SRD STD SVC SYP SZL THB TJS TMT TND TOP TRY TTD TWD TZS UAH UGX USD UYU UZS VEF VND VUV WST XAF XAG XAU XCD XDR XOF XPF YER ZAR ZMK ZMW ZWL BYN BYR BZD CAD CDF CHF CLF CLP CNY COP"))
                else:
                    val = res["converted_value"]
                    try:
                        frm = res["source"]
                        too = res["destination"]
                        amt = int(amt)
                        val = int(val)
                        camt = amt*val
                        await message.channel.send(embed=discord.Embed(title=":yen: Currency Converter :euro:", description=f"{frm} to {too} \n1 {frm} = {val}{too} \n {amt} {frm} = **{camt}{too}** <a:ag_tickop:781395575962599445>", color=0x02FE95))
                    except:
                        await message.channel.send(embed=discord.Embed(title="Enter a Valid amount!", color=0xF84309))
            except:
                await message.channel.send(embed=discord.Embed(title="INVALID SYNTAX", description="Use `a/ convert help` for more info", color=0xFF4900))
        except:
            await message.channel.send(embed=discord.Embed(title="An error Occurred", description="If this occurs again and again Please Report this to the [Support Server](https://discord.gg/teszgSR9yK)", color=0xFF4900))

    if message.content.find("a/ radians ") != -1 or message.content.find("a/radians ") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        radians = message.content.split(" ")[-1]
        radians = float(radians)
        cans = math.radians(radians)
        await message.channel.send(embed=discord.Embed(title=f"Radians in {radians} = {cans}", color=0x05FCE2))

    if message.content.find("a/ degrees ") != -1 or message.content.find("a/degrees ") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        degrees = message.content.split(" ")[-1]
        degrees = float(degrees)
        cans = math.degrees(degrees)
        await message.channel.send(embed=discord.Embed(title=f"Degrees in {degrees} = {cans}", color=0x05FCE2))

    if message.content.find("a/ far ") != -1 or message.content.find("a/far ") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        far = message.content.split(" ")[-1]
        far = float(far)
        cans = far - 32
        cans = cans * 5
        cans = cans / 9
        # (32°F − 32) × 5 / 9 = 0°C
        # (0°C × 9/5) + 32 = 32°F
        await message.channel.send(embed=discord.Embed(title=f"{far} Farenheit = {cans} Degrees", color=0x05FCE2))

    if message.content.find("a/ cel ") != -1 or message.content.find("a/cel ") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        deg = message.content.split(" ")[-1]
        deg = float(deg)
        cans = deg*9
        cans = cans/5
        cans = cans+32
        # (32°F − 32) × 5 / 9 = 0°C
        # (0°C × 9/5) + 32 = 32°F
        await message.channel.send(embed=discord.Embed(title=f"{deg} Degrees = {cans} Farenheit", color=0x05FCE2))

    if message.content.find("a/ cel-kel ") != -1 or message.content.find("a/cel-kel ") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        kelf = message.content.split(" ")[-1]
        kelf = float(kelf)
        cans = kelf+273
        await message.channel.send(embed=discord.Embed(title=f"{kelf} Degrees = {cans} Kelvin", color=0x05FCE2))

    if message.content.find("a/ far-kel ") != -1 or message.content.find("a/far-kel ") != -1:
        far = message.content.split(" ")[-1]
        far = float(far)
        cans = far - 32
        cans = cans * 5
        cans = cans / 9
        cans = cans+273
        # (32°F − 32) × 5 / 9 = 0°C
        # (0°C × 9/5) + 32 = 32°F
        await message.channel.send(embed=discord.Embed(title=f"{far} Farenheit = {cans} Kelvin", color=0x05FCE2))

# EMBED CREATOR
    if (message.content.find("a/ embed") !=-1 or message.content.find("a/ embed") !=-1) and (message.content != "a/ embed help" and message.content != "a/ help embed"):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        til = ""
        dess = ""
        if message.author.guild_permissions.manage_messages:
            tef = r"\n"
            mos = await message.channel.send(embed=discord.Embed(title="Embed Creation Wizard", description=f"Enter a title {message.author.mention}\nEnter `none` if you don't want a title.\nMake sure you reade the embed help menu using `a/ embed help` for some cool features and avoid bugs", color=0x05FCE2))
            def check(m):
                return m.channel == message.channel and m.author == message.author
            combtil = ""
            combdes = ""
            try:
                til = await client.wait_for('message', timeout=30.0, check=check)
                til = str(til.content)
                newtil = til.split(r"\n")
                for i in range(0, len(newtil)):
                    combtil += f"{newtil[i]}\n"
                if til == "none" or til == "None":
                    combtil = None
            except asyncio.TimeoutError:
                await mos.edit(embed=discord.Embed(title="**YOU TOOK TOO LONG**\nNow atleast enter a description!", color=0xFD7803))

            def checkw(m):
                return m.channel == message.channel and m.author == message.author

            try:
                await message.channel.send(embed=discord.Embed(title=f"Now Enter a Description for the embed", color=0x05FCE2))
                dess = await client.wait_for('message', timeout=30.0, check=checkw)
                dess = str(dess.content)
                newdes = dess.split(r"\n")
                for i in range(0, len(newdes)):
                    combdes += f"{newdes[i]}\n"
                if dess == "none" or dess == "None":
                    desstil = None
                embee = discord.Embed(title=f"{combtil}", description=f"{combdes}", color=0x05FCE2)
                embee.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
                await message.channel.send(embed=embee)
            except asyncio.TimeoutError:
                await mos.edit(embed=discord.Embed(title="**YOU TOOK TOO LONG**", color=0xFD7803))
        else:
            await message.channel.send(embed=discord.Embed(title="You Don't have Permission to Manage Messages <a:ag_exc:781410611366985748>", color=0xFC4905))

# Data Save


# Ticketing

    # await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)

    if (message.content.startswith("a/ create ticket") or message.content.startswith("a/ new ticket") or message.content.startswith("a/new ticket") or message.content.startswith("a/ticket new") or message.content.startswith("a/ ticket new")) and message.content != "a/ ticket create":
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        srlst = collection.find_one({"_id" : 1341})
        if int(message.guild.id) in srlst["ids"]:
            edsf = await message.channel.send(embed=discord.Embed(title="<a:ag_ldingwin:781410586138902529> Creating...", color=0x05FCE2))
            tickid = randata()
            tiiid = tickid
            tickid = f"ticket-{tickid}"
            overwrites = {
                message.guild.default_role: discord.PermissionOverwrite(read_messages=False)
            }
            ochan = await message.guild.create_text_channel(f'{tickid}', overwrites=overwrites, category=client.get_channel(message.channel.category.id))
            await ochan.set_permissions(message.author, read_messages=True, send_messages=True)
            try:
                roledic = collection.find_one({"_id": int(message.guild.id)})
                rolelst = roledic["ticketroleid"]
                for i in range(0, len(rolelst)):
                    roleid = rolelst[i]
                    roleid = int(roleid)
                    print(rolelst)
                    print(roleid)
                    role = message.guild.get_role(roleid)
                    await ochan.set_permissions(role, read_messages=True, send_messages=True)
            except Exception as e:
                print(e)
            lstrrr = srlst["chan"]
            lstrrr.append(int(ochan.id))
            collection.update_one({"_id":1341}, {"$set":{"chan":lstrrr}})
            tickde = discord.Embed(title=f"Created! <a:ag_tickop:781395575962599445>", description=f"Here: {ochan.mention}", color=0x2AE717)
            tickde.set_footer(text=f"Requested by: {message.author}", icon_url=f"{message.author.avatar_url}")
            try:
                tickrsn = fetch_data(message.content)
            except:
                tickrsn = "None"
            await ochan.send(embed=discord.Embed(title=f"Ticket-{tiiid}", description=f"__Created by__: **{message.author}**\n__Reason__: **{tickrsn}**", color=0x2AE717))
            await edsf.edit(embed=tickde)
        else:
            await message.channel.send(embed=discord.Embed(title="This server has not enabled Ticketing System", description="To enable use `a/ ticket help`", color=0x2AE717))

    if message.content == "a/ close" or message.content == "a/close":
        vars = collection.find_one({"_id":1341})
        vers = vars["chan"]
        if int(message.channel.id) in vers:
            vers.remove(int(message.channel.id))
            collection.update_one({"_id":1341}, {"$set":{"chan":vers}})
            await message.channel.delete()

    if message.content == "a/ close all" or message.content == "a/close all":
        if message.author.guild_permissions.manage_channels:
            clsallmsg = await message.channel.send(embed=discord.Embed(title=f"<a:ag_ldingwin:781410586138902529> Deleteing all created tickets...", description=f"Requested by: {message.author.mention}", color=0x2AE717))
            vars = collection.find_one({"_id": 1341})
            vers = vars["chan"]
            for dh in message.guild.channels:
                if int(dh.id) in vers:
                    await dh.delete()
            await clsallmsg.edit(embed=discord.Embed(title="All Tickets Closed (Deleted) <a:ag_tickop:781395575962599445>", description=f"Requested by: {message.author.mention}", color=0x2AE717))
        else:
            await message.channel.send(embed=discord.Embed(title="You Don't have Permission to Manage Channels <a:ag_exc:781410611366985748>", color=0xFC4905))

# Google search
    if message.content.startswith('a/ google') or message.content.startswith('a/google'):
        if message.content != 'a/ google' or message.content != 'a/ google help' or message.content != 'a/ help google' or message.content != 'a/google' or message.content != 'a/google help' or message.content != 'a/help google':
            ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
            edglm = await message.channel.send(embed=discord.Embed(title="Searching... <a:ag_ldingwin:781410586138902529>", color=0x09BEFC))
            searchContent = ""
            text = str(message.content).split(' ')
            for i in range(2, len(text)):
                searchContent = searchContent + text[i]
            for j in search(searchContent, tld="co.in", num=1, stop=1, pause=4):
                await edglm.delete()
                await message.channel.send(j)

# YT Search
    if (message.content.startswith("a/yt") or message.content.startswith("a/youtube") or message.content.startswith("a/ yt") or message.content.startswith("a/ youtube")) and (not message.content.startswith("a/ ytcomment") and not message.content.startswith("a/ytcomment")):
        try:
            if message.content == "a/yt " or message.content == "a/yt" or message.content == "a/youtube " or message.content == "a/youtube" or message.content == "a/ yt " or message.content == "a/ yt" or message.content == "a/ youtube " or message.content == "a/ youtube":
                await message.channel.send("Make sure you enter a term to search the youtube!")
            else:
                srch = fetch_data(message.content)
                url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=20&q={srch}&type=video&key=AIzaSyARxYh8cdcmHJrEIZ_Ppmphaz6AwgHDWCs'
                response = json.loads(requests.get(url).content)
                res = response["items"]
                res = res[0]
                snpt = res["snippet"]
                yttitle = snpt["title"]
                ytpubt = snpt["publishedAt"]
                ytdesc = snpt["description"]
                tn = snpt["thumbnails"]
                tn = tn["medium"]
                ytthnb = tn["url"]
                ytchan = snpt["channelTitle"]
                vid = res["id"]
                vid = vid["videoId"]
                vidlnk = f"https://www.youtube.com/watch?v={vid}"
                ytmbd = discord.Embed(title=f"{yttitle}", description=f"Video Description: {ytdesc}\n\nUploaed By: {ytchan}\n\nPublished At: {ytpubt}\n", color=0xF7341C)
                ytmbd.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
                ytmbd.set_image(url=ytthnb)
                ytmbd.set_thumbnail(url="https://pngimg.com/uploads/youtube/youtube_PNG13.png")
                await message.channel.send(embed=ytmbd)
        except Exception as e:
            await message.channel.send(embed=discord.Embed(title="An error Occurred", description="If this occurs again and again Please Report this to the [Support Server](https://discord.gg/teszgSR9yK)", color=0xFF4900))

# SUGGEST
    if message.content.startswith("a/ suggest ") or message.content.startswith("a/suggest "):
        ncmnda()
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        sugg = fetch_data(message.content)
        await message.channel.send(embed=discord.Embed(title=" <a:ag_reddot:781410740619051008> Suggested! <a:ag_reddot:781410740619051008> ", description="Thanks for Your Valuable Suggestion!\nYour Suggestion Has Been Submitted! <a:ag_tickop:781395575962599445> ", color=0x04FD03))
        channel = client.get_channel(784697044236763176)
        sogs = await channel.send(embed=discord.Embed(title=f" <a:ag_reddot:781410740619051008> Suggestion by :**{message.author}** From **{message.guild}** <a:ag_reddot:781410740619051008> ", description=f"`{sugg}`", color=0x04FD03))
        await sogs.add_reaction('👍')
        await sogs.add_reaction('👎')

# add word
    if message.content.startswith("a/ badword ") or message.content.startswith("a/badword "):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.author.guild_permissions.manage_messages:
            gid = int(message.guild.id)
            fin = collection.find_one({"_id": gid})
            if fin == None:
                collection.insert({"_id": gid, "chatmod": 1, "badwords": [], "moddel": 0})
                wordb = fetch_data(message.content)
                fina = collection.find_one({"_id":gid})
                fina = fina["badwords"]
                fina.append(wordb)
                collection.update_one({"_id": gid}, {"$set": {"badwords":fina}})
                await message.channel.send(embed=discord.Embed(title="Bad word Added and Chat Moderation Enabled", description="Chat in this Server **WILL** be moderated with a warn message for the words you have added using `a/ badword =<badword>`\nIf you want to Delete AND Warn pls type `a/ set delmod true`\n For more use `a/ mod help` or `a/ set help`", color=0x2AE717))
            else:
                wordb = fetch_data(message.content)
                fina = collection.find_one({"_id": gid})
                fina = fina["badwords"]
                fina.append(wordb)
                collection.update_one({"_id": gid}, {"$set": {"badwords": fina, "chatmod":1}})
                await message.channel.send(embed=discord.Embed(title="Bad word Added", description="Members will be warned on using the blacklisted words. If you want to Delete AND Warn For using Blacklisted words pls type `a/ set delmod true`\nIf Done already pls Ignore\n For more use `a/ mod help` or `a/ set help`", color=0x2AE717))
        else:
            await message.channel.send(embed=discord.Embed(title="You Don't have Permission to Manage Messages <a:ag_exc:781410611366985748>", color=0xFC4905))

    if message.content == ("a/ badword defaults") or message.content == ("a/ badwords defaults") or message.content == ("a/ badwords defaults") or message.content == ("a/ badwords default") or message.content == ("a/ badword default") or message.content == ("a/badword defaults") or message.content == ("a/badwords defaults") or message.content == ("a/badwords defaults") or message.content == ("a/badwords default") or message.content == ("a/badword default"):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.author.guild_permissions.manage_messages:
            gid = int(message.guild.id)
            fin = collection.find_one({"_id": gid})
            if fin == None:
                collection.insert({"_id": gid, "chatmod": 1, "badwords": [], "moddel": 0})
                fina = collection.find_one({"_id":gid})
                fina = fina["badwords"]
                for i in badwrds:
                    fina.append(i)
                collection.update_one({"_id": gid}, {"$set": {"badwords":fina}})
                await message.channel.send(embed=discord.Embed(title="Default Bad words Added and Chat Moderation Enabled", description="Chat in this Server **WILL** be moderated with a warn message for the words you have added using `a/ badword =<badword>`\nIf you want to Delete AND Warn pls type `a/ set delmod true`\nIf Done already pls Ignore\n For more use `a/ mod help` or `a/ set help`", color=0x2AE717))
            else:
                fina = fin["badwords"]
                for i in badwrds:
                    fina.append(i)
                collection.update_one({"_id": gid}, {"$set": {"chatmod": 1, "moddel": 0, "badwords":fina}})
                await message.channel.send(embed=discord.Embed(title="Default Bad words Added", description="Chat in this Server **WILL** be Moderated with a Warn message for the words you have added using `a/ badword =<badword>`\nIf Done already pls Ignore\nIf you want to Delete AND Warn pls type `a/ set delmod true`\nIf Done already pls Ignore\nFor more use `a/ mod help` or `a/ set help`", color=0x2AE717))
        else:
            await message.channel.send(embed=discord.Embed(title="You Don't have Permission to Manage Messages <a:ag_exc:781410611366985748>", color=0xFC4905))

    if message.content.startswith("a/ badword remove ") or message.content.startswith("a/ remove badword ") or message.content.startswith("a/ remove badword ") or message.content.startswith("a/ badword remove"):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.author.guild_permissions.manage_messages:
            gid = int(message.guild.id)
            fin = collection.find_one({"_id": gid})
            if fin == None:
                await message.channel.send(embed=discord.Embed(title="NO Badwords Found", description="Pls add using `a/ badword =<badword>` or `a/ badword default` to add default words\nIf you want to Delete AND Warn for using blacklisted words pls type `a/ set delmod true`\n For more use `a/ mod help` or `a/ set help`", color=0x2AE717))
            else:
                wordb = fetch_data(message.content)
                wordblst = wordb.split(" ")
                wordb = ""
                for i in range(1,len(wordblst)):
                    ietjwieji = wordblst[i]
                    wordb += f"{ietjwieji} "
                fina = collection.find_one({"_id": gid})
                fina = fina["badwords"]
                for i in range(0,len(fina)):
                    if fina[i] == wordb:
                        asfdaf = fina.pop(i)
                        collection.update_one({"_id": gid}, {"$set": {"badwords": fina}})
                await message.channel.send(embed=discord.Embed(title="Bad word Removed", description="Members will be warned on using the blacklisted words. If you want to Delete AND Warn For using Blacklisted words pls type `a/ set delmod true`\nIf Done already pls Ignore\n For more use `a/ mod help` or `a/ set help`", color=0x2AE717))
        else:
            await message.channel.send(embed=discord.Embed(title="You Don't have Permission to Manage Messages <a:ag_exc:781410611366985748>", color=0xFC4905))

    if message.content == ("a/ badword list") or message.content == ("a/ badwords list") or message.content == ("a/badword list") or message.content == ("a/badwords list"):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.author.guild_permissions.manage_messages:
            gid = int(message.guild.id)
            fin = collection.find_one({"_id": gid})
            if fin == None:
                await message.channel.send(embed=discord.Embed(title="Chat Modearation Disabled and No Badwords Found !!", description="Enable using `a/ chatmod true`\n For more use `a/ mod help` or `a/ set help`", color=0xFF6602))
            elif fin["badwords"] == mtlist:
                await message.channel.send(embed=discord.Embed(title="Chat Modearation Enabled BUT NO Badwords Found !!", description="Pls add using `a/ badword=<badword>` or load defaults using `a/ badword default`\n For more use `a/ mod help` or `a/ set help`", color=0xFF6602))
            else:
                await message.channel.send(embed=discord.Embed(title="This may Expose **NFSW** content You sure?",description="If yes React with :thumbsup: within 20 sec\nYou can delete them using `a/ delete help`", color=0xFF6602))

                def checkc(reaction, user):
                    return user == message.author and str(reaction.emoji) == '👍'

                try:
                    reaction, user = await client.wait_for('reaction_add', timeout=30.0, check=checkc)
                    fin = fin["badwords"]
                    await message.channel.send(":underage: List of Blacklisted Words of this server :underage:")
                    for i in fin:
                        await message.channel.send(embed=discord.Embed(description=f"{i}", color=0xFD8805))
                except asyncio.TimeoutError:
                    print("rcn timeout")
        else:
            await message.channel.send(embed=discord.Embed(title="You Don't have Permission to Manage Messages <a:ag_exc:781410611366985748>", color=0xFC4905))

    if message.content == "a/ badwords clear" or message.content == "a/ clear badwords" or message.content == "a/badwords clear" or message.content == "a/clear badwords":
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.author.guild_permissions.manage_messages:
            gid = int(message.guild.id)
            fin = collection.find_one({"_id": gid})
            if fin == None:
                await message.channel.send(embed=discord.Embed(title="NO Badwords Found", description="Pls add using `a/ badword =<badword>` or `a/ badword default` to add default words\nIf you want to Delete AND Warn for using blacklisted words pls type `a/ set delmod true`\n For more use `a/ mod help` or `a/ set help`", color=0x2AE717))
            else:
                fina = collection.find_one({"_id": gid})
                fina = fina["badwords"]
                collection.update_one({"_id": gid}, {"$set": {"badwords": []}})
                await message.channel.send(embed=discord.Embed(title="Bad words Cleared", description="Members will be warned on using the blacklisted words. If you want to Delete AND Warn For using Blacklisted words pls type `a/ set delmod true`\nIf Done already pls Ignore\n For more use `a/ mod help` or `a/ set help`", color=0x2AE717))
        else:
            await message.channel.send(embed=discord.Embed(title="You Don't have Permission to Manage Messages <a:ag_exc:781410611366985748>", color=0xFC4905))

# MSG DELETE
    if message.content.startswith("a/ delete ") or message.content.startswith("a/delete ") or message.content.startswith("a/purge ") or message.content.startswith("a/ purge "):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.author.guild_permissions.manage_messages:
            try:
                delee = 0
                delee = message.content.split(' ')[-1]
                delee = int(delee)
                delee = delee + 1
                await message.channel.purge(limit=delee)
                delmss = await message.channel.send(embed=discord.Embed(title=f"{delee-1} Messages :x: Deleted! <a:ag_tickop:781395575962599445>", description=f"Requested By {message.author}", color=0xFD3A01))
                await asyncio.sleep(2)
            except:
                await message.reply("Message Count Must be a number not a word or letter!")
            await delmss.delete()
        else:
            await message.channel.send(embed=discord.Embed(title="You Don't have Permission to Manage Messages <a:ag_exc:781410611366985748>", color=0xFC4905))

# POLL
    if message.content.find("a/ poll ") !=-1 or message.content.find("a/ poll1 ") != -1 or message.content.find("a/poll ") !=-1 or message.content.find("a/poll1 ") != -1:
        po = fetch_data(message.content)
        pollmbd = discord.Embed(title=f"{po}", color=0xFD3A01)
        pollmbd.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
        pola = await message.channel.send(embed=pollmbd)
        await pola.add_reaction('👍')
        await pola.add_reaction('👎')

    if message.content.find("a/poll2 ") != -1 or message.content.find("a/ poll2 ") != -1:
        po = fetch_data(message.content)
        pollmbd = discord.Embed(title=f"{po}", color=0xFD3A01)
        pollmbd.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
        pola = await message.channel.send(embed=pollmbd)
        await pola.add_reaction('<:ag_upvote:816330395506180107>')
        await pola.add_reaction('<:ag_downvote:816330463937167391>')

# RANDOMS
    if message.content.find("a/ random") != -1 or message.content.find("a/random") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.content == "a/ random":
            await message.channel.send(embed=discord.Embed(title="Syntax Error <a:ag_exc:781410611366985748>", description="Usage Syntax:\n`a/ random <number of options>`\n**Example:**\n`a/ random 5`\n For more help: `a/ random help`", color=0xFCBC05))
        if message.content.find("a/ random ") != -1:
            randgi = message.content.split(' ')[-1]
            randgi = int(randgi)
            rando = random.randint(1, randgi)
            await message.channel.send(embed=discord.Embed(title=f"{rando}", description=f"The Random Outcome of {randgi} Numbers", color=0x48FC05))

# QUZZZZ
    if message.content == ("a/ quiz start") != -1 or message.content == ("a/quiz start") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="**INVALID SYNTAX**", description="Syntax: `a/ quiz start <level> <topic id>`\nExample: `a/ quiz start 2 12` (Topic id is optional)", color=0xFC0505))

    if message.content.startswith("a/ quiz start ") or message.content.startswith("a/quiz start "):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        diffc = message.content.split(" ")[-2]
        cat = 9
        try:
            cata = message.content.split(" ")[-1]
            if cata == "1":
                cat = "9"
            elif cata == "2":
                cat = "10"
            elif cata == "3":
                cat = "11"
            elif cata == "4":
                cat = "12"
            elif cata == "5":
                cat = "13"
            elif cata == "6":
                cat = "14"
            elif cata == "7":
                cat = "15"
            elif cata == "8":
                cat = "16"
            elif cata == "9":
                cat = "17"
            elif cata == "10":
                cat = "18"
            elif cata == "11":
                cat = "19"
            elif cata == "12":
                cat = "20"
            elif cata == "13":
                cat = "21"
            elif cata == "14":
                cat = "22"
            elif cata == "15":
                cat = "23"
            elif cata == "16":
                cat = "24"
            elif cata == "17":
                cat = "25"
            elif cata == "18":
                cat = "26"
            elif cata == "19":
                cat = "27"
            elif cata == "20":
                cat = "28"
            elif cata == "21":
                cat = "29"
            elif cata == "22":
                cat = "30"
            elif cata == "23":
                cat = "31"
            elif cata == "24":
                cat = "32"
        except Exception as e:
            print("no topic given")
        diff = 'easy'
        if diffc == "2":
            diff = 'medium'
        elif diffc == "3":
            diff = 'hard'
        topm = 1
        rp = 0
        while topm == 1:
            topm = 0
            mos = await message.channel.send(embed=discord.Embed(title="Question in 2 secs!!", color=0xFDFC03))
            await asyncio.sleep(1)
            url = f"https://opentdb.com/api.php?amount=1&category={cat}&difficulty={diff}&type=boolean"
            data = json.loads(requests.get(url).content)
            # data = {"response_code":0,"results":[{"category":"General Knowledge","type":"boolean","difficulty":"easy","question":"On average, at least 1 person is killed by a drunk driver in the United States every hour.","correct_answer":"True","incorrect_answers":["False"]}]}
            # data = {"response_code":0,"results":[{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"An eggplant is a vegetable.","correct_answer":"False","incorrect_answers":["True"]}]}
            topic = data["results"]
            topic = topic[0]
            topic = topic["category"]
            ques = data["results"]
            ques = ques[0]
            ques = ques["question"]
            cora = data["results"]
            cora = cora[0]
            cora = cora["correct_answer"]
            if cora == "True":
                cora = "true"
                nocora = "false"
            elif cora == "False":
                cora = "false"
                nocora = "true"
            print(cora)
            channel = message.channel
            ques = ques.replace("&quote;", "`")
            await mos.edit(embed=discord.Embed(title=f"**Question 1 ({topic})**", description=f"**{ques}**\n\n**Give Your Answer within 10s as**\na/ true or a/ false", color=0xFD7803))
            def check(m):
                return m.channel == channel and m.content.lower() in ["a/ true", "a/ false"]

            try:
                msg = await client.wait_for('message', timeout=20.0, check=check)
                if msg.content.lower() == f"a/ {cora}":
                    await msg.add_reaction('✅')
                    await mos.edit(embed=discord.Embed(title="**CORRECT**", description=f"Answer Given By:{msg.author}\n\nReact with :thumbsup: For next Question", color=0x01FD14))
                    await mos.add_reaction('👍')
                else:
                    await msg.add_reaction('❌')
                    await mos.edit(embed=discord.Embed(title="**WRONG**", description=f"Answer Given By:{msg.author}\n\nReact with :thumbsup: For next Question", color=0xFC4905))
                    await mos.add_reaction('👍')
            except asyncio.TimeoutError:
                await mos.edit(embed=discord.Embed(title="**YOU TOOK TOO LONG**", description="Time to answer : 20s\n\nReact with :thumbsup: For next Question", color=0xFD7803))
                await mos.add_reaction('👍')

            channel = message.channel

            def checkb(reaction, user):
                return user == message.author and str(reaction.emoji) == '👍'

            try:
                reaction, user = await client.wait_for('reaction_add', timeout=30.0, check=checkb)
            except asyncio.TimeoutError:
                print("rcn timeout")
            else:
                topm = 1

# SAY
    if message.content.startswith("a/ say ") or message.content.startswith("a/ say "):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        saymsg = fetch_data(message.content)
        await message.channel.send(embed=discord.Embed(title=f"{saymsg}", description=f"Asked to Say By: {message.author}", color=0x02BDFE))

    if message.content.startswith("a/ delsay ") or message.content.startswith("a/delsay "):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        delsay = fetch_data(message.content)
        await message.delete()
        await message.channel.send(embed=discord.Embed(title=f"{delsay}", description=f"Asked to Delete and Say By: {message.author}", color=0x02BDFE))

    if message.content.startswith("a/ op say ") and int(message.author.id) == 782624720989585409:
        temsay = fetch_data(message.content)
        await message.channel.send(temsay)

# MEMES
    if message.content == ("a/ meme") or message.content == ("a/meme"):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        try:
            whilego = 1
            while whilego == 1:
                memesrt = random.choice(["meme", "dankmeme", "PhoenixSC"])
                memeurl = f"https://meme-api.herokuapp.com/gimme/{memesrt}"
                memedata = json.loads(requests.get(memeurl).content)
                if (str(memedata["nsfw"]) == "false") or (str(memedata["nsfw"]) == "False"):
                    whilego = 0
            memetxt = memedata["title"]
            memeurl = memedata["url"]
            memembd = discord.Embed(title=f"{memetxt}", description=f"Neither Asteroid nor its Developers make, promote, endorse or take responsibility for the content shown. The content must be taken only in the perspective of humor. If any unwanted or NSFW content is shown please forgive us and click the 🗑️ reaction to delete this msg. For complaints you may create a ticket in our [Support Server](https://discord.gg/teszgSR9yK)", color=0x00A6FF)
            image_url = f"{memeurl}"
            nname = randata()
            save_name = f'./imgcache/image{nname}.png'
            urllib.request.urlretrieve(image_url, save_name)
            file = discord.File(save_name, filename=f"image{nname}.png")
            memembd.set_image(url=f"attachment://image{nname}.png")
            memembd.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
            await message.channel.send(file=file, embed=memembd)
            await asyncio.sleep(1)
            if os.path.exists(save_name):
                os.remove(save_name)
        except Exception as e:
            print(e)
            await message.channel.send(embed=discord.Embed(title="An error Occurred", description="If this occures again and again Please Report this to the [Support Server](https://discord.gg/teszgSR9yK)", color=0xFF4900))

    if message.content == ("a/ meme mc") or message.content == ("a/meme mc") or message.content == ("a/ mc meme") or message.content == ("a/mc meme"):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        try:
            whilego = 1
            while whilego == 1:
                memesrt = random.choice(["PhoenixSC"])
                memeurl = f"https://meme-api.herokuapp.com/gimme/{memesrt}"
                memedata = json.loads(requests.get(memeurl).content)
                if (str(memedata["nsfw"]) == "false") or (str(memedata["nsfw"]) == "False"):
                    whilego = 0
                memetxt = memedata["title"]
                memeurl = memedata["url"]
                memembd = discord.Embed(title=f"{memetxt}", description=f"Neither Asteroid nor its Developers make, promote, endorse or take responsibility for the content shown. The content must be taken only in the perspective of humor. If any unwanted or NSFW content is shown please forgive us and click the 🗑️ reaction to delete this msg. For complaints you may create a ticket in our [Support Server](https://discord.gg/teszgSR9yK)", color=0x00A6FF)
                image_url = f"{memeurl}"
                nname = randata()
                save_name = f'./imgcache/image{nname}.png'
                urllib.request.urlretrieve(image_url, save_name)
                file = discord.File(save_name, filename=f"image{nname}.png")
                memembd.set_image(url=f"attachment://image{nname}.png")
                memembd.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
                await message.channel.send(file=file, embed=memembd)
                await asyncio.sleep(1)
                if os.path.exists(save_name):
                    os.remove(save_name)
        except Exception as e:
            print(e)
            await message.channel.send(embed=discord.Embed(title="An error Occurred", description="If this occures again and again Please Report this to the [Support Server](https://discord.gg/teszgSR9yK)", color=0xFF4900))

# Reddit Search

    if message.content.startswith("a/ reddit") or message.content.startswith("a/reddit"):
        if message.content == ("a/ reddit") or message.content == ("a/reddit") or message.content == ("a/ reddit ") or message.content == ("a/reddit "):
            await message.channel.send("Make sure you enter a subreddit to search!")
        else:
            ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
            try:
                subre = fetch_data("message.content")
                whilego = 1
                while whilego == 1:
                    memesrt = random.choice([f"{subre}"])
                    memeurl = f"https://meme-api.herokuapp.com/gimme/{memesrt}"
                    memedata = json.loads(requests.get(memeurl).content)
                    if (str(memedata["nsfw"]) == "false") or (str(memedata["nsfw"]) == "False"):
                        whilego = 0
                memetxt = memedata["title"]
                memeurl = memedata["url"]
                memembd = discord.Embed(title=f"SubReddit: {subre}" , description=f"{memetxt}", color=0x00A6FF)
                memembd.set_image(url=f"{memeurl}")
                memembd.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
                mememsg = await message.channel.send(embed=memembd)
            except Exception as e:
                await message.channel.send(embed=discord.Embed(title="An error Occurred", description=f"Your Requested SubReddit **{subre}** is not found!\n If you are sure **{subre}** Exists then if this occures again and again Please Report this to the [Support Server](https://discord.gg/teszgSR9yK)", color=0xFF4900))

# CHAT

    chnlfile = open("chatchannellist.dat", "rb")
    try:
        chtchnlids = pplpcl.load(chnlfile)
    except Exception as e:
        print(e)
    chnlfile.close()

    if int(message.channel.id) in chtchnlids or str(message.channel.id) in chtchnlids:
        with message.channel.typing():
            bwordic = {"wechat": "Yes we chat!", "scmaster": "What do you mean?", "name": "My name is Asteroid! Hope you Already knew that!", "master": "My master is Vignesh_x64ᴰᵉᵛ#8351", "location": "https://asteroidbot.xyz", "email":"Why do you want my email?", "company": "The Asteroid Comapany LOL", "build": f"Asteroid Version {version}"}
            inggg = 1
            if message.content in bwordic:
                inggg = 0
                await message.reply(f"{bwordic[message.content]}")
            if message.content.find("&") != -1 or message.content.find("version") != -1:
                await message.content.send(f"Asteroid Version {version}")
                inggg = 0
            if inggg == 1:
                chaturl = f"http://api.brainshop.ai/get?bid=156189&key=ecd0iMK2fXNDloqw&uid=ecd0iMK2fXNDloqw&msg={message.content}"
                chatdata = json.loads(requests.get(chaturl).content)
                chatmsg = chatdata["cnt"]
                await message.reply(f"{chatmsg}")

    if message.content.find("a/ beat") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send("<a:ag_pprbt:781410629180194826>")
    if message.content.find("a/ twirl") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send("<a:twirl:781410568657043506>")
    if message.content.find("a/ kasa") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send("<:ag_ks:781410607672852500>")
    if message.content.find("a/ mind") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send("<:ag_mind:781410713981288468>")
    if message.content.find("a/ tnt") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send("<:ag_tnt:781395412648460288>")
    if message.content.find("bigfan") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send("<:bigfan:781410551016062987>")
    if message.content == ("a/ op") or message.content == ("a/op") or message.content == ("a/ OP") :
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send("<:ag_op:781395451492302859>")
    if message.content == ("a/ gg") or message.content == ("a/gg") or message.content == ("a/ GG"):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send("<:ag_GG:781410564839964672>")

# Joke

    if message.content.startswith("a/joke") or message.content.startswith("a/ joke"):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        try:
            jkfile = open("jokes.json", "r")
            jklst = json.load(jkfile)
            jkfile.close()
            jkid = random.randint(0, len(jklst) - 1)
            jkdic = jklst[jkid]
            jkid = jkdic["id"]
            jktyp = jkdic["type"]
            jk = jkdic["setup"]
            jkans = jkdic["punchline"]
            await message.channel.send(embed=discord.Embed(title=f"{jk}", description=f"|| {jkans} ||\n**ID: {jkid}**\nIf you find any inappropriate or unwanted or offensive or nsfw content above just remember the joke ID(Joke ID: **{jkid}**) and please send it to us using a suggestion(`a/ suggest help`) or a message in our [Support Server](https://discord.gg/teszgSR9yK) and that joke will be removed and you will be rewarded AstroCash. Sorry for the inconvenience.", color=0x02BDFE))
        except Exception as e:
            await message.channel.send(embed=discord.Embed(title="An error Occured", description="If this occurs again and again Please Report To our [Support Server](https://discord.gg/teszgSR9yK)", color=0xFF4900))
            jkfile.close()
            print(e)

# IMGENS

    if message.content.startswith('a/rainbow') or message.content.startswith('a/ rainbow'):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        try:
            imgenuser = message.mentions[0]
            imgenimg = message.mentions[0].avatar_url_as(format=None, static_format='png', size=1024)
        except:
            imgenuser = message.author
            imgenimg = message.author.avatar_url_as(format=None, static_format='png', size=1024)
        rnbombd = discord.Embed(title=f"{imgenuser}'s Rainbowed Avatar!", color=0xDFFF00)
        image_url = f"https://some-random-api.ml/canvas/gay?key={srakey}&avatar={imgenimg}"
        nname = randata()
        save_name = f'./imgcache/image{nname}.png'
        urllib.request.urlretrieve(image_url, save_name)
        file = discord.File(save_name, filename=f"image{nname}.png")
        rnbombd.set_image(url=f"attachment://image{nname}.png")
        rnbombd.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
        await message.channel.send(file=file, embed=rnbombd)
        await asyncio.sleep(1)
        if os.path.exists(save_name):
            os.remove(save_name)

    if message.content.startswith('a/glass') or message.content.startswith('a/ glass'):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        try:
            imgenuser = message.mentions[0]
            imgenimg = message.mentions[0].avatar_url_as(format=None, static_format='png', size=1024)
        except:
            imgenuser = message.author
            imgenimg = message.author.avatar_url_as(format=None, static_format='png', size=1024)
        rnbombd = discord.Embed(title=f"{imgenuser}'s Glazed Avatar!")
        image_url = f"https://some-random-api.ml/canvas/glass?key={srakey}&avatar={imgenimg}"
        nname = randata()
        save_name = f'./imgcache/image{nname}.png'
        urllib.request.urlretrieve(image_url, save_name)
        file = discord.File(save_name, filename=f"image{nname}.png")
        rnbombd.set_image(url=f"attachment://image{nname}.png")
        rnbombd.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
        await message.channel.send(file=file, embed=rnbombd)
        await asyncio.sleep(1)
        if os.path.exists(save_name):
            os.remove(save_name)

    if message.content.startswith('a/wasted') or message.content.startswith('a/ wasted'):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        try:
            imgenuser = message.mentions[0]
            imgenimg = message.mentions[0].avatar_url_as(format=None, static_format='png', size=1024)
        except:
            imgenuser = message.author
            imgenimg = message.author.avatar_url_as(format=None, static_format='png', size=1024)
        rnbombd = discord.Embed(title=f"{imgenuser}'s Wasted Avatar!")
        image_url = f"https://some-random-api.ml/canvas/wasted?key={srakey}&avatar={imgenimg}"
        nname = randata()
        save_name = f'./imgcache/image{nname}.png'
        urllib.request.urlretrieve(image_url, save_name)
        file = discord.File(save_name, filename=f"image{nname}.png")
        rnbombd.set_image(url=f"attachment://image{nname}.png")
        rnbombd.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
        await message.channel.send(file=file, embed=rnbombd)
        await asyncio.sleep(1)
        if os.path.exists(save_name):
            os.remove(save_name)

    if message.content.startswith('a/triggered') or message.content.startswith('a/ triggered') or message.content.startswith('a/trigger') or message.content.startswith('a/ trigger'):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        try:
            imgenuser = message.mentions[0]
            imgenimg = message.mentions[0].avatar_url_as(format=None, static_format='png', size=1024)
        except:
            imgenuser = message.author
            imgenimg = message.author.avatar_url_as(format=None, static_format='png', size=1024)
        rnbombd = discord.Embed(title=f"{imgenuser}'s Triggered Avatar!")
        image_url = f"https://some-random-api.ml/canvas/triggered?key={srakey}&avatar={imgenimg}"
        nname = randata()
        save_name = f'./imgcache/image{nname}.png'
        urllib.request.urlretrieve(image_url, save_name)
        file = discord.File(save_name, filename=f"image{nname}.png")
        rnbombd.set_image(url=f"attachment://image{nname}.png")
        rnbombd.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
        await message.channel.send(file=file, embed=rnbombd)
        await asyncio.sleep(1)
        if os.path.exists(save_name):
            os.remove(save_name)

    if message.content.startswith('a/bw') or message.content.startswith('a/ bw') or message.content.startswith('a/greyscale') or message.content.startswith('a/ greyscale'):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        try:
            imgenuser = message.mentions[0]
            imgenimg = message.mentions[0].avatar_url_as(format=None, static_format='png', size=1024)
        except:
            imgenuser = message.author
            imgenimg = message.author.avatar_url_as(format=None, static_format='png', size=1024)
        rnbombd = discord.Embed(title=f"{imgenuser}'s Black n White Avatar!")
        image_url = f"https://some-random-api.ml/canvas/gay?key={srakey}&greyscale={imgenimg}"
        nname = randata()
        save_name = f'./imgcache/image{nname}.png'
        urllib.request.urlretrieve(image_url, save_name)
        file = discord.File(save_name, filename=f"image{nname}.png")
        rnbombd.set_image(url=f"attachment://image{nname}.png")
        rnbombd.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
        await message.channel.send(file=file, embed=rnbombd)
        await asyncio.sleep(1)
        if os.path.exists(save_name):
            os.remove(save_name)

    if message.content.startswith('a/invert') or message.content.startswith('a/ invert'):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        try:
            imgenuser = message.mentions[0]
            imgenimg = message.mentions[0].avatar_url_as(format=None, static_format='png', size=1024)
        except:
            imgenuser = message.author
            imgenimg = message.author.avatar_url_as(format=None, static_format='png', size=1024)
        rnbombd = discord.Embed(title=f"{imgenuser}'s Inverted Avatar!")
        image_url = f"https://some-random-api.ml/canvas/invert?key={srakey}&avatar={imgenimg}"
        nname = randata()
        save_name = f'./imgcache/image{nname}.png'
        urllib.request.urlretrieve(image_url, save_name)
        file = discord.File(save_name, filename=f"image{nname}.png")
        rnbombd.set_image(url=f"attachment://image{nname}.png")
        rnbombd.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
        await message.channel.send(file=file, embed=rnbombd)
        await asyncio.sleep(1)
        if os.path.exists(save_name):
            os.remove(save_name)

    if message.content.startswith('a/bright') or message.content.startswith('a/ bright'):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        try:
            imgenuser = message.mentions[0]
            imgenimg = message.mentions[0].avatar_url_as(format=None, static_format='png', size=1024)
        except:
            imgenuser = message.author
            imgenimg = message.author.avatar_url_as(format=None, static_format='png', size=1024)
        rnbombd = discord.Embed(title=f"{imgenuser}'s Bightened Avatar!")
        image_url = f"https://some-random-api.ml/canvas/brightness?key={srakey}&avatar={imgenimg}"
        nname = randata()
        save_name = f'./imgcache/image{nname}.png'
        urllib.request.urlretrieve(image_url, save_name)
        file = discord.File(save_name, filename=f"image{nname}.png")
        rnbombd.set_image(url=f"attachment://image{nname}.png")
        rnbombd.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
        await message.channel.send(file=file, embed=rnbombd)
        await asyncio.sleep(1)
        if os.path.exists(save_name):
            os.remove(save_name)

    if message.content.startswith('a/sepia') or message.content.startswith('a/ sepia'):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        try:
            imgenuser = message.mentions[0]
            imgenimg = message.mentions[0].avatar_url_as(format=None, static_format='png', size=1024)
        except:
            imgenuser = message.author
            imgenimg = message.author.avatar_url_as(format=None, static_format='png', size=1024)
        rnbombd = discord.Embed(title=f"{imgenuser}'s Sepia Avatar!")
        image_url = f"https://some-random-api.ml/canvas/sepia?key={srakey}&avatar={imgenimg}"
        nname = randata()
        save_name = f'./imgcache/image{nname}.png'
        urllib.request.urlretrieve(image_url, save_name)
        file = discord.File(save_name, filename=f"image{nname}.png")
        rnbombd.set_image(url=f"attachment://image{nname}.png")
        rnbombd.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
        await message.channel.send(file=file, embed=rnbombd)
        await asyncio.sleep(1)
        if os.path.exists(save_name):
            os.remove(save_name)

    if message.content.startswith('a/red') or message.content.startswith('a/ red'):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        try:
            imgenuser = message.mentions[0]
            imgenimg = message.mentions[0].avatar_url_as(format=None, static_format='png', size=1024)
        except:
            imgenuser = message.author
            imgenimg = message.author.avatar_url_as(format=None, static_format='png', size=1024)
        rnbombd = discord.Embed(title=f"{imgenuser}'s Red Avatar!")
        image_url = f"https://some-random-api.ml/canvas/red?key={srakey}&avatar={imgenimg}"
        nname = randata()
        save_name = f'./imgcache/image{nname}.png'
        urllib.request.urlretrieve(image_url, save_name)
        file = discord.File(save_name, filename=f"image{nname}.png")
        rnbombd.set_image(url=f"attachment://image{nname}.png")
        rnbombd.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
        await message.channel.send(file=file, embed=rnbombd)
        await asyncio.sleep(1)
        if os.path.exists(save_name):
            os.remove(save_name)

    if message.content.startswith('a/green') or message.content.startswith('a/ green'):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        try:
            imgenuser = message.mentions[0]
            imgenimg = message.mentions[0].avatar_url_as(format=None, static_format='png', size=1024)
        except:
            imgenuser = message.author
            imgenimg = message.author.avatar_url_as(format=None, static_format='png', size=1024)
        rnbombd = discord.Embed(title=f"{imgenuser}'s Green Avatar!")
        image_url = f"https://some-random-api.ml/canvas/green?key={srakey}&avatar={imgenimg}"
        nname = randata()
        save_name = f'./imgcache/image{nname}.png'
        urllib.request.urlretrieve(image_url, save_name)
        file = discord.File(save_name, filename=f"image{nname}.png")
        rnbombd.set_image(url=f"attachment://image{nname}.png")
        rnbombd.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
        await message.channel.send(file=file, embed=rnbombd)
        await asyncio.sleep(1)
        if os.path.exists(save_name):
            os.remove(save_name)

    if message.content.startswith('a/blue') or message.content.startswith('a/ blue'):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        try:
            imgenuser = message.mentions[0]
            imgenimg = message.mentions[0].avatar_url_as(format=None, static_format='png', size=1024)
        except:
            imgenuser = message.author
            imgenimg = message.author.avatar_url_as(format=None, static_format='png', size=1024)
        rnbombd = discord.Embed(title=f"{imgenuser}'s Blue Avatar!")
        image_url = f"https://some-random-api.ml/canvas/blue?key={srakey}&avatar={imgenimg}"
        nname = randata()
        save_name = f'./imgcache/image{nname}.png'
        urllib.request.urlretrieve(image_url, save_name)
        file = discord.File(save_name, filename=f"image{nname}.png")
        rnbombd.set_image(url=f"attachment://image{nname}.png")
        rnbombd.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
        await message.channel.send(file=file, embed=rnbombd)
        await asyncio.sleep(1)
        if os.path.exists(save_name):
            os.remove(save_name)

    if message.content.startswith('a/avatar') or message.content.startswith('a/ avatar'):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        try:
            imgenuser = message.mentions[0]
            imgenimg = message.mentions[0].avatar_url_as(format=None, static_format='png', size=1024)
        except:
            imgenuser = message.author
            imgenimg = message.author.avatar_url_as(format=None, static_format='png', size=1024)
        rnbombd = discord.Embed(title=f"{imgenuser}'s Avatar!")
        rnbombd.set_image(url=f"{imgenimg}")
        rnbombd.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
        await message.channel.send(embed=rnbombd)

    if message.content.startswith('a/pixel') or message.content.startswith('a/ pixel'):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        try:
            imgenuser = message.mentions[0]
            imgenimg = message.mentions[0].avatar_url_as(format=None, static_format='png', size=1024)
        except:
            imgenuser = message.author
            imgenimg = message.author.avatar_url_as(format=None, static_format='png', size=1024)
        rnbombd = discord.Embed(title=f"{imgenuser}'s Pixelated Avatar!")
        image_url = f"https://some-random-api.ml/canvas/pixelate?key={srakey}&avatar={imgenimg}"
        nname = randata()
        save_name = f'./imgcache/image{nname}.png'
        urllib.request.urlretrieve(image_url, save_name)
        file = discord.File(save_name, filename=f"image{nname}.png")
        rnbombd.set_image(url=f"attachment://image{nname}.png")
        rnbombd.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
        await message.channel.send(file=file, embed=rnbombd)
        await asyncio.sleep(1)
        if os.path.exists(save_name):
            os.remove(save_name)

    if message.content.startswith('a/threshold') or message.content.startswith('a/ threshold'):
        try:
            imgenuser = message.mentions[0]
            imgenimg = message.mentions[0].avatar_url_as(format=None, static_format='png', size=1024)
        except:
            imgenuser = message.author
            imgenimg = message.author.avatar_url_as(format=None, static_format='png', size=1024)
        rnbombd = discord.Embed(title=f"{imgenuser}'s Rainbowed Avatar!")
        image_url = f"https://some-random-api.ml/canvas/threshold?key={srakey}&avatar={imgenimg}"
        nname = randata()
        save_name = f'./imgcache/image{nname}.png'
        urllib.request.urlretrieve(image_url, save_name)
        file = discord.File(save_name, filename=f"image{nname}.png")
        rnbombd.set_image(url=f"attachment://image{nname}.png")
        rnbombd.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
        await message.channel.send(file=file, embed=rnbombd)
        await asyncio.sleep(1)
        if os.path.exists(save_name):
            os.remove(save_name)

    if message.content.startswith('a/ytcomment') or message.content.startswith('a/ ytcomment'):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        try:
            imgencnt = fetch_data(message.content)
            imgenuser = message.author.name
            imgenimg = message.author.avatar_url_as(format=None, static_format='png', size=1024)
        except:
            imgenuser = message.author.name
            imgenimg = message.author.avatar_url_as(format=None, static_format='png', size=1024)
        rnbombd = discord.Embed(title=f"{imgenuser}'s Youtube Comment!")
        image_url = f"https://some-random-api.ml/canvas/youtube-comment?key={srakey}&avatar={imgenimg}&username={imgenuser}&comment={imgencnt}"
        nname = randata()
        save_name = f'./imgcache/image{nname}.png'
        urllib.request.urlretrieve(image_url, save_name)
        file = discord.File(save_name, filename=f"image{nname}.png")
        rnbombd.set_image(url=f"attachment://image{nname}.png")
        rnbombd.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
        await message.channel.send(file=file, embed=rnbombd)
        await asyncio.sleep(1)
        if os.path.exists(save_name):
            os.remove(save_name)

# premium
#     QR code, or quick response code, is a trademark for a type of 2 dimensional barcode. 2 dimensional barcodes are similar to one dimensional barcodes, but can store more information per unit area.

# QR Code
    if (message.content.startswith("a/qr") or message.content.startswith("a/ qr")) and not (message.content.startswith("a/qrread") or message.content.startswith("a/ qrread") or message.content.startswith("a/qread") or message.content.startswith("a/ qread")):
        ncmnda()
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        qrdata = fetch_data(message.content)
        qrmsg = await message.channel.send(embed=discord.Embed(title="Generating... <a:ag_ldingwin:781410586138902529>", color=0x09BEFC))
        try:
            Logo = Image.open(r'./astersmall.jpg')
            qr = qrcode.QRCode(
                version=12,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=1
            )
            qr.add_data(f"{qrdata}")
            img_qr_big = qr.make_image(fill_color="black", back_color="white").convert('RGB')
            pos = ((img_qr_big.size[0] - Logo.size[0]) // 2, (img_qr_big.size[1] - Logo.size[1]) // 2)
            img_qr_big.paste(Logo, pos)
            nname = randata()
            save_name = f'./imgcache/image{nname}.png'
            img_qr_big.save(f'{save_name}')
            filee = discord.File(save_name, filename=f"image{nname}.png")
            qrmbd = discord.Embed(title=f"QR Code for **{qrdata}**", color=0x09BEFC)
            qrmbd.set_image(url=f"attachment://image{nname}.png")
            qrmbd.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
            await qrmsg.delete()
            await message.channel.send(file=filee, embed=qrmbd)
            await asyncio.sleep(1)
            if os.path.exists(save_name):
                os.remove(save_name)
        except Exception as e:
            print(e)
            await qrmsg.edit(embed=discord.Embed(title="An error Occured", description="If this occurs again and again Please Report To our [Support Server](https://discord.gg/teszgSR9yK)", color=0xFF4900))

#     if message.content.startswith("a/qrread") or message.content.startswith("a/ qrread") or message.content.startswith("a/qread") or message.content.startswith("a/ qread") or message.content.startswith("a/readqr") or message.content.startswith("a/ readqr"):
#         ncmnda()
#         await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
#         qrmsg = await message.channel.send(embed=discord.Embed(title="Decoding... <a:ag_ldingwin:781410586138902529>", color=0x09BEFC))
#         try:
#             qrurl = message.attachments[0].url
#         except:
#             try:
#                 qrurl = fetch_data(message.content)
#             except:
#                 await qrmsg.edit(embed=discord.Embed(title="An error Occured", description="If this occures again and again Please Report To our [Support Server](https://discord.gg/teszgSR9yK)", color=0xFF4900))
#         if qrurl.startswith("https://") or qrurl.startswith("http://"):
#             image_url = f"{qrurl}"
#             nname = randata()
#             save_name = f'./imgcache/image{nname}.png'
#             try:
#                 req = urllib.request.Request(f'{qrurl}')
#                 req.add_header('User-Agent', 'Mozilla/5.0')
#                 image_64_encode = urllib.request.urlopen(req).read()
#                 qrimage = Image.open(io.BytesIO(image_64_encode))
#                 qrimage.save(f"{save_name}")
#                 qrdata = pyzbar.pyzbar.decode(Image.open(f'./imgcache/image{nname}.png'))
#                 print(qrdata)
#                 try:
#                     if os.path.exists(save_name):
#                         os.remove(save_name)
#                 except:
#                     pass
#                 if len(qrdata) < 1:
#                     await qrmsg.edit(embed=discord.Embed(title="Failed to detect QR Code in given image", color=0xFF4900))
#                 else:
#                     qrmaind = qrdata[0]
#                     qrmaind = str(qrmaind[0])
#                     qrmaind = qrmaind.split(r"'")[1]
#                     qrtyp = qrmaind[1]
#                     qrmbd = discord.Embed(title="QR & BarCode Reader", description=f"__Type:__: {qrtyp} \nImage Link: [Click Here]({qrurl}) \nDecoded Message: {qrmaind}", color=0x09BEFC)
#                     qrmbd.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
#                     await qrmsg.edit(embed=qrmbd)
#             except Exception as e:
#                 print(e)
#                 await qrmsg.edit(embed=discord.Embed(title="An error Occured", description="If this occures again and again Please Report To our [Support Server](https://discord.gg/teszgSR9yK)", color=0xFF4900))
#                 try:
#                     if os.path.exists(save_name):
#                         os.remove(save_name)
#                 except:
#                     pass
#         else:
#             await qrmsg.edit(embed=discord.Embed(title="Invalid Image Link", description="If you feel this must be a mistake, please report this to [Support Server](https://discord.gg/teszgSR9yK)", color=0xFF4900))

# Lyrics

    if message.content.startswith('a/lyric') or message.content.startswith('a/ lyric'):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        lyrmsg = await message.channel.send(embed=discord.Embed(title="Searching... <a:ag_ldingwin:781410586138902529>", color=0x09BEFC))
        lyrsrch = fetch_data(message.content)
        if lyrsrch == None:
            await lyrmsg.edit(embed=discord.Embed(title="Enter a song Name!", description="Make sure you enter a song name to search for Lyrics!"))
        else:
            try:
                lyr_url = f"https://some-random-api.ml/lyrics?key={srakey}&title={lyrsrch}"
                lyraw = json.loads(requests.get(lyr_url).content)
                try:
                    lyraw["error"]
                    await lyrmsg.edit(embed=discord.Embed(title=f"Sorry I could not find **{lyrsrch}**'s Lyrics", color=0xF88409))
                    print(lyraw)
                except:
                    lyrt = lyraw["title"]
                    lyrr = lyraw["lyrics"]
                    lyrauth = lyraw["author"]
                    lyrth = lyraw["thumbnail"]
                    lyrthumb = lyrth["genius"]
                    lyrmbd = discord.Embed(title=f"{lyrt}", description=f"__Author:__ {lyrauth} \n__Lyrics:__\n {lyrr}", color=0x0BFAA3)
                    lyrmbd.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
                    lyrmbd.set_thumbnail(url=f"{lyrthumb}")
                    await lyrmsg.edit(embed=lyrmbd)
            except Exception as e:
                print(e)
                await lyrmsg.edit(embed=discord.Embed(title="An error Occured", description="If this occures again and again Please Report To our [Support Server](https://discord.gg/teszgSR9yK)", color=0xFF4900))

#     https: // translate.googleapis.com / translate_a / single?client = gtx & sl =$ta & tl =$en & dt = t & ie = UTF - 8 & oe = UTF - 8 & q =$hi

# github
    if message.content.startswith("a/github") or message.content.startswith("a/ github"):
        try:
            ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
            gitsrch = fetch_data(message.content)
            git_url = f"https://api.github.com/users/{gitsrch}"
            gitfo = json.loads(requests.get(git_url).content)
            try:
                afuhauhdf = gitfo["message"]
                await message.channel.send("Not found")
            except:
                uname = gitfo["login"]
                id = gitfo["id"]
                gitav = gitfo["avatar_url"]
                giturl = gitfo["html_url"]
                follower = gitfo["followers"]
                following = gitfo["following"]
                naame = gitfo["name"]
                comp = gitfo["company"]
                wesite = gitfo["blog"]
                locat = gitfo["location"]
                bio = gitfo["bio"]
                pub_repo = gitfo["public_repos"]
                pub_gist = gitfo["public_gists"]
                gitbed = discord.Embed(title=f"**{uname}**'s GitHub Account", description=f"__Details:__\nUsername: {uname} \nName: {naame} \nCompany: {comp} \nWebsite: {wesite} \nLocation: {locat} \nRepositories: {pub_repo} \nGists: {pub_gist} \nID: {id} \nFollowers: {follower} \nFollowing: {following} \nBio: {bio} \n\n__Links:__ \n[Profile]({giturl}) \n [Avatar]({gitav})", color=0x00A6FF)
                gitbed.set_thumbnail(url=f"{gitav}")
                gitbed.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
                await message.channel.send(embed=gitbed)
        except Exception as e:
            print(e)
            await message.channel.send(embed=discord.Embed(title="An error Occured", description="If this occures again and again Please Report To our [Support Server](https://discord.gg/teszgSR9yK)", color=0xFF4900))

# Playstore

    if message.content.startswith("a/playstore") or message.content.startswith("a/ playstore") or message.content.startswith("a/ googleplay") or message.content.startswith("a/googleplay"):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        try:
            playmsg = await message.channel.send(embed=discord.Embed(title="Searching... <a:ag_ldingwin:781410586138902529>", color=0x09BEFC))
            srch_term = fetch_data(message.content)
            app_lst = play_scraper.search(f'{srch_term}')
            app_one = app_lst[0]
            app_id = app_one["app_id"]
            app_data = google_play_scraper.app(f'{app_id}', lang='en', country='us')
            app_name = app_data["title"]
            app_dev = app_data["developer"]
            app_mail = app_data["developerEmail"]
            app_desc = app_data["description"]
            app_size = app_data["size"]
            app_summ = app_data["summary"]
            app_link = app_data["url"]
            app_ver = app_data["version"]
            app_photo = app_data["screenshots"]
            app_photo = app_photo[1]
            app_rate = app_data["score"]
            app_revs = app_data["reviews"]
            app_ratings = app_data["ratings"]
            app_date = app_data["released"]
            app_changes = app_data["recentChanges"]
            app_pp = app_data["privacyPolicy"]
            app_downs = app_data["installs"]
            app_inapp = app_data["inAppProductPrice"]
            app_icon = app_data["icon"]
            app_img = app_data["headerImage"]
            app_genre = app_data["genre"]
            app_ec = app_data["editorsChoice"]
            app_website = app_data["developerWebsite"]
            app_age = app_data["contentRating"]
            app_ads = app_data["containsAds"]
            app_android = app_data["androidVersionText"]
            if app_data["free"] == True:
                app_price = "Free"
            else:
                app_price = app_data["price"]
            app_desc = app_data["description"]
            app_rdesc = ""
            for ii in range(0,1000):
                app_rdesc += list(app_desc)[ii]

            playmbd = discord.Embed(title=f"{app_name}", description=f"Name: {app_name} \nPrice: {app_price} \nRating: {app_rate} \nTotal Ratings: {app_ratings} \nReviews: {app_revs}\nDeveloper: {app_dev} \nID: {app_id} \nSize: {app_size} \nDownloads: {app_downs} \nGenre: {app_genre} \nWebsite: {app_website} \n Android Version: {app_android} \nReleased on {app_date} \nContains Ads: {app_ads} \nContent Rating: {app_age} \nInApp Items: {app_inapp} \nEditor's Choice: {app_ec} \nMail: {app_mail} \nVersion: {app_ver} \n\nAbout: ```{app_summ}``` \nDescription: ```{app_rdesc}``` \nRecent Changes: ```{app_changes}```", color=0x0BFA19)
            try:
                playmbd.set_thumbnail(url=f"{app_icon}")
                playmbd.set_image(url=f"{app_img}")
            except:
                pass
            playmbd.set_footer(text=f"Requested by : {message.author}", icon_url=f"{message.author.avatar_url}")
            await playmsg.edit(embed=playmbd)
        except Exception as e:
            print(e)
            if str(e) == "list index out of range":
                try:
                    await playmsg.edit(embed=discord.Embed(title="Game Not found!", description="If you think this must not be happening then Please Report To our [Support Server](https://discord.gg/teszgSR9yK)", color=0xFF4900))
                except:
                    await message.channel.send(embed=discord.Embed(title="Game Not found!", description="If you think this must not be happening then Please Report To our [Support Server](https://discord.gg/teszgSR9yK)", color=0xFF4900))
            else:
                try:
                    await playmsg.edit(embed=discord.Embed(title="An error Occured", description="If this occures again and again Please Report To our [Support Server](https://discord.gg/teszgSR9yK)", color=0xFF4900))
                except:
                    await message.channel.send(embed=discord.Embed(title="An error Occured", description="If this occures again and again Please Report To our [Support Server](https://discord.gg/teszgSR9yK)", color=0xFF4900))


                    
    if message.content.startswith("a/ poker help"):
        gmhmbd = discord.Embed(title="Poker Night <:ag_poker:854976463962636339>", description="**Game Info:**\nDiscord Poker Night is a Texas hold 'em style game mode with up to 8 players total per game (you + 7 others) played right within a Discord voice channel. You can also have up to 17 additional spectators max.\n\n**Ingame Items:**\n__Poker Pass__:\nPrice: \nWith Nitro: $4.99\nWithout Nitro: $2.99\n__About:__ The Poker Pass is a one-time purchase that gives players special access to themes and customizations for your Poker experience with friends. Poker Pass does not impact the gameplay dynamics or add any value to the cartoon chips.\n\n**How to Play:**\nComming soon")
        gmhmbd.set_image(url="https://cdn.discordapp.com/attachments/829651215235153954/854972045905494046/pokerni8.png")
        await message.channel.send(embed=gmhmbd)

    if message.content.startswith("a/ party help") or message.content.startswith("a/party help") or message.content.startswith("a/help party") or message.content.startswith("a/ help party") or message.content.startswith("a/game") or message.content.startswith("a/ game"):
        gmhmbd = discord.Embed(title="Party Games!! <:ag_poker:854976463962636339>", description="__List of games:__\nPoker - `a/ poker start`\nChess -`a/ chess start` \nBetrayal.io `a/ betrayal start` \nFishington `a/ fishington start`\nYoutube Together - `a/ youtube start`\n__Rules:__\nYou should be on a PC version of Discord(Discord Limitation)\nMust join a voice channel.\n**Discord together does not load?** \n Sometimes Discord together does not load. To fix this go into settings and Authorised Apps. Then remove Youtube Together, Poker Night, CG 2 Dev, Betrayal.io, or Fishington.io. After that fully close and reopen Discord. This should fix the issue", color=0x00FFFB)
        await message.channel.send(embed=gmhmbd)
    
    if message.content.startswith("a/poker start") or message.content.startswith("a/ poker start") or message.content.startswith("a/start poker") or message.content.startswith("a/ start poker"):
        try:
            gmgo = 0
            try:
                gmchannel = message.author.voice.channel.id
                gmgo = 1
            except:
                await message.reply(embed=discord.Embed(title="Make sure you have joined a voice channel to Start The game!", color=0xFB1F1F))
            if gmgo == 1:
                gamelink = await togetherControl.create_link(gmchannel, 'poker')
                gamembd = discord.Embed(title="Poker Night <:ag_poker:854976463962636339>", description=f"**Steps to Start Poker:**\n:one: - All the players join a voice channel. \n:two: - [Click Here]({gamelink}) to Start the game!!\n:three: - Enjoy the game", color=0x8000FF)
                gamembd.set_footer(text="For How to Play and other info use a/ poker help", icon_url=f"{message.author.avatar_url}")
                gamembd.set_image(url="https://cdn.discordapp.com/attachments/829651215235153954/854972045905494046/pokerni8.png")
                await message.reply(embed=gamembd)
        except Exception as e:
            print(e)
            await message.reply(embed=discord.Embed(title="An error Occurred", description="If this occurs again and again Please Report to [Support Server](https://discord.gg/teszgSR9yK)", color=0xFB1F1F))

    if message.content.startswith("a/fishing start") or message.content.startswith("a/ fishing start") or message.content.startswith("a/start fishing") or message.content.startswith("a/ start fishing") or message.content.startswith("a/fishington start") or message.content.startswith("a/ fishington start") or message.content.startswith("a/start fishington") or message.content.startswith("a/ start fishington"):
        try:
            gmgo = 0
            try:
                gmchannel = message.author.voice.channel.id
                gmgo = 1
            except:
                await message.reply(embed=discord.Embed(title="Make sure you have joined a voice channel to Start The game!", color=0xFB1F1F))
            if gmgo == 1:
                gamelink = await togetherControl.create_link(gmchannel, 'fishing')
                gamembd = discord.Embed(title="Fishingtion :tropical_fish: ", description=f"**Steps to Start Fishington:**\n:one: - All the players join a voice channel. \n:two: - [Click Here]({gamelink}) to Start the game!!\n:three: - Enjoy the game", color=0x8000FF)
                gamembd.set_footer(text="For How to Play and other info use a/ fishington help", icon_url=f"{message.author.avatar_url}")
                gamembd.set_image(url="https://cdn.discordapp.com/attachments/829651215235153954/854972042637082634/fishington.jpg")
                await message.reply(embed=gamembd)
        except Exception as e:
            print(e)
            await message.reply(embed=discord.Embed(title="An error Occurred", description="If this occurs again and again Please Report to [Support Server](https://discord.gg/teszgSR9yK)", color=0xFB1F1F))

            
    if message.content.startswith("a/chess start") or message.content.startswith("a/ chess start") or message.content.startswith("a/start chess") or message.content.startswith("a/ start chess"):
        try:
            gmgo = 0
            try:
                gmchannel = message.author.voice.channel.id
                gmgo = 1
            except:
                await message.reply(embed=discord.Embed(title="Make sure you have joined a voice channel to Start The game!", color=0xFB1F1F))
            if gmgo == 1:
                gamelink = await togetherControl.create_link(gmchannel, 'chess')
                gamembd = discord.Embed(title="Chess <:ag_chess:854977611264032798>", description=f"**Steps to Start Chess:**\n:one: - All the players join a voice channel. \n:two: - [Click Here]({gamelink}) to Start the game!!\n:three: - Enjoy the game", color=0x8000FF)
                gamembd.set_footer(text="For How to Play and other info use `a/ chess help`", icon_url=f"{message.author.avatar_url}")
                gamembd.set_image(url="https://cdn.discordapp.com/attachments/829651215235153954/854975789890928670/chess.png")
                await message.reply(embed=gamembd)
        except Exception as e:
            print(e)
            await message.reply(embed=discord.Embed(title="An error Occurred", description="If this occurs again and again Please Report to [Support Server](https://discord.gg/teszgSR9yK)", color=0xFB1F1F))

    if message.content.startswith("a/betrayalio start") or message.content.startswith("a/ betrayalio start") or message.content.startswith("a/start betrayalio") or message.content.startswith("a/ start betrayalio") or message.content.startswith("a/betrayal.io start") or message.content.startswith("a/ betrayal.io start") or message.content.startswith("a/start betrayal.io") or message.content.startswith("a/ start betrayal.io") or message.content.startswith("a/betrayal start") or message.content.startswith("a/ betrayal start") or message.content.startswith("a/start betrayal") or message.content.startswith("a/ start betrayal"):
        try:
            gmgo = 0
            try:
                gmchannel = message.author.voice.channel.id
                gmgo = 1
            except:
                await message.reply(embed=discord.Embed(title="Make sure you have joined a voice channel to Start The game!", color=0xFB1F1F))
            if gmgo == 1:
                gamelink = await togetherControl.create_link(gmchannel, 'betrayal')
                gamembd = discord.Embed(title="Betrayal.io <:ag_betrayal:855368649682190367>", description=f"**Steps to Start Betrayal.io:**\n:one: - All the players join a voice channel. \n:two: - [Click Here]({gamelink}) to Start the game!!\n:three: - Enjoy the game", color=0x8000FF)
                gamembd.set_footer(text="For How to Play and other info use `a/ betrayalio help`", icon_url=f"{message.author.avatar_url}")
                gamembd.set_image(url="https://cdn.discordapp.com/attachments/829651215235153954/855367754269196328/co2hnz.png")
                await message.reply(embed=gamembd)
        except Exception as e:
            print(e)
            await message.reply(embed=discord.Embed(title="An error Occurred", description="If this occurs again and again Please Report to [Support Server](https://discord.gg/teszgSR9yK)", color=0xFB1F1F))

    if message.content.startswith("a/youtube start") or message.content.startswith("a/ youtube start") or message.content.startswith("a/start youtube") or message.content.startswith("a/ start youtube") or message.content.startswith("a/yt together start") or message.content.startswith("a/ yt together start") or message.content.startswith("a/start yt together") or message.content.startswith("a/ start yt together") or message.content.startswith("a/ytt start") or message.content.startswith("a/ ytt start") or message.content.startswith("a/start ytt") or message.content.startswith("a/ start ytt"):
        try:
            gmgo = 0
            try:
                gmchannel = message.author.voice.channel.id
                gmgo = 1
            except:
                await message.reply(embed=discord.Embed(title="Make sure you have joined a voice channel to Start The game!", color=0xFB1F1F))
            if gmgo == 1:
                gamelink = await togetherControl.create_link(gmchannel, 'youtube')
                gamembd = discord.Embed(title="Youtube Together <a:ag_youtubegif:855369950604951572>", description=f"**Steps to Start Youtube Together:**\n:one: - All the players join a voice channel. \n:two: - [Click Here]({gamelink}) to Start the game!!\n:three: - Enjoy the game", color=0x8000FF)
                gamembd.set_footer(text="For How to Use and other info use `a/ youtube help`", icon_url=f"{message.author.avatar_url}")
                gamembd.set_image(url="https://cdn.discordapp.com/attachments/829651215235153954/855371877127421952/ytparty.jpg")
                await message.reply(embed=gamembd)
        except Exception as e:
            print(e)
            await message.reply(embed=discord.Embed(title="An error Occurred", description="If this occurs again and again Please Report to [Support Server](https://discord.gg/teszgSR9yK)", color=0xFB1F1F))


    if message.content == "a/rrdc":
        try:
            vc = await message.guild.voice_client.disconnect()
        except:
            await message.reply(embed=discord.Embed(title="An error Occurred", description="If this occurs again and again Please Report to [Support Server](https://discord.gg/teszgSR9yK)", color=0xFB1F1F))

    if message.content == "a/rrdc":
        try:
            await message.author.voice.channel.connect()
        except:
            await message.reply(embed=discord.Embed(title="An Error Occurred", description="Are you Connected to a Voice Channel??\nIf this occurs again and again Please Report to [Support Server](https://discord.gg/teszgSR9yK)", color=0xFB1F1F))
                   
 # MISC
    if (message.content == ("a/ clear ram") or message.content == ("a/ clean ram")) and str(message.author.id) == "641305773095387156":
        gc.collect()
        await message.channel.send("RAM Cleared!")

    if message.content == "a/ logout" and str(message.author.id) == "641305773095387156":
        await message.reply("okk logging out :(")
        await client.close()

    if message.content == ("debugserverct asteroid"):
        tserver = len(client.guilds)
        await message.channel.send(f"srvr={tserver}")

    if (message.content.find("a/ member") != -1) or (message.content.find("a/member") != -1):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        servermem = message.guild.member_count
        await message.channel.send(embed=discord.Embed(title=f"{message.guild}", description=f"Number of Members: {servermem} <a:ag_reddot:781410740619051008>", color=0xFEE702))

    if message.content == ("a/ server") or message.content == "a/ servers":
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        tserver = len(client.guilds)
        await message.channel.send(embed=discord.Embed(title="Server Count", description=f"Serving {tserver} Servers <a:ag_tickop:781395575962599445> Now \nWOW!!!" , color=0x01FD59))

    if message.content.find("a/ serverid") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        tserverid = message.guild.id
        await message.channel.send(embed=discord.Embed(title=f"Server ID of {message.guild}", description=f"{tserverid} <a:ag_tickop:781395575962599445>", color=0x01FD59))

    # if message.content.startswith("a/") and ncmnd != 1:
    #         await message.channel.send(embed=discord.Embed(title="Command Not Found <a:ag_exc:781410611366985748>", description="If you feel this must be a mistake please report this to [Support Server](https://discord.gg/teszgSR9yK)", color=0xFB1F1F))

    if (message.content.find("a/ update") != -1) or (message.content.find("a/update") != -1):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="**v1.9 UPDATES !!**\nWebsite for Asteroid is out, Make sure you check it out!! ||[ https://asteroidbot.xyz ]||", description="<a:ag_arrowgif:781395494127271947> A dedicated website for Asteroid has been made with the help of *dchu096#3732* Try `a/ website`\n<a:ag_arrowgif:781395494127271947> Our new Support Email is created! For any enquires, suggestions, complaints etc etc please email us at: **support@asteroidbot.xyz**\n<a:ag_arrowgif:781395494127271947> One of The most awaited Feature AI Chat Is Added! Try `a/ chat help`\n<a:ag_arrowgif:781395494127271947> Added Party Games. Must Try!! `a/ game help`\n<a:ag_arrowgif:781395494127271947> Added QR Code Generator and QR cum BarCode Reader! Try: `a/ qr help`\n<a:ag_arrowgif:781395494127271947> Added Currency Converter Whose values are updated every 15 mins!! Try `a/ convert help`\n<a:ag_arrowgif:781395494127271947> Added a lot of Image generation Commands! Try `a/ imgen help`\n<a:ag_arrowgif:781395494127271947> Added Meme command! Try `a/ meme help`\n<a:ag_arrowgif:781395494127271947> Added YouTube Search! Try `a/ web help`\n<a:ag_arrowgif:781395494127271947> Added Lyrics Search! Try `a/ web help`\n<a:ag_arrowgif:781395494127271947> Added Image search! Try `a/ web help`\n<a:ag_arrowgif:781395494127271947> Added GitHub Account Details Fetcher! Try `a/ web help`\n<a:ag_arrowgif:781395494127271947> Added Reddit Fetcher Try `a/ web help`\n<a:ag_arrowgif:781395494127271947> Added a command to add role access to ticket channels. Try `a/ ticket help`\n<a:ag_arrowgif:781395494127271947> Removed the `=` sighn from all syntax!\n<a:ag_arrowgif:781395494127271947> Removed the space between `a/` and `command` from all the commands, if you find any roblems please report it :pray: \n<a:ag_arrowgif:781395494127271947> I might have missed out some feaures or updates, help msges etc as this update took some time, so please report if any problem if found or something goes missing :man_facepalming:\n\n<a:ag_arrowgif:781395494127271947> Major Bug Fixes :tools:\n\n<a:ag_arrowgif:781395494127271947> Use `a/ suggest help` To report bugs and give suggestions !! :pray:", color=0x05BAFD))

# TESTS
    if message.content.startswith("a/ testit") or message.content.startswith("a/testit"):
        await message.channel.send("click fast hmm",components = [Button(label = "Website", disabled=False, style=5, url="https://asteroidbot.xyz")])

# PING
    if message.content.find("a/ ping") != -1 or message.content.find("a/ uptime") != -1 or message.content.find("a/ping") != -1 or message.content.find("a/uptime") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        start = perf_counter()
        mesa = await message.channel.send(embed=discord.Embed(title="Pinging... <a:ag_ldingwin:781410586138902529>", description="May take some time..", color=0x09BEFC))
        end = perf_counter()
        duration = (end - start) * 1000
        duration = math.floor(duration)
        ping = client.latency
        ping = ping * 1000
        ping = math.floor(ping)
        startdb = perf_counter()
        pidic = collection.find_one({"_id":9999})
        pilist = pidic["ping"]
        ajz = 0
        if pilist == 0:
            ajz = 1
        elif pilist == 1:
            ajz = 0
        collection.update_one({"_id":9999}, {"$set":{"ping":ajz}})
        enddb = perf_counter()
        duradb = (enddb - startdb) * 1000
        duradb = duradb/2
        duradb = math.floor(duradb)
        startwiki = perf_counter()
        def woki_summary(argo):
            definii = wikipedia.summary(argo, sentences=5, chars=1000, auto_suggest=True, redirect=True)
            return definii
        word0s = str(randata())
        desco = woki_summary(word0s)
        endwiki = perf_counter()
        durawiki = (endwiki - startwiki) * 1000
        durawiki = math.floor(durawiki)
        startdic = perf_counter()
        url = "https://api.urbandictionary.com/v0/define?term=ping"
        response = json.loads(requests.get(url).content)
        enddic = perf_counter()
        duradic = (enddic - startdic) * 1000
        duradic = math.floor(duradic)
        startggl = perf_counter()
        searchCont = "asteroid"
        for j in search(searchCont, tld="co.in", num=1, stop=1, pause=4):
            print("hmm")
        endggl = perf_counter()
        duraggl = (endggl - startggl) * 1000
        duraggl = math.floor(duraggl)
        # enduptime = int(uptime.uptime())
        # uptimm = int(enduptime-strtuptime)
        # upsec = uptimm
        # upmin = 0
        # uphr = 0
        # upday = 0
        # if uptimm > 59:
        #     upsec = uptimm%60
        #     upmin = int(uptimm/60)
        #     if upmin > 60:
        #         upmin = int(upmin%60)
        #         uphr = int(upmin/60)
        #         if uphr > 24:
        #             uphr = uphr%24
        #             upday = int(uphr/24)
        await mesa.edit(embed=discord.Embed(title="Pings and Pongs <a:ag_ggl:781410701327335445>", description=f":alarm_clock: API Ping: {ping}ms\n:satellite: Latency: {duration}ms\n:hourglass: Total Ping: {ping+duration}ms\n<:ag_gglsym:817776047315091459> Google Ping: {duraggl}ms\n:card_box: DataBase Ping: {duradb}ms\n:scroll: Wikipedia Ping: {durawiki}ms\n<a:ag_book_pgs:781410721397080084> Dictionary Ping: {duradic}ms\n\nUptime: Error\nNode: US1", color=0x02BDFE))

# BAD WORD MODERATION
    gid = message.guild.id
    brds = collection.find_one({"_id":gid})
    if brds != None and brds["chatmod"] == 1:
        brdsa = brds["badwords"]
        for i in brdsa:
            i = i.lower()
            if message.content.find(i) != -1:
                print("A bad word(", message.content, ") was said by =>", message.author, "in channel |", message.channel, "in server =>", message.guild)
                if brds["moddel"] == 1:
                    await message.channel.purge(limit=1)
                await message.channel.send(embed=discord.Embed(title=" :x: **Bad Word Warning** :warning: ", description=f"{message.author}, Do NOT :x: Use Bad Words!, You Have been Warned :warning: ", color=0x04FD03))

# AFK Status
    donto = 0
    if message.content.startswith("a/ afk =") or message.content.startswith("a/ afk=") or message.content.startswith("a/afk =") or message.content.startswith("a/afk="):
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        fio = collection.find_one({"_id": 222})
        afkdic = fio["afkdic"]
        afkmsg = message.content.split('=')[-1]
        afkmens = message.author.id
        afkmens = f"<@!{afkmens}>"
        afkdic[afkmens] = afkmsg
        collection.update_one({"_id":222},{"$set":{"afkdic":afkdic}})
        donto = 1
        target = message.author
        try:
            # await target.edit(nick=f"[AFK] {message.author}")
            pass
        except Exception as e:
            await message.channel.send(embed=discord.Embed(title="<a:ag_exc:781410611366985748> Missing Permissions <a:ag_exc:781410611366985748>", description="Your AFK Status is set but Nickname Not changed\n__Possible Reason__:\n<a:ag_arrowgif:781395494127271947> I Don't have Manage Nickname Permissions\n<a:ag_arrowgif:781395494127271947> You have a Higher Role than Me\n<a:ag_arrowgif:781395494127271947> You have a loooong name!", color=0xFD4201))
        await message.channel.send(embed=discord.Embed(title="AFK Status Set! <a:ag_tickop:781395575962599445>", description=f"AFK status will be removed automatically in 1 day\n**Message From {afkmens} :**\n{afkmsg}", color=0xFBFE02))

    if message.content.find('<@!'):
        fio = collection.find_one({"_id": 222})
        afkdic = fio["afkdic"]

        for i in afkdic:
            k = list(i)
            teks = ""
            for j in k:
                if j == "0" or j == "1" or j == "2" or j == "3" or j == "4" or j == "5" or j == "6" or j == "7" or j == "8" or j == "9":
                    teks += j
            if int(message.author.id) == int(teks) and donto == 0:
                ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
                for jk in afkdic:
                    idh = message.author.id
                    idh = f"<@!{idh}>"
                    if idh == jk:
                        tempdis = afkdic
                        del tempdis[idh]
                        collection.update_one({"_id":222},{"$set":{"afkdic":tempdis}})
                        await message.channel.send(embed=discord.Embed(title="AFK Staus Removed! <a:ag_tickop:781395575962599445>", description=f"Afk Status For {i} is Removed", color=0x08FE73))

        for i in afkdic:
            if message.content.find(i) != -1:
                await message.channel.send(embed=discord.Embed(title="<a:ag_exc:781410611366985748> USER AFK <a:ag_exc:781410611366985748>", description=f"Do not Ping {i} <a:ag_pprbt:781410629180194826>\n**Message for U from {i}**\n{afkdic[i]}", color=0xFE0202))

    if message.content.find("a/ afk list") != -1:
        ncmnda(), await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        fio = collection.find_one({"_id": 222})
        afkdic = fio["afkdic"]
        nemaf = len(afkdic)
        afklos = afkdic.keys()
        await message.channel.send(embed=discord.Embed(title=f"AFK USERS LIST", description=f"{nemaf} Users Are AFK(Incl. of all my Servers)"))

    if message.content == "qwertyvignesh":
      await message.author.voice.channel.connect()
      await message.channel.send("done")
        
# Msg count
    try:
        try:
            message_count_file = open(f"message_count.txt", "r")
            message_count = message_count_file.readline()
            message_count_file.close()
        except:
            message_count_file.close()
        try:
            message_count_file = open(f"message_count.txt", "w")
            message_count_file.write(f"{int(message_count) + 1}")
            message_count_file.close()
        except:
            message_count_file.close()
    except:
        pass


client.loop.create_task(update_stats())

keep_alive()
client.run(toktok)
