import tkinter as tk;
global root

root = tk.Tk()
# Adjust size 
root.geometry("800x500")
root.resizable(False, False)
root.title("Block'nFocus")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (800 / 2)
y = (screen_height / 2 ) - (500 / 2)

root.geometry(f'800x500+{int(x)}+{int(y)}')

global mainFrame

mainFrame = tk.Frame(root)
mainFrame.pack()
mainFrame.propagate(False)
mainFrame.configure(width = 800, height = 500)

def displayPage(page):
    deletePage()
    page()

#need to delete other frames, otherwise it will all duplicate, just followed the video
def deletePage():
    for frame in mainFrame.winfo_children():
        frame.destroy()

#empty function for disabling x button on titlebar on ongoingBlock
def disableButton():
    pass

#returning the function og x button on titlebar to normal function
def enableExit():
    root.protocol("WM_DELETE_WINDOW", root.destroy)
