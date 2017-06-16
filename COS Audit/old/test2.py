# Imports
import csv, os, openpyxl

# Global Variables


# Working Directory
root = os.getcwd()
os.chdir('{0}\\COS Audit\\'.format(root))
wd = os.getcwd()

# Open the Excel Worksheet
mc_wb = openpyxl.load_workbook('COS_Managed_Computers.xlsx')
mc_s = mc_wb.get_sheet_by_name('Managed Computers')

# Worksheet Headers
h_computers = mc_s['A1']
h_ad = mc_s['B1']
h_sccm = mc_s['C1']
h_jamf = mc_s['D1']
h_notes = mc_s['E1']

# Working Directory
# print(os.getcwd())
os.chdir('{0}\\Managed_Computers\\'.format(os.getcwd()))
# print(os.getcwd())

# For Each File
for _list in os.listdir('.'):
    if not _list.endswith('.csv'):
        continue    # skip non-csv files
    # print(_list)
    with open(_list,'r') as csv_input:
        if '\0' in open(_list).read():
            # print('Null Byte')
            reader = csv.reader(x.replace('\0','') for x in csv_input)
        else:
            # print('No Null Byte')
            reader = csv.reader(csv_input)
        for row in reader:
            print(row[0])
            for cellObj in next(mc_s.columns):
                print(cellObj.value)
                # print(row[0])
                if cellObj.value == row[0]:
                    print("Matched")
                    break
