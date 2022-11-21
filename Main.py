import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

#open text file in read mode
text_file = open(file_path, "r")
 
#read whole file to a string
data = text_file.read()

print(data)