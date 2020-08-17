import re

str1 = 'SP21_pousheng_Test_20200817143705'
str2 = 'BUFFER_BUY-f2cd3dfd-8096-4587-92ac-b2aa22000a0b'
pattern = '^BUFFER_BUY'

result1 = re.match(pattern, str1)
if result1 != None:
    print(result1.group())

result2 = re.match(pattern, str2)
if result2 != None:
    print(result2.group())

# result3 = re.match('page\d{1,2}.json', 'prepost.json')
# if result3 != None:
#     print(result3)
