#!/usr/bin/python
# -*- encoding: utf-8 -*-

from tkinter import *


root = Tk()
textLabel = Label(root, text="this is textlabel hellO world")
textLabel.pack(side=LEFT)
photo = PhotoImage('df.jpg')
imgLabel = Label(root, image=photo)
imgLabel.pack(side=RIGHT)
mainloop()


root = Tk()
photo = PhotoImage('js.jpg')
textLabel1 = Label(
    root,
    text="hello world",
    justify=LEFT,
    image=photo,
    compound=CENTER,
    font=("微软雅黑", 15),
    bg="red"
)
textLabel1.pack()
mainloop()


