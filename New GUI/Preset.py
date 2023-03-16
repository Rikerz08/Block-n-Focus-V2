from tkinter import *
import linecache
import datetime

#we set unblock time to placeholding(1 year in minutes) value that is so long just so it's viable for the outer "if conditions" to work
#this is just to make the code run long enough to reach the asking of user input for the minutes
unblock_time = datetime.datetime.now() + datetime.timedelta(minutes=525600)


def BrowserExitWarn():
    from LogicFunctions import killBrowsers
    newwin = Toplevel(root)
    newwin.geometry("800x200")
    newwin.resizable(False, False)
    
    #making the window always pop up at the center of the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()   
    
    x = (screen_width / 2) - (800 / 2)
    y = (screen_height / 2 ) - (200 / 2)
    
    newwin.geometry(f'800x200+{int(x)}+{int(y)}')

    #placing the bg image by using label
    label2 = Label(newwin, image= BrowserExitWarnBg)
    label2.place(x = -2, y = -2)
    
    #creating the Understand button
    button= Button(newwin, image=Proceed, command=lambda:[killBrowsers(),switch()],borderwidth=0, background="#1E1A1A")
    button.place(x = 187, y = 138)
    
    button= Button(newwin, image=ManuallyClose, command=lambda:[switch()],borderwidth=0, background="#1E1A1A")
    button.place(x = 430, y = 138)
    
    newwin.mainloop()

