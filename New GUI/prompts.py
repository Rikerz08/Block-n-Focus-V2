import tkinter as tk;
from constants import *
from switchFuncs import changeToDashboard, switch

#Images for Warning prompt
warning = tk.PhotoImage(file='images/Warning 2.png')
understood = tk.PhotoImage(file='images/Understood.png')

def warningStart():
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
    label2 = tk.Label(newwin, image= warning)
    label2.place(x = -2, y = -2)
    
    #creating the Understand button
    button= tk.Button(newwin, image=understood, command=lambda:[changeToDashboard(newwin)],borderwidth=0)
    button.grid(column=1, row=1, padx=311, pady=142)
    
    newwin.mainloop()
    

#Images for Exit prompt
ExitWarnbg = tk.PhotoImage(file='images/QuitWarn.png')
No = tk.PhotoImage(file='images/No.png')
Yes = tk.PhotoImage(file='images/Yes.png')


def exitWarn():
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
    label2 = tk.Label(newwin, image= ExitWarnbg)
    label2.place(x = -2, y = -2)
    
    #creating the Understand button
    button= tk.Button(newwin, image=Yes, command=lambda:[root.destroy()],borderwidth=0, background="#1E1A1A")
    button.place(x = 187, y = 138)
    
    button= tk.Button(newwin, image=No, command=lambda:[newwin.destroy()],borderwidth=0, background="#1E1A1A")
    button.place(x = 430, y = 138)
    
    newwin.mainloop()



#Images for killing browsers
ManuallyClose = tk.PhotoImage(file='images/ManuallyClose.png')
Proceed = tk.PhotoImage(file='images/Proceed.png')
BrowserExitWarnBg = tk.PhotoImage(file='images/BrowserExitWarnBg.png')

#Warning for killing browsers
def browserExitWarn(pagename):
    from logicFunctions import killBrowsers
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
    label2 = tk.Label(newwin, image= BrowserExitWarnBg)
    label2.place(x = -2, y = -2)
    
    #creating the Understand button
    button= tk.Button(newwin, image=Proceed, command=lambda:[newwin.destroy(),killBrowsers(),switch(pagename)],borderwidth=0, background="#1E1A1A")
    button.place(x = 187, y = 138)
    
    button= tk.Button(newwin, image=ManuallyClose, command=lambda:[newwin.destroy(),switch(pagename)],borderwidth=0, background="#1E1A1A")
    button.place(x = 430, y = 138)
    
    newwin.mainloop()


#Image error prompt
ErrorMsgBg = tk.PhotoImage(file='images/ErrorBg.png')
Okay = tk.PhotoImage(file='images/Okay.png')

#Error message prompt
def errorMsg():
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
    label2 = tk.Label(newwin, image= ErrorMsgBg)
    label2.place(x = -2, y = -2)
    
    
    button= tk.Button(newwin, image=Okay, command=lambda:[newwin.destroy()],borderwidth=0, background="#1E1A1A")
    button.place(x = 310, y = 138)
    
    newwin.mainloop()


#Image for deletion waring
WarningDelbg = tk.PhotoImage(file='images/WarningDelete.png')

#Deleting preset warning
def deleteWarn(listbox, listboxname):
    from presetAndWriteFunctions import delete
    # from preset import my_listbox
    #If no item is selected, then just not run the function
    if not listbox.curselection():
        return errorMsg()
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
    label2 = tk.Label(newwin, image= WarningDelbg)
    label2.place(x = -2, y = -2)
    
    #creating the Understand button
    button= tk.Button(newwin, image=Yes, command=lambda:[delete(newwin, listbox, listboxname)],borderwidth=0, background="#1E1A1A")
    button.place(x = 187, y = 138)
    
    button= tk.Button(newwin, image=No, command=lambda:[newwin.destroy()],borderwidth=0, background="#1E1A1A")
    button.place(x = 430, y = 138)
    
    newwin.mainloop()

#Image for select prompt
Selectbg = tk.PhotoImage(file='images/Selectbg.png')

#Prompt for selecting a preset to block
def selectWarn(pagename,a):
    a.destroy()
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
    label2 = tk.Label(newwin, image= Selectbg)
    label2.place(x = -2, y = -2)
    
    #creating the Understand button
    button= tk.Button(newwin, image=No, command=lambda:[newwin.destroy()],borderwidth=0, background="#1E1A1A")
    button.place(x = 187, y = 138)
    
    button= tk.Button(newwin, image=Yes, command=lambda:[newwin.destroy(),browserExitWarn(pagename)],borderwidth=0, background="#1E1A1A")
    button.place(x = 430, y = 138)
    
    newwin.mainloop()

