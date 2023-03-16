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
    button= Button(newwin, image=Proceed, command=lambda:[delete(newwin), killBrowsers(),switch()],borderwidth=0, background="#1E1A1A")
    button.place(x = 187, y = 138)
    
    button= Button(newwin, image=ManuallyClose, command=lambda:[switch()],borderwidth=0, background="#1E1A1A")
    button.place(x = 430, y = 138)
    
    newwin.mainloop()

def switchScreen():
    from OngoingBlock import ongoingBlock
    select()
    # a.destroy()
    root.destroy()
    ongoingBlock()
    



def write():
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
    
    global write_bg
    global Select
    global Delete
    global DeleteAll
    global WarningDelbg
    global WarningDelAllbg
    global Back2
    global No
    global Yes
    global Selectbg
    global presetBlock
    global timeSetBg
    global ErrorMsgBg
    global Okay
    global Add
    global remove
    global BrowserExitWarnBg
    global Proceed
    global ManuallyClose
    
    ManuallyClose = PhotoImage(file='images/ManuallyClose.png')
    Proceed = PhotoImage(file='images/Proceed.png')
    BrowserExitWarnBg = PhotoImage(file='images/BrowserExitWarnBg.png')
    remove = PhotoImage(file='images/Remove.png')
    write_bg = PhotoImage(file='images/WriteBg.png')
    Add = PhotoImage(file='images/Add.png')
    presetBlock = PhotoImage(file='images/PresetBlock.png')
    Delete = PhotoImage(file='images/PresetDelete.png')
    WarningDelbg = PhotoImage(file='images/WarningDelete.png')
    WarningDelAllbg = PhotoImage(file='images/WarningDeleteAll.png')
    timeSetBg = PhotoImage(file='images/timeSetbg.png')
    Selectbg = PhotoImage(file='images/Selectbg.png')
    ErrorMsgBg = PhotoImage(file='images/ErrorBg.png')
    No = PhotoImage(file='images/No.png')
    Yes = PhotoImage(file='images/Yes.png')
    Back2 = PhotoImage(file='images/Back 2.png')
    Okay = PhotoImage(file='images/Okay.png')
    
    
    
    label3 = Label(root, image= write_bg)
    label3.place(x = -2, y = -2)
    
    
    # Create frame and scrollbar
    my_frame = Frame(root)
    my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)
    
    my_scrollbarX = Scrollbar(my_frame, orient= HORIZONTAL)
    

    # Listbox!
    # SINGLE, BROWSE, MULTIPLE, EXTENDED
    global my_listbox
    my_listbox = Listbox(my_frame, width=53,height=5, yscrollcommand=my_scrollbar.set,xscrollcommand=my_scrollbarX.set, font=('Times', 21), selectmode=SINGLE, borderwidth=0, activestyle="none")
    #configure scrollbar
    my_scrollbar.config(command=my_listbox.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_scrollbarX.pack(side= BOTTOM, fill= X)
    my_scrollbarX.config(command=my_listbox.xview)
    
    my_frame.place(x = 22, y = 124)
    my_frame.configure(background="#FFFBFD")
    
    my_listbox.pack(pady=0)

    global entrySiteList
    global finalEntrySiteList
    global noWwwList
    entrySiteList = []
    finalEntrySiteList = []
    noWwwList = []
    # noWwwListComp = [site for site in finalEntrySiteList if "www." not in site]
   
    Write_Start()
    
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



def getInput():
    # global noDupFinalEntrySiteList
    #we need to define global entrySiteList here so that our listbox can access it
    #and make listbox display them
    siteValue = str(entry1.get())
    if len(siteValue) == 0:
            print("Please input something on field the blank field")
            ErrorMsg()
            return
    #if there is white space, validate it
    if " " in siteValue:
        print(siteValue + " has a space in it. Please enter a valid input.")
        ErrorMsg()
        return
    #avoiding duplication of display for the current input
    if siteValue in entrySiteList:
        print(siteValue + " is already listed")
        ErrorMsg()
    #append also a version without "www." and vice versa
    if "www." in siteValue:
        entrySiteList.append(siteValue)
        entrySiteList.append(siteValue.replace("www.",""))
    elif "www." not in siteValue:
        entrySiteList.append(siteValue)
        entrySiteList.append("www." + siteValue)
    print("entry", entrySiteList)
    
    for item in entrySiteList.copy():
        if item in noWwwList:
            print(item + " is already displayed")
            entrySiteList.clear()
            ErrorMsg()
        else: 
            my_listbox.insert(END, item)
            finalEntrySiteList.append(item)
            entrySiteList.remove(item)

    entrySiteList.clear()

    #noWwwList for removing all elements in finalEntrySiteList that contains "www"
    #since ex."reddit" is a part of "www.reddit.com" but not vice versa
    #therefore reddit can not be inputted since its already in the list.
    for site in finalEntrySiteList:
        if "www." not in site and site not in str(noWwwList):
            noWwwList.append(site)
    print("final", finalEntrySiteList)
    print("noWWW", noWwwList)
    print("entry", entrySiteList, "\n-----------------------------------------")
    clear_text()

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

# def DeleteAllWarn():
#     if len(finalEntrySiteList) == 0:
#         ErrorMsg()
#     newwin = Toplevel(root)
#     newwin.geometry("800x200")
#     newwin.resizable(False, False)
    
#     #making the window always pop up at the center of the screen
#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()
    
#     x = (screen_width / 2) - (800 / 2)
#     y = (screen_height / 2 ) - (200 / 2)
    
#     newwin.geometry(f'800x200+{int(x)}+{int(y)}')

#     #placing the bg image by using label
#     label2 = Label(newwin, image= WarningDelAllbg)
#     label2.place(x = 0, y = 0)
    
#     #creating the Understand button
#     button= Button(newwin, image=Yes, command=lambda:[newwin.destroy(),timeSet()],borderwidth=0, background="#1E1A1A")
#     button.place(x = 187, y = 138)
    
#     button= Button(newwin, image=No, command=lambda:[newwin.destroy()],borderwidth=0, background="#1E1A1A")
#     button.place(x = 430, y = 138)
    
#     newwin.mainloop()
        
def delete(a):
	#curselection will capture the current selection in the listbox by iterating thru it
	#then we assign the index to a variable in order for it to be deleted in webfile
    delValue = 0
    for item in my_listbox.curselection():
        delValue = item
    finalEntrySiteList.pop(delValue)

    a.destroy()
    my_listbox.delete(ANCHOR)
    # my_label.config(text='')
    print(finalEntrySiteList)



def timeSet():
    if len(finalEntrySiteList) == 0:
        ErrorMsg()
    global timeInput
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
    writeToHost(finalEntrySiteList)
    print("WRITTEN TO HOST")
    writeToBoolCache()
    with open ("webstores.txt", "a+") as f:
        f.seek(0)
        f.writelines(' '.join(finalEntrySiteList))
        f.write("\n")
    current_time = datetime.datetime.now()
    timeDifference = current_time - start_time
    unblock_time += timeDifference
    checkTime(current_time, unblock_time, finalEntrySiteList)
    
# def delete_all(a):
#     with open('webstores.txt', 'w') as f:
#         f.truncate(0)
#     a.destroy()
#     my_listbox.delete(0, END)

# def blockWebsites():
#     from Preset import timeSet, timeSet2, select
#     timeSet()

def clear_text():
       entry1.delete(0, END)

def Write_Start():
    # my_button = Button(root, text="Delete", command=delete)
    # my_button.pack(pady=10)
    global entry1
    entry1 = Entry(root, width=50, font=("Helvetica", 20))
    entry1.place(x = 22, y = 367)
    
    button1= Button(root, image=Add,borderwidth=0,command=getInput, bg="#FDFCDC")
    button1.place(x = 55, y = 415)
    
    button2= Button(root, image=Delete,borderwidth=0,command=DeleteWarn, bg="#FDFCDC")
    button2.place(x = 310, y = 415)
    
    button3= Button(root, image=presetBlock,borderwidth=0,command=timeSet, bg="#FDFCDC")
    button3.place(x = 578, y = 415)
    
    button4= Button(root, image=Back2,borderwidth=0,command=back, border=-5, background="#1E1A1A")
    button4.place(x = 53, y = 10)


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
# write()
