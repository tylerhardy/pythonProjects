# Imports
import csv, os, openpyxl

# Working Directory
root = os.getcwd()
os.chdir('{0}\\COS Audit\\Managed_Computers\\'.format(root))
wd = os.getcwd()

# Open the Excel Worksheet
mc_wb = openpyxl.load_workbook('COS_Managed_Computers.xlsx')
mc_s = mc_wb.get_sheet_by_name('Managed Computers')

# Open the CSV files
for _lists in os.listdir('.'):
    if not _lists.endswith('.csv'):
        continue    # skip non-csv files
    # print(_lists)
    with open(_lists,'r') as _lists:
        reader = csv.reader(_lists)
        if _lists.name == 'JAMF_Computers.csv':
            break
        for computerName in reader:
            for rowNum in range(2, mc_s.max_row + 1):
                Alread_Listed_Computer_Name = mc_s.cell(row=rowNum, column=1).value
                if Alread_Listed_Computer_Name != computerName[0]:
                    mc_s.cell(row=(len(mc_s['A'])+1), column=1).value = computerName[0]
                elif Alread_Listed_Computer_Name == computerName[0]:
                    mc_s.cell(row=rowNum, column=2).value = 'X'
                    # print(len(mc_s['A']))
                    # print(computerName[0])
                    # print(mc_s.cell(row=(len(mc_s['A'])+1), column=1).value)
    _lists.close()
mc_wb.save('New_File.xlsx')