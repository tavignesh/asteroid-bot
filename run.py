# google search
# image search

import discord
import time
import asyncio
import math
import random
import psutil
import json
import requests
import wikipedia
import datetime
import string
import pymongo
from pymongo import MongoClient
import bs4
import urllib
import urllib3

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

cluster = MongoClient("mongodb+srv://bot:1234@cluster0.5bkqm.mongodb.net/discord?retryWrites=true&w=majority")
db = cluster["discord"]
collection = db["bot"]

# TOKENS
token = "NzgwNDcyMDcwMDcyNjk2ODUy.X7vlQQ.Or3lU9RbeWevMYmK8nZiyXwjtuY"
# betatoken
# token = "NzgwNzM0MDYwMjQ2MDczMzc0.X7zZQQ.XO0sNCFFH5sXCo7ZMnRP87L3hWM"
wthapikey = "b79ac8eaa95ac8f6d9248eeee1fd3f08"
# ag srvr id      = 708329597141385229
# id support srvr = 780625655657791518

# user = message.mentions[0]
# user.send("Your message")
messages = joined = 0
mtlist = []

# PRE DECLARE
helpmbd = discord.Embed(title="**Hey,**\nI am **Asteroid** Made by:\n**『ȺG』*₊⋆》V!GПΣ$hᴰᵉᵛ♪ــﮩ.ﮩ٨ــ#5105**\nMy Prefix is `a/`\n▬▬▬▬▬▬▬▬▬▬\n Make sure to leave a space between `a/` and command\n▬▬▬▬▬▬▬▬▬▬", description="Use `a/ <module id> help` for More Info!\nIn the Place of <module id> put the text in (Brackets) After each Module\n\n**Modules** :control_knobs: \n▬▬▬▬▬▬▬▬▬▬\n<a:ag_arrowgif:781395494127271947> Moderati\
on :tools: (mod)\n<a:ag_arrowgif:781395494127271947> Invite <a:ag_flyn_hrts_red:781395643134115852>\n<a:ag_arrowgif:781395494127271947> Deletion :x: (delete)\n<a:ag_arrowgif:781395494127271947> Calculation :1234: (calculate)\n<a:ag_arrowgif:781395494127271947> TAX :ag_tax: (tax)\n<a:ag_arrowgif:781395494127271947> Say :love_letter: (say)\n<a:ag_arrowgif:781395494127271947> Random:game_die: (random)\n<a:ag_arrowgif:781395494127271947> Date Ti\
me etc :date: (today)\n<a:ag_arrowgif:781395494127271947> Weather :white_sun_rain_cloud: (weather)\n<a:ag_arrowgif:781395494127271947> Chat Beta :speech_balloon: (chat)\n<a:ag_arrowgif:781395494127271947> Poll  (poll)\n<a:ag_arrowgif:781395494127271947> Suggestion :pencil: (sugges\
t)\n<a:ag_arrowgif:781395494127271947> Wikipedia Search :mag: (wiki)\n<a:ag_arrowgif:781395494127271947> AFK :zzz: (afk)\n<a:ag_arrowgif:781395494127271947> Quizz :interrobang: (quiz)\n<a:ag_arrowgif:781395494127271947> My Statistics :level_slider: (stats)\n<a:ag_arrowgif:781395494127271947> Server Statistics :level_slider: (stats)\n▬▬▬▬▬▬▬▬▬▬\n**Example:**\n`a/ delete help`", color=0x01FD14)

invitembd = discord.Embed(title=" <a:ag_reddot:781410740619051008> **Usefull Links** <a:ag_reddot:781410740619051008> \n▬▬▬▬▬▬▬▬▬▬", description="<a:ag_arrowgif:781395494127271947> [Invite Me](https://discord.com/oauth2/authorize?client_id=780472070072696852&scope=bot&permissions=809500159) <a:ag_tickop:781395575962599445> \n<a:ag_arrowgif:781395494127271947> [VOTE ME](https://top.gg/bot/780472070072696852/vote)\n<a:ag_arrowgif:781395494127271947> [Support Server Beta](https://discord.gg/teszgSR9yK) <a:ag_discord:781395597277134869>\n<a:ag_arrowgif:781395494127271947> [ASTEROID GAMING](https://discord.gg/CjKRmV7ptm) <a:ag_discord:781395597277134869>", color=0x13FD03)

tstmbd = discord.Embed(title="Your title\n___________", description="Your description\ndescreption2", color=000000)

badwrds =                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ["fuck", "porn", "slut", "gangbang"]

rp = 0

@client.event
async def on_ready():
    if token == "NzgwNzM0MDYwMjQ2MDczMzc0.X7zZQQ.XO0sNCFFH5sXCo7ZMnRP87L3hWM":
        game = discord.Game("Having Fun Testing New Features")
        # await client.change_presence(status=discord.Status.idle, activity=game)
        # await client.change_presence(status=discord.Status.online, activity=game)
        # await client.change_presence(status=discord.Status.invisible, activity=game)
        await client.change_presence(status=discord.Status.do_not_disturb, activity=game)
    else:
        # game = discord.Game("With 『AG』》Vigne$hᴰᵉᵛ#8351 a/ help")
        game = discord.Game("Quiz, Ya its Ready !! Try a/ quiz help")
        await client.change_presence(status=discord.Status.idle, activity=game)
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
    global messages
    messages += 1
    ans = "none"
# serverid = client.get_guild(780625655657791518)

    chtchannel = ["❄》💬asteroid-chat"]
    a = 0
    rp = 0
    # if message.content.startswith("a/") :
    print("The Message | ", message.content, " | Was sent in | ", message.channel, " | Channel by | ", message.author, "| in SERVER =>", message.guild)

# CRIETERIA FILTER
    if message.author == client.user:
        return
    if message.author.bot:
        return

