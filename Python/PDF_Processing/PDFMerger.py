# run python3 PDFMerger.py [enter as many files as you want]
# this will merge all the PDFs into one in the order they are entered

import PyPDF2
import sys
import os


inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    print('Order of appending:\n')
    order = 1
    for pdf in pdf_list:
        merger.append(pdf)
        print(f'{order}. {pdf}')
        order += 1
    print()
    merger.write('super.pdf')  # overwrites whatever is there

pdf_combiner(inputs)