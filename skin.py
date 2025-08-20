from colorama import Fore, init
from cfonts import render, say
import time
import os
import requests
import subprocess
import json
name = 'none'
output = render('skins', gradient=['red','blue'])
os.system('cls')
print(output)
print(f"""
			{Fore.LIGHTRED_EX}lyt1x#6666 / inspired by doop#0001{Fore.RESET}
""")
exec(open("refresh.py").read())
print('[=========================================================================================]')
print('')

with open("auth-token.txt", 'r') as f:
    token = f.readline()
url = "https://us-central1-justbuild-cdb86.cloudfunctions.net/player"
r = requests.get(url,headers={"auth-token": token})
text = r.text.split('],')
text2 = r.text.split(',')
skinlist = {
    'Default': 'Default',
    'lol.1v1.playerskins.pack.1': 'Agent Olivia',
    'lol.1v1.playerskins.pack.2': 'SWAT',
    'lol.1v1.playerskins.pack.3': 'XBOT',
    'lol.1v1.playerskins.pack.4': 'Skater Boy',
    'lol.1v1.playerskins.pack.5': 'Lola',
    'lol.1v1.playerskins.pack.6': 'Ninja',
    'lol.1v1.playerskins.pack.7': 'Caty',
    'lol.1v1.playerskins.pack.8': 'Beach Girl',
    'lol.1v1.playerskins.pack.9': 'LOL Pump',
    'lol.1v1.playerskins.pack.10': 'Rey',
    'lol.1v1.playerskins.pack.11': 'Justin',
    'lol.1v1.playerskins.pack.12': 'Hot Dog Man',
    'lol.1v1.playerskins.pack.13': 'Zombie (Female)',
    'lol.1v1.playerskins.pack.14': 'Zombie (Male)',
    'lol.1v1.playerskins.pack.15': 'Regular Zombie',
}

skins = ''
for i in range(len(text)):
    if '"CharacterSkins"' in text[i]:
        skins = text[i]
        break
for i in range(len(text2)):
    if '"Nickname"' in text2[i]:
        name = text2[i]
        name = name.replace('"Nickname":','')
        name = name.replace('{','')
        name = name.replace('}','')
        name = name.replace('"','')
skins = skins.split(',')
hisskins = []
for i in range(len(skins)):
    skin = skins[i]
    skin = skin.replace('"','')
    if skin in skinlist:
        hisskins.append(skinlist[skin])
print(hisskins)
print(f'[{Fore.LIGHTYELLOW_EX}>{Fore.RESET}] Logged Into: {Fore.LIGHTRED_EX}{name}{Fore.RESET}')
print('')
print('[#]=========================================================================================]')
print('')
keyy = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
print(f'[{Fore.LIGHTRED_EX}>{Fore.RESET}] Key for {Fore.LIGHTRED_EX}{name}{Fore.RESET}: {keyy}')
print('')
key = requests.get('https://pastebin.com/raw/SS3HbSPT')
try:
    if keyy in key.text:
        pass
    else:
        print(f'[{Fore.LIGHTRED_EX}>{Fore.RESET}] Key declined...')
        time.sleep(5)
        os._exit(0)
except:
    print(f"[{Fore.LIGHTRED_EX}>{Fore.RESET}] Couldn't connect to the database")
    time.sleep(5)
    os._exit(0)
print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Key accepted!')
print('')
input(f'[{Fore.LIGHTRED_EX}>{Fore.RESET}] Press "Enter" to start the boosting proccess: ')
print('')
print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Boosting Started!')
print('')
init(convert=True)
auth = 0
while True:
    with open('header.txt','r') as f:
        header = f.readline()
    if header == '{}':
        auth += 1
    text = header.split(',')
    for i in range(len(text)):
        if '"CustomRating"' in text[i]:
            elo = text[i]
            elo = elo.replace('"CustomRating":', '')
            elo = elo.replace('{', '')
            elo = elo.replace('}', '')
            break
    try:
        print(f"[{Fore.LIGHTMAGENTA_EX}ELO{Fore.RESET}] {elo}")
    except Exception as e:
        print(e)
    if auth == 1:
        print(f"{Fore.LIGHTGREEN_EX}The current auth token stopped working, getting a new one{Fore.RESET}")
        exec(open("refresh.py").read())
        auth = 0
    time.sleep(1)