# HELPS
    if message.content.startswith("A/"):
        await message.channel.send(embed=discord.Embed(description="My prefix is `a/`", color=0x04FD03))
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
    if message.content == ("a/") or message.content == ("a/ "):
        await message.channel.send(embed=discord.Embed(title="Yes? , How May i Help You?",description=("Use `a/ help` for More!\n Make sure there is a space between `a/` and `help`"), color=0x04FD03))
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
    if message.content == "<@!780472070072696852>":
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(description="My prefix is `a/`", color=0x04FD03))
        # await message.channel.send(embed=discord.Embed(title="Check Your dms <a:ag_reddot:781410740619051008>", description="Hope they Are open For me!\nStill u can see the Help Message Here using `a/ help here'"))
    if message.content == "a/ help" or message.content == "a/help" or message.content == "A/help" or message.content == "A/ help":
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=helpmbd)
        userdm = client.get_user(message.author.id)
        await userdm.send(embed=helpmbd)
    if message.content.find("a/ invite") != -1 or message.content == "a/invite" or message.content == 'a/vote' or message.content == 'a/ vote':
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=invitembd)
    if message.content == "a/ delete" or message.content == "a/delete":
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(description="Use `a/ delete help` for Help Regarding Delete messges"))
    if message.content.startswith("a/ mod ") or message.content.startswith("a/mod"):
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title=":tools: Moderation <a:ag_book_pgs:769053582472642561>\n▬▬▬▬▬▬▬▬▬▬", description="All moderation Commands Needs You and Me to have Specific **Permissions** to perform Moderation!\n\n**Commands:**\n<a:ag_arrowgif:781395494127271947> <:ag_ban:774867115529469992> - `a/ ban <mention user>`\n<a:ag_arrowgif:781395494127271947> Kick - `a/ kick <mention user>`\n<a:ag_arrowgif:781395494127271947> Delete - Use `a/ delete help` For more!\n<a:ag_arrowgif:781395494127271947> Pls Use `a/ pref help` for Chat and BadWord (Customisable) Moderation\n<a:ag_arrowgif:781395494127271947> Member Count - `a/ members`", color=0xFDDE01))
    if message.content == "a/ delete help" or message.content == "a/ help delete":
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="**Delete Messages** :x:\n▬▬▬▬▬▬▬▬▬▬", description="Maximum of 500 Messages can be Deleted at a Time <a:ag_reddot:781410740619051008>\nYou need to Have Manage Messages Permisiion \n\nSyntax : `a/ delete <Number of msges in number>`\n\nExample:\n`a/ delete 15`", color=0x04FD03))
    if message.content == "a/ suggest help" or message.content == "a/ help suggest":
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="**Suggesions on Me** <a:ag_discord:781395597277134869> \n▬▬▬▬▬▬▬▬▬▬", description="Your Suggesions are Really Valuable to us(me) , It helps in Improving The Bot! <a:ag_reddot:781410740619051008> \n▬▬▬▬▬▬▬▬▬▬\n\nSyntax : `a/ suggest =<your suggesion>`\n\nExample:\n`a/ suggest =plz include multiplayer`",color=0x04FD03))
    if message.content == "a/ calculate help" or message.content == "a/ help calculate":
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="**Basic Calculator** :1234:\n▬▬▬▬▬▬▬▬▬▬", description="**Mathematical Operators**\n▬▬▬▬▬▬▬▬▬▬\n`add` => Addition\n `sub` => Subtraction\n `mult` => Multiplication \n `div` => Division\n\nSyntax: `a/ <mathamatical operator>  <1st number>  <2nd number>`\nExample : `a/ add 13 2`\n\n**LCM and HCF**\n▬▬▬▬▬▬▬▬▬▬\n`lcm` => Least Common Multiple\n `hcf` => Highest Common Factor\n\n**Complex Calculations**\n▬▬▬▬▬▬▬▬▬▬\n For More Use `a/ complexcal help`", color=0x05FCF1))
    if message.content == "a/ complexcal help" or message.content == "a/ help complexcal":
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="**Complex Calculation**:1234:\n▬▬▬▬▬▬▬▬▬▬", description="I can do a lot of **Complex Calculations**!\nThere are 2 types of Complex Calculations\n\n <a:ag_arrowgif:781395494127271947> Single input Calculation\nUse `a/ complexcal 1 help`\n\n <a:ag_arrowgif:781395494127271947> Double Input Calculation\n Use `a/ complexcal 2 help`", color=0xD705FC))
    if message.content == "a/ complexcal 1 help":
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="**Complex Calculator #1** :1234:\n▬▬▬▬▬▬▬▬▬▬", description="Single Input Functions\n All single Input variable = `a`\n▬▬▬▬▬▬▬▬▬▬\n`ceil` => Gives the Nearest Integer Greater than `a`\nExample: `a/ ceil 2.4` Gives `3`\n\n`pi` => Gives the Value of `Pi`\n`e` => Gives the Value of `e`\n\n\n`floor` => Gives the Nearest Integer\
         Lessser than `a`\nExample : `a/ floor 3.9` Gives `3`\n\n `sqrt` => Gives the Square Root of `a`\nExample : `a/ sqrt 9` Gives `3`\n\n `facto` => Gives the Factorial of `a`\nExample : `a/ facto 5` Gives `120`\n\n`exp` Gives the Value of `e^a`\nExample : `a/ exp 4` Gives `54.598150033144236`\n\n`log` => Gives the Natural Log of `a`\nExample : `a/ log 2` Gives `0.6931471805599453`\n\n`log10` => Gives the Log to the Base 10 of `a`\nExample : `a/ log10 2` Gives\
         `0.3010299956639812`\n\n`sin, cos, tan` => Gives the Trigonometric (sin or cos or tan as Specified) Values\nExample : `a/ sin 30` Gives `0.5`\n\nCommon\
         Syntax: `a/ <operator> <value(a)>`\n\n▬▬▬▬▬▬▬▬▬▬\n**More Calculations in `a/ complex 2 help`**\n\n If your Preffered Calculation is not available then plz Suggest using `a/ suggest help`", color=0xD705FC))
    if message.content == "a/ convert help" or message.content == "a/ help convert":
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="**Converter** :scales:\n▬▬▬▬▬▬▬▬▬▬", description="**Radians to Degrees**\nConverts `a` in Radians to Degrees\n Example : `a/ degrees 5` Gives `286.4788975654116`\n\n**Degrees to Radians**\nConverts `a` in Degrees to Radians\nExample : `a/ radians 90` Gives `1.5707963267948966`\n\n**Farenheit to Celcius**\nConverts Tempereture `a`\
        in Farenheit to Celcius\nExample : `a/ far 32` Gives `0`\n\n**Celcius to Farenheit**\nConverts Tempereture `a` in Celcius to Farenheit\nExample : `a/ cel 0` Gives `32`\n\n**Celcius to Kelvin**\nConverts Tempereture `a` in Celcius to Kelvin\nExample : `a/ cel 0` Gives `273`\n\n**Farenheit to Kelvin**\nConverts Tempereture `a` in Celcius to Farenheit\nExample : `a/ cel 0` Gives `32`", color=0xD705FC))
    if message.content == "a/ complexcal 2 help":
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="**Complex Calculator #2** :1234:\n▬▬▬▬▬▬▬▬▬▬", description="Single Input Functions\n All Double Input variable = `a` and `b`\n▬▬▬▬▬▬▬▬▬▬\n`bilog` => Gives the Value of Log `a` to the Base `b`\nExample: `a/ bilog 100 2` Gives `6.643856189774725`\n\n`pow` => Gives the Value of `a` to the Power `b`\nExample: `a/ pow 5 2` Gives `25`\n\n▬▬▬▬▬▬▬▬▬▬\n**TAX**\n`tax` => Gives tax amount and Amount after tax, `a` is tax% and `b` is amount\nExample: `a/ tax 12 1000`\n\n`danktax` => Gives tax that DankMemer(bot) put on transferres\nExample: `a/ danktax 150000`", color=0xD705FC))
    if message.content == "a/ afk help" or message.content == "a/ help afk" or message.content == "a/ afk" or message.content == "a/afk help":
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="AFK Status :zzz:\n▬▬▬▬▬▬▬▬▬▬", description="If u set afk status all the Messages tht Ping U will be Deleted :x: with a msg U gave!\n\n**Syntax:**\n<a:ag_arrowgif:781395494127271947> Set AFK - `a/ afk =<reason>`\n<a:ag_arrowgif:781395494127271947> Remove AFK - `a/ afk remove`", color=0xA205FC))
    if message.content == "a/ say help" or message.content == "a/ help say" or message.content == "a/ say":
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="SAY :speech_balloon: \n▬▬▬▬▬▬▬▬▬▬", description="This Command Makes Me to Say or Delete and Say What U say!!\n\n**Syntax:**\n`a/ say = <text>` or `a/ delsay = <text>`\n\n**Example:**\n`a/ say =text this you bot!`", color=0x4805FC))
    if message.content == "a/ random help" or message.content == "a/ help random":
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="Random :game_die: \n▬▬▬▬▬▬▬▬▬▬", description="This Chooses a number from 1 to `a` randomly.\n\n**Syntax:** \n`a/ random <Number>`\n\n**Example:**\n`a/ random 3`", color=0xFC058C))
    if message.content == 'a/ stats help' or message.content == "a/ help stats":
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="My Statistics :level_slider:\n▬▬▬▬▬▬▬▬▬", description="**Syntax**\n`a/ <id>` The `id` is in (brackets)\n\n**Commands**\n<a:ag_arrowgif:781395494127271947> Version Updates (updates)\n<a:ag_arrowgif:781395494127271947> CPU Usage (cpu)\n<a:ag_arrowgif:781395494127271947> Server Count (server)\n<a:ag_arrowgif:781395494127271947> My Ping or Latency (ping)\n<a:ag_arrowgif:781395494127271947> Server ID (serverid)\n\n**Example:**\n`a/ cpu`", color=0x04FD03))
    if message.content == "a/ setup chat":
        if message.author.guild_permissions.administrator:
            await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
            await message.guild.create_text_channel('❄》💬asteroid-chat')
            await message.channel.send(embed=discord.Embed(title="Chat Channel Created", description="You can Chat with Me in that channel without my Prefix!\n**NOTE!**: Chat is not ready", color=0x01FD14))
            await message.channel.send(embed=discord.Embed(title="<a:ag_exc:781410611366985748> Warning <a:ag_exc:781410611366985748>", description="DO NOT CHANGE NAME OF THE CHANNEL\nBut you Can Move It and Change Permissions", color=0x01FD14))
        else:
            await message.channel.send(embed=discord.Embed(title="You Don't have Permmission to Manage Channels <a:ag_exc:781410611366985748>"))
    if message.content.find("a/") != -1 and message.content.find("create") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="**『AG』》V!GNΣ$hᴰᵉᵛ#5105** <a:ag_flyn_hrts_cyn:781395468978356235>\nCreated me on 23th Nov 2020", description="**With The Help of:**\nRice Cake#9760\nLone#6015\nSUNAPANA™#3377",color=0x04FD03))
    if message.content.find("a/ chat help") != -1 or message.content == "a/ help chat":
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="CHAT :speech_balloon:\n▬▬▬▬▬▬▬▬▬▬", description="<a:ag_arrowgif:781395494127271947> `a/ setup chat` will Create a New Channel to Chat mith Meee!\n<a:ag_arrowgif:781395494127271947> <More To be added here>", color=0xFC058C))
    if message.content.find("a/ today help") != -1 or message.content == "a/ help today" or message.content.find("a/today help") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="Today :date:\n▬▬▬▬▬▬▬▬▬▬", description="**Commands:**\n<a:ag_arrowgif:781395494127271947> `a/ time` :clock3: Shows the Time Now\n<a:ag_arrowgif:781395494127271947> `a/ date` :date: Shows the Date Today\n<a:ag_arrowgif:781395494127271947> <More to be added here>", color=0x6E05FC))
    if message.content == "a/ wiki help" or message.content == "a/ help wiki" or message.content == "a/ wiki" or message.content == "a/wiki help":
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="Wikipedia Search :mag:\n▬▬▬▬▬▬▬▬▬▬", description="This commands Fetches Descreption about the Keyword you give.\n**Syntax:**\n`a/ wiki =keyword`\n\n**Example:**\n`a/ wiki =bot`", color=0x05B5FC))
    if message.content == "a/ help weather" or message.content == "a/ weather help" or message.content == "a/help weather":
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="Weather Reports\n▬▬▬▬▬▬▬▬▬▬", description="This Feature allows You to Get a weather Report Of your Preffered Location\n\n**Syntax:**\n`a/ weather =<location>`\n\n**Example:**\n`a/ weather =Chennai`", color=0x0527FC))
    if message.content == "a/ quiz help" or message.content == "a/quiz help":
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title=":speech_balloon: QUIZ <a:ag_book_pgs:769053582472642561>\n▬▬▬▬▬▬▬▬▬▬", description="Type `a/ quiz start <level> <topic id>`\n**For Topic ID Type** `a/ list topic` (Default - General Knowledge) \nLevels :\nEasy: 1\nMedium: 2\nHard: 3\nExample: `a/ quiz start 2`\nTo start a quiz and after answering react with a :thumbsup: for next question\nMark Counting Feature Under Development Sorry..", color=0xFDDE01))
    if message.content == "a/ list topic" or message.content == "a/ topic list" or message.content == "a/list topic":
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="**Topic List**", description="ID |       TOPIC\n1  <a:ag_arrw_hrt:781410692321640530> General Knowledge\n2  <a:ag_arrw_hrt:781410692321640530> Entertainment: Books\n3  <a:ag_arrw_hrt:781410692321640530> Entertainment: Film\n4  <a:ag_arrw_hrt:781410692321640530> Entertainment: Music\n5  <a:ag_arrw_hrt:781410692321640530> Entertainment: Musicals &\
         Theatres\n6  <a:ag_arrw_hrt:781410692321640530> Entertainment: Television\n7  <a:ag_arrw_hrt:781410692321640530> Entertainment: Video Games\n8  <a:ag_arrw_hrt:781410692321640530> Entertainment: Board Games\n9  <a:ag_arrw_hrt:781410692321640530> Science & Nature\n10 <a:ag_arrw_hrt:781410692321640530> Science: Computers\n11 <a:ag_arrw_hrt:781410692321640530> Science: Mathematics\n12\
          <a:ag_arrw_hrt:781410692321640530> Mythology\n13 <a:ag_arrw_hrt:781410692321640530> Sports\n14 <a:ag_arrw_hrt:781410692321640530> Geography\n15 <a:ag_arrw_hrt:781410692321640530> History\n16 <a:ag_arrw_hrt:781410692321640530> Politics\n17 <a:ag_arrw_hrt:781410692321640530> Art\n18 <a:ag_arrw_hrt:781410692321640530> Celebrities\n19 <a:ag_arrwhrt:781410692321640530> Animals\n20\
           <a:ag_arrw_hrt:781410692321640530> Vehicles\n21 <a:ag_arrw_hrt:781410692321640530> Entertainment: Comics\n22 <a:ag_arrw_hrt:781410692321640530> Science: Gadgets\n23 <a:ag_arrw_hrt:781410692321640530> Entertainment: Japanese Anime & Manga\n24 <a:ag_arrw_hrt:781410692321640530> Entertainment: Cartoon & Animations\n", color=0xFDDE01))
    if message.content == "a/ help set" or message.content == "a/ set help" or message.content == "a/ pref help" or message.content == "a/ help pref":
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="Chat Moderation Preferences\n▬▬▬▬▬▬▬▬▬▬", description="<a:ag_arrowgif:781395494127271947> Chat Moderation Enable or Disable `a/ set chatmod true(or)false`\n<a:ag_arrowgif:781395494127271947> Deletion of Blacklisted Words `a/ set delmod true(or)false`\n<a:ag_arrowgif:781395494127271947> Add badwords to Blacklisted words `a/ badword=<word here>` Example : `a/ badword=die`\n<a:ag_arrowgif:781395494127271947> \
        Remove Blacklisted word `a/ remove badword=<word>`\n<a:ag_arrowgif:781395494127271947> Add some Default Badwords `a/ badword defaults`\n<a:ag_arrowgif:781395494127271947> Clear All badwords `a/ badwords clear`", color=0xBCFC09))
    if message.content == 'a/ tax' or message.content == 'a/ tax help' or message.content == 'a/ help tax':
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="TAX\n▬▬▬▬▬▬▬▬▬▬", description="**TAX**\n`tax` => Gives tax amount and Amount after tax.\nSyntax : `a/ tax <tax rate> <amt>`\nExample: `a/ tax 12 1000` or `a/ t 12 1000`\n\n`danktax` => Gives tax that DankMemer(bot) put on transferres\nSyntax : `a/ danktax <amt>`\nExample: `a/ danktax 150000` or `a/ dt 150000`", color=0xD705FC))

    if message.content == 'a/ tax' or message.content == 'a/ poll help' or message.content == 'a/ help poll':
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="POLL\n▬▬▬▬▬▬▬▬▬▬", description="This command is usefull For conducting Yes or No questions\nSyntax : `a/ poll =<question>`\nExample: `a/ poll =How is This Bot?`\nLot of features like custom emoji reaction custom color to be added soon!", color=0xBCFC09))

