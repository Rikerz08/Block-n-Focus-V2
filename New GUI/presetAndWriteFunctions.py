from constants import *
from prompts import *
import datetime, linecache

#Images for inputting time prompt
timeSetBg = tk.PhotoImage(file='images/timeSetbg.png')
presetBlock = tk.PhotoImage(file='images/PresetBlock.png')

def timeSet(pagename):
    if pagename == "preset":
        from preset import presetMyListbox
        #We initialized the selection for the currentpreset here in timeSet func
        #instead of select func, so that even before we input the time, there is already a stored value in the list
        #this is because we notice that when we select an element, and then double click the entry on timeSet window
        #the selection disappears thus going into the error of "if not my_listbox.curselection()"

        #we initialize delIndex as 0 since it cannot be global since its initialized inside a for loop
        delIndex = 0
        global currentPreset
        global currentPresetList
        global noDupCurrentPresetList
        for item in presetMyListbox.curselection():
            delIndex = (item+1)
        currentPreset = linecache.getline("webstores.txt", delIndex)
        currentPresetList = currentPreset.split()
        noDupCurrentPresetList = list(dict.fromkeys(currentPresetList))
        #If no item is selected, then just not run the function
        if not presetMyListbox.curselection():
            return errorMsg()
        global timeInput
        # a.destroy()
        newwin = tk.Toplevel(root)
        newwin.geometry("800x200")
        newwin.resizable(False, False)
        
        #making the window always pop up at the center of the screen
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        x = (screen_width / 2) - (800 / 2)
        y = (screen_height / 2 ) - (200 / 2)
        
        newwin.geometry(f'800x200+{int(x)}+{int(y)}')

        #placing the bg image by using label
        label2 = tk.Label(newwin, image= timeSetBg)
        label2.place(x = -2, y = -2)
        
        timeInput = tk.Entry(newwin, font="Arial 45")
        timeInput.place(x = 180, y = 70, width=200, height=50)
        
        #creating the Understand button
        button= tk.Button(newwin, image=presetBlock, command=lambda:[timeSet2(pagename, newwin)],borderwidth=0, background="#524B62")
        button.place(x = 187, y = 138)
        
        button= tk.Button(newwin, image=No, command=lambda:[newwin.destroy()],borderwidth=0, background="#524B62")
        button.place(x = 430, y = 138)
        
        newwin.mainloop()
    
    elif pagename == "write":
        from write import finalEntrySiteList
        if len(finalEntrySiteList) == 0:
            errorMsg()
        newwin = tk.Toplevel(root)
        newwin.geometry("800x200")
        newwin.resizable(False, False)
        
        #making the window always pop up at the center of the screen
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        
        x = (screen_width / 2) - (800 / 2)
        y = (screen_height / 2 ) - (200 / 2)
        
        newwin.geometry(f'800x200+{int(x)}+{int(y)}')

        #placing the bg image by using label
        label2 = tk.Label(newwin, image= timeSetBg)
        label2.place(x = -2, y = -2)
        
        timeInput = tk.Entry(newwin, font="Arial 45")
        timeInput.place(x = 180, y = 70, width=200, height=50)
        
        #creating the Understand button
        button= tk.Button(newwin, image=presetBlock, command=lambda:[timeSet2(pagename, newwin)],borderwidth=0, background="#524B62")
        button.place(x = 187, y = 138)
        
        button= tk.Button(newwin, image=No, command=lambda:[newwin.destroy()],borderwidth=0, background="#524B62")
        button.place(x = 430, y = 138)
        
        newwin.mainloop()

#Function for setting input variables for time setting in preset
def timeSet2(pagename,a):
    import datetime
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
                errorMsg()
                continue
            break
        except ValueError:
            errorMsg()
    start_time = datetime.datetime.now()
    unblock_time = start_time + datetime.timedelta(minutes=interval)
    selectWarn(pagename,a)
    # from LogicFunctions import timeSetLogic
    # timeSetLogic(timeInput)

#Function for writing to hosts and calculating the differences in unblock time and everything
def select(pagename):   
    if pagename == "preset":
        print("WRITE FROM PRESET")
        # if not my_listbox.curselection():
        #     print("KANI JD")
        #     return ErrorMsg()
        global timeDifference
        global unblock_time
        # a.destroy()
        from logicFunctions import checkTime, writeToHost
        writeToHost(noDupCurrentPresetList)
        print("WRITTEN TO HOST")
        # writeToBoolCache()
        current_time = datetime.datetime.now()
        timeDifference = current_time - start_time
        unblock_time += timeDifference
        checkTime(unblock_time, currentPresetList)

    elif pagename == "write":
        print("WRITE FROM WRITE")
        from write import finalEntrySiteList
        # if not writeMyListbox.curselection():
        #     print("KANI JD")
        #     return errorMsg()
        # a.destroy()
        from logicFunctions import checkTime, writeToHost
        writeToHost(finalEntrySiteList)
        print("WRITTEN TO HOST")
        # writeToBoolCache()
        with open ("webstores.txt", "a+") as f:
            f.seek(0)
            f.writelines(' '.join(finalEntrySiteList))
            f.write("\n")
        current_time = datetime.datetime.now()
        timeDifference = current_time - start_time
        unblock_time += timeDifference
        checkTime(unblock_time, finalEntrySiteList)

#Deleting all presets
def deleteAll(a):
    from preset import presetMyListbox
    with open('webstores.txt', 'w') as f:
        f.truncate(0)
    a.destroy()
    presetMyListbox.delete(0, tk.END)

#Delete single selected preset
def delete(a, listbox, listboxname):
	#curselection will capture the current selection in the listbox by iterating thru it
	#then we assign the index to a variable in order for it to be deleted in webfile

    #run this code if listbox is from preset page
    if listboxname == "presetMyListbox":
        for item in listbox.curselection():
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
        listbox.delete(tk.ANCHOR)
        # my_label.config(text='')
    
    #run this code if listbox is from write page
    elif listboxname == "writeMyListbox":
        from write import finalEntrySiteList 
        #curselection will capture the current selection in the listbox by iterating thru it
        #then we assign the index to a variable in order for it to be deleted in webfile
        delValue = 0
        for item in listbox.curselection():
            delValue = item
        finalEntrySiteList.pop(delValue)

        a.destroy()
        listbox.delete(tk.ANCHOR)
        # my_label.config(text='')
        print(finalEntrySiteList)
    
# Input validation for the website
def getInput():
    from write import entry1, entrySiteList,noWwwList, writeMyListbox, finalEntrySiteList, clear_text
    # global noDupFinalEntrySiteList
    #we need to define global entrySiteList here so that our listbox can access it
    #and make listbox display them
    siteValue = str(entry1.get())
    if len(siteValue) == 0:
            print("Please input something on field the blank field")
            errorMsg()
            return
    #if there is white space, validate it
    if " " in siteValue:
        print(siteValue + " has a space in it. Please enter a valid input.")
        errorMsg()
        return
    #avoiding duplication of display for the current input
    if siteValue in entrySiteList:
        print(siteValue + " is already listed")
        errorMsg()
    #append also a version without "www." and vice versa
    if "www." in siteValue:
        entrySiteList.append(siteValue)
        entrySiteList.append(siteValue.replace("www.",""))
    elif "www." not in siteValue:
        entrySiteList.append(siteValue)
        entrySiteList.append("www." + siteValue)
    print("entry", entrySiteList)
    
    for item in entrySiteList.copy():

        if item in noWwwList or item in finalEntrySiteList:
            print(item + " is already displayed")
            entrySiteList.clear()
            errorMsg()
        else: 
            writeMyListbox.insert(tk.END, item)
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