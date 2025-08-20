import requests
with open("auth-token.txt", 'r') as f:
    token = f.readline()
url = "https://us-central1-justbuild-cdb86.cloudfunctions.net/player/updateProgressAndStats?gameMode=1v1_Competitive&isVictory=true&killsCount=-20000000000&deathsCount=0&isCompetitive=true&isBox=false"
r = requests.get(url, headers={"auth-token": token})