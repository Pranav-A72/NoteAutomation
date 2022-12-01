import tkinter as tk
from tkinter import filedialog
import requests
from reportlab.pdfgen import canvas
import io
from reportlab.lib.pagesizes import letter
packet = io.BytesIO()
import random
from PyPDF2 import PdfFileWriter, PdfFileReader
new_page_check = 0
counter_char = 0
can = canvas.Canvas(packet, pagesize=letter)
ycount = 0
intentran = random.randrange(10, 17)
x = 185 + intentran
import math
pchecker = 0

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

#toauto check every answer mark as True
forcedanswertoggle = True

pdfmetrics.registerFont(TTFont('TestFont0', 'Boesjake0-Regular.ttf'))
pdfmetrics.registerFont(TTFont('TestFont1', 'Jakehand1-Regular.ttf'))
pdfmetrics.registerFont(TTFont('TestFont2', 'Jakehand2-Regular.ttf'))
pdfmetrics.registerFont(TTFont('TestFont3', 'Boesjake3-Regular.ttf'))
pdfmetrics.registerFont(TTFont('TestFont4', 'Boesjake4-Regular.ttf'))
pdfmetrics.registerFont(TTFont('TestFont5', 'Boesjake5-Regular.ttf'))
pdfmetrics.registerFont(TTFont('TestFont6', 'Boesjake6-Regular.ttf'))
pdfmetrics.registerFont(TTFont('TestFont7', 'Boesjake7-Regular.ttf'))

pagecounter = 0

fonts = [ 'TestFont0', 'TestFont1', 'TestFont2', 'TestFont3', 'TestFont4', 'TestFont5', 'TestFont6', 'TestFont7']
dontsize = random.randrange(190, 210)/10
fontnum = random.randrange(1, 7)
string_counter = 0
def setcolor(can):
    can.setFillColorRGB(0, 0.1, 0.5)
can.line(2,2,2, 2)
jumper = 580


root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

from PyPDF2 import PdfReader
corneltext = '' 
reader = PdfReader(file_path)
pageNum = reader.getNumPages() - 1
while pageNum > -1:
    page = reader.pages[pageNum]
    corneltext = page.extract_text() + corneltext
    pageNum -= 1

cornel_splited_str = corneltext.splitlines(True)
timesused = 0

emptycounter = 0
emptylimits = len(cornel_splited_str)


removed = 0

print("hi")
print(cornel_splited_str[2])
print("    ")
counter5 = 0
blanks = ["   \n", "  \n", " \n"]
while counter5 < len(cornel_splited_str) - 1:
    # if cornel_splited_str[counter5] == blanks:
    #     cornel_splited_str.pop[counter5]
    # else:

    if cornel_splited_str[counter5 + 1] == "   \n" or cornel_splited_str[counter5 + 1] == "  \n" or cornel_splited_str[counter5 + 1] == " \n" or cornel_splited_str[counter5] == "   \n" or cornel_splited_str[counter5] == "  \n" or cornel_splited_str[counter5] == " \n":
        
        counter5 += 1
       
    else:
        if "\n" in cornel_splited_str[counter5 + 1]:
            placehold = cornel_splited_str[counter5]
            cornel_splited_str[counter5] = placehold.replace('\n', ' ')
        cornel_splited_str[counter5] = cornel_splited_str[counter5] + cornel_splited_str[counter5 + 1]
        cornel_splited_str.pop(counter5 + 1)
print(cornel_splited_str)

# print(cornel_splited_str[2])
_saver = cornel_splited_str.copy()
print(_saver[2])
empty_cornel = cornel_splited_str
print(_saver[2])

print("hey")
print(cornel_splited_str[2])

# print(empty_cornel)

empty_counter2 = 0

edit_emptycornel = empty_cornel
# print(edit_emptycornel[2])

redundent_words = [' the ', ' that ', ' for ', ' two ', ' an ', ' it ', ' than ', 'Notes', 'Cornell', 'Questions', ' does ', ' or ', ' from ', ' to ', ' and ', "(", ")", ".", ",", "?", " is ", " important", "Study", "Describe", " are ", " of ", " Date ", " Name ", ":", " Class ", "/", " Period ", "5", "6", "7", "8", "9", "0", ' as', ' by', ' in ', "As ", '\'', " do", " most ", " we", " a ", "1", "2", "3", "4", " world ", " level ", " regard ", " people " " v ", " vs ", " role ", " at ", "Look ", " look ", "Why ", "How ", "What ", "Who ", "Where ", ' why ', " what ", " how ", ' who ', ' when ', ' where ', '’s', 'v.', "v ", " high ", " low", "with ", " see ", " per ", " used ", " factors ", " money ", " in ", " countries ", "theredifference", "measurecountry", " population ", " work ", " collected", " but ", " about ", " benefit ", " value "]
empty_counter = 0
emptylimits = len(redundent_words)

