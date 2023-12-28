import requests, json
r = requests.get('https://api.ipify.org?format=json')
ip = json.loads(r.text)['ip']
print(ip)