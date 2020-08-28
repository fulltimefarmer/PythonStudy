import os
import datetime
import time
import json

# file_path1 = '..'+ os.sep + 'file' + os.sep + 'json' + os.sep + 'page13.json'
# print(file_path1)
# dict_data = []
#
# with open(file_path1, 'r+', encoding='utf-8') as file:
#     dict_data = json.load(file)
#     print(dict_data)
#     sdap_list = dict_data['sdap_list']
#     for sdap in sdap_list:
#         sdap['size_qty'] = 8
#
# print(dict_data)
#
# with open(file_path1, 'w+') as file:
#     str_time = datetime.datetime.now().strftime('%Y%m%d%H%M')
#     dict_data['update_time'] = str_time
#     json.dump(dict_data, file)


file_path2 = '..'+ os.sep + 'file' + os.sep + 'json' + os.sep + 'order.json'
print(file_path2)

with open(file_path2, 'r', encoding='utf-8') as file:
    dict_data = json.load(file)
    print(dict_data)
    data = dict_data['data'][0]
    print(data)
    # for order in data:
    #     print(order['id'])