# PREFERENCE
    if message.content.find("a/ set chatmod false") != -1 or message.content.find("a/set chatmod false") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.author.guild_permissions.manage_messages:
            gid = int(message.guild.id)
            fin = collection.find_one({"_id":gid})
            if fin == None:
                collection.insert({"_id":gid,"chatmod":0,"badwords":[],"moddel":0})
                await message.channel.send(embed=discord.Embed(title="Chat Moderation Diabled", description="Chat in this Server will **NOT** be moderated with a warn message for the words you have added using `a/ badword =<badword>`\n For more use `a/ mod help` or `a/ set help`", color=0x2AE717))
            else:
                collection.update_one({"_id":gid},{"$set":{"chatmod":0}})
            await message.channel.send(embed=discord.Embed(title="Chat Moderation Diabled", description="Chat in this Server will **NOT** be moderated with a warn message for the words you have added using `a/ badword =<badword>`\n For more use `a/ mod help` or `a/ set help`", color=0x2AE717))
        else:
            await message.channel.send(embed=discord.Embed(title="You Don't have Permmission to Manage Messages <a:ag_exc:781410611366985748>", color=0xFC4905))

    if message.content.find("a/ set chatmod true") != -1 or message.content.find("a/ set chatmod true") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.author.guild_permissions.manage_messages:
            gid = int(message.guild.id)
            fin = collection.find_one({"_id":gid})
            if fin == None:
                collection.insert({"_id":gid,"chatmod":1,"badwords":[],"moddel":0})
                await message.channel.send(embed=discord.Embed(title="Chat Moderation Enabled", description="Chat in this Server **WILL** be moderated with a warn message for the words you have added using `a/ badword =<badword>`\nIf you want to Delete AND warn pls type `a/ set delmod true`\n For more use `a/ mod help` or `a/ set help`"))
            else:
                collection.update_one({"_id":gid},{"$set":{"chatmod":1}})
            await message.channel.send(embed=discord.Embed(title="Chat Moderation Enabled", description="Chat in this Server **WILL** be moderated with a warn message for the words you have added using `a/ badword =<badword>`\nIf you want to Delete AND warn pls type `a/ set delmod true`\n For more use `a/ mod help` or `a/ set help`", color=0x2AE717))
        else:
            await message.channel.send(embed=discord.Embed(title="You Don't have Permmission to Manage Messages <a:ag_exc:781410611366985748>", color=0xFC4905))

    if message.content.find("a/ set delmod true") != -1 or message.content.find("a/ set delmod true") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
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
            await message.channel.send(embed=discord.Embed(title="You Don't have Permmission to Manage Messages <a:ag_exc:781410611366985748>", color=0xFC4905))

    if message.content == ("a/ set delmod false") or message.content == ("a/ set delmod false"):
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
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
            await message.channel.send(embed=discord.Embed(title="You Don't have Permmission to Manage Messages <a:ag_exc:781410611366985748>", color=0xFC4905))

