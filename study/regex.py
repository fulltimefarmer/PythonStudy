import re

result1 = re.match('page\d{1,2}.json', 'page1.json')
if result1 != None:
    print(result1)
result2 = re.match('page\d{1,2}.json', 'page11.json')
if result2 != None:
    print(result2)
result3 = re.match('page\d{1,2}.json', 'prepost.json')
if result3 != None:
    print(result3)