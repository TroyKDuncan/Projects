import PyPDF2

with open('dummy.pdf', 'rb') as file:  # make sure to use rb for the mode as read binary
    reader = PyPDF2.PdfFileReader(file)  # reader object
    page = reader.getPage(0)  # page object
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()  # writer object
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)