#Images for delete all prompt
WarningDelAllbg = tk.PhotoImage(file='images/WarningDeleteAll.png')

#Deleting all presets prompt
def DeleteAllWarn():
    from presetAndWriteFunctions import deleteAll
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
    label2 = tk.Label(newwin, image= WarningDelAllbg)
    label2.place(x = -2, y = -2)
    
    #creating the Understand button
    button= tk.Button(newwin, image=Yes, command=lambda:[deleteAll(newwin)],borderwidth=0, background="#1E1A1A")
    button.place(x = 187, y = 138)
    
    button= tk.Button(newwin, image=No, command=lambda:[newwin.destroy()],borderwidth=0, background="#1E1A1A")
    button.place(x = 430, y = 138)
    
    newwin.mainloop()


#Images for forcedUnblock prompt
yes = tk.PhotoImage(file='images/Yes.png')
forcedUnblockBg = tk.PhotoImage(file='images/ForcedUnblockBg.png')

#Initialization of comfirmatory variable to see if user opens quiz window
quizNewwinExist = False

#Force unblocked prompt
def forcedUnblockWarn():
    from questions import quiz
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
    label2 = tk.Label(newwin, image= forcedUnblockBg)
    label2.place(x = -2, y = -2)
    
    #creating the Understand button
    button= tk.Button(newwin, image=yes, command=lambda:[newwin.destroy(), makeVariable(), quiz(), ],borderwidth=0)
    button.grid(column=1, row=1, padx=305, pady=142)
    
    newwin.mainloop()

#function to let the checkTime func know if user tried to take a quiz or not
def makeVariable():
    global quizNewwinExist
    quizNewwinExist = True

# Images for Successfully Unblocked prompt
unblockedbg = tk.PhotoImage(file='images/SuccessUnblockBg.png')
proceed = tk.PhotoImage(file='images/proceed.png')


# Successfully Unblocked prompt
def unblockedMsg():
    # from Questions import Quiz
    from dashboard import dashboardStart      
    root.withdraw()
    newwin = tk.Toplevel(root)
    newwin.geometry("800x200")
    newwin.resizable(False, False)
    # newwin.overrideredirect(True)
    
    #making the window always pop up at the center of the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = (screen_width / 2) - (800 / 2)
    y = (screen_height / 2 ) - (200 / 2)
    
    newwin.geometry(f'800x200+{int(x)}+{int(y)}')

    #placing the bg image by using label
    label2 = tk.Label(newwin, image= unblockedbg)
    label2.place(x = -2, y = -2)
    
    
    button= tk.Button(newwin, image=proceed, command=lambda:[newwin.destroy(), makeVariableFalse(), root.deiconify(), root.overrideredirect(False), displayPage(dashboardStart)],borderwidth=0, background="#1E1A1A")
    button.place(x = 310, y = 138)
    
    newwin.mainloop()

#function for returning quizNewwinExist to False value because it seems na 
#ma carry over siya the next iterations
def makeVariableFalse():
    global quizNewwinExist
    quizNewwinExist = False

#Quiz failed prompt images
UnblockFailedbg = tk.PhotoImage(file='images/UnblockFailedBg.png')
ISuck = tk.PhotoImage(file='images/I Suck.png')

#Quiz failed prompt
def unblockFailed():
    from ongoingBlock import ongoingBlockStart
    newwin = tk.Toplevel(root)
    newwin.geometry("800x200")
    newwin.resizable(False, False)
    newwin.overrideredirect(True)
    
    #making the window always pop up at the center of the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = (screen_width / 2) - (800 / 2)
    y = (screen_height / 2 ) - (200 / 2)
    
    newwin.geometry(f'800x200+{int(x)}+{int(y)}')

    #placing the bg image by using label
    label2 = tk.Label(newwin, image= UnblockFailedbg)
    label2.place(x = -2, y = -2)
    
    
    button= tk.Button(newwin, image=ISuck, command=lambda:[newwin.destroy(), displayPage(ongoingBlockStart)],borderwidth=0, background="#1E1A1A")
    button.place(x = 310, y = 138)
    
    newwin.mainloop()