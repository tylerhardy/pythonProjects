import PyPDF2, os

os.chdir('C:\\Users\\tylerhardy\\Developer\\pythonProjects\\COS Audit\\computer_assets')

pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

# print(pdfFiles)
for i in pdfFiles:
    pdfFileObj = open(i,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # print(pdfReader.numPages)
    pageObj = pdfReader.getPage(0)
    page_list = pageObj.extractText()
    # print(page_list)
    newpagelist = page_list.split('\n')
    # print(newpagelist)
    print(newpagelist[13])