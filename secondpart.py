#Imports
from reportlab.pdfgen import canvas
import io
from reportlab.lib.pagesizes import letter
import random
from PyPDF2 import PdfFileWriter, PdfFileReader
import math
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

#counters
new_page_check = 0
counter_char = 0
ycount = 0
pchecker = 0
pagecounter = 0
string_counter = 0
number = 0


#Writitng specs
intentran = random.randrange(10, 17)
x = 185 + intentran
jumper = 580 #satrting pos - 580 defualt

packet = io.BytesIO()
can = canvas.Canvas(packet, pagesize=letter)


pdfmetrics.registerFont(TTFont('TestFont0', 'BoesJake0-Regular.ttf'))
pdfmetrics.registerFont(TTFont('TestFont1', 'Jakehand1-Regular.ttf'))
pdfmetrics.registerFont(TTFont('TestFont2', 'Jakehand2-Regular.ttf'))


fonts = [ 'TestFont0', 'TestFont1', 'TestFont2',]

def setcolor(can):
    can.setFillColorRGB(0, 0.1, 0.5)


string0 = ""
string1 = "" 
string2 = "" 
string4 = "" 
string5 = "" 
strign6 = "" 
string8 = "" 
string9 = "" 


lines = [5, 9 , 9]
strings = [string0, string1, string2]

while string_counter < len(lines):
    finalsummary = strings[string_counter]
    #setting lines jumped
    linebreaks = lines[string_counter]
    #Eliminating unused characters
    if "[...]" in finalsummary:
        finalsummary = finalsummary.replace("[...]", '')
    if "-" in finalsummary:
        finalsummary = finalsummary.replace("-", "")
    if "As you have read, t" in finalsummary:
        finalsummary = finalsummary.replace("As you have read, t", "T")
    if "1" in finalsummary:
        finalsummary = finalsummary.replace("1", "")
    if "2" in finalsummary:
        finalsummary = finalsummary.replace("2", "")
    if "3" in finalsummary:
        finalsummary = finalsummary.replace("3", "")
    if "4" in finalsummary:
        finalsummary = finalsummary.replace("4", "")
    if "5" in finalsummary:
        finalsummary = finalsummary.replace("5", "")
    if "6" in finalsummary:
        finalsummary = finalsummary.replace("6", "")
    if "7" in finalsummary:
        finalsummary = finalsummary.replace("7", "")
    if "8" in finalsummary:
        finalsummary = finalsummary.replace("8", "")
    if "9" in finalsummary:
        finalsummary = finalsummary.replace("9", "")
    if "0" in finalsummary:
        finalsummary = finalsummary.replace("0", "")
    if ".; . " in finalsummary:
        finalsummary = finalsummary.replace("0", "")
    if "m. t" in finalsummary:
        finalsummary = finalsummary.replace("0", "m t")

    stringfinal = finalsummary
    print(stringfinal)
    characters = ([*stringfinal])
    print(new_page_check)

        


    if number != 4:
        print(number)
        if " Participation (" in _saver[number]:
            jumplines = (linebreaks[string_counter + 1])* 21.7 + 40
        elif len(_saver[number]) < 83:
            jumplines = (linebreaks[string_counter + 1])* 21.7 + 21.7
            # jumplines = (linebreaks[string_counter + 2] - 1)* 22 + 55
        elif len(_saver[number ]) < 160:
            
            jumplines = (linebreaks[string_counter + 1])* 21.7 + 28
        elif len(_saver[number]) < 280:

            jumplines = (linebreaks[string_counter + 1])* 21.7 + 37
        elif len(_saver[number]) < 375:

            jumplines = ((linebreaks[string_counter + 1])-5)* 21.7 + 70
        else:
            jumplines = (linebreaks[string_counter + 1])* 21.7 + 77
        
        jumper = jumper - jumplines
        print(jumper)
    if (jumper) <= 20:
            can.showPage()
            pagecounter += 1
            ycount = 0
            jumper = 749
            new_page_check = 1
            if "Income (Gross Domestic Product" in finalsummary[number]:
                jumplines = 44 + 21.7
            elif len(_saver[number]) < 90:
                jumplines =  21.7 + 21.7
                # jumplines = (linebreaks[string_counter + 2] - 1)* 22 + 55
            elif len(_saver[number ]) < 160:
                
                jumplines =  28 + 21.7
            elif len(_saver[number]) < 280:
        
                jumplines =  37 + 21.7
            elif len(_saver[number]) < 375:
                jumplines = 75 + 21.7 * 4
            else:
                jumplines = 77 + 21.7
            jumper = jumper - jumplines
            print(jumper)
            print(ycount)

    while counter_char < len(characters):
        if "(" in characters[counter_char]:
            pchecker = 1
        if ")" in characters[counter_char]:
            pchecker = 0
            counter_char += 1
        if pchecker == 0:
            dontsize = random.randrange(245, 250)/10
            fontnum = str(random.randrange(0, 2))
            intentran = random.randrange(7, 15) # 20
            wordspacing2 = random.randrange(4, 20) # 33
            char_spacing2 = random.randrange(84, 87) / 10 #94
            charvar = random.randrange(10,  20) / 10
            wordspacing = random.randrange(280, 370) / 10
            
            can.setFont("TestFont" + fontnum, dontsize)
            
            can.drawString(x, (jumper + ycount * 21.7), characters[counter_char], wordSpace= wordspacing, charSpace= charvar)
        
            if characters[counter_char] == " ":
                x = x + wordspacing2 + 3
            else:
                if characters[counter_char] == "W" or characters[counter_char] == "M" or characters[counter_char] == "m" or characters[counter_char] == "w" or characters[counter_char] == "I" or characters[counter_char] == "p" or characters[counter_char] == "D" or characters[counter_char] == "v" or characters[counter_char] == "k" or characters[counter_char] == "T":
                    x = x + (len(characters[counter_char]) * (char_spacing2) + 4)
                else: 
                    x = x + (len(characters[counter_char]) * char_spacing2)
            if x > 490 and characters[counter_char] == " ":
                x = 185 + intentran
                ycount += -1
        counter_char += 1
            
        
    ycount = 0

    x = 185
    counter_char = 0
    string_counter += 1

  

        
can.save()
#move to the beginning of the StringIO buffer
packet.seek(0)
# create a new PDF with Reportlab
new_pdf = PdfFileReader(packet)
# read your existing PDF
existing_pdf = PdfFileReader(open('current.pdf', "rb"))
output = PdfFileWriter()
# add the "watermark" (which is the new pdf) on the existing page
pgcounter2 = 0
while pgcounter2 < pagecounter + 1:
    page = existing_pdf.getPage(pgcounter2)
    page.mergePage(new_pdf.getPage(pgcounter2))
    output.addPage(page)
    pgcounter2 += 1
# finally, write "output" to a real file
outputStream = open("destination.pdf", "wb")
output.write(outputStream)
outputStream.close()
print(linebreaks)


