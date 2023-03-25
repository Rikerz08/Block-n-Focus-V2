from constants import *
from prompts import *

#global variables to make it accessible
global ongoingBlockBg
global click_btn


ongoingBlockBg = tk.PhotoImage(file = "images/OngoingBlockBg.png")
click_btn= tk.PhotoImage(file='images/Unblock 2.png')


#running the index screen
def ongoingBlockStart():    
    label1 = tk.Label(mainFrame, image = ongoingBlockBg)
    label1.place(x = -2, y = -2)

    #Let us create a dummy button and pass the image
    button= tk.Button(mainFrame, image=click_btn,command=lambda:[forcedUnblockWarn()],borderwidth=0, background="#000000")
    button.place(x = 318, y = 400)
    # root.overrideredirect(True)
    root.protocol("WM_DELETE_WINDOW", disableButton)

