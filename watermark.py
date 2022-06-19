from re import template
import PyPDF2

Template = PyPDF2.PdfFileReader(open('./pdf-playground/super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('./pdf-playground/wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(Template.getNumPages()):
    page = Template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermark.pdf', 'wb') as my_file:
        output.write(my_file)
