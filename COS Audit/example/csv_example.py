import csv, os, codecs
root = os.getcwd()
print(root)
os.chdir('{0}\\COS Audit\\'.format(root))
wd = os.getcwd()
print(wd)
# exampleFile = open('example.csv')
# exampleReader = csv.reader(exampleFile)
# exampleData = list(exampleReader)
# print(exampleData)

with open('AD_computers.csv', 'r', encoding='utf=16') as readFile:
    reader = csv.DictReader(readFile)
    csvRows = []
    for line in reader:
        csvRows.append(line['computers'])
    print(csvRows)

with open('COS_Audit.csv','w') as writeFile:
    fieldnames = ['AD_Computers', 'SCCM_Computers']
    writer = csv.DictWriter(writeFile, fieldnames=fieldnames)
    writer.writeheader()
    for row in csvRows:
        writer.writerow(row)


outputFile = open('output.csv','w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam','eggs','bacon','ham'])
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1,2,3.141592,4])
outputFile.close()

csvFile = open('example.tsv', 'w', newline='')
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
csvWriter.writerow(['apples', 'oranges', 'grapes'])
csvWriter.writerow(['eggs', 'bacon', 'ham'])
csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
csvFile.close()

