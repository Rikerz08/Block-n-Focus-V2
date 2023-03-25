from tkinter import *
from constants import *

Dashboard_bg = PhotoImage(file='images/Dashboard 4.png')
Block = PhotoImage(file='images/Block 2.png')
Unblock = PhotoImage(file='images/Unblock.png')
Exit = PhotoImage(file='images/Exit.png')

#running the dashboard screen
def dashboardStart():
    from blockScreen import blockScreenStart
    from prompts import exitWarn
    label3 = Label(mainFrame, image= Dashboard_bg)
    label3.place(x = -2, y = -2)

    
    blockStartButton= Button(mainFrame, image=Block,borderwidth=0,command=lambda:[displayPage(blockScreenStart)], bg="#FDFCDC")
    blockStartButton.place(x = 178, y = 190)
    
    Exitbutton= Button(mainFrame, image=Exit,borderwidth=0,command=lambda:[exitWarn()], bg="#FDFCDC")
    Exitbutton.place(x = 18, y = 35)
