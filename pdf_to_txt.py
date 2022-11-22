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

# print(type(corneltext))
cornel_splited_str = corneltext.splitlines(True)
# print(type(cornel_splited_str))

#We need to save this so we can figure how many sentances to pull = space on page (lines breaks)
# print(cornel_splited_str)

emptycounter = 0
emptylimits = len(cornel_splited_str)
empty_cornel = cornel_splited_str
# empty_cornel.remove("Cornell")
# empty_cornel.remove("Topic/Objective")
# empty_cornel.remove('Name')
# empty_cornel.remove('Date')
# empty_cornel.remove('Essential Question')
# empty_cornel.remove('Questions:')
removed = 0
# print(emptylimits)
# print(cornel_splited_str[emptycounter])
# while emptycounter < emptylimits :
#     if emptycounter >= len(empty_cornel):
#         emptycounter = emptylimits
#     else:
#         if cornel_splited_str[emptycounter] == ' \n' or cornel_splited_str[emptycounter] == '  \n' or cornel_splited_str[emptycounter] == '   \n':
#             remover = emptycounter + removed
#             empty_cornel.pop(remover)
#             # print(emptycounter)
#             # print(len(empty_cornel))
#             # print("a")
#         else:
#             emptycounter += 1
#             # print(emptycounter)
#             # print(len(empty_cornel))
#             # print("b")
print(cornel_splited_str)
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
        cornel_splited_str[counter5] = cornel_splited_str[counter5] + cornel_splited_str[counter5 + 1]
        cornel_splited_str.pop(counter5 + 1)
print(cornel_splited_str)

# print(cornel_splited_str[2])





# print(empty_cornel)

empty_counter2 = 0

edit_emptycornel = empty_cornel
# print(edit_emptycornel[2])

redundent_words = [' the', ' the', ' that', ' it', ' than', 'Notes', 'Cornell', 'Questions', ' does', ' or', ' from', 'to ', ' and', "(", ")", ".", ",", "?", "is ", " important", "Study", "Describe", " are", " of", "Date", "Name", ":", "Class", "/", "Period", "5", "6", "7", "8", "9", "0", ' as', ' by', ' in', "As ", '\'', " do", " most", " we", " a ", "1", "2", "3", "4", " world", " level", " regard", " people" " v", " vs", " role", " at ", "Look ", " look", "Why ", "How ", "What ", "Who ", "Where ", ' why', " what", " how", ' who', ' when', ' where', "'s", "with ", " see ", " per ", " used", " factors", " money", "in ", "countries", "theredifference", "measurecountry", "population", " work", " collected", " core", "periphery"]
empty_counter = 0
emptylimits = len(redundent_words)

while empty_counter2 < len(edit_emptycornel) - 1:
    words_cornel = edit_emptycornel[empty_counter2]
    while empty_counter < emptylimits - 1:
        if empty_counter >= len(redundent_words) - 1:
            empty_counter = emptylimits
        else:
            if redundent_words[empty_counter] in words_cornel:
                if redundent_words[empty_counter] == " \n" or redundent_words[empty_counter] == "'":
                     words_cornel = words_cornel.replace(redundent_words[empty_counter], ' ')
                else:
                    words_cornel = words_cornel.replace(redundent_words[empty_counter], '')
                empty_counter += 1
                # print(empty_counter)
            else:
                empty_counter += 1
                # print(empty_counter)
    edit_emptycornel[empty_counter2] = words_cornel
    empty_counter2 += 1
    # print(empty_counter2)
    empty_counter = 0



print(edit_emptycornel[28])
morewords_cornel = edit_emptycornel[28].split()
print(morewords_cornel)



import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

with open(file_path, 'r', encoding="utf8") as f:
    contents = f.read()
    # print(contents)

paratext = contents.split("\n")






number = 0
print(edit_emptycornel[number])
print(empty_cornel[number])

while number < len(edit_emptycornel) - 1:
    morewords_cornel = edit_emptycornel[number].split()
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

    counter_repeat = 0
    counter_remove = 0
    while counter_repeat < len(paratext) - 1:
        useage = sentancestaken.count(counter_repeat)
        if 0 < useage and useage < round(len(morewords_cornel) / 2):
            while counter_remove < useage:
                sentancestaken.remove(counter_repeat)
                counter_remove += 1
            counter_remove = 0
        counter_repeat += 1

    if len(sentancestaken) < 1:
        print(" ")
    else:
        high_low = sentancestaken.sort()
        print(sentancestaken)
        final_para = list(range(sentancestaken[0], (sentancestaken[len(sentancestaken) - 1]) + 1))
        print(final_para)
        # print(paratext[final_para[0]])

        counter_final = 0
        block = ""
        while counter_final < len(final_para):
            block = block + " " + paratext[final_para[counter_final]]
            counter_final += 1
        # print(block)



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
        if '1.  ' in cornel_splited_str[number] or '2.  ' in cornel_splited_str[number] or '3.  ' in cornel_splited_str[number] or '4.  ' in empty_cornel[number]:
            print(" ")
        else:
            print(cornel_splited_str[number])
            print("")
            print(summary)
            print(" ")
    number +=1
