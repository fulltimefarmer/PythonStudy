import requests

resp = requests.get('https://github.com/timeline.json')

resp.encoding = 'utf-8'
isOk = resp.ok
print('isOk: %s' % isOk)
json = resp.json()
print('json: %s' % json)
