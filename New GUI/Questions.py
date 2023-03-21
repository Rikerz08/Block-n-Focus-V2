from tkinter import *
from tkinter import messagebox as mb
import json
from constants import *
# from tkinter.font import Font

# def changeToDash(newwin):
#     from dashboard import dashboard
#     newwin.destroy()
#     dashboard()

# def UnblockedMsg():
#     from dashboard import dashboard
#     newwin.withdraw()
#     newwin = Toplevel(newwin)
#     newwin.geometry("800x200")
#     newwin.resizable(False, False)
#     newwin.overrideredirect(True)
    
#     #making the window always pop up at the center of the screen
#     screen_width = newwin.winfo_screenwidth()
#     screen_height = newwin.winfo_screenheight()
    
#     x = (screen_width / 2) - (800 / 2)
#     y = (screen_height / 2 ) - (200 / 2)
    
#     newwin.geometry(f'800x200+{int(x)}+{int(y)}')

#     #placing the bg image by using label
#     label2 = Label(newwin, image= unblockedbg)
#     label2.place(x = -2, y = -2)
    
    
#     button= Button(newwin, image=proceed, command=lambda:[newwin.destroy(),dashboard()],borderwidth=0, background="#1E1A1A")
#     button.place(x = 310, y = 138)
    
#     newwin.mainloop()


# def UnblockFailed():
#     from ongoingBlock import ongoingBlock
#     newwin = Toplevel(newwin)
#     newwin.geometry("800x200")
#     newwin.resizable(False, False)
#     newwin.overrideredirect(True)
    
#     #making the window always pop up at the center of the screen
#     screen_width = newwin.winfo_screenwidth()
#     screen_height = newwin.winfo_screenheight()
    
#     x = (screen_width / 2) - (800 / 2)
#     y = (screen_height / 2 ) - (200 / 2)
    
#     newwin.geometry(f'800x200+{int(x)}+{int(y)}')

#     #placing the bg image by using label
#     label2 = Label(newwin, image= UnblockFailedbg)
#     label2.place(x = -2, y = -2)
    
    
#     button= Button(newwin, image=ISuck, command=lambda:[newwin.destroy(), ongoingBlock()],borderwidth=0, background="#1E1A1A")
#     button.place(x = 310, y = 138)
    
#     newwin.mainloop()
    
# def quiz():
#     global newwin
#     newwin = Tk()
#     newwin.geometry("800x500")
#     newwin.title("Quiz")
#     # newwin.overrideredirect(True)
    
#     screen_width = newwin.winfo_screenwidth()
#     screen_height = newwin.winfo_screenheight()

#     x = (screen_width / 2) - (800 / 2)
#     y = (screen_height / 2 ) - (500 / 2)

#     newwin.geometry(f'800x500+{int(x)}+{int(y)}')
    
#     with open('quiz.json') as f:
#         obj = json.load(f)
        
#     global q
#     global options
#     global a
#     q = (obj['ques'])
#     options = (obj['options'])
#     a = (obj['ans'])
    
    
    
#     # global Question_bg
#     # global unblockedbg
#     # global proceed
#     # proceed = PhotoImage(file='images/proceed.png')
#     # unblockedbg = PhotoImage(file='images/SuccessUnblockBg.png')
#     Question_bg = PhotoImage(file='images/Question.png')

#     label3 = Label(newwin, image= Question_bg)
#     label3.place(x = -2, y = -2)
    
#     QuizStart()
#     newwin.mainloop()

def quiz():
    global newwin    
    newwin = tk.Toplevel(root)
    newwin.geometry("800x200")
    newwin.resizable(False, False)
    
    #making the window always pop up at the center of the screen
    screen_width = newwin.winfo_screenwidth()
    screen_height = newwin.winfo_screenheight()
    
    x = (screen_width / 2) - (800 / 2)
    y = (screen_height / 2 ) - (200 / 2)
    
    newwin.geometry(f'800x200+{int(x)}+{int(y)}')

    with open('quiz.json') as f:
        obj = json.load(f)
        
    global q
    global options
    global a
    q = (obj['ques'])
    options = (obj['options'])
    a = (obj['ans'])
    
    Question_bg = PhotoImage(file='images/Question.png')

    #placing the bg image by using label
    label3 = tk.Label(newwin, image= Question_bg)
    label3.place(x = -2, y = -2)


    newwin.mainloop()

class QuizStart:
    def __init__(self):
        self.qn = 0
        self.ques = self.question(self.qn)
        self.opt_selected = IntVar()
        self.opts = self.radiobtns()
        self.display_options(self.qn)
        self.buttons()
        self.correct = 0

    def question(self, qn):
        # t = Label(newwin, text="Quiz in Python Programming", width=50, bg="blue", fg="white", font=("times", 20, "bold"))
        # t.place(x=0, y=2)
        qn = Label(newwin, text=q[qn], width=60, font=("Arial", 16, "bold"), anchor="w", bg="#FDFCDC")

        qn.place(x=70, y=115)
        return qn

    def radiobtns(self):
        val = 0
        b = []
        yp = 160
        while val < 4:
            btn = Radiobutton(newwin, text=" ", variable=self.opt_selected, value=val + 1, font=("Arial", 14), bg="#FDFCDC")
            b.append(btn)
            btn.place(x=100, y=yp)
            val += 1
            yp += 40
        return b

    def display_options(self, qn):
        val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        for op in options[qn]:
              self.opts[val]['text'] = op
              val += 1

    def buttons(self):
        from ongoingBlock import ongoingBlock
        nbutton = Button(newwin, text="Next",command=self.nextbtn, width=10,bg="green",fg="white",font=("Roboto",16,"bold"))
        nbutton.place(x=200,y=380)
        quitbutton = Button(newwin, text="Quit", command= lambda:[newwin.destroy(),ongoingBlock()] ,width=10,bg="red",fg="white", font=("Roboto",16,"bold"))
        quitbutton.place(x=380,y=380)

    def checkans(self, qn):
        if self.opt_selected.get() == a[qn]:
             return True
        
    def nextbtn(self):
        if self.checkans(self.qn):
            self.correct += 1
        self.qn += 1
        if self.qn == len(q):
            self.display_result()
        else:
            self.display_options(self.qn)       
        

    def display_result(self):
        from logicFunctions import unBlock, currList
        from prompts import unblockedMsg, unblockFailed
        score = int(self.correct / len(q) * 100)
        result = "Score: " + str(score) + "%"
        wc = len(q) - self.correct
        correct = "No. of correct answers: " + str(self.correct)
        wrong = "No. of wrong answers: " + str(wc)
        mb.showinfo("Result", "\n".join([result, correct, wrong]))
        # currentTime = datetime.datetime.now()
        # negativeTime = currentTime - datetime.timedelta(minutes=1)
        if score < 70:
            unblockFailed()
        else:
            # with open("./cacheApproach/currListCache.txt", "r") as f:
            #     for line in f:
            #         currLineList = line.split()
            # with open("./cacheApproach/boolValCache.txt", "w") as f:
            #     f.truncate(0)
            #     #this is for the boolean that stops the checktime func when quiz is passed
            #     f.write("True")
            unBlock(currList)
            # checkTime(currentTime,negativeTime,currLineList)
            unblockedMsg()
            # newwin.destroy()










