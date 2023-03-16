from tkinter import *
from PIL import Image
from constants import *
from prompts import *

def index() :
    label1 = tk.Label(mainFrame, image = bg)
    label1.place(x = -2, y = -2)

    #Let us create a dummy button and pass the image
    button= tk.Button(mainFrame, image=click_btn,command=lambda:[Warning_Start()],borderwidth=0)
    # button.grid(column=1, row=1, padx=460, pady=170)
    button.place(x = 460, y = 170)
    
index()
root.mainloop()









































# #----------- Warning window
# def Warning_Start(root):
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
#     label2 = Label(newwin, image= warning)
#     label2.place(x = -2, y = -2)
    
#     #creating the Understand button
#     button= Button(newwin, image=understood, command=lambda:[change(root)],borderwidth=0)
#     button.grid(column=1, row=1, padx=311, pady=142)
    
#     newwin.mainloop()

# #switch window
# def change(root):
#     from LogicFunctions import copyHosts
#     copyHosts()
#     root.destroy()
#     dashboard()
    
# #Making windows dimensions
# def call():
#     root = Tk()
#   # Adjust size 
#     root.geometry("800x500")
#     root.resizable(False, False)
#     root.title("Block'nFocus")
    
#     #making the window always pop up at the center of the screen
#     screen_width = root.winfo_screenwidth()
#     screen_height = root.winfo_screenheight()

#     x = (screen_width / 2) - (800 / 2)
#     y = (screen_height / 2 ) - (500 / 2)

#     root.geometry(f'800x500+{int(x)}+{int(y)}')
 
    
    # #global variables to make it accessible
    # global bg
    # global click_btn
    # global warning
    # global understood

    # bg = PhotoImage(file = "images/index.png")
    # click_btn= PhotoImage(file='images/Start button.png')
    # warning = PhotoImage(file='images/Warning 2.png')
    # understood = PhotoImage(file='images/Understood.png')


    # index(root)
    # root.mainloop()


