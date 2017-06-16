def split_name(list_name):
    new_name = list_name.split('_',1)
    return new_name

def check_assets(lists, dictionary, name):
    for items in dictionary[lists]:
        count = 1
        print(dictionary[lists])
        for row in ws.iter_rows(min_row=2, max_col=1):
            print('Iterating cells in [{0}]'.format(row))
            for cell in row:
                count += 1
                print('Checking cell [{0}] if [{1}] matches [{2}]'.format(cell.coordinate, cell.value, items))
                if cell.value == items:
                    row_num = cell.row
                    print("Match! [{0}] detected in cell [{1}], writing 'X' in cell [{2}]".format(list,cell.coordinate,ws.cell(row=row_num, column=2).coordinate))
                    ws.cell(row=row_num, column=2).value = 'X'
                    ws.cell(row=row_num, column=5).value = int(name[0])
                    ws.cell(row=row_num, column=6).value = name[1]
                    ws.cell(row=row_num, column=7).value = name[1]
                    ws.cell(row=row_num, column=8).value = name[1]
                    ws.cell(row=row_num, column=9).value = name[1]
                    ws.cell(row=row_num, column=10).value = name[1]
                    wb.save('test.xlsx')
                    return [cell, True]

def loop_assets(dictionary):
    for department in dictionary:
        depart_org = department.split('_',1)
        for lists in dictionary[department]:
            check_assets(lists,dictionary[department],depart_org)