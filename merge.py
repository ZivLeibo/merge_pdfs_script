from PyPDF2 import PdfFileMerger
from pathlib import Path

pdfs = []
num = 13

merger = PdfFileMerger()

for i in range(num):
    try:
        merger.append("files/" + str(i+1) + '.pdf')
    except FileNotFoundError:
        merger.append("files/" + str(i + 1) + 'a.pdf')
        merger.append("files/" + str(i + 1) + 'b.pdf')


merger.write("result.pdf")
merger.close()

print("done")