while empty_counter2 < len(edit_emptycornel) - 1:
    words_cornel = edit_emptycornel[empty_counter2]
    while empty_counter < emptylimits - 1:
        if empty_counter >= len(redundent_words) - 1:
            empty_counter = emptylimits
        else:
            if redundent_words[empty_counter] in words_cornel:
                if redundent_words[empty_counter] == "\n" or redundent_words[empty_counter] == "'":
                     words_cornel = words_cornel.replace(redundent_words[empty_counter], ' ')
                else:
                    words_cornel = words_cornel.replace(redundent_words[empty_counter], ' ')
                empty_counter += 1
                # print(empty_counter)
            else:
                empty_counter += 1
                # print(empty_counter)
    edit_emptycornel[empty_counter2] = words_cornel
    empty_counter2 += 1
    # print(empty_counter2)
    empty_counter = 0

print(_saver[2])

print(edit_emptycornel[28])
morewords_cornel = edit_emptycornel[28].split()
print(morewords_cornel)

counter58 = 2
ncounter = 0
linebreaks = []
while counter58 < len(_saver):
    if _saver[counter58] == ' \n' or _saver[counter58] == '  \n' or _saver[counter58] == '   \n' or _saver[counter58] == '    \n':
        ncounter += 1
    else:
        linebreaks.append(ncounter)
        ncounter = 0
    counter58 += 1

print(linebreaks)


import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

with open(file_path, 'r', encoding='utf-8') as f:
    contents = f.read()
    # print(contents)

paratext = contents.split("\n")



import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()


with open(file_path, 'w') as f:
    f.write(" ")


number = 0



