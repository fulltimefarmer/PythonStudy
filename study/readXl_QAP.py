from openpyxl import load_workbook

wb_key_look_mapping = load_workbook('../file/key_look_mapping.xlsx')
#wb_ae_qap = load_workbook('../file/ae_qap.xlsx')

ws_key_look_mapping = wb_key_look_mapping.worksheets[0]
#ws_ae_qap = wb_ae_qap.worksheets[0]

dict_key_look_mapping = {}

for row in ws_key_look_mapping.rows:
    dict_data = {'concept': row[1].value, 'key': row[2].value}
    dict_key_look_mapping[row[0].value] = dict_data
    # for cell in row:
    #     print(cell.value, end='\t\t')
    # print('\n')

for k in dict_key_look_mapping.keys():
    print(k, dict_key_look_mapping[k])


