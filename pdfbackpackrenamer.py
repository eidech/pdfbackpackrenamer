from PyPDF2 import PdfReader, PdfWriter
import re, os

def main():
    pdfpath = "C:/Users/ceide/Desktop/Python Scripts/pdfbackpackrenamer/Straight8Merge.pdf"

    # open the PDF
    print("Opening " + pdfpath)
    inputpdf = PdfReader(open(pdfpath, "rb"))

    for i in range(len(inputpdf.pages)):

        # get the page
        pdfpage = inputpdf.pages[i]
        pagetext = pdfpage.extract_text()
        
        # set up the output
        output = PdfWriter()
        output.add_page(pdfpage)

        # parse the PDF for the student number
        studentnumber = re.search('[0-9]{8}|[0-9]{7}', pagetext).group(0)

        outputpath = "C:/Users/ceide/Desktop/Python Scripts/pdfbackpackrenamer/output/" + studentnumber + ".pdf"

        # check to see if file already exists; if not, write it
        if not os.path.exists(outputpath):
            with open(outputpath, "wb") as outputStream:
                output.write(outputStream)
                print(outputpath + " created")

if __name__== "__main__":
    main()