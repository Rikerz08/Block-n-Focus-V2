from tkinter import *
from PIL import Image



def Warning():
    root = Tk()
  # Adjust size 
    root.geometry("800x200")
    root.resizable(False, False)
    global bg
    global click_btn
    global warning
    global understood
    global Dashboard_bg
    global Block
    global Unblock

    bg = PhotoImage(file = "images/index.png")
    click_btn= PhotoImage(file='images/Start button.png')
    warning = PhotoImage(Image.open('images/Warning 2.png'))
    understood = PhotoImage(Image.open('images/Understood.png'))
    Dashboard_bg = PhotoImage(file='images/Dashboard.png')
    Block = PhotoImage(file='images/Block.png')
    Unblock = PhotoImage(file='images/Unblock.png')
    Warning_Start(root)
    root.mainloop()

def change(root):
    root.destroy()
    Dashboard_start()
    
def Warning_Start(root):
    label2 = Label(root, image= warning)
    label2.place(x = 0, y = 0)
    
    button= Button(root, image=understood,command=change(root),borderwidth=0)
    button.grid(column=1, row=1, padx=311, pady=142)
