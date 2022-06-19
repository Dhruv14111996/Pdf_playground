import PyPDF2
# import sys


with open('./pdf-playground/super.pdf', 'rb') as my_file:  # rb define "Readbinary mode."
    reader = PyPDF2.PdfReader(my_file)
    print(reader.numPages)

# Below program is use to merge two pdf file and generate new pdf file.

t1 = PyPDF2.PdfFileReader(open('./pdf-playground/dummy.pdf', 'rb'))
t2 = PyPDF2.PdfFileReader(open('./pdf-playground/twopage.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(t1.getNumPages()):
    page = t1.getPage(i)
    output.addPage(page)
for j in range(t2.getNumPages()):
    page = t2.getPage(j)
    output.addPage(page)
    page.mergePage(page)

    with open('super.pdf', 'wb') as file:
        output.write(file)
