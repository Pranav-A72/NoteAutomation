'''
# 1.) isolate every "block" (edited)
# [10:00 PM]
2.) isolate sentacnes/topics
ex: Climate. What is a climate? Why is it important to agriculture?
Into: [climate][what is climate][why is it important] (edited)
[10:00 PM]
3.) emlinate unless words
ex: [why is important to agriculture] to [important, arguculture]
[10:00 PM]
4. find the first sentance with that phrase
[10:01 PM]
5.) elimate repeats
ex: [climate][what is climate]
to [climate][climate]
[10:01 PM]
to [climate]
'''

import tkinter as tk
from tkinter import filedialog

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


# import textrazor

# textrazor.api_key = "fda84616d56c219481d317b308114baf4d94ce274a7dc5255bd86b91"

# client = textrazor.TextRazor(extractors=["entities"])
# response = client.analyze(texting)

# for entity in response.entities():
#     print(entity.id)

print(type(corneltext))
cornel_splited_str = corneltext.splitlines(True)
print(type(cornel_splited_str))

#We need to save this so we can figure how many sentances to pull = space on page (lines breaks)
print(cornel_splited_str)

emptycounter = 0
emptylimits = len(cornel_splited_str)
empty_cornel = cornel_splited_str
removed = 0
print(emptylimits)
# print(cornel_splited_str[emptycounter])
while emptycounter < emptylimits :
    if emptycounter >= len(empty_cornel):
        emptycounter = emptylimits
    else:
        if cornel_splited_str[emptycounter] == ' \n' or cornel_splited_str[emptycounter] == '  \n' or cornel_splited_str[emptycounter] == '   \n':
            remover = emptycounter + removed
            empty_cornel.pop(remover)
            # print(emptycounter)
            # print(len(empty_cornel))
            # print("a")
        else:
            emptycounter += 1
            # print(emptycounter)
            # print(len(empty_cornel))
            # print("b")
print(empty_cornel)
print(len(empty_cornel))