# WIKIPEDIA
    if message.content.find("a/ wiki =") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        words = message.content.split("=")[-1]
        def wiki_summary(arg):
            definition = wikipedia.summary(arg, sentences=5, chars=1000, auto_suggest=True, redirect=True)
            return definition
        try:
            desc = wiki_summary(words)
            search = discord.Embed(title=f"{words}", description=f"**Defenition According to WikiPedia:**\n{desc}", color=0x05FCB1)
            await message.channel.send(embed=search)
        except Exception as e:
            await message.channel.send(embed=discord.Embed(title="Page Not Found", description=f"**Possible Reasons:**\n<a:ag_arrowgif:781395494127271947> The Keyword **{words}** did not Match any Pages\n<a:ag_arrowgif:781395494127271947> My Ping or Latency is High\n<a:ag_arrowgif:781395494127271947> WikiPedia's Server is Down or not Responding", color=0xFC8C05))

# WEATHER
    if message.content.startswith("a/ weather ="):
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        location = message.content.split("=")[-1]
        if len(location) >= 1:
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

            print(stat)

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

            await message.channel.send(embed=discord.Embed(title=f"{location} Weather Report\n▬▬▬▬▬▬▬▬▬▬", description=f"{emoj}{emoj}{emoj}{emoj}{emoj}{emoj}\n<a:ag_arrowgif:781395494127271947> Longitide : {lon}\n<a:ag_arrowgif:781395494127271947> Latitude\
            : {lat}\n<a:ag_arrowgif:781395494127271947> Status : {stat}\n<a:ag_arrowgif:781395494127271947> Temperature : {temp}\n<a:ag_arrowgif:781395494127271947> Feels Like : {feels}\n<a:ag_arrowgif:781395494127271947> Minimum Temperature : {mintem}\n<a:ag_arrowgif:781395494127271947> Maximum Temperature : {maxtem}\n<a:ag_arrowgif:781395494127271947> Pressure : {press}\n<a:ag_arrowgif:781395494127271947> Humidity : {humid}\n<a:ag_arrowgif:781395494127271947> Wind Speed : {wndspd}", color=0x057DFC))
        else:
            await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
            await message.channel.send(embed=discord.Embed(title="Invalid Location <a:ag_exc:781410611366985748>", description="Enter a Valid Location", color=0xFC5F05))

# SYSTEM STATS
    if message.content.find("a/ cpu") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        cpupert = psutil.cpu_percent()
        cpun = psutil.cpu_count()
        cpusw = psutil.swap_memory()
        cpupers = psutil.cpu_percent(percpu=1)
        cpubat = psutil.sensors_battery()

         # sbattery(percent=80, secsleft= < BatteryTime.POWER_TIME_UNLIMITED: -2 >, power_plugged = True)
        cpubat = str(cpubat)
        cpubatp = cpubat.split('=')[1]
        cpubatp = cpubatp.split(",")[0]

        cpubatc = cpubat.split("=")[-1]
        cpubatc = cpubatc.split(")")[0]

        cpui = psutil.cpu_freq()
        cpui = str(cpui)
        cpui = cpui.split("=")[-1]
        cpui = cpui.split(")")[0]
        cpui = float(cpui)
        cpui = cpui / 1000
        cpuo = cpupers[0]
        cput = cpupers[1]
        cpuy = cpupers[2]
        cpuf = cpupers[3]

        # sswap(total=10694811648, used=6834396100, free=2350850048, percent=78.0, sin=0, sout=0)

        cpusw = str(cpusw)
        cpuswt = cpusw.split("=")[1]
        cpuswt = cpuswt.split(",")[0]
        cpuswt = float(cpuswt)
        cpuswt = cpuswt/10000000
        cpuswt = math.floor(cpuswt)
        cpuswt = cpuswt/100

        cpusw = str(cpusw)
        cpuswu = cpusw.split("=")[2]
        cpuswu = cpuswu.split(",")[0]
        cpuswu = float(cpuswu)
        cpuswu = cpuswu / 10000000
        cpuswu = math.floor(cpuswu)
        cpuswu = cpuswu / 100

        cpusw = str(cpusw)
        cpuswf = cpusw.split("=")[3]
        cpuswf = cpuswf.split(",")[0]
        cpuswf = float(cpuswf)
        cpuswf = cpuswf / 10000000
        cpuswf = math.floor(cpuswf)
        cpuswf = cpuswf / 100

        cpusw = str(cpusw)
        cpuswp = cpusw.split("=")[4]
        cpuswp = cpuswp.split(",")[0]
        # await message.channel.send(cpuidk)
        await message.channel.send(embed=discord.Embed(title="CPU STATS :tools:", description=f"**Processor**\nCores = {cpun}\nSpeed = {cpui}Ghz\nTotal Usage = {cpupert}%\nCore 1 = {cpuo}%\nCore 2 = {cput}%\nCore 3 = {cpuy}%\nCore 4 = {cpuf}%\n\n**Swap Memory**\nTotal = {cpuswt} Gb\nUsed = {cpuswu} Gb\nPercentage = {cpuswp}%\nFree = {cpuswf} Gb\n\n**Battery**\nAvailable = {cpubatp}% :battery: \nCharging = {cpubatc}", color=0xFD9E01))

# DATE TIME
    if message.content.find("a/ time") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        time = datetime.datetime.now()
        time = str(time)
        time = time.split()[-1]
        time = time.split('.')[0]
        await message.channel.send(embed=discord.Embed(title=f"{time}", description="The Time NOW According to My server", color=0x05ADFC))

    if message.content.find("a/ date") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        date = datetime.datetime.now()
        date = str(date)
        date = date.split()[0]
        await message.channel.send(embed=discord.Embed(title=f"{date}", description="Date Today According to My server", color=0x05ADFC))

# AFK Status
    fio = collection.find_one({"_id": 222})
    afkdic = fio["afkdic"]
    if message.content.startswith("a/ afk =") or message.content.startswith("a/ afk="):
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        afkmsg = message.content.split('=')[-1]
        afkmens = message.author.id
        afkmens = f"<@!{afkmens}>"
        afkdic[afkmens] = afkmsg
        collection.update_one({"_id":222},{"$set":{"afkdic":afkdic}})
        await message.channel.send(embed=discord.Embed(title="AFK Status Set! <a:ag_tickop:781395575962599445>", description=f"AFK status will be removed automatically in 1 day**Message From {afkmens}**\n{afkmsg}", color=0xFBFE02))

    for i in afkdic:
        if message.content.find(i) != -1:
            await message.channel.send(embed=discord.Embed(title="<a:ag_exc:781410611366985748> USER AFK <a:ag_exc:781410611366985748>", description=f"Do not Ping {i} <a:ag_pprbt:781410629180194826>\n**Message for U from {i}**\n{afkdic[i]}", color=0xFE0202))

    if message.content.find("a/ afk list") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        nemaf = len(afkdic)
        afklos = afkdic.keys()
        await message.channel.send(embed=discord.Embed(title=f"AFK USERS LIST", description=f"{nemaf} Users Are AFK(Incl. of all my Servers)\n\nAfk Users list:"))

    for i in afkdic:
        k = list(i)
        teks = ""
        for j in k:
            if j == "0" or j == "1" or j == "2" or j == "3" or j == "4" or j == "5" or j == "6" or j == "7" or j == "8" or j == "9":
                teks += j
        if int(message.author.id) == int(teks):
            await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
            for jk in afkdic:
                idh = message.author.id
                idh = f"<@!{idh}>"
                if idh == jk:
                    del afkdic[idh]
                    collection.update_one({"_id":222},{"$set":{"afkdic":afkdic}})
                    await message.channel.send(embed=discord.Embed(title="AFK Staus Removed! <a:ag_tickop:781395575962599445>", description=f"Afk Status For {i} is Removed", color=0x08FE73))

