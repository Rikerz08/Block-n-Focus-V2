from constants import *

def preset(root):
    from preset import preset
    root.destroy()
    preset()

def writeswitch(root):
    from write import write
    root.destroy()
    write()
    
ManuallyClose = tk.PhotoImage(file='images/ManuallyClose.png')
Proceed = tk.PhotoImage(file='images/Proceed.png')
BrowserExitWarnBg = tk.PhotoImage(file='images/BrowserExitWarnBg.png')
Block_bg = tk.PhotoImage(file='images/BlockBg.png')
Preset =  tk.PhotoImage(file='images/Preset.png')
Write =  tk.PhotoImage(file='images/Write.png')
Back = tk.PhotoImage(file='images/Back.png')

#running the dashboard screen
def blockScreenStart():
    from dashboard import dashboardStart
    from preset import presetStart
    from write import writeStart
    label3 = tk.Label(mainFrame, image= Block_bg)
    label3.place(x = -2, y = -2)

    
    blockScreenPresetButton= tk.Button(mainFrame, image=Preset ,borderwidth=0,command=lambda:[displayPage(presetStart)], bg="#FDFCDC", border=0)
    blockScreenPresetButton.place(x = 235, y = 65)
    
    blockScreenWriteButton= tk.Button(mainFrame, image=Write ,borderwidth=0,command=lambda:[displayPage(writeStart)], bg="#FDFCDC")
    blockScreenWriteButton.place(x=55,y=300)
     
    blockScreenBackButton= tk.Button(mainFrame, image=Back,borderwidth=0,command=lambda:[displayPage(dashboardStart)], bg="#FFFBFD", border=0)
    blockScreenBackButton.place(x = 15, y = 27)
