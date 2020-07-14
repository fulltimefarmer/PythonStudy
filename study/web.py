import requests
import json

url = "https://scapi-qa.nike.com/move/auth/v1/public/get_token_by_pwd"
headers = {'Content-Type': 'application/json'}
data = json.dumps({"username":"admin", "password":"1234", "projectId":1})

#resp = requests.get('https://github.com/timeline.json')
resp = requests.post(url=url, data=data, headers=headers)

resp.encoding = 'utf-8'
isOk = resp.ok
print('isOk: %s' % isOk)
json = resp.json()
print('json: %s' % json)
