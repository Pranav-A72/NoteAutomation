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

cornel_splited_str = corneltext.splitlines(True)


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

redundent_words = [' the ', ' that ', ' it ', ' than ', 'Notes', 'Cornell', 'Questions', ' does ', ' or ', ' from ', ' to ', ' and ', "(", ")", ".", ",", "?", " is ", " important", "Study", "Describe", " are ", " of ", " Date ", " Name ", ":", " Class ", "/", " Period ", "5", "6", "7", "8", "9", "0", ' as', ' by', ' in ', "As ", '\'', " do", " most ", " we", " a ", "1", "2", "3", "4", " world ", " level ", " regard ", " people " " v ", " vs ", " role ", " at ", "Look ", " look ", "Why ", "How ", "What ", "Who ", "Where ", ' why ', " what ", " how ", ' who ', ' when ', ' where ', '’s', 'v.', "v ", " high ", " low", "with ", " see ", " per ", " used ", " factors ", " money ", " in ", " countries ", "theredifference", "measurecountry", " population ", " work ", " collected"]
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


import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

with open(file_path, 'r') as f:
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
    # print(sentancestaken)

    counter_repeat = 0
    counter_remove = 0
    while counter_repeat < len(paratext) - 1:
        useage = sentancestaken.count(counter_repeat)
        if 0 < useage and useage < (round(len(morewords_cornel) - add_check) / 2):
            while counter_remove < useage:
                sentancestaken.remove(counter_repeat)
                counter_remove += 1
            counter_remove = 0
        counter_repeat += 1
 
    if len(sentancestaken) < 1:
        zero = 0
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
            if sentancestaken[counter_outlie] > sentancestaken[3] + 7:
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
            print(final_para)

            counter_final = 0
            block = ""
            while counter_final < len(final_para):
                block = block + " " + paratext[final_para[counter_final]]
                counter_final += 1
            # print(block)

        #WIKI ARTICLE START











            import nltk 
            from nltk.corpus import stopwords
            from nltk.tokenize import word_tokenize, sent_tokenize

            # Input text - to summarize 
            text = block

            # Tokenizing the text
            stopWords = set(stopwords.words("english"))
            words = word_tokenize(text)

            # Creating a frequency table to keep the 
            # score of each word

            freqTable = dict()
            for word in words:
                word = word.lower()
                if word in stopWords:
                    continue
                if word in freqTable:
                    freqTable[word] += 1
                else:
                    freqTable[word] = 1

            # Creating a dictionary to keep the score
            # of each sentence
            sentences = sent_tokenize(text)
            sentenceValue = dict()
            # print(sentences)
            for sentence in sentences:
                for word, freq in freqTable.items():
                    if word in sentence.lower():
                        if sentence in sentenceValue:
                            sentenceValue[sentence] += freq
                        else:
                            sentenceValue[sentence] = freq



            sumValues = 0
            for sentence in sentenceValue:
                sumValues += sentenceValue[sentence]

            # Average value of a sentence from the original text

            average = int(sumValues / len(sentenceValue))

            # Storing sentences into our summary.
            summary = ''
            for sentence in sentences:
                if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
                    summary += " " + sentence
            if summary == " " or summary == "":
                zero = 0
            else:
                print(_saver[number])
                print("")
                print(summary)
                print(" ")
                with open(file_path, 'a') as f:
                    f.write("\n" + _saver[number] + "\n\n" + summary + "\n\n\n")
    number +=1
        


