import requests
import os
while True:
    with open("auth-token.txt",'r') as f:
        token = f.readline()
    try:
        url = "https://us-central1-justbuild-cdb86.cloudfunctions.net/player/updateProgressAndStats?gameMode=1v1_Competitive&isVictory=true&killsCount=1&deathsCount=0&isCompetitive=true&isBox=false"
        #url = "https://us-central1-justbuild-cdb86.cloudfunctions.net/player/updateProgressAndStats?gameMode=BattleRoyale_Teams_4v4&isVictory=true&killsCount=0&deathsCount=0&isCompetitive=false&isBox=false"
        r = requests.get(url,headers={"auth-token": token})
        with open('header.txt','w') as f:
            f.write(r.text)
    except Exception as e:
        os.system('python booster.py')
        exit()