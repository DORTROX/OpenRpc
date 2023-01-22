import subprocess

required_libs = ['pypresence', 'psutil']
installed_libs = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE)
installed_libs = str(installed_libs.stdout, 'utf-8').split('\n')

for lib in required_libs:
    if lib not in installed_libs:
        subprocess.run(["pip", "install", lib])
    else:
        pass

import pypresence
import time
import psutil

rpc = pypresence.Presence("your application id here")
rpc.connect()
letters = ["Web Developer 2k19", "S Developer 2k20", "Cyber Sec 2k21", "Game Dev 2k22"]
letterN = 0
count = 0

while True:
    if (count == 15):
        count = 0
        if (letterN == len(letters)):
            letterN = 0
        else:
            letterN = letterN + 1
    else:
        count = count + 1
    cpu_per = round(psutil.cpu_percent(),1)
    mem = psutil.virtual_memory()
    mem_per = round(psutil.virtual_memory().percent,1)
    rpc.update(large_image="sukuna", large_text="Kaizen Domain Expansion", small_image="qin_shi_huang", small_text="Known 1",state="CPU: " + str(cpu_per) + "% " + "RAM: "+str(mem_per)+"%", details=str(letters[letterN]), buttons= [{"label": "Github","url":"https://github.com/DORTROX"}, {"label": "Instagram","url":"https://www.instagram.com/dortrox4u/"}])
    time.sleep(1)