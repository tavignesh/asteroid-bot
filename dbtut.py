import psutil

cpupers = psutil.cpu_percent(percpu=1)
cpui = psutil.cpu_freq()
cpui = str(cpui)
cpui = cpui.split("=")[-1]
cpui = cpui.split(")")[0]
cpui = float(cpui)
cpui = cpui / 1000
cpuppp = ""
print("printing hereeeeee: ", cpupers)
print(type(cpupers))
for i in range(len(cpupers)):
   cpuo = cpupers[int(i)]
   cpuppp += f"Core{int(i)}: {cpuo}%\n"
   print(cpuppp)