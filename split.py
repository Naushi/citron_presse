import glob
import os
from PyPDF2 import PdfFileWriter, PdfFileReader


def list_files():
    for f in glob.glob('./PDF/**/*.pdf', recursive=True):
        split_file(f)

def split_file(filename: str):
    print(f"Handling {filename}")
    pdf_name = os.path.basename(filename)[:-4]
    pdf_path = os.path.dirname(filename)
    input_pdf = PdfFileReader(filename)
    for page_number in range(0, len(input_pdf.pages)):
        output = PdfFileWriter()
        page_filename = f"{pdf_path}/{pdf_name}-{page_number}.pdf"
        print(page_filename)
        output.addPage(input_pdf.getPage(page_number))
        with open(page_filename, "wb") as output_stream:
            output.write(output_stream)

if __name__ == "__main__":
    list_files()