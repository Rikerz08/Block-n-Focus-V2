from tkinter import *
from PIL import Image


#----------- Warning window
def ForcedUnblockWarn():
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
    label2 = Label(newwin, image= forcedUnblockBg)
    label2.place(x = -2, y = -2)
    
    #creating the Understand button
    button= Button(newwin, image=yes, command=lambda:[change()],borderwidth=0)
    button.grid(column=1, row=1, padx=305, pady=142)
    
    newwin.mainloop()

#switch window
def change():
    from Questions import Quiz
    root.destroy()
    Quiz()


#Making windows dimensions
def ongoingBlock():
    global root
    root = Tk()
  # Adjust size 
    root.geometry("800x500")
    root.resizable(False, False)
    root.overrideredirect(True)
    root.title("Block'nFocus")
    
    #making the window always pop up at the center of the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (800 / 2)
    y = (screen_height / 2 ) - (500 / 2)

    root.geometry(f'800x500+{int(x)}+{int(y)}')
 
    
    #global variables to make it accessible
    global ongoingBlockBg
    global click_btn
    global forcedUnblockBg
    global yes
    global unblockedbg
    global proceed
    unblockedbg = PhotoImage(file='images/SuccessUnblockBg.png')
    proceed = PhotoImage(file='images/proceed.png')
    ongoingBlockBg = PhotoImage(file = "images/OngoingBlockBg.png")
    click_btn= PhotoImage(file='images/Unblock 2.png')
    forcedUnblockBg = PhotoImage(file='images/ForcedUnblockBg.png')
    yes = PhotoImage(file='images/Yes.png')


    OngoingblockStart()
    
    root.mainloop()

#running the index screen
def OngoingblockStart():    
    label1 = Label(root, image = ongoingBlockBg)
    label1.place(x = -2, y = -2)

    #Let us create a dummy button and pass the image
    button= Button(root, image=click_btn,command=lambda:[ForcedUnblockWarn()],borderwidth=0, background="#000000")
    button.place(x = 318, y = 400)
    

# doneblock
def UnblockedMsg():
    # from Questions import Quiz
    from dashboard import dashboard
    root.destroy()
    newwin = Toplevel(root)
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
    label2 = Label(newwin, image= unblockedbg)
    label2.place(x = -2, y = -2)
    
    
    button= Button(newwin, image=proceed, command=lambda:[root.destroy(), dashboard()],borderwidth=0, background="#1E1A1A")
    button.place(x = 310, y = 138)
    
    newwin.mainloop()
