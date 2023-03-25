from tkinter import *
from constants import *
from prompts import *

#Index images
bg = tk.PhotoImage(file = "images/index.png")
click_btn= tk.PhotoImage(file='images/Start button.png')

def index() :
    label1 = tk.Label(mainFrame, image = bg)
    label1.place(x = -2, y = -2)

    #Let us create a dummy button and pass the image
    startButton= tk.Button(mainFrame, image=click_btn,command=lambda:[warningStart()],borderwidth=0)
    # button.grid(column=1, row=1, padx=460, pady=170)
    startButton.place(x = 460, y = 170)
    
index()
root.mainloop()

#testing
