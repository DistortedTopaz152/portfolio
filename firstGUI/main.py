# Dyson Smith
# Jan. 14-2021
# Gui basics

from tkinter import *
from tkinter import font as font

root = Tk()
root.title("first Gui")
root.geometry("400x400")
root.configure(bg="dark green")
# root.attributes('-fullscreen',True)
lblfnt = font.Font(family="Papyrus", size=32, weight="bold")

frame = Frame(root)
frame.grid()

lbl = Label(frame, text="This is the best label ever", font=lblfnt, bg="magenta", fg="light blue")
lbl2 = Label(frame, text="More Labels", font=lblfnt, bg="magenta", fg="light blue")
lbl3 = Label(frame, text="LABELS", font=lblfnt, bg="magenta", fg="light blue")
lbl.grid()
lbl2.grid()
lbl3.grid()

for i in range(10):
    bttn = Button(frame, text="Monsted"+str(i+1))
    bttn.grid()

bttn1 = Button(text="Do NOT Click!")
bttn1.grid()
bttn2 = Button(frame)
bttn2.configure(text="Really Do NOT Click!")
bttn2.grid()
bttn3 = Button(frame)
bttn3.grid()
bttn3["text"] = "Fine Click it"
keys = {"favcolor": "Red", "favfood": "pizza"}
favlbl = Label(frame, text=keys["favcolor"], font=lblfnt, bg="salmon")
favlbl.grid()

root.mainloop()
