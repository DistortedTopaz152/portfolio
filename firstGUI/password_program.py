from tkinter import *
from tkinter import font as font


class App(Frame):
    usernames = ["dyson"]
    passwords = ["password"]
    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.trys = 0

    def create_widgets(self):
        self.lbl1 = Label(self, font=lblfont, text="Welcome User",fg="blue")
        self.lbl2 = Label(self, font=lblfont, text="Enter Username")
        self.lbl3 = Label(self, font=lblfont, text="Enter Password")
        self.bttn_submit = Button(self, font=lblfont, text="Submit", bg="blue", fg="white")
        self.bttn_submit["command"]=self.submit
        self.user_tb = Entry(self)
        self.pw_tb = Entry(self)
        self.output = Text(self)

        # placing on grid

        self.lbl1.grid(row=0,column=0,columnspan=3)
        self.lbl2.grid(row=1,column=0,sticky=NW)
        self.lbl3.grid(row=2,column=0,sticky=SW)
        self.bttn_submit.grid(row=3,column=0,sticky=W)
        self.user_tb.grid(row=1,column=1,columnspan=2)
        self.pw_tb.grid(row=2, column=1,columnspan=2)
        self.pw_tb.configure(show="*")
        self.output.grid(row=4,column=0,columnspan=3)
        self.output.configure(width=31)

    def submit(self):
        username = self.user_tb.get()
        password = self.pw_tb.get()
        if username in self.usernames:
            if password in self.passwords:
                message = "you got in"
                self.trys = 0
            else:
                message = "wrong password"
                self.trys += 1
        else:
            message = "wrong user name"
            self.trys += 1
        self.output.delete(0.0,END)
        self.output.insert(0.0,message)
        if self.trys > 3:
            message = "To many failed attempts "
            self.output.delete(0.0, END)
            self.output.insert(0.0, message)
            self.user_tb.configure(state=DISABLED)
            self.pw_tb.configure(state=DISABLED)
            self.bttn_submit.configure(state=DISABLED)


root = Tk()
root.title("Passwords")
root.geometry("250x250")
lblfont = font.Font(family="Papyrus", size=11)
app = App(root)

root.mainloop()
