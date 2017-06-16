#! python3
import csv, os, openpyxl

def pop_list():
    """Searches fo CSV files and create a list with its contents"""
    # Create dict_list
    dict_list = {}
    for csvFilename in os.listdir('.'):
        if not csvFilename.endswith('.csv'):
            continue    # skip non-csv files
        name_var = os.path.splitext(csvFilename)[0]
        # print(name_var)
        with open(csvFilename,'r') as csvFileObj:
            readerObj = csv.reader(csvFileObj)
            var_list = []
            for row in readerObj:
                var_list.append(row)
                dict_list[str(name_var)] = var_list
        csvFileObj.close()
    return dict_list

def match_pc(list,pc_name, list_name):
    """Checks if a PC matches a PC in a list"""
    print(list_name)
    total = 0
    for i in range(0,len(list)):
        total += 1
        if list[i] == pc_name.lower() and list_name == 'AD_Computers':
            # print("{0} Match at {1}".format(pc_name,total))
            mc_s.cell(row=rowNum, column=2).value = 'X'
        elif list[i] == pc_name.lower() and list_name == 'JAMF_Computers':
            mc_s.cell(row=rowNum, column=3).value = 'X'
        elif list[i] == pc_name.lower() and list_name == 'SCCM_Computers':
            mc_s.cell(row=rowNum, column=4).value = 'X'
        else:
            print(list[i])
            mc_s.cell(row=(len(mc_s['A'])+1), column=1).value = list[i]

    return True

def list_lower(list):
    """Converts list to lower"""
    lower_list = []
    for i in list:
        for j in i:
            lower_list.append(j.lower())
    return lower_list

# Change Working Directory
os.chdir('{0}\\COS Audit\\Managed_Computers\\'.format(os.getcwd()))

# Open Excel Workbook
mc_wb = openpyxl.load_workbook('COS_Managed_Computers.xlsx')
mc_s = mc_wb.get_sheet_by_name('Managed Computers')

dict_list = pop_list()

for listObj in dict_list:
    my_var = str(listObj)
    listObj = list_lower(dict_list[listObj])
    for rowNum in range(2, mc_s.max_row + 1):
        computerName = mc_s.cell(row=rowNum, column=1).value
        match_pc(listObj, computerName, my_var)

mc_wb.save('New_File.xlsx')

"""

Start with a blank worksheet
load list of computers names from AD, SCCM, or JAMF
search work sheet for computer, if found then mark X in the column of what list the computer name is being compared (AD, SCCM, or JAMF)
if not found then add computer to the computer column then mark the column where the computer came from (AD, SCCM, or JAMF)


"""