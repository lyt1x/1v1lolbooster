import requests
import json
with open('tokens.json','r') as f:
    data = json.load(f)
with open('person.txt','r') as f:
    person = f.readline()
url = 'https://securetoken.googleapis.com/v1/token?key=AIzaSyBPrAfspM9RFxuNuDtSyaOZ5YRjDBNiq5I'
payload = {
    "grant_type": "refresh_token",
    "refresh_token": data[person]
}
r = requests.post(url,data=payload)
print(r.text)
auth_token = r.text.split(',')
for i in range(len(auth_token)):
    if '"access_token"' in auth_token[i]:
        new_token = auth_token[i]
        break
new_token = new_token.replace('{','')
new_token = new_token.replace('"access_token"','')
new_token = new_token.replace('"','')
new_token = new_token.replace(':','')
new_token = new_token.replace(' ','')
new_token = new_token.replace('''
''','')
with open('auth-token.txt','w') as f:
    f.write(new_token)