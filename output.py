from colorama import Fore, init
from cfonts import render, say
import time
import os
import requests
import subprocess
import json
elo = 'none'
name = 'none'
output = render('booster', gradient=['red','blue'])
os.system('cls')
print(output)
print(f"""
			{Fore.LIGHTRED_EX}lyt1x#6666 / Stormy{Fore.RESET}
""")
exec(open("refresh.py").read())
print('#=========================================================================================#')
print('')

with open("auth-token.txt", 'r') as f:
    token = f.readline()
url = "https://us-central1-justbuild-cdb86.cloudfunctions.net/player/updateProgressAndStats?gameMode=1v1&isVictory=true&killsCount=1&deathsCount=0&isCompetitive=false&isBox=false"
r = requests.get(url,headers={"auth-token": token})
with open('header.txt', 'w') as f:
    f.write(r.text)
with open('header.txt','r') as f:
    header = f.readline()
text = header.split(',')
both = 0
for i in range(len(text)):
    if both == 2:
        break
    if '"CustomRating"' in text[i]:
        elo = text[i]
        elo = elo.replace('"CustomRating":', '')
        elo = elo.replace('{', '')
        elo = elo.replace('}', '')
        both += 1
    elif '"Nickname"' in text[i]:
        name = text[i]
        name = name.replace('"Nickname":','')
        name = name.replace('{','')
        name = name.replace('}','')
        name = name.replace('"','')
        both += 1
print(f'[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Logged Into: {Fore.LIGHTRED_EX}{name}{Fore.RESET}')
print('')
print(f'[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Account Elo: {Fore.LIGHTRED_EX}{elo}{Fore.RESET}')
print('')
print('#=========================================================================================#')
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