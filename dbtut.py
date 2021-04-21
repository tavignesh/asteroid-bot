import platform
import discord
print(help(discord))
print("going again")

print("System: " + platform.system())

print("Architecture: " + platform.architecture()[0])

# machine
print("Machine: " + platform.machine())

# node
print("Node: " + platform.node())

# distribution
dist = platform.dist()
dist = " ".join(x for x in dist)
print("Distribution: " + dist)

print("Memory Info: ")
with open("/proc/meminfo", "r") as f:
    lines = f.readlines()

print("     " + lines[0].strip())
print("     " + lines[1].strip())

print("Processors: ")
with open("/proc/cpuinfo", "r")  as f:
    info = f.readlines()

cpuinfo = [x.strip().split(":")[1] for x in info if "model name"  in x]
for index, item in enumerate(cpuinfo):
    print("    " + str(index) + ": " + item)

uptime = None
with open("/proc/uptime", "r") as f:
    uptime = f.read().split(" ")[0].strip()
uptime = int(float(uptime))
uptime_hours = uptime // 3600
uptime_minutes = (uptime % 3600) // 60
print("Uptime: " + str(uptime_hours) + ":" + str(uptime_minutes) + " hours")

with open("/proc/loadavg", "r") as f:
    print("Average Load: " + f.read().strip())



print("SECOND LEVELS COEDEEEE")


import platform

# Architecture
print("Architecture: " + platform.architecture()[0])

# machine
print("Machine: " + platform.machine())

# node
print("Node: " + platform.node())

# processor
print("Processors: ")
with open("/proc/cpuinfo", "r")  as f:
    info = f.readlines()

cpuinfo = [x.strip().split(":")[1] for x in info if "model name"  in x]
for index, item in enumerate(cpuinfo):
    print("    " + str(index) + ": " + item)

# system
print("System: " + platform.system())

# distribution
dist = platform.dist()
dist = " ".join(x for x in dist)
print("Distribution: " + dist)

# Load
with open("/proc/loadavg", "r") as f:
    print("Average Load: " + f.read().strip())

# Memory
print("Memory Info: ")
with open("/proc/meminfo", "r") as f:
    lines = f.readlines()

print("     " + lines[0].strip())
print("     " + lines[1].strip())

# uptime
uptime = None
with open("/proc/uptime", "r") as f:
    uptime = f.read().split(" ")[0].strip()
uptime = int(float(uptime))
uptime_hours = uptime // 3600
uptime_minutes = (uptime % 3600) // 60
print("Uptime: " + str(uptime_hours) + ":" + str(uptime_minutes) + " hours")



    if message.content.find("a/ data =") !=-1:
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        fetcda = await message.channel.send(embed=discord.Embed(title="Loading Database..", color=0x05FCE2))
        inpdata = message.content.split("=")[1]
        usrnum = collection.find_one({"_id":2344})
        uid = message.author.id
        uid = int(uid)
        adid = f"1{uid}"
        adid = int(adid)
        ingo = 0
        if str(uid) not in usrnum:
            await fetcda.edit(content="new guy u hav 20 space")
            collection.insert_one({"_id":adid})
            collection.update_one({"_id":2344}, {"$set": {str(uid):0}})
            ingo = 1
        elif int(usrnum[str(uid)]) < 20:
            bsz = int(usrnum[str(uid)])
            await fetcda.edit(content=f"you have {19-bsz} threads left. You can get more by deleting some or getting premium(which is free!!)! To know more abt premium use `a/ premium`")
            ingo = 1
        elif int(usrnum[str(uid)]) >= 20:
            await fetcda.edit(embed=discord.Embed(title="Your Database Is Full", description="Your Database has 20 threads, delete some to add more.", color=0xFD7803))
        print(ingo)
        if ingo == 1:
            adng = await message.channel.send(embed=discord.Embed(title="adding..."))
            usrnum = collection.find_one({"_id": 2344})
            print(usrnum)
            adsid = collection.find_one({"_id":int(adid)})
            dataid = randata()
            print(dataid)
            collection.update_one({"_id":adid},{"$set":{dataid:str(inpdata)}})
            newusrn = int(usrnum[str(uid)])
            newusrn += 1
            collection.update_one({"_id":2344}, {"$set": {str(uid):newusrn}})
            print(adsid,usrnum,newusrn)
            print("dooodododoooneee OP")

    if message.content == "a/ data list" or message.content == "a/ list data":
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        usrnum = collection.find_one({"_id": 2344})
        uid = message.author.id
        uid = int(uid)
        adid = f"1{uid}"
        adid = int(adid)
        if str(uid) not in usrnum:
            await fetcda.edit(content="new guy u hav no data sored in our dataB")
        else:
            datadic = collection.find_one({"_id": int(adid)})
            mtstng = ""
            for dataiddd in datadic:
                if dataiddd != "_id":
                    mtstng += f"{dataiddd}     :     {datadic[dataiddd]} \n"
            print(mtstng)
            await message.channel.send(embed=discord.Embed(title="Your Data", description=f"**Data ID\t Data**\n{mtstng}\n\nTo add more data or to delete data use `a/ data help`\nTo get more data space get premium(which is free)"))

    if message.content.startswith("a/ delete data ") or message.content.startswith("a/ data delete "):
        await message.add_reaction("<a:ag_flyn_hrts_cyn:781395468978356235>")
        usrnum = collection.find_one({"_id": 2344})
        uid = message.author.id
        uid = int(uid)
        adid = f"1{uid}"
        adid = int(adid)
        if str(uid) not in usrnum:
            await fetcda.edit(content="new guy u hav no data sored in our dataB")
        else:
            datadic = collection.find_one({"_id": int(adid)})
            print(datadic)


#   key1 : aofads
#   key2 : afoiefio
#
#
