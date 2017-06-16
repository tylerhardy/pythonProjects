import sqlite3, os, csv, openpyxl, datetime
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Protection, Font
"""
1. Grab headers
2. Map headers to db columns
3. Check if key column has value
    if value - new dict > add key (asset_tag) value (WS0002131) to 

    else pass
"""

conn = sqlite3.connect("blah.db")
c = conn.cursor()

"""Searches fo CSV files and create a list with its contents"""
# Create dict_list
dict_list = {}
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue    # skip non-csv files
    name_var = os.path.splitext(csvFilename)[0]
    # print('Getting list of assets from [{0}]'.format(name_var))
    with open(csvFilename,'r') as csvFileObj:
        readerObj = csv.reader(csvFileObj)
        var_list = []
        hrow = next(readerObj)
        print(hrow)
        
        asset_id = hrow.index('D_CODE')
        type_id = hrow.index('D_TYPE')
        serial_id = hrow.index('D_SERIAL_NUM')
        location_id = hrow.index('D_LOCN_CODE_RESP')
        description_id = hrow.index('D_DESC')
        for row in readerObj:
            if row[type_id] == 'PC' or  row[type_id] == 'LT':
                var_list.append([row[asset_id]])
                dict_list[str(name_var)] = var_list
    csvFileObj.close()

for k, v in hrow:
    print(k)
