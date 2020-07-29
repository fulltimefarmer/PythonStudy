import os

filename = '..' + os.sep + 'file' + os.sep + 'sample.txt'

txt = open(filename)

print(txt.read())