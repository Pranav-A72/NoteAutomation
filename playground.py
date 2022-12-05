import fpdf 
from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
packet = io.BytesIO()
import random
string0 = "sample"
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
x = 175


from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('TestFont0', 'Anuraagpranav1-Regular.ttf'))
pdfmetrics.registerFont(TTFont('TestFont1', 'Anuraagpranav2-Regular.ttf'))
pdfmetrics.registerFont(TTFont('TestFont2', 'Anuraagpranav3-Regular.ttf'))
# pdfmetrics.registerFont(TTFont('TestFont3', 'Boesjake3-Regular.ttf'))
# pdfmetrics.registerFont(TTFont('TestFont4', 'Boesjake4-Regular.ttf'))
# pdfmetrics.registerFont(TTFont('TestFont5', 'Boesjake5-Regular.ttf'))
# pdfmetrics.registerFont(TTFont('TestFont6', 'Boesjake6-Regular.ttf'))
# pdfmetrics.registerFont(TTFont('TestFont7', 'Boesjake7-Regular.ttf'))

fonts = ['TestFont', 'TestFont1', 'TestFont2']
dontsize = random.randrange(190, 210)/10
fontnum = random.randrange(0, 7)
string_counter = 0

def setcolor(can):
    can.setFillColorRGB(0, 0.1, 0.5)
can.line(2,2,2, 2)
jumper = 502

# while string_counter < len(lines):
print(string_counter)
stringfinal = strings[string_counter]
print(stringfinal)
characters = ([*stringfinal])
print(string_counter)
jumplines = (lines[string_counter] - 1)* 22
while counter_char < len(characters):
    
    dontsize = random.randrange(285, 290)/10
    fontnum = str(random.randrange(0, 3))
    intentran = random.randrange(2, 3)
    wordspacing = random.randrange(7, 12)
    char_spacing2 = random.randrange(84, 87) / 10
   
    can.setFont("TestFont" + fontnum, dontsize)
    def setcolor(can):
        if characters[counter_char] == ".":
            can.drawString(x, 3+jumper + ycount * 21.7, characters[counter_char], wordSpace= 10, charSpace= 1.5)
        else:
            can.drawString(x, jumper + ycount * 21.7, characters[counter_char], wordSpace= 10, charSpace= 1.5)
    setcolor(can)
    if characters[counter_char] == " ":
        x = x + wordspacing #+ 3
    else:
        Hoangletters0 = [ "h", "p", "o", "B"]
        Hoangletters2 = ["H", "m", ]
        Hoangletters1 = ["w", "M"]
        if characters[counter_char] in Hoangletters0:
            x = x + (len(characters[counter_char]) * (char_spacing2) + 2)
        elif characters[counter_char] in Hoangletters1:
            x = x + (len(characters[counter_char]) * (char_spacing2) + 7)
        elif characters[counter_char] in Hoangletters2: 
            x = x + (len(characters[counter_char]) * (char_spacing2) + 5)
        else: 
            x = x + (len(characters[counter_char]) * char_spacing2)
        zero=0
    if x > 500 and characters[counter_char] == " ":
        x = 175 + intentran
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
page = existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)
# page = existing_pdf.getPage(1)
# page.mergePage(new_pdf.getPage(1))
# output.addPage(page)
# finally, write "output" to a real file
outputStream = open("destination.pdf", "wb")
output.write(outputStream)
outputStream.close()