def preset():
    global root
    root = Tk()
    root.title('Codemy.com')
    root.geometry("800x500")
    root.resizable(False, False)
    root.overrideredirect(True)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (800 / 2)
    y = (screen_height / 2 ) - (500 / 2)
    
    root.geometry(f'800x500+{int(x)}+{int(y)}')
    
    global preset_bg
    global Select
    global Delete
    global DeleteAll
    global WarningDelbg
    global WarningDelAllbg
    global Back
    global No
    global Yes
    global Selectbg
    global presetBlock
    global timeSetBg
    global ErrorMsgBg
    global Okay
    global BrowserExitWarnBg
    global Proceed
    global ManuallyClose
    
    ManuallyClose = PhotoImage(file='images/ManuallyClose.png')
    Proceed = PhotoImage(file='images/Proceed.png')
    BrowserExitWarnBg = PhotoImage(file='images/BrowserExitWarnBg.png')
    preset_bg = PhotoImage(file='images/Presets.png')
    Select = PhotoImage(file='images/PresetSelect.png')
    presetBlock = PhotoImage(file='images/PresetBlock.png')
    Delete = PhotoImage(file='images/PresetDelete.png')
    DeleteAll = PhotoImage(file='images/PresetDeleteAll.png')
    WarningDelbg = PhotoImage(file='images/WarningDelete.png')
    WarningDelAllbg = PhotoImage(file='images/WarningDeleteAll.png')
    timeSetBg = PhotoImage(file='images/timeSetbg.png')
    Selectbg = PhotoImage(file='images/Selectbg.png')
    ErrorMsgBg = PhotoImage(file='images/ErrorBg.png')
    No = PhotoImage(file='images/No.png')
    Yes = PhotoImage(file='images/Yes.png')
    Back = PhotoImage(file='images/Back.png')
    Okay = PhotoImage(file='images/Okay.png')
    
    
    
    label3 = Label(root, image= preset_bg)
    label3.place(x = -2, y = -2)
    
    
    # Create frame and scrollbar
    my_frame = Frame(root)
    my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)
    
    my_scrollbarX = Scrollbar(my_frame, orient= HORIZONTAL)
    

    # Listbox!
    # SINGLE, BROWSE, MULTIPLE, EXTENDED
    global my_listbox
    my_listbox = Listbox(my_frame, width=53,height=8, yscrollcommand=my_scrollbar.set,xscrollcommand=my_scrollbarX.set, font=('Times', 20), selectmode=SINGLE, borderwidth=0, activestyle="none")
    #configure scrollbar
    my_scrollbar.config(command=my_listbox.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_scrollbarX.pack(side= BOTTOM, fill= X)
    my_scrollbarX.config(command=my_listbox.xview)
    
    my_frame.place(x = 22, y = 100)
    my_frame.configure(background="#FFFBFD")
    
    my_listbox.pack(pady=0)
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
        my_listbox.insert(END, item)
    
    Preset_Start()
    
    root.mainloop()


def back():
    from BlockScreen import blockScreen
    root.destroy()
    blockScreen()
    
def DeleteWarn():
    #If no item is selected, then just not run the function
    if not my_listbox.curselection():
        return ErrorMsg()
    newwin = Toplevel(root)
    newwin.geometry("800x200")
    newwin.resizable(False, False)
    
    #making the window always pop up at the center of the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = (screen_width / 2) - (800 / 2)
    y = (screen_height / 2 ) - (200 / 2)
    
    newwin.geometry(f'800x200+{int(x)}+{int(y)}')

    #placing the bg image by using label
    label2 = Label(newwin, image= WarningDelbg)
    label2.place(x = -2, y = -2)
    
    #creating the Understand button
    button= Button(newwin, image=Yes, command=lambda:[delete(newwin)],borderwidth=0, background="#1E1A1A")
    button.place(x = 187, y = 138)
    
    button= Button(newwin, image=No, command=lambda:[newwin.destroy()],borderwidth=0, background="#1E1A1A")
    button.place(x = 430, y = 138)
    
    newwin.mainloop()

def SelectWarn(a):
    a.destroy()
    newwin = Toplevel(root)
    newwin.geometry("800x200")
    newwin.resizable(False, False)
    
    #making the window always pop up at the center of the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = (screen_width / 2) - (800 / 2)
    y = (screen_height / 2 ) - (200 / 2)
    
    newwin.geometry(f'800x200+{int(x)}+{int(y)}')

    #placing the bg image by using label
    label2 = Label(newwin, image= Selectbg)
    label2.place(x = -2, y = -2)
    
    #creating the Understand button
    button= Button(newwin, image=Yes, command=lambda:[newwin.destroy(),BrowserExitWarn()],borderwidth=0, background="#1E1A1A")
    button.place(x = 187, y = 138)
    
    button= Button(newwin, image=No, command=lambda:[newwin.destroy()],borderwidth=0, background="#1E1A1A")
    button.place(x = 430, y = 138)
    
    newwin.mainloop()

def timeSet():
    #We initialized the selection for the currentpreset here in timeSet func
    #instead of select func, so that even before we input the time, there is already a stored value in the list
    #this is because we notice that when we select an element, and then double click the entry on timeSet window
    #the selection disappears thus going into the error of "if not my_listbox.curselection()"

    #we initialize delIndex as 0 since it cannot be global since its initialized inside a for loop
    delIndex = 0
    global currentPreset
    global currentPresetList
    global noDupCurrentPresetList
    for item in my_listbox.curselection():
        delIndex = (item+1)
    currentPreset = linecache.getline("webstores.txt", delIndex)
    currentPresetList = currentPreset.split()
    noDupCurrentPresetList = list(dict.fromkeys(currentPresetList))
    #If no item is selected, then just not run the function
    if not my_listbox.curselection():
        return ErrorMsg()
    global timeInput
    # a.destroy()
    newwin = Toplevel(root)
    newwin.geometry("800x200")
    newwin.resizable(False, False)
    
    #making the window always pop up at the center of the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = (screen_width / 2) - (800 / 2)
    y = (screen_height / 2 ) - (200 / 2)
    
    newwin.geometry(f'800x200+{int(x)}+{int(y)}')

    #placing the bg image by using label
    label2 = Label(newwin, image= timeSetBg)
    label2.place(x = -2, y = -2)
    
    timeInput = Entry(newwin, font="Arial 45")
    timeInput.place(x = 180, y = 70, width=200, height=50)
    
    #creating the Understand button
    button= Button(newwin, image=presetBlock, command=lambda:[timeSet2(newwin)],borderwidth=0, background="#524B62")
    button.place(x = 187, y = 138)
    
    button= Button(newwin, image=No, command=lambda:[newwin.destroy()],borderwidth=0, background="#524B62")
    button.place(x = 430, y = 138)
    
    newwin.mainloop()

def timeSet2(a):
    timeValue = timeInput.get()
    global start_time
    global unblock_time
    while True:
        try:
            interval = float(timeValue)
            #convert interval to string so that it can be checked with rsplit since float
            #doesnt have .rsplit attributes
            strInterval = str(interval)
            if len(strInterval.rsplit('.')[-1]) > 2:
                print("Please enter a value with only 2 decimal places.")
                ErrorMsg()
                continue
            break
        except ValueError:
            ErrorMsg()
    start_time = datetime.datetime.now()
    unblock_time = start_time + datetime.timedelta(minutes=interval)
    SelectWarn(a)
    # from LogicFunctions import timeSetLogic
    # timeSetLogic(timeInput)

def ErrorMsg():
    newwin = Toplevel(root)
    newwin.geometry("800x200")
    newwin.resizable(False, False)
    
    #making the window always pop up at the center of the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = (screen_width / 2) - (800 / 2)
    y = (screen_height / 2 ) - (200 / 2)
    
    newwin.geometry(f'800x200+{int(x)}+{int(y)}')

    #placing the bg image by using label
    label2 = Label(newwin, image= ErrorMsgBg)
    label2.place(x = -2, y = -2)
    
    
    button= Button(newwin, image=Okay, command=lambda:[newwin.destroy()],borderwidth=0, background="#1E1A1A")
    button.place(x = 310, y = 138)
    
    newwin.mainloop()

def DeleteAllWarn():
    newwin = Toplevel(root)
    newwin.geometry("800x200")
    newwin.resizable(False, False)
    
    #making the window always pop up at the center of the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = (screen_width / 2) - (800 / 2)
    y = (screen_height / 2 ) - (200 / 2)
    
    newwin.geometry(f'800x200+{int(x)}+{int(y)}')

    #placing the bg image by using label
    label2 = Label(newwin, image= WarningDelAllbg)
    label2.place(x = -2, y = -2)
    
    #creating the Understand button
    button= Button(newwin, image=Yes, command=lambda:[delete_all(newwin)],borderwidth=0, background="#1E1A1A")
    button.place(x = 187, y = 138)
    
    button= Button(newwin, image=No, command=lambda:[newwin.destroy()],borderwidth=0, background="#1E1A1A")
    button.place(x = 430, y = 138)
    
    newwin.mainloop()
        
def delete(a):
	#curselection will capture the current selection in the listbox by iterating thru it
	#then we assign the index to a variable in order for it to be deleted in webfile

    for item in my_listbox.curselection():
        delIndex = (item+1)

    lines = []
    # read file
    with open("webstores.txt", 'r') as fp:
        # read an store all lines into list
        lines = fp.readlines()
    # Write file
    with open("webstores.txt", 'w') as fp:
        # iterate each line
        for number, line in enumerate(lines):
            # delete line 5 and 8. or pass any Nth line you want to remove
            # note list index starts from 0
            if number not in [delIndex-1]:
                fp.write(line)
    a.destroy()
    my_listbox.delete(ANCHOR)
    # my_label.config(text='')


def switch():
    from OngoingBlock import ongoingBlock
    select()
    # a.destroy()
    root.destroy()
    ongoingBlock()
 


def select():   
    # if not my_listbox.curselection():
    #     print("KANI JD")
    #     return ErrorMsg()
    global timeDifference
    global unblock_time
    # a.destroy()
    from LogicFunctions import checkTime, writeToHost, writeToBoolCache
    writeToHost(noDupCurrentPresetList)
    print("WRITTEN TO HOST")
    writeToBoolCache()
    current_time = datetime.datetime.now()
    timeDifference = current_time - start_time
    unblock_time += timeDifference
    checkTime(current_time, unblock_time, currentPresetList)
    
def delete_all(a):
    with open('webstores.txt', 'w') as f:
        f.truncate(0)
    a.destroy()
    my_listbox.delete(0, END)
  
def Preset_Start():
   
    # my_button = Button(root, text="Delete", command=delete)
    # my_button.pack(pady=10)
    button1= Button(root, image=presetBlock,borderwidth=0,command=timeSet, bg="#FDFCDC")
    button1.place(x = 55, y = 408)
    
    button2= Button(root, image=Delete,borderwidth=0,command=DeleteWarn, bg="#FDFCDC")
    button2.place(x = 310, y = 408)
    
    button3= Button(root, image=DeleteAll,borderwidth=0,command=DeleteAllWarn, bg="#FDFCDC")
    button3.place(x = 578, y = 408)
    
    button4= Button(root, image=Back,borderwidth=0,command=back, bg="#FFFBFD", border=0)
    button4.place(x = 53, y = 53)


    # my_button2 = Button(root, text="Select", command=select)
    # my_button2.pack(pady=10)
    

    # global my_label
    # my_label = Label(root, text='')
    # my_label.pack(pady=5)

    # my_button3 = Button(root, text="Delete All", command=delete_all)
    # my_button3.pack(pady=10)

    # my_button4 = Button(root, text="Select All", command=select_all)
    # my_button4.pack(pady=10)

    # my_button5 = Button(root, text="Delete Multiple", command=delete_multiple)
    # my_button5.pack(pady=10)



######################################################################################################################################################################################
# preset()
