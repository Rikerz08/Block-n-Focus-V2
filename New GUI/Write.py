from tkinter import *
import datetime
from prompts import *
from presetAndWriteFunctions import *

#we set unblock time to placeholding(1 year in minutes) value that is so long just so it's viable for the outer "if conditions" to work
#this is just to make the code run long enough to reach the asking of user input for the minutes
unblock_time = datetime.datetime.now() + datetime.timedelta(minutes=525600)
    
remove = PhotoImage(file='images/Remove.png')
write_bg = PhotoImage(file='images/WriteBg.png')
Add = PhotoImage(file='images/Add.png')
Delete = PhotoImage(file='images/PresetDelete.png')
Back2 = PhotoImage(file='images/Back 2.png')

def clear_text():
       entry1.delete(0, END)

def writeStart():
    from blockScreen import blockScreenStart
    label3 = Label(mainFrame, image= write_bg)
    label3.place(x = -2, y = -2)
       
    # Create frame and scrollbar
    my_frame = Frame(mainFrame)
    my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)
    my_scrollbarX = Scrollbar(my_frame, orient= HORIZONTAL)
    
    # Listbox!
    global writeMyListbox
    writeMyListbox = Listbox(my_frame, width=53,height=5, yscrollcommand=my_scrollbar.set,xscrollcommand=my_scrollbarX.set, font=('Times', 21), selectmode=SINGLE, borderwidth=0, activestyle="none")
    #configure scrollbar
    my_scrollbar.config(command=writeMyListbox.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_scrollbarX.pack(side= BOTTOM, fill= X)
    my_scrollbarX.config(command=writeMyListbox.xview)
    
    my_frame.place(x = 22, y = 124)
    my_frame.configure(background="#FFFBFD")
    writeMyListbox.pack(pady=0)

    global entrySiteList
    global finalEntrySiteList
    global noWwwList
    entrySiteList = []
    finalEntrySiteList = []
    noWwwList = []
    # noWwwListComp = [site for site in finalEntrySiteList if "www." not in site]
        
    button1= Button(mainFrame, image=Add,borderwidth=0,command=getInput, bg="#FDFCDC")
    button1.place(x = 55, y = 415)
    
    button2= Button(mainFrame, image=Delete,borderwidth=0,command=lambda:[deleteWarn(writeMyListbox, "writeMyListbox")], bg="#FDFCDC")
    button2.place(x = 310, y = 415)
    
    button3= Button(mainFrame, image=presetBlock,borderwidth=0,command=lambda:[timeSet("write")], bg="#FDFCDC")
    button3.place(x = 578, y = 415)
    
    button4= Button(mainFrame, image=Back2,borderwidth=0,command=lambda:[displayPage(blockScreenStart)], border=-5, background="#1E1A1A")
    button4.place(x = 53, y = 10)

    global entry1
    entry1 = Entry(mainFrame, width=50, font=("Helvetica", 20))
    entry1.place(x = 22, y = 367)