import datetime
from random import choice
from openpyxl import Workbook
from openpyxl import utils

wb = Workbook()

ws = wb.create_sheet("Sheet1", 0)

ws.append(['TITLE', 'TIME', 'A-Z'])

for i in range(99):
    TITLE = 'No %d' % i
    TIME = datetime.datetime.now().strftime("%H:%M:%S")
    A_Z = utils.get_column_letter(choice(range(1, 50)))
    ws.append([TITLE, TIME, A_Z])

wb.save('../file/test.xlsx')