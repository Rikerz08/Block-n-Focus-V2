from tkinter import *
from pygame import *
from constants import *
from prompts import *

def unblock(root):
    from Questions import Quiz
    root.destroy()
    Quiz()

def block(root):
    from BlockScreen import blockScreen
    root.destroy()
    blockScreen()


Dashboard_bg = PhotoImage(file='images/Dashboard 4.png')
Block = PhotoImage(file='images/Block 2.png')
Unblock = PhotoImage(file='images/Unblock.png')
Exit = PhotoImage(file='images/Exit.png')

#running the dashboard screen
def Dashboard_start():

    label3 = Label(mainFrame, image= Dashboard_bg)
    label3.place(x = -2, y = -2)

    
    button= Button(mainFrame, image=Block,borderwidth=0,command=lambda:[block(root)], bg="#FDFCDC")
    button.place(x = 178, y = 190)
    
    Exitbutton= Button(mainFrame, image=Exit,borderwidth=0,command=lambda:[ExitWarn()], bg="#FDFCDC")
    Exitbutton.place(x = 18, y = 35)
    




















    
    # button2= Button(root, image=Unblock ,borderwidth=0,command=lambda:[unblock(root)], bg="#FDFCDC")
    # button2.place(x=128,y=257)









# global Dashboard_bg
# global Block
# global Unblock
# global Exit
# global ExitWarnbg
# global No
# global Yes
# ExitWarnbg = PhotoImage(file='images/QuitWarn.png')
# No = PhotoImage(file='images/No.png')
# Yes = PhotoImage(file='images/Yes.png')




# def ExitWarn():
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
#     label2 = Label(newwin, image= ExitWarnbg)
#     label2.place(x = -2, y = -2)
    
#     #creating the Understand button
#     button= Button(newwin, image=Yes, command=lambda:[root.destroy()],borderwidth=0, background="#1E1A1A")
#     button.place(x = 187, y = 138)
    
#     button= Button(newwin, image=No, command=lambda:[newwin.destroy()],borderwidth=0, background="#1E1A1A")
#     button.place(x = 430, y = 138)
    
#     newwin.mainloop()


# #Making windows dimensions
# def dashboard():
#     global root
#     root = Tk()
#     root.geometry("800x500")
#     root.resizable(False, False)
#     root.title("Block'nFocus")
#     root.overrideredirect(True)
    
#     #making the window always pop up at the center of the screen
#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()

#     x = (screen_width / 2) - (800 / 2)
#     y = (screen_height / 2 ) - (500 / 2)

#     root.geometry(f'800x500+{int(x)}+{int(y)}')
    
    #global variables to make it accessible
    # global Dashboard_bg
    # global Block
    # global Unblock
    # global Exit
    # global ExitWarnbg
    # global No
    # global Yes
    # Dashboard_bg = PhotoImage(file='images/Dashboard 4.png')
    # Block = PhotoImage(file='images/Block 2.png')
    # Unblock = PhotoImage(file='images/Unblock.png')
    # Exit = PhotoImage(file='images/Exit.png')
    # ExitWarnbg = PhotoImage(file='images/QuitWarn.png')
    # No = PhotoImage(file='images/No.png')
    # Yes = PhotoImage(file='images/Yes.png')

    # Dashboard_start(root)
    # root.mainloop()
    #global variables to make it accessible