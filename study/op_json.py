import os
import datetime
import time
import json

file_path = '..'+ os.sep + 'file' + os.sep + 'json' + os.sep + 'page13.json'
print(file_path)
dict_data = []

with open(file_path, 'r+', encoding='utf-8') as file:
    dict_data = json.load(file)
    print(dict_data)
    sdap_list = dict_data['sdap_list']
    for sdap in sdap_list:
        sdap['size_qty'] = 8

print(dict_data)

with open(file_path, 'w+') as file:
    str_time = datetime.datetime.now().strftime('%Y%m%d%H%M')
    dict_data['update_time'] = str_time
    json.dump(dict_data, file)