# EVAL
    if message.content.find("a/ eval ^") != -1 and message.author.id == 782624720989585409:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        ecol = message.content.split('^')[-1]
        opt = eval(ecol)
        await message.channel.send(embed=discord.Embed(title=f"{opt}", description=f"Evauated by {message.author}"))

# OWNER
    if message.content.find("a/ perm") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        owie = message.author.guild_permissions
        await message.channel.send(embed=discord.Embed(title=f"{message.author}'s Permissions in {message.guild}", description=f"{owie}"))

# MODERATION
    if message.content.find("a/ kick") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        try:
            if message.author.guild_permissions.kick_members:
                kikser = message.mentions[0]
                await kikser.kick()
                await message.channel.send(embed=discord.Embed(title="<a:ag_exc:781410611366985748> KICKED <a:ag_exc:781410611366985748>", description=f"{message.author} has Kicked {kikser} from {message.guild}", color=0xFD0101))

            else:
                await message.channel.send(embed=discord.Embed(title="You Don't have Permmission to Kick Members <a:ag_exc:781410611366985748>", color=0xFC4905))
        except Exception as exp:
            exp = str(exp)
            exp = exp.split(': ')[-1]
            if exp == ("Missing Permissions"):
                await message.channel.send(embed=discord.Embed(title="<a:ag_exc:781410611366985748> Missing Permissions <a:ag_exc:781410611366985748>", description="Possible Reasons:\n<a:ag_arrowgif:781395494127271947> I Don't have Kick Permissions\n<a:ag_arrowgif:781395494127271947> The Member You are trying to Kick has a Higher Role than Me", color=0xFD4201))

    if message.content.find("a/ ban") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        try:
            if message.author.guild_permissions.ban_members:
                banser = message.mentions[0]
                await banser.ban()
                await message.channel.send(embed=discord.Embed(title="<a:ag_exc:781410611366985748> BANNED <a:ag_exc:781410611366985748>", description=f"**{message.author}** has Banned **{banser}** from {message.guild}", color=0xFD0101))

            else:
                await message.channel.send(embed=discord.Embed(title="You Don't have Permmission to Ban Members <a:ag_exc:781410611366985748>", color=0xFC4905))
        except Exception as exp:
            exp = str(exp)
            exp = exp.split(': ')[-1]
            if exp == ("Missing Permissions"):
                await message.channel.send(embed=discord.Embed(title="<a:ag_exc:781410611366985748> Missing Permissions <a:ag_exc:781410611366985748>", description="Possible Reasons:\n<a:ag_arrowgif:781395494127271947> I Don't have Ban Permissions\n<a:ag_arrowgif:781395494127271947> The Member You are trying to Ban has a Higher Role than Me", color=0xFD4201))

    if message.content.find("a/ unban") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        try:
            if message.author.guild_permissions.ban_members:
                unbanser = message.mentions[0]
                await unbanser.pardon()
                await message.channel.send(embed=discord.Embed(title="<a:ag_exc:781410611366985748> UNBANNED <a:ag_exc:781410611366985748>", description=f"{message.author} has UNBANNED {unbanser} in {message.guild}", color=0xFD0101))

            else:
                await message.channel.send(embed=discord.Embed(title="You Don't have Permmission to UNBAN Members <a:ag_exc:781410611366985748>", color=0xFC4905))
        except Exception as exp:
            exp = str(exp)
            exp = exp.split(': ')[-1]
            if exp == ("Missing Permissions"):
                await message.channel.send(embed=discord.Embed(title="<a:ag_exc:781410611366985748> Missing Permissions <a:ag_exc:781410611366985748>", description="Possible Reasons:\n<a:ag_arrowgif:781395494127271947> I Don't have Kick Permissions\n<a:ag_arrowgif:781395494127271947> The Member You are trying to Kick has a Higher Role than Me", color=0xFD4201))
            else:
                await message.channel.send(embed=discord.Embed(title="An Error Occured"), color=0xFD4201)

    if message.content.find("a/ mute") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.author.guild_permissions.administrator:
            mutser = message.mentions[0]
            await mutser.mute()
            await message.channel.send(embed=discord.Embed(title="<a:ag_exc:781410611366985748> MUTED <a:ag_exc:781410611366985748>", description=f"**{message.author}** has MUTED **{mutser}**", color=0xFD0101))

        else:
            await message.channel.send(embed=discord.Embed(title="You Don't have Permmission to Mute Members <a:ag_exc:781410611366985748>", color=0xFC4905))

# EMOTIFY
    if message.content.find("a/ emotify =") !=-1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        emo = message.content.split('=')[-1]
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
    if message.content.find('a/ div') != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.content.split(' ')[-3] == 'divide' or message.content.split(' ')[-3] == 'div':
            divv = message.content.split(' ')[-2]
            div = message.content.split(' ')[-1]
        divv = float(divv)
        div = float(div)
        divans = divv/div
        await message.channel.send(embed=discord.Embed(title=":1234: CALCULATOR :1234:", description=f"**{divv}** Divided by **{div}** =\n **{divans}** <a:ag_tickop:781395575962599445>\n\n{message.channel}", color=0x02FE95))

    if message.content.find('a/ add') != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.content.split(' ')[-3] == 'add' or message.content.split(' ')[-3] == 'addition':
            addd = message.content.split(' ')[-2]
            adddd = message.content.split(' ')[-1]
        addd = float(addd)
        adddd = float(adddd)
        addans = addd + adddd
        await message.channel.send(embed=discord.Embed(title=":1234: CALCULATOR :1234:", description=f"**{addd}** Added to **{adddd}** =\n **{addans}** <a:ag_tickop:781395575962599445>", color=0x02FE95))

    if message.content.find('a/ sub') != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.content.split(' ')[-3] == 'sub' or message.content.split(' ')[-3] == 'subtract':
            subb = message.content.split(' ')[-2]
            subbb = message.content.split(' ')[-1]
        subb = float(subb)
        subbb = float(subbb)
        subans = subb - subbb
        await message.channel.send(embed=discord.Embed(title=":1234: CALCULATOR :1234:", description=f"**{subbb}** Subtracted from **{subb}** =\n **{subans}** <a:ag_tickop:781395575962599445>", color=0x02FE95))

    if message.content.find('a/ mult') != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.content.split(' ')[-3] == 'mult' or message.content.split(' ')[-3] == 'multiply':
            mult = message.content.split(' ')[-2]
            multt = message.content.split(' ')[-1]
        mult = float(mult)
        multt = float(multt)
        multans = mult * multt
        await message.channel.send(embed=discord.Embed(title=":1234: CALCULATOR :1234:", description=f"**{mult}** Multiplied by **{multt}** =\n **{multans}** <a:ag_tickop:781395575962599445>", color=0x02FE95))

    if message.content.find('a/ lcm') != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.content.split(' ')[-3] == 'lcm':
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

    if message.content.find('a/ hcf') != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.content.split(' ')[-3] == 'hcf':
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

    if message.content.find('a/ tax') != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.content.split(' ')[-3] == 'tax' or message.content.split(' ')[-2] == 't':
            num1 = message.content.split(' ')[-2]
            num2 = message.content.split(' ')[-1]
            num1 = int(num1)
            num2 = int(num2)
            atxr = num2*num1
            atxr = atxr/100
            await message.channel.send(embed=discord.Embed(title=":1234: CALCULATOR :1234:", description=f"**{num2}** Amount\n**{num1}%** tax \nTax Amount = **{atxr}**\nBal Amount = {num2-atxr} <a:ag_tickop:781395575962599445>", color=0x02FE95))

    if message.content.find('a/ danktax') != -1 or message.content.find('a/ dt ') != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.content.split(' ')[-2] == 'danktax' or message.content.split(' ')[-2] == 'dt':
            num2 = message.content.split(' ')[-1]
            num2 = int(num2)
            num1 = 0
            if num2 > 25000 and num1 <= 50000:
                num1 = 1
            elif num2 > 50000 and num1 <= 100000:
                num1 = 3
            elif num2 > 100000 and num1 <= 749999:
                num1 = 5
            elif num2 > 750000 and num1 <= 2499999:
                num1 = 8
            elif num2 > 2500000:
                num1 = 15
            atxr = num2 * num1
            atxr = atxr / 100
            await message.channel.send(embed=discord.Embed(title=":1234: CALCULATOR :1234:", description=f"**{num2}** Amount\n**{num1}%** Tax\nTax Amount = **{atxr}**\nBal Amount = {num2-atxr}<a:ag_tickop:781395575962599445>", color=0x02FE95))

