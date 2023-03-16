import tkinter as tk;
from constants import *
from switchFuncs import change


#Images for Warning prompt
warning = tk.PhotoImage(file='images/Warning 2.png')
understood = tk.PhotoImage(file='images/Understood.png')

def Warning_Start():
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
    button= tk.Button(newwin, image=understood, command=lambda:[change(newwin)],borderwidth=0)
    button.grid(column=1, row=1, padx=311, pady=142)
    
    newwin.mainloop()
    


#Images for Exit prompt
ExitWarnbg = tk.PhotoImage(file='images/QuitWarn.png')
No = tk.PhotoImage(file='images/No.png')
Yes = tk.PhotoImage(file='images/Yes.png')


def ExitWarn():
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