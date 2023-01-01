from PyPDF2 import PdfMerger

from constants import OUTPUT_PDF, PDF_FOLDER


def merge_prints(badges):
    merger = PdfMerger()

    for fandom in badges.keys():
        for badge in badges[fandom]:
            for i in range(badge["qty"]):
                merger.append(f"{PDF_FOLDER}{fandom}/{badge['name']}.pdf")
    merger.write(OUTPUT_PDF)
    merger.close()
    print(f"File created in {OUTPUT_PDF}")
