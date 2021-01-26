from tkinter import *
from tkinter import font as font


class App(Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid()
        self.clicks = 0
        self.colors = ["red", "blue", "yellow", "green", "pink", "purple"]
        self.color_index = 0
        self.create_widgets()

    def create_widgets(self):
        self.lbltotal = Label(self, text="Total clicks:")
        self.lblnumclicks = Label(self, text=str(self.clicks))
        self.addbttn = Button(self, text="+ to count")
        self.minbttn = Button(self, text="- from count")
        self.colorbttn = Button(self, text="change color")
        self.addbttn.configure(width=28, height=3)
        self.addbttn["command"] = self.add_to_count
        self.colorbttn.configure(width=28, height=3)
        self.colorbttn["command"] = self.change_color
        self.minbttn.configure(width=28, height=3)
        self.minbttn["command"] = self.minus_to_count

        self.colorbttn.grid()
        self.lbltotal.grid()
        self.lblnumclicks.grid()
        self.addbttn.grid()
        self.minbttn.grid()

    def add_to_count(self):
        self.clicks += 1
        print(self.clicks)
        self.lblnumclicks.configure(text=self.clicks)

    def minus_to_count(self):
        self.clicks -= 1
        if self.clicks < 0:
            self.clicks = 0
        print(self.clicks)
        self.lblnumclicks.configure(text=self.clicks)

    def change_color(self):
        self.color_index += 1
        if self.color_index >= 6:
            self.color_index = 0
        self.configure(bg=self.colors[self.color_index])
        self.lbltotal.configure(bg=self.colors[self.color_index])
        self.lblnumclicks.configure(bg=self.colors[self.color_index])
        self.addbttn.configure(bg=self.colors[self.color_index])
        self.minbttn.configure(bg=self.colors[self.color_index])
        self.colorbttn.configure(bg=self.colors[self.color_index])


root = Tk()
root.title("first Gui")
root.geometry("200x200")
# root.attributes('-fullscreen',True)
app = App(root)

root.mainloop()