# COMPLEX CALCULATOR 1
    if message.content.find("a/ ceil ") != -1:
        ceil = message.content.split(" ")[-1]
        ceil = float(ceil)
        cans = math.ceil(ceil)
        await message.channel.send(embed=discord.Embed(title=f"Ceil of {ceil} = {cans}", color=0x05FCE2))

    if message.content.find("a/ sqrt ") != -1:
        sqrt = message.content.split(" ")[-1]
        sqrt = float(sqrt)
        cans = math.sqrt(sqrt)
        await message.channel.send(embed=discord.Embed(title=f"Square Root of {sqrt} = {cans}", color=0x05FCE2))

    if message.content.find("a/ exp ") != -1:
        exp = message.content.split(" ")[-1]
        exp = float(exp)
        cans = math.exp(exp)
        await message.channel.send(embed=discord.Embed(title=f"Log `e` to the Power {exp} = {cans}", description="Use `a/ val e` for the Value of `e`", color=0x05FCE2))

    if message.content.find("a/ floor ") != -1:
        floor = message.content.split(" ")[-1]
        floor = float(floor)
        cans = math.floor(floor)
        await message.channel.send(embed=discord.Embed(title=f"Floor Value of {floor} = {cans}", color=0x05FCE2))

    if message.content.find("a/ log ") != -1:
        log = message.content.split(" ")[-1]
        log = float(log)
        if log >= 0 :
            cans = math.log(log)
            await message.channel.send(embed=discord.Embed(title=f"Natural Log of {log} = {cans}", color=0x05FCE2))
        else:
            await message.channel.send(embed=discord.Embed(title=f"Natural Log of {log} is Not Defined", color=0xFC4905))

    if message.content.find("a/ log10 ") != -1:
        log = message.content.split(" ")[-1]
        log = float(log)
        if log >= 0:
            cans = math.log10(log)
            await message.channel.send(embed=discord.Embed(title=f"Log to the Base 10 of {log} = {cans}", color=0x05FCE2))
        else:
            await message.channel.send(embed=discord.Embed(title=f"The Log to the Base 10 of {log} is Not Defined", color=0xFC4905))

    if message.content.find("a/ sin ") != -1:
        sin = message.content.split(" ")[-1]
        sin = float(sin)
        sin = math.radians(sin)
        cans = math.sin(sin)
        await message.channel.send(embed=discord.Embed(title=f"Sin of {sin} = {cans}", color=0x05FCE2))

    if message.content.find("a/ cos ") != -1:
        cos = message.content.split(" ")[-1]
        cos = float(cos)
        cos = math.radians(cos)
        cans = math.cos(cos)
        await message.channel.send(embed=discord.Embed(title=f"Cos of {cos} = {cans}", color=0x05FCE2))

    if message.content.find("a/ tan ") != -1:
        tan = message.content.split(" ")[-1]
        tan = float(tan)
        tan = math.radians(tan)
        cans = math.tan(tan)
        await message.channel.send(embed=discord.Embed(title=f"Tan of {tan} = {cans}", color=0x05FCE2))

    if message.content.find("a/ factorial ") != -1:
        fct = message.content.split(" ")[-1]
        fct = float(fct)
        cans = math.factorial(fct)
        await message.channel.send(embed=discord.Embed(title=f"Factorial of {fct} = {cans}", color=0x05FCE2))

# COMPLEX CALCULATOR 2

    if message.content.find("a/ bilog ") != -1:
        blga = message.content.split(" ")[-2]
        blga = float(blga)
        blgb = message.content.split(" ")[-1]
        blgb = float(blgb)
        cans = math.log(blga, blgb)
        await message.channel.send(embed=discord.Embed(title=f"The Value of {blga} to the Power {blgb} = {cans}", color=0x05FCE2))

    if message.content.find("a/ pow ") != -1:
        powa = message.content.split(" ")[-2]
        powa = float(powa)
        powb = message.content.split(" ")[-1]
        powb = float(powb)
        cans = math.pow(powa, powb)
        await message.channel.send(embed=discord.Embed(title=f"The Value of {powa} to the Power {powb} = {cans}", color=0x05FCE2))

# CONVERTERS
    if message.content.find("a/ radians ") != -1:
        radians = message.content.split(" ")[-1]
        radians = float(radians)
        cans = math.radians(radians)
        await message.channel.send(embed=discord.Embed(title=f"Radians in {radians} = {cans}", color=0x05FCE2))

    if message.content.find("a/ degrees ") != -1:
        degrees = message.content.split(" ")[-1]
        degrees = float(degrees)
        cans = math.degrees(degrees)
        await message.channel.send(embed=discord.Embed(title=f"Degrees in {degrees} = {cans}", color=0x05FCE2))

    if message.content.find("a/ far ") != -1:
        far = message.content.split(" ")[-1]
        far = float(far)
        cans = far - 32
        cans = cans * 5
        cans = cans / 9
        # (32°F − 32) × 5 / 9 = 0°C
        # (0°C × 9/5) + 32 = 32°F
        await message.channel.send(embed=discord.Embed(title=f"{far} Farenheit = {cans} Degrees", color=0x05FCE2))

    if message.content.find("a/ cel ") != -1:
        deg = message.content.split(" ")[-1]
        deg = float(deg)
        cans = deg*9
        cans = cans/5
        cans = cans+32
        # (32°F − 32) × 5 / 9 = 0°C
        # (0°C × 9/5) + 32 = 32°F
        await message.channel.send(embed=discord.Embed(title=f"{deg} Degrees = {cans} Farenheit", color=0x05FCE2))

    if message.content.find("a/ cel-kel ") != -1:
        kelf = message.content.split(" ")[-1]
        kelf = float(kelf)
        cans = cans+273
        await message.channel.send(embed=discord.Embed(title=f"{kelf} Degrees = {cans} Kelvin", color=0x05FCE2))

    if message.content.find("a/ far-kel ") != -1:
        far = message.content.split(" ")[-1]
        far = float(far)
        cans = far - 32
        cans = cans * 5
        cans = cans / 9
        cans = cans+273
        # (32°F − 32) × 5 / 9 = 0°C
        # (0°C × 9/5) + 32 = 32°F
        await message.channel.send(embed=discord.Embed(title=f"{far} Farenheit = {cans} Kelvin", color=0x05FCE2))

# Google search
    if message.content.startswith("a/ google =") or message.content.startswith("a/ google="):
        url = "https://google-search3.p.rapidapi.com/api/v1/search/q=elon+musk&num=1"

        headers = {
            'x-rapidapi-key': "7acfb85b32msh218cdca2c7e7bdfp1163b1jsna314ac48f283",
            'x-rapidapi-host': "google-search3.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)

        print(response.text)

# SUGGEST
    if message.content.startswith("a/ suggest =") or message.content.startswith("a/ suggest="):
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        sugg = message.content.split('=')[-1]
        await message.channel.send(embed=discord.Embed(title=" <a:ag_reddot:781410740619051008> Suggested! <a:ag_reddot:781410740619051008> ", description="Thanks for Your Valuable Suggestion!\nYour Suggestion Has Been Submitted! <a:ag_tickop:781395575962599445> ", color=0x04FD03))
        channel = client.get_channel(784697044236763176)
        await channel.send(embed=discord.Embed(title=f" <a:ag_reddot:781410740619051008> Suggestion by \n{message.author} <a:ag_reddot:781410740619051008> ", description=f"`{sugg}`", color=0x04FD03))

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


# add word
    if message.content.startswith("a/ badword=") or message.content.startswith("a/ badword ="):
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.author.guild_permissions.manage_messages:
            gid = int(message.guild.id)
            fin = collection.find_one({"_id": gid})
            if fin == None:
                collection.insert({"_id": gid, "chatmod": 1, "badwords": [], "moddel": 0})
                wordb = message.content.split("=")[-1]
                fina = collection.find_one({"_id":gid})
                fina = fina["badwords"]
                fina.append(wordb)
                collection.update_one({"_id": gid}, {"$set": {"badwords":fina}})
                await message.channel.send(embed=discord.Embed(title="Bad word Added and Chat Moderation Enabled", description="Chat in this Server **WILL** be moderated with a warn message for the words you have added using `a/ badword =<badword>`\nIf you want to Delete AND Warn pls type `a/ set delmod true`\n For more use `a/ mod help` or `a/ set help`", color=0x2AE717))
            else:
                wordb = message.content.split("=")[-1]
                fina = collection.find_one({"_id": gid})
                fina = fina["badwords"]
                fina.append(wordb)
                collection.update_one({"_id": gid}, {"$set": {"badwords": fina, "chatmod":1}})
                await message.channel.send(embed=discord.Embed(title="Bad word Added", description="Members will be warned on using the blacklisted words. If you want to Delete AND Warn For using Blacklisted words pls type `a/ set delmod true`\nIf Done already pls Ignore\n For more use `a/ mod help` or `a/ set help`", color=0x2AE717))
        else:
            await message.channel.send(embed=discord.Embed(title="You Don't have Permmission to Manage Messages <a:ag_exc:781410611366985748>", color=0xFC4905))

    if message.content == ("a/ badword defaults") or message.content == ("a/ badwords defaults") or message.content == ("a/ badwords defaults") or message.content == ("a/ badwords default") or message.content == ("a/ badword default"):
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
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
            await message.channel.send(embed=discord.Embed(title="You Don't have Permmission to Manage Messages <a:ag_exc:781410611366985748>", color=0xFC4905))

    if message.content.startswith("a/ badword remove =") or message.content.startswith("a/ remove badword=") or message.content.startswith("a/ remove badword =") or message.content.startswith("a/ badword remove="):
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.author.guild_permissions.manage_messages:
            gid = int(message.guild.id)
            fin = collection.find_one({"_id": gid})
            if fin == None:
                await message.channel.send(embed=discord.Embed(title="NO Badwords Found", description="Pls add using `a/ badword =<badword>` or `a/ badword default` to add default words\nIf you want to Delete AND Warn for using blacklisted words pls type `a/ set delmod true`\n For more use `a/ mod help` or `a/ set help`", color=0x2AE717))
            else:
                wordb = message.content.split("=")[-1]
                fina = collection.find_one({"_id": gid})
                fina = fina["badwords"]
                for i in range(0,len(fina)):
                    if fina[i] == wordb:
                        asfdaf = fina.pop(i)
                        collection.update_one({"_id": gid}, {"$set": {"badwords": fina}})
                await message.channel.send(embed=discord.Embed(title="Bad word Removed", description="Members will be warned on using the blacklisted words. If you want to Delete AND Warn For using Blacklisted words pls type `a/ set delmod true`\nIf Done already pls Ignore\n For more use `a/ mod help` or `a/ set help`", color=0x2AE717))
        else:
            await message.channel.send(embed=discord.Embed(title="You Don't have Permmission to Manage Messages <a:ag_exc:781410611366985748>", color=0xFC4905))

    if message.content == ("a/ badword list") or message.content == ("a/ badwords list"):
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
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
            await message.channel.send(embed=discord.Embed(title="You Don't have Permmission to Manage Messages <a:ag_exc:781410611366985748>", color=0xFC4905))

    if message.content == "a/ badwords clear" or message.content == "a/ clear badwords":
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
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
            await message.channel.send(embed=discord.Embed(title="You Don't have Permmission to Manage Messages <a:ag_exc:781410611366985748>", color=0xFC4905))

# MSG DELETE
    if message.content.startswith("a/ delete "):
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.author.guild_permissions.manage_messages:
            delee = 0
            delee = message.content.split(' ')[-1]
            delee = int(delee)
            delee = delee + 1
            await message.channel.purge(limit=delee)
            await message.channel.send(embed=discord.Embed(title=f"{delee} Messages :x: Deleted! <a:ag_tickop:781395575962599445>", description=f"Requested By {message.author}", color=0xFD3A01))
        else:
            await message.channel.send(embed=discord.Embed(title="You Don't have Permmission to Manage Messages <a:ag_exc:781410611366985748>", color=0xFC4905))

# POLL
    if message.content.find("a/ poll =") !=-1:
        po = message.content.split('=')[-1]
        pola = await message.channel.send(embed=discord.Embed(title=f"**{po}**", description=f"React with :thumbsup: or :thumbsdown:\nRequested By: *{message.author}*", color=0xFD3A01))
        await pola.add_reaction('👍')
        await pola.add_reaction('👎')

# CHAT
    if str(message.channel) in chtchannel:
        if message.content.find("Hi") != -1:
            await message.channel.send(embed=discord.Embed(description="<a:ag_hoi:781395433842409473> , How Are You?", color=0x04FD03))
        if message.content.find("die") != -1:
            await message.channel.send("<a:ag_stv_dnc:781410697825222686>")
        if message.content.find("loading") != -1:
            await message.channel.send("<a:ag_ldingwin:781410586138902529>")
        if message.content == "hi":
            await message.channel.send(embed=discord.Embed(description="<a:ag_hoi:781395433842409473> , How Are You?", color=0x04FD03))
        # if message.content.find("hi") != -1 and message.content != "a/ hi":
        #     await message.channel.send(embed=discord.Embed(description="<a:ag_hoi:781395433842409473> , How Are You?\n Plz Use MY Prefix `a/`", color=0x04FD03))
        if message.content.find("fine") != -1:
            await message.channel.send(embed=discord.Embed(description="Oh Nice!", color=0x04FD03))
        if message.content.find("Fine") != -1:
            await message.channel.send(embed=discord.Embed(description="Oh Nice!", color=0x04FD03))

# WISHES

        if message.content.find("you?") != -1:
            await message.channel.send(embed=discord.Embed(description="<a:ag_imfn:781058534543589376>", color=0x04FD03))
        if message.content.find("You?") != -1:
            await message.channel.send(embed=discord.Embed(description="<a:ag_imfn:781058534543589376>", color=0x04FD03))
        if message.content.find("ok") != -1:
            await message.channel.send(embed=discord.Embed(description="Hmm ok then?", color=0x04FD03))
        if message.content.find("Ok") != -1:
            await message.channel.send(embed=discord.Embed(description="Hmm ok then?", color=0x04FD03))
        if message.content.find("bye") != -1:
            await message.channel.send(embed=discord.Embed(description="No plzz Don't go :pleading_face:", color=0x04FD03))
        if message.content.find("Bye") != -1:
            await message.channel.send(embed=discord.Embed(description="No plzz Don't go :pleading_face:", color=0x04FD03))
        if message.content.find("hmm") != -1:
            await message.channel.send(embed=discord.Embed(description="hmmmmmmm so what next?", color=0x04FD03))

        if message.content.find("lol") != -1:
            await message.channel.send(":rofl:")
        if message.content.find("Lol") != -1:
            await message.channel.send(":rofl:")
        if message.content.find("cry") != -1:
            await message.channel.send(":sob:")
        if message.content.find("Cry") != -1:
            await message.channel.send(":sob:")
        if message.content.find("-_-") != -1:
            await message.channel.send(":expressionless:")
        if message.content.find("How r u") != -1:
            await message.channel.send(embed=discord.Embed(description="Fine", color=0x04FD03))
        if message.content.find("how r u") != -1:
            await message.channel.send(embed=discord.Embed(description="Fine", color=0x04FD03))
        if message.content.find("How are u") != -1:
            await message.channel.send(embed=discord.Embed(description="Fine", color=0x04FD03))
        if message.content.find("how are u") != -1:
            await message.channel.send(embed=discord.Embed(description="Fine", color=0x04FD03))
        if message.content.find("How are you") != -1:
            await message.channel.send(embed=discord.Embed(description="Fine", color=0x04FD03))
        if message.content.find("how are you") != -1:
            await message.channel.send(embed=discord.Embed(description="Fine", color=0x04FD03))
        if message.content.find("How r you") != -1:
            await message.channel.send(embed=discord.Embed(description="Fine", color=0x04FD03))
        if message.content.find("how r you") != -1:
            await message.channel.send(embed=discord.Embed(description="Fine", color=0x04FD03))
        if message.content.find("a/ sad") != -1:
            await message.channel.send(embed=discord.Embed(description="C'mon Don't be Sad!! Be Happy Always!!", color=0x0803FD))
        if message.content.find("a/ Sad") != -1:
            await message.channel.send(embed=discord.Embed(description="C'mon Don't be Sad!! Be Happy Always!!", color=0x0803FD))

    if message.content.find("a/ beat") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send("<a:ag_pprbt:781410629180194826>")
    if message.content.find("a/ twirl") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send("<a:twirl:781410568657043506>")
    if message.content.find("a/ kasa") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send("<:ag_ks:781410607672852500>")
    if message.content.find("a/ mind") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send("<:ag_mind:781410713981288468>")
    if message.content.find("a/ tnt") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send("<:ag_tnt:781395412648460288>")
    if message.content.find("bigfan") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send("<:bigfan:781410551016062987>")
    if message.content == ("op") or message.content == ("Op") or message.content == ("OP") :
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send("<:ag_op:781395451492302859>")
    if message.content == ("gg") or message.content == ("Gg") or message.content == ("GG"):
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send("<:ag_GG:781410564839964672>")
    if message.content.find("Good morning") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(description="Good Morning!!", color=0x04FD03))
    if message.content.find("good morning") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(description="Good Morning!!", color=0x04FD03))
    if message.content.find("Good afternoon") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(description="Good Afternoon!!", color=0x04FD03))
    if message.content.find("good afternoon") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(description="Good Afternoon!!", color=0x04FD03))
    if message.content.find("Good evening") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(description="Good Evening!!", color=0x04FD03))
    if message.content.find("good evening") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(description="Good Evening!!", color=0x04FD03))
    if message.content.find("Good night") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(description="Good Night!!", color=0x04FD03))
    if message.content.find("good night") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(description="Good Night!!", color=0x04FD03))

