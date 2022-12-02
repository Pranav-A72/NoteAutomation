import fpdf 
from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
packet = io.BytesIO()
import random
string0 = "Test"
string1 = "GDP and GNP are ways of measuring economic growth within a country. Formal and inform sectors are things. Informal is like government and stuff anf formal is another thing that relates to sectors."
string2 = 'In addition to classifying economic sectors, the structure of an economy can also be broken into two categories: the formal sector and the informal sector. The formal sector includes businesses, enterprises, and other economic activities that have government supervision, monitoring, and protection, and are taxed.'
lines = [5, 9 , 9]
strings = [string0, string1, string2]
# characters = string.split()
characters = ([*string0])
counter_char = 0
can = canvas.Canvas(packet, pagesize=letter)
ycount = 0
intentran = random.randrange(10, 17)
x = 190


from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('TestFont0', 'Myfont-Regular.ttf'))
# pdfmetrics.registerFont(TTFont('TestFont1', 'Jakehand1-Regular.ttf'))
# pdfmetrics.registerFont(TTFont('TestFont2', 'Jakehand2-Regular.ttf'))
# pdfmetrics.registerFont(TTFont('TestFont3', 'Boesjake3-Regular.ttf'))
# pdfmetrics.registerFont(TTFont('TestFont4', 'Boesjake4-Regular.ttf'))
# pdfmetrics.registerFont(TTFont('TestFont5', 'Boesjake5-Regular.ttf'))
# pdfmetrics.registerFont(TTFont('TestFont6', 'Boesjake6-Regular.ttf'))
# pdfmetrics.registerFont(TTFont('TestFont7', 'Boesjake7-Regular.ttf'))

# fonts = ['TestFont', 'TestFont1', 'TestFont2', 'TestFont3', 'TestFont4', 'TestFont5', 'TestFont6', 'TestFont7']
dontsize = random.randrange(190, 210)/10
fontnum = random.randrange(0, 7)
string_counter = 0

def setcolor(can):
    can.setFillColorRGB(0, 0.1, 0.5)
can.line(2,2,2, 2)
jumper = 749 - 23.8 * 2
setcolor(can)
# while string_counter < len(lines):
print(string_counter)
stringfinal = strings[string_counter]
print(stringfinal)
characters = ([*stringfinal])
print(string_counter)
can.showPage()
can.showPage()
jumplines = (lines[string_counter] - 1)* 22
while counter_char < len(characters):
    
    dontsize = random.randrange(245, 250)/10
    fontnum = str(random.randrange(0, 2))
    intentran = random.randrange(7, 20)
    wordspacing2 = random.randrange(4, 33)
    char_spacing2 = random.randrange(84, 92) / 10
    charvar = random.randrange(10,  20) / 10
    wordspacing = random.randrange(280, 370) / 10
    def setcolor(can):
        can.drawString(x, jumper + ycount * 21.7, characters[counter_char], wordSpace= 10, charSpace= 1.5)
    setcolor(can)
    if characters[counter_char] == " ":
        x = x + wordspacing2 + 3
    else:
        if characters[counter_char] == "m" or characters[counter_char] == "w" or characters[counter_char] == "I" or characters[counter_char] == "p" or characters[counter_char] == "D" or characters[counter_char] == "v" or characters[counter_char] == "k" or characters[counter_char] == "T":
            x = x + (len(characters[counter_char]) * (char_spacing2) + 5)
        else: 
            x = x + (len(characters[counter_char]) * char_spacing2)
    if x > 500 and characters[counter_char] == " ":
        x = 185 + intentran
        ycount += -1
    counter_char += 1
    if (jumper + ycount * 21.7) <= 0:
        can.showPage()
        ycount = 0
        jumper = 577
ycount = 0
jumper = jumper - jumplines
x = 185
string_counter += 1
counter_char = 0

can.save()
#move to the beginning of the StringIO buffer
packet.seek(0)
# create a new PDF with Reportlab
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open('current.pdf', "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
page = existing_pdf.getPage(2)
page.mergePage(new_pdf.getPage(2))
output.addPage(page)
# page = existing_pdf.getPage(1)
# page.mergePage(new_pdf.getPage(1))
# output.addPage(page)
# finally, write "output" to a real file
outputStream = open("destination.pdf", "wb")
output.write(outputStream)
outputStream.close()
