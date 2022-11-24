import fpdf 
from fpdf import FPDF

from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


pdf = FPDF()
pdf.add_page()

#Really Jake? I had to install a font named MyFont? I told you to change this
pdf.set_font("arial", "", 20)

pdf.set_xy(100, 50)

with open("Output.txt") as f:
    lines = f.readlines()

text = ("").join(lines)

pdf.multi_cell(w= 200, h=50, txt=text, align="L")

pdf.output("testoverlay_out.pdf")


"""
packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)
can.drawString(10, 100, "Hello world")
can.save()

#move to the beginning of the StringIO buffer
packet.seek(0)

# create a new PDF with Reportlab
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open("original.pdf", "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# finally, write "output" to a real file
outputStream = open("destination.pdf", "wb")
output.write(outputStream)
outputStream.close()

"""