# RANDOMS
    if message.content.find("a/ random") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        if message.content == "a/ random":
            await message.channel.send(embed=discord.Embed(title="Syntax Error <a:ag_exc:781410611366985748>", description="Use Syntax:\n`a/ random <number of options>`\n**Example:**\n`a/ random 5`", color=0xFCBC05))
        if message.content.find("a/ random ") != -1:
            randgi = message.content.split(' ')[-1]
            randgi = int(randgi)
            rando = random.randint(1, randgi)
            await message.channel.send(embed=discord.Embed(title=f"{rando}", description=f"The Random Outcome of {randgi} Numbers", color=0x48FC05))

# TESTS
    if message.content.startswith("testit"):
        mage = await message.channel.send(embed=discord.Embed(title="hi how ads u"))
        await asyncio.sleep(5)
        await mage.edit(embed=discord.Embed(title="dodod"))
        await mage.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")


#         else:
#             print("no perm lol")
#

    # if message.content.find("a/ 2test") != -1:
    #     chanid = message.id
    #     await message.channel.send(embed=discord.Embed(title=f"{chanid}", description="Your description\ndescreption2", color=000000))
#     if message.content.find('a/ tstdivide') != -1:
#         if message.content.split(' ')[-3] == 'divide':
#             weer = message.content.split(' ')[-2]
#             wer = message.content.split(' ')[-1]
#         weer = int(weer)
#         wer = int(wer)
#         anss = weer/wer
#         print(wer)
#         print(weer)
#         await message.channel.send(anss)
#     if message.content.find("hillo") != -1:
#         await message.channel.send("hillo")

# QUZZZZ

    if message.content == ("a/ quiz start") != -1 or message.content == ("a/quiz start") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="**INVALID SYNTAX**", description="Syntax: `a/ quiz start <level> <topic id>`\nExample: `a/ quiz start 2 12` (Topic id is optional)", color=0xFC0505))
    if message.content.startswith("a/ quiz start "):
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        diffc = message.content.split(" ")[3]
        cat = 9
        try:
            cata = message.content.split(" ")[4]
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
            # if
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
            await mos.edit(embed=discord.Embed(title=f"**Question 1 ({topic})**", description=f"**{ques}**\n\n**Give Your Answer within 10s as**\na/ true or a/ false", color=0xFD7803))
            # <Message id=801741193565831218 channel=<TextChannel id=781754334571921438 name='beta-bot-testing-1' position=9 nsfw=False news=False category_id=781753841162518539> type=<MessageType.default: 0> author=<Member id=782624720989585409 name='『AG』》V!GПΣ$hᴰᵉᵛ' discriminator='5105' bot=False nick=None guild=<Guild id=780625655657791518 name='Asteroid Support Server' shard_id=None chunked=False member_count=14>> flags=<MessageFlags value=0>>
            def check(m):
                return m.channel == channel and m.content.lower() in ["a/ true", "a/ false"]

            try:
                msg = await client.wait_for('message', timeout=20.0, check=check)
                if msg.content.lower() == f"a/ {cora}":
                    await msg.add_reaction('✅')
                    await mos.edit(embed=discord.Embed(title="**CORRECT**", description=f"Answer Given By:{message.author}\n\nReact with :thumbsup: For next Question", color=0x01FD14))
                    await mos.add_reaction('👍')
                else:
                    await msg.add_reaction('❌')
                    await mos.edit(embed=discord.Embed(title="**WRONG**", description=f"Answer Given By:{message.author}\n\nReact with :thumbsup: For next Question", color=0xFC4905))
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
    if message.content.startswith("a/ say =") or message.content.startswith("a/ say="):
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        saymsg = message.content.split('=')[-1]
        await message.channel.send(embed=discord.Embed(title=f"{saymsg}", description=f"Asked to Say By: {message.author}", color=0x02BDFE))

    if message.content.startswith("a/ delsay =") or message.content.startswith("a/ delsay="):
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        delsay = message.content.split('=')[-1]
        await message.channel.purge(limit=1)
        await message.channel.send(embed=discord.Embed(title=f"{delsay}", description=f"Asked to Delete and Say By: {message.author}", color=0x02BDFE))

    if message.content.startswith("a/ op say=") and int(message.author.id) == 782624720989585409:
        temsay = message.content.split("=")[-1]
        await message.channel.send(temsay)

# MISC
    if message.content.find("a/ member") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        servermem = message.guild.member_count
        await message.channel.send(embed=discord.Embed(title=f"{message.guild}", description=f"Number of Members: {servermem} <a:ag_reddot:781410740619051008>", color=0xFEE702))

    if message.content == ("a/ server") or message.content == "a/ servers":
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        tserver = len(client.guilds)
        await message.channel.send(embed=discord.Embed(title="Server Count", description=f"Serving {tserver} Servers <a:ag_tickop:781395575962599445> Now \nWOW!!!" , color=0x01FD59))

    if message.content.find("a/ serverid") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        tserverid = message.guild.id
        await message.channel.send(embed=discord.Embed(title=f"Server ID of {message.guild}", description=f"{tserverid} <a:ag_tickop:781395575962599445>", color=0x01FD59))

    for i in string.ascii_lowercase:
        if message.content.startswith(f"a/{i}"):
            await message.channel.send(embed=discord.Embed(title="Please leave a space between `a/` and command", description="Example: `a/ help`", color=0xFB1F1F))

    if message.content.find("a/ update") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        await message.channel.send(embed=discord.Embed(title="**v1.5 UPDATES !!**", description="Added Vote(me) in invite menu and `a/ vote`\nAdded TAX Calculation Try `a/ tax help`\nAdded Emotify command Try `a/ emotify help` or `a/ misc help`\nAdded Poll System Try `a/ poll help` Will be improved so much in upcomming updates like custom emojis\nAFK status will be removed as soon as you type a message\nNow Bot responds to incomplete commands(mostly)\nQuiz System Enhanced\nEdited some help messages\nMajor Bug Fixes :tools:\n\nUse `a/ suggest help` To help me more and report bugs and add more features!! :pray:", color=0x05BAFD))

    if message.content.find("a/ xxd") !=-1:
        if message.author.guild_permissions.manage_messages:
            uhu = message.guild.members
            nomes = ""
            for i in range(0,len(uhu)):
                topo = uhu[i]
                topo = str(topo)
                diso = topo
                topo = topo.split('name=')[1]
                topo = topo.split(' discri')[0]
                diso = diso.split("ator=")[1]
                diso = diso.split(" bot=")
                topo += diso
                nomes += f"{topo}\n"
                await message.channel.send(embed=discord.Embed(title=f"Member List of {message.guild}\n▬▬▬▬▬▬▬▬▬▬", description=f"nomes"))
        else:
            await message.channel.send(embed=discord.Embed(title="You Don't have Permmission to Manage Messages <a:ag_exc:781410611366985748>", color=0xFC4905))

    if message.content.find("a/ xd") != -1:
        uhu = message.guild.members
        adf = uhu[0]
        print(adf)

# PING
    if message.content.find("a/ ping") != -1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        ping = client.latency
        ping = ping*1000
        ping = math.floor(ping)
        await message.channel.send(embed=discord.Embed(title="My PING <a:ag_ggl:781410701327335445>", description=f":hourglass: {ping}ms", color=0x02BDFE))

client.loop.create_task(update_stats())


client.run(token)

#   ||| CMD COMMANDS |||
# do to directory in cmd
# heroku login
# git init
# heroku git:remote -a asteroidgaming
# git commit -am 'cool'
# git add .
# git push heroku master