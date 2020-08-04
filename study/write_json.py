import os
import datetime
import time
import json

file_path = '..'+ os.sep + 'file' + os.sep + 'json' + os.sep + 'prepost.json'

dict_data = []

with open(file_path, 'r') as file:
    dict_data = json.load(file)
    print(dict_data)

with open(file_path, 'w') as file:
    str_time = datetime.datetime.now().strftime('%Y%m%d%H%M')
    dict_data['update_time'] = str_time
    json.dump(dict_data, file)
