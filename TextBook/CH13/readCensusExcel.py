import openpyxl, pprint

print('ワークブックを開いています...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
county_data = {'AK': {'Aleutians East': {'pop': 3141, 'tracts': 1}, 'Aleutians West': {'pop': 5561, 'tracts' 2}, 

print('行を読み込んでいます...')
for row in range(2, sheet.max_row):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