while number < len(edit_emptycornel) - 1:
    morewords_cornel = edit_emptycornel[number].split()
    print(_saver[number])
    print(morewords_cornel)
    add_check = 0
    if "TFR" in morewords_cornel or 'tfr' in morewords_cornel:
        morewords_cornel.append('fertility')
        add_check += 1
    print(morewords_cornel)
    question_words = ["Why", "How", "What", "Who", "Where", 'why', "what", "how", 'who', 'when', 'where']
    counter4 = 0
    para_counter = 0
    question_counter = 0
    block = ""
    sentancestaken = []

    while counter4 < len(morewords_cornel):
        if morewords_cornel[counter4] in question_words:
            counter4 += 1
        else:
            # print('check')
            while para_counter < len(paratext):
                # print("check3")
                # print(para_counter)
                if morewords_cornel[counter4].lower() in paratext[para_counter] or morewords_cornel[counter4] in paratext[para_counter] or morewords_cornel[counter4].upper() in paratext[para_counter]:
                    # print("check2")
                    sentancestaken.append(para_counter)
                    # print(sentancestaken)
                    # print(block)
                para_counter += 1
            counter4 += 1
            para_counter = 0
    
    # print(block)
    # print(len(paratext) - 1)
    print(sentancestaken)




    counter_repeat = 0
    counter_remove = 0
    copysentance = sentancestaken.copy()
    while counter_repeat < len(paratext) - 1:
        useage = sentancestaken.count(counter_repeat)
        if len(morewords_cornel) == 1:
            if 0 < useage and useage < (round(len(morewords_cornel) - add_check) / 2 ):
                while counter_remove < useage:
                    sentancestaken.remove(counter_repeat)
                    counter_remove += 1
                counter_remove = 0
            counter_repeat += 1
        else:
            if 0 < useage and useage < (round(len(morewords_cornel) - add_check) / 2 + 1):
                while counter_remove < useage:
                    sentancestaken.remove(counter_repeat)
                    counter_remove += 1
                counter_remove = 0
            counter_repeat += 1
    counter_repeat = 0
    subtractor = 2
    if len(sentancestaken) == 0 and len(_saver[number]) > 50 and number != 2:
        while counter_repeat < len(paratext) - 1:
            useage = copysentance.count(counter_repeat)
            if 0 < useage and useage < 6:
                while counter_remove < useage:
                    copysentance.remove(counter_repeat)
                    counter_remove += 1
                counter_remove = 0
            counter_repeat += 1
            
            print(copysentance)
          
        sentancestaken = copysentance.copy()
    print(sentancestaken)
    if ' \n' == _saver[number] or '  \n' == _saver[number] or '   \n' == _saver[number] or '  \n' == _saver[number]:
      zero = 0
    else:
        if len(sentancestaken) < 1 and len(_saver[number]) > 2 or "1. " in _saver[number] or "3. " in _saver[number] or "2. " in _saver[number] or "4. " in _saver[number] or "Name: " in _saver[number] or "page" in _saver[number] or "Case Study" in _saver[number] or "Reproductive Health and the GII" in _saver[number] or forcedanswertoggle == True:
            zero = 0 
            finalsummary = input("Answer")
        else:
            sentancestaken.sort()
            twenty_six = sentancestaken.count(len(paratext) - 1)
            counter26 = 0
            if sentancestaken[len(sentancestaken)- 1] == len(paratext) - 1:
                while counter26 < twenty_six:
                    sentancestaken.remove(len(paratext) - 1)
                    counter26 += 1
            # print(sentancestaken)
            counter_outlie = 0
            while counter_outlie < len(sentancestaken):
                if sentancestaken[counter_outlie] > sentancestaken[1] + 7:
                    sentancestaken.pop(counter_outlie)
                else:
                    counter_outlie += 1
            if len(sentancestaken) < 1:
                zero = 0
            else:
                
                final_para = list(range(sentancestaken[0], (sentancestaken[len(sentancestaken) - 1]) + 1))
                # print(final_para)
                # print(paratext[final_para[0]])
                if len(morewords_cornel) > 24 and len(final_para) < 3:
                    final_para.append(final_para[len(final_para) -1] + 1)
                    final_para.append(final_para[len(final_para) -1] + 1)
                    final_para.append(final_para[len(final_para) -1] + 1)
                else:
                    if len(morewords_cornel) > 19 and len(final_para) < 3:
                        final_para.append(final_para[len(final_para) -1] + 1)
                        final_para.append(final_para[len(final_para) -1] + 1)
                print(final_para)

                counter_final = 0
                block = ""
                while counter_final < len(final_para):
                    block = block + " " + paratext[final_para[counter_final]]
                    counter_final += 1
                print(block)

            #WIKI ARTICLE START




            
            if len(_saver[number]) < 300 and len(_saver[number]) > 221:
                sentances = str(round(linebreaks[timesused] / 8))
            elif "Gender Disparities" in _saver[number]:
                sentances = 3
            else:
                sentances = str(round(linebreaks[timesused] / 4))
            


            url = "https://meaningcloud-summarization-v1.p.rapidapi.com/summarization-1.0"

            querystring = {"sentences":sentances,"txt":block}

            headers = {
                "Accept": "application/json",
                "X-RapidAPI-Key": "05820c2b4emshe8ad672ce51e1a4p1732e7jsn196f3864394f",
                "X-RapidAPI-Host": "meaningcloud-summarization-v1.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            summary = response.json()
            print(summary)
            countersplit = 0
            split_summary = summary["summary"].split()
            finalsummary = ""
            andcounter = 0
            print(split_summary[andcounter])
            print(split_summary[andcounter].upper())
            print(len(split_summary[andcounter]))
            while split_summary[andcounter] == split_summary[andcounter].upper():
                if len(split_summary[andcounter]) > 3:
                    del split_summary[andcounter]
                elif split_summary[andcounter] == 'AND':
                    del split_summary[andcounter]
                else:
                    andcounter += 1
                print(split_summary)
            while countersplit < len(split_summary):
            
                finalsummary = finalsummary + " " + split_summary[countersplit]
                countersplit += 1
            print(summary["summary"])
            print(finalsummary)
        if "[...]" in finalsummary:
            finalsummary = finalsummary.replace("[...]", '')
        if "-" in finalsummary:
            finalsummary = finalsummary.replace("-", "")
        if "As you have read, t" in finalsummary:
            finalsummary = finalsummary.replace("As you have read, t", "T")
        # if "1" in finalsummary:
        #     finalsummary = finalsummary.replace("1", "")
        # if "2" in finalsummary:
        #     finalsummary = finalsummary.replace("2", "")
        # if "3" in finalsummary:
        #     finalsummary = finalsummary.replace("3", "")
        # if "4" in finalsummary:
        #     finalsummary = finalsummary.replace("4", "")
        # if "5" in finalsummary:
        #     finalsummary = finalsummary.replace("5", "")
        # if "6" in finalsummary:
        #     finalsummary = finalsummary.replace("6", "")
        # if "7" in finalsummary:
        #     finalsummary = finalsummary.replace("7", "")
        # if "8" in finalsummary:
        #     finalsummary = finalsummary.replace("8", "")
        # if "9" in finalsummary:
        #     finalsummary = finalsummary.replace("9", "")
        # if "0" in finalsummary:
        #     finalsummary = finalsummary.replace("0", "")
        if ".; . " in finalsummary:
            finalsummary = finalsummary.replace("0", "")
        if "m. t" in finalsummary:
            finalsummary = finalsummary.replace("0", "m t")
        print(_saver[number])
        isBig = input("Is bold: ")
        if isBig == "y" or isBig == "1":
            lending = 23.8
        else:
            lending = 21.4
        
        if finalsummary == " " or finalsummary == "" or number == 0 or number == 1:
            zero = 0
        else:
            
            
            stringfinal = finalsummary
            print(stringfinal)
            characters = ([*stringfinal])
            print(new_page_check)
           
                
            
            
            if number != 4:
                print(number)
                if " Participation (" in _saver[number]:
                    jumplines = (linebreaks[string_counter + 1])* lending + 40
                elif len(_saver[number]) < 83:
                    jumplines = (linebreaks[string_counter + 1])* lending + lending
                    # jumplines = (linebreaks[string_counter + 2] - 1)* 22 + 55
                elif len(_saver[number ]) < 160:
                    
                    jumplines = (linebreaks[string_counter + 1])* lending + 28
                elif len(_saver[number]) < 280:
        
                    jumplines = (linebreaks[string_counter + 1])* lending + 37
                elif len(_saver[number]) < 375:
        
                    jumplines = ((linebreaks[string_counter + 1])-5)* lending + 70
                else:
                    jumplines = (linebreaks[string_counter + 1])* lending + 77
                
                jumper = jumper - jumplines
                print(jumper)
            if (jumper) <= 20:
                    can.showPage()
                    pagecounter += 1
                    ycount = 0
                    jumper = 749
                    new_page_check = 1
                    if "Income (Gross Domestic Product" in _saver[number]:
                        jumplines = 44 + lending
                    elif len(_saver[number]) < 55:
                        jumplines =  lending * 4 + lending
                    elif len(_saver[number]) < 83 :
                        jumplines =  lending + lending
                        # jumplines = (linebreaks[string_counter + 2] - 1)* 22 + 55
                    elif len(_saver[number ]) < 160:
                        
                        jumplines =  30 + lending
                    elif len(_saver[number]) < 280:
                
                        jumplines =  37 + lending
                    elif len(_saver[number]) < 375:
                        jumplines = 75 + lending * 4
                    else:
                        jumplines = 77 + lending
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
                    if isBig == "0":
                        if ycount < -2:
                            lending = 23.8
                        print(lending)
                    if isBig == "1":
                        print(ycount)
                        if ycount >= -2:
                            lending = 23.8
                        else:
                            lending = 21.7
                        print(lending)
                    can.drawString(x, (jumper + ycount * lending), characters[counter_char], wordSpace= wordspacing, charSpace= charvar)
                
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
                
                    # if "Income (Gross Domestic Product" in _saver[number]:
                    #     jumplines =  44
                    # elif len(_saver[number + 1]) < 92:
                    #     jumplines =  21.7
                    #     # jumplines = (linebreaks[string_counter + 2] - 1)* 22 + 55
                    # elif len(_saver[number + 1]) < 160:
                        
                    #     jumplines =  28
                    # elif len(_saver[number + 1]) < 280:
            
                    #     jumplines =  37
                    # else:
                    #     jumplines = 77
                    
                
            ycount = 0
            
            x = 185
            counter_char = 0
            string_counter += 1
            print(_saver[number])
            print("")
            print(finalsummary)
            print(" ")
            with open(file_path, 'a') as f:
                f.write("\n" + _saver[number] + "\n\n" + finalsummary + "\n\n\n")
        timesused += 1
    number +=1
        
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

#positioning, pdf overlay
"""
import fpdf 
from fpdf import FPDF

from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

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