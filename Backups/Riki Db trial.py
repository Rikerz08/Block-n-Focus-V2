import os
import tkinter
import customtkinter

#setting theme, window, and mode for GUI
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()
root.geometry("500x300")


# hosts path for windows (uncomment the code according to your system)
hostsPath = "C:\Windows\System32\drivers\etc\hosts"

# #hosts path for linux/mac (uncomment the code according to your system)
# hostspath = "/etc/hosts"

localRedirect = "127.0.0.1"
webLists = [];
#list for websites

def plus(a):
    a.destroy()
    WebReg()
    

def dec(a):
    global number_of_inputs
    if number_of_inputs == 1:
        number_of_inputs = 1
    else:
        number_of_inputs = number_of_inputs - 1
    a.destroy()
    WebReg()
    

number_of_inputs = 1




def WebReg():
    newwin = customtkinter.CTkToplevel()

    frame = customtkinter.CTkFrame(master=newwin)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    
    entry_widget = []
    
    for j in range(number_of_inputs):
        label = customtkinter.CTkLabel(master=frame, text="Entry: " +str(j+1), font=customtkinter.CTkFont(size=25, family="Roboto", weight="bold"))
        label.grid(row=j, column=0,padx=3)
        
        entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="EX.(www.google.com)")
        entry1.grid(row=j, column=1,padx=10,pady=3) 
        entry_widget.append(entry1)
        
        
        
    buttonPlus = customtkinter.CTkButton(master=frame, text="next", command=lambda:([webLists.append(w.get()) for w in entry_widget], plus(newwin)))
    buttonPlus.grid(row=j+1,column=0,padx=3,pady=5)
    
    # buttonDec = customtkinter.CTkButton(master=frame, text="-", command=lambda: [dec(newwin)])
    # buttonDec.grid(row=j+1,column=1,padx=3,pady=5)
        
    button1 = customtkinter.CTkButton(master=frame, text="finish", command=lambda: ([webLists.append(w.get()) for w in entry_widget], verify(newwin)))
    button1.grid(row=j+1,column=2,padx=3,pady=5)

def taskkill(a,b):
    a.destroy()
    b.destroy()
    os.system("taskkill /im firefox.exe /f")
    os.system("taskkill /im chrome.exe /f")
    os.system("taskkill /im opera.exe /f")
    os.system("taskkill /im msedge.exe /f")
    
     

def exit(a):
    # b.destroy()
    oldtab = a
    newwin = customtkinter.CTkToplevel()
    frame = customtkinter.CTkFrame(master=newwin)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    
    label1 = customtkinter.CTkLabel(master=frame, text="Proceeding will exit all browsers. Unsaved progress will be lost.", font=customtkinter.CTkFont(size=25, family="Roboto", weight="bold"))
    label1.pack(pady=12, padx=10)
    # print("Proceeding will exit all browsers. Unsaved progress will be lost.")
    label2 = customtkinter.CTkLabel(master=frame, text="Do you wish to proceed or exit browsers manually? ", font=customtkinter.CTkFont(size=25, family="Roboto"))
    label2.pack(pady=12, padx=10)
    # killDecision = input("Do you wish to proceed or exit browsers manually? (Y/N) ")

    button1 = customtkinter.CTkButton(master=frame, text="Proceed", command=lambda: [taskkill(newwin,oldtab)])
    button1.pack(pady=12, padx=10)

    # if killDecision == "Y":
    #     os.system("taskkill /im firefox.exe /f")
    #     os.system("taskkill /im chrome.exe /f")
    #     os.system("taskkill /im opera.exe /f")
    #     os.system("taskkill /im msedge.exe /f")
     
def verify(a):
    oldtab = a
    newwin = customtkinter.CTkToplevel()
    print(webLists)
    with open (hostsPath, 'a+') as f:
        f.seek(0)
        fileContent = f.read()
        
        for web in webLists:
            if web in fileContent:
                frame = customtkinter.CTkFrame(master=newwin)
                frame.pack(pady=20, padx=60, fill="both", expand=True)
                label = customtkinter.CTkLabel(master=frame, text= web + " is already listed.", font=customtkinter.CTkFont(size=25, family="Roboto", weight="bold"))
                label.pack(pady=12, padx=10)
                button1 =customtkinter.CTkButton(master=frame, text="Ok", command= lambda:[newwin.destroy()])
                button1.pack(pady=12, padx=10)
                pass

            else:
                newwin.destroy()
                f.write("\n")
                f.write(localRedirect + " " + web)
                exit(oldtab)
def Unblock():  
    print("unblock sites")
    with open (hostsPath, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            #statement to know if there are no words in the line that belong to the weblists, 
            # because if there are none found, the line would be written back to the hostfile, and not removed
            if not any(web in line for web in webLists):
                f.write(line)
        #cuts of all lines that were not written in line 72
        f.truncate()




frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="BlocknGo", font=customtkinter.CTkFont(size=25, family="Roboto", weight="bold"))
label.pack(pady=12, padx=10)

button =customtkinter.CTkButton(master=frame, text="Start Blocking", command=WebReg)
button.pack(pady=12, padx=10)

buttonUnblock =customtkinter.CTkButton(master=frame, text="Unblock", command=Unblock)
buttonUnblock.pack(pady=12, padx=10)



root.mainloop()