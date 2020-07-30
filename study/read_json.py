import os
import re
import json

dirpath = '..'+ os.sep + 'file' + os.sep + 'json'
dir = os.listdir(dirpath)

filepath = dirpath + os.sep + 'prepost.json'

# with open(filepath, 'w') as f:
#     json.dump(data, f)

with open(filepath, 'r') as f:
    data = json.load(f)
    print(data)
    data['batch_id'] = 'abc'
    data['total_count'] = 123
    print(data)

# for filename in dir:
#     result = re.match('page\d{1,2}.json', filename)
#     if result != None:
#         filepath = dirpath + os.sep + filename
#         print(filepath)
#         data = json.load(open(filepath))
#         print(data)
#     print('\n')
