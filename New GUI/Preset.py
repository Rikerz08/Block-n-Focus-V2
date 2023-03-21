from tkinter import *
import datetime
from prompts import *
from presetAndWriteFunctions import *

#we set unblock time to placeholding(1 year in minutes) value that is so long just so it's viable for the outer "if conditions" to work
#this is just to make the code run long enough to reach the asking of user input for the minutes
unblock_time = datetime.datetime.now() + datetime.timedelta(minutes=525600)
    
preset_bg = PhotoImage(file='images/Presets.png')
Delete = PhotoImage(file='images/PresetDelete.png')
DeleteAll = PhotoImage(file='images/PresetDeleteAll.png')
Back = PhotoImage(file='images/Back.png')

def presetStart():
    from blockScreen import blockScreenStart
    label3 = Label(mainFrame, image = preset_bg)
    label3.place(x = -2, y = -2)

    # Create frame and scrollbar
    my_frame = Frame(mainFrame)
    my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)
    my_scrollbarX = Scrollbar(my_frame, orient= HORIZONTAL) 

    # Listbox!
    global presetMyListbox
    presetMyListbox = Listbox(my_frame, width=53,height=8, yscrollcommand=my_scrollbar.set,xscrollcommand=my_scrollbarX.set, font=('Times', 20), selectmode=SINGLE, borderwidth=0, activestyle="none")
    #configure scrollbar
    my_scrollbar.config(command=presetMyListbox.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_scrollbarX.pack(side= BOTTOM, fill= X)
    my_scrollbarX.config(command=presetMyListbox.xview)

    my_frame.place(x = 22, y = 100)
    my_frame.configure(background="#FFFBFD")

    presetMyListbox.pack(pady=0)

    #This code is for getting the lines from the txt file and displaying them into the list box
    global presetList
    presetList = []
    with open('webstores.txt', 'r') as f:
        for line in f:
            #splits line elements with commas and creates it into list
            currLineList = line.split()
            #joins all the elements of the list with comma and space
            stringLineList = (', '.join(currLineList))
            presetList.append(stringLineList)
        # presetList = [line.strip() for line in f]

    for item in presetList:
        presetMyListbox.insert(END, item)

    button1= Button(mainFrame, image=presetBlock,borderwidth=0,command=lambda:[timeSet("preset")], bg="#FDFCDC")
    button1.place(x = 55, y = 408)
    
    button2= Button(mainFrame, image=Delete,borderwidth=0,command=lambda:[deleteWarn(presetMyListbox, "presetMyListbox")], bg="#FDFCDC")
    button2.place(x = 310, y = 408)
    
    button3= Button(mainFrame, image=DeleteAll,borderwidth=0,command=DeleteAllWarn, bg="#FDFCDC")
    button3.place(x = 578, y = 408)
    
    button4= Button(mainFrame, image=Back,borderwidth=0,command=lambda:[displayPage(blockScreenStart)], bg="#FFFBFD", border=0)
    button4.place(x = 53, y = 53)