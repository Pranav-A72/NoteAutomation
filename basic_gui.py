import PySimpleGUI as sg
 
layout = [[sg.Button('Buttton', size=(30,4))]]
 
#Draw the window
window = sg.Window('GUIWINDOW', layout, size=(500,400))
 
#Define what happens when the button is clicked
event, values = window.read()