import discord
from discordTogether import DiscordTogether


client = discord.Client()
togetherControl = DiscordTogether(client)
global message


# helpmbd = discord.Embed(title="**Hey,**\nI am **Asteroid** Made by:\n**Vignesh_x64ᴰᵉᵛ#8351**\nMy Prefix is `a/`\n▬▬▬▬▬▬▬▬▬▬\n Make sure to leave a space between `a/` and command\n▬▬▬▬▬▬▬▬▬▬", description="Use `a/ <module id> help` for More Info!\nIn the Place of <module id> put the text in (Brackets) After each Module\n\n**Modules** :control_knobs: \n▬▬▬▬▬▬▬▬▬▬\n<a:ag_arrowgif:781395494127271947> Moderati\
# on :tools: (mod)\n<a:ag_arrowgif:781395494127271947> Invite <a:ag_flyn_hrts_red:781395643134115852>\n<a:ag_arrowgif:781395494127271947> Deletion :x: (delete)\n<a:ag_arrowgif:781395494127271947> Calculation :1234: (calculate)\n<a:ag_arrowgif:781395494127271947> TAX <:ag_tax:807893601244676116> (tax)\n<a:ag_arrowgif:781395494127271947> Ticket System :tickets: (ticket)\n<a:ag_arrowgif:781395494127271947> Embed Creation :card_index: (embed)\n<a:ag_arrowgif:781395494127271947> Say :love_letter: (say)\n<a:ag_arrowgif:781395494127271947> Random :game_die: (random)\n<a:ag_arrowgif:781395494127271947> Date Ti\
# me etc :date: (today)\n<a:ag_arrowgif:781395494127271947> Random Facts :scream: (fact)\n<a:ag_arrowgif:781395494127271947> Weather :white_sun_rain_cloud: (weather)\n<a:ag_arrowgif:781395494127271947> Chat Beta :speech_balloon: (chat)\n<a:ag_arrowgif:781395494127271947> Poll :man_raising_hand: (poll)\n<a:ag_arrowgif:781395494127271947> Suggestion :pencil: (suggest)\n<a:ag_arrowgif:781395494127271947> Dictionary Search <a:ag_book_pgs:781410721397080084> (def,dic)\
# \n<a:ag_arrowgif:781395494127271947> Google Search <a:ag_ggl:781410701327335445> (google)\n<a:ag_arrowgif:781395494127271947> Wikipedia Search :mag: (wiki)\n<a:ag_arrowgif:781395494127271947> AFK :zzz: (afk)\n<a:ag_arrowgif:781395494127271947> Quizz :interrobang: (quiz)\n<a:ag_arrowgif:781395494127271947> My Statistics :level_slider: (stats)\n<a:ag_arrowgif:781395494127271947> Server Statistics :level_slider: (stats)\n▬▬▬▬▬▬▬▬▬▬\n**Example:**\n`a/ embed help`", color=0x01FD14)
# helpmbd.set_image(url="https://cdn.discordapp.com/attachments/829651215235153954/850253992993882142/asteroid1.gif")
# helpmbd.add_field(name="Moderation", value="`Includes a lot of moderation commands needed for maintaning the server.`\n```yaml\na/ mod help```")
# helpmbd.add_field(name="Fun", value="`Imgens, Memes, Quiz, Joke, Facts,etc.`\n```yaml\na/ fun help```")
# helpmbd.add_field(name="Stats", value="`Server, menber info, load, etc`\n```yaml\na/ stats help```")
# helpmbd.add_field(name="Web", value="`Google, Wikipedia, Playstore, Reddit, Dictionary etc\n```yaml\na/ web help```")
# helpmbd.add_field(name="Moderation", value="``\n```yaml\na/ mod help```")
# helpmbd.set_footer(text="INVITE ME => a/ invite")


@client.event
async def on_ready():
    game = discord.Game("with v1.9.0 and Having Fun Testing New Features")
    print("{} is ONLINE!!".format(client.user))

@client.event
async def on_message(message):

    if message.content.startswith("a/ poker help"):
        gmhmbd = discord.Embed(title="Poker Night <:ag_poker:854976463962636339>", description="**Game Info:**\nDiscord Poker Night is a Texas hold 'em style game mode with up to 8 players total per game (you + 7 others) played right within a Discord voice channel. You can also have up to 17 additional spectators max.\n\n**Ingame Items:**\n__Poker Pass__:\nPrice: \nWith Nitro: $4.99\nWithout Nitro: $2.99\n__About:__ The Poker Pass is a one-time purchase that gives players special access to themes and customizations for your Poker experience with friends. Poker Pass does not impact the gameplay dynamics or add any value to the cartoon chips.\n\n**How to Play:**\nComming soon")
        gmhmbd.set_image(url="https://cdn.discordapp.com/attachments/829651215235153954/854972045905494046/pokerni8.png")
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


client.run("NzgwNzM0MDYwMjQ2MDczMzc0.X7zZQQ.BO_zx8evsBwlYUzECe833V2FvL8")
