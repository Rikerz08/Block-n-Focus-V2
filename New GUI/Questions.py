from tkinter import *
from tkinter import messagebox as mb
import json
from constants import *


def quiz():
    # initialize variable to let logicFunc page know if quiz was passed or not
    global isQuizPassed
    isQuizPassed = False
    global quizNewwin    
    quizNewwin = tk.Toplevel(root)
    quizNewwin.geometry("800x500")
    quizNewwin.resizable(False, False)
    #making the window always pop up at the center of the screen
    screen_width = quizNewwin.winfo_screenwidth()
    screen_height = quizNewwin.winfo_screenheight()
    
    x = (screen_width / 2) - (800 / 2)
    y = (screen_height / 2 ) - (500 / 2)
    
    quizNewwin.geometry(f'800x500+{int(x)}+{int(y)}')

    with open('quiz.json') as f:
        obj = json.load(f)
        
    global q
    global options
    global a
    q = (obj['ques'])
    options = (obj['options'])
    a = (obj['ans'])
    
    Question_bg = PhotoImage(file='images/Question2.png')

    #placing the bg image by using label
    label3 = tk.Label(quizNewwin, image= Question_bg)
    label3.place(x = -2, y = -2)

    quizStart()
    quizNewwin.mainloop()

class quizStart:
    def __init__(self):
        self.qn = 0
        self.ques = self.question(self.qn)
        self.opt_selected = IntVar()
        self.opts = self.radiobtns()
        self.display_options(self.qn)
        self.buttons()
        self.correct = 0

    def question(self, qn):
        # t = Label(quizNewwin, text="Quiz in Python Programming", width=50, bg="blue", fg="white", font=("times", 20, "bold"))
        # t.place(x=0, y=2)
        qn = Label(quizNewwin, text=q[qn], width=60, font=("Arial", 16, "bold"), anchor="w", bg="#FDFCDC")

        qn.place(x=70, y=115)
        return qn

    def radiobtns(self):
        val = 0
        b = []
        yp = 160
        while val < 4:
            btn = Radiobutton(quizNewwin, text=" ", variable=self.opt_selected, value=val + 1, font=("Arial", 14), bg="#FDFCDC",fg="black")
            # btn = Radiobutton(quizNewwin, text=" ", variable=self.opt_selected, value=val + 1, font=("Arial", 14), bg="#FDFCDC",fg="white", selectcolor = "black")
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
        from ongoingBlock import ongoingBlockStart
        nbutton = Button(quizNewwin, text="Next",command=self.nextbtn, width=10,bg="green",fg="white",font=("Roboto",16,"bold"))
        nbutton.place(x=200,y=380)
        quitbutton = Button(quizNewwin, text="Quit", command= lambda:[root.deiconify(),quizNewwin.destroy(), ongoingBlockStart()] ,width=10,bg="red",fg="white", font=("Roboto",16,"bold"))
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
        from logicFunctions import unBlock, questionCurrList
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
            quizNewwin.destroy()
            unblockFailed()
        else:
            #idk why global should be inside here instead sa outside func and pinakataas of the page
            global isQuizPassed
            isQuizPassed = True
            quizNewwin.destroy()
            unBlock(questionCurrList)
            unblockedMsg()
            # with open("./cacheApproach/currListCache.txt", "r") as f:
            #     for line in f:
            #         currLineList = line.split()
            # with open("./cacheApproach/boolValCache.txt", "w") as f:
            #     f.truncate(0)
            #     #this is for the boolean that stops the checktime func when quiz is passed
            #     f.write("True")
            # checkTime(currentTime,negativeTime,currLineList)
            
            # quizNewwin.destroy()