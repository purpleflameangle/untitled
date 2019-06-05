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

