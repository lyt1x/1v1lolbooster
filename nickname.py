import requests
with open("auth-token.txt", 'r') as f:
    token = f.readline()
payload = {
    "nickname": "lyt1x owns you <3"
}
url = "https://us-central1-justbuild-cdb86.cloudfunctions.net/player/nickname"
r = requests.post(url, headers={"auth-token": token}, data=payload)