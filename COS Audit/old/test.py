import csv, os, codecs
root = os.getcwd()
print(root)
os.chdir('{0}\\COS Audit\\'.format(root))
wd = os.getcwd()
print(wd)

# with open('AD_computers.csv', 'r', encoding='utf=16') as readFile:
#     reader = csv.reader(readFile)
#     csvRows = []
#     for line in reader:
#         csvRows.append(line)
#     print(csvRows)
#     readFile.close()

# with open('COS_Audit.csv','w', newline='', encoding='utf=16') as writeFile:
#     # fieldnames = ['AD_Computers', 'SCCM_Computers']
#     # writer = csv.DictWriter(writeFile, fieldnames=fieldnames)
#     writer = csv.writer(writeFile)
#     # writer.writeheader()
#     for row in csvRows:
#         writer.writerow(row)
#     writeFile.close()

with open('AD_computers.csv','r',encoding='utf-16') as csvinput:
    with open('COS_Audit.csv','w',encoding='utf-16') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)

        all = []
        all.append(['AD Computers'])

        for row in reader:
            all.append(row)
        writer.writerows(all)
        csvinput.close()
        csvoutput.close()