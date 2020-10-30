
content = 'NIKESPORT-S-280-1509K-NATIONAL-UNIFIED-East'

arr = content.split('-')
# arr[len(arr)-1] = 'QTY'
del arr[len(arr)-1]
new_str = '-'.join(arr)
print(new_str)

# for str in arr:
#     print(str)