
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

from PyPDF2 import PdfReader
texting = '' 
reader = PdfReader(file_path)
pageNum = reader.getNumPages() - 1
while pageNum > -1:
    page = reader.pages[pageNum]
    texting = page.extract_text() + texting
    pageNum -= 1


import textrazor

textrazor.api_key = "fda84616d56c219481d317b308114baf4d94ce274a7dc5255bd86b91"

client = textrazor.TextRazor(extractors=["entities"])
response = client.analyze(texting)

for entity in response.entities():
    print(entity.id)