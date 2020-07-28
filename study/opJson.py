import os
import re
import json

dirpath = '..'+ os.sep + 'file' + os.sep + 'json'

dir = os.listdir(dirpath)

for filename in dir:
    result = re.match('page\d{1,2}.json', filename)
    if result != None:
        filepath = dirpath + os.sep + filename
        print(filepath)
        data = json.load(open(filepath))
        print(data)
    print('\n')
