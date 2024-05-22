# sys.argv[1] is the source
# sys.argv[2] is the watermark
# sys.argv[3] is the destination file

import PyPDF2
import sys


template = PyPDF2.PdfFileReader(open(sys.argv[1], 'rb'))
watermark = PyPDF2.PdfFileReader(open(sys.argv[2], 'rb'))
destination = sys.argv[3]
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open(sys.argv[3], 'wb') as output_file:
        output.write(output_file)