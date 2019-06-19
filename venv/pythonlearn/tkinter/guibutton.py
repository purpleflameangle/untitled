#!/usr/bin/python
# -*- encoding: utf-8 -*-
import tkinter as tk
from tkinter import *


def callback():
    var.set("callback")

# 创建一个主窗口，用于容纳整个gui程序
# 设置主窗口对象的标题栏
# 添加一个Label组件，Label组件是gui程序中最常用的组件之一
# Label组件可以显示文本、图标或者图片
# 在这里我们让它显示制定文档
# 然后我们调用Label组件的pack（）方法，用于自动调节组件自身的尺寸
# 注意，这时候窗体还是不会显示的
# 除非执行下面这条代码


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World \n(click me"
        self.hi_there['command'] = self.say_hi
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there,everyone!")


root = tk.Tk()
app = Application(master=root)
app.mainloop()


# checkbutton
root = Tk()
numb = ["一个", 'second', 'third', "four"]
v = []
for num in numb:
    v.append(IntVar())
    b = Checkbutton(root, text=numb, variable=v[-1])
    b.pack()

mainloop()


root = Tk()
v = IntVar()
Radiobutton(root, text="One", variable=v, value=1).pack(anchor=W)
Radiobutton(root, text="Second", variable=v, value=2).park(anchor=W)
Radiobutton(root, text="third", variable=v, value=3).pack(anchor=W)
mainloop()


root = Tk()
LANGS = [("Python", 1), ("Perl", 2), ("Ruby", 3), ("Lua", 4)]
v = IntVar()
v.set(1)
for lang,num in LANGS:
    b = Radiobutton(root, text=lang, variable=v, value=num)
    b.pack(anchor=W)

mainloop()


root = Tk()
LANGS = [("Python", 1), ("Perl", 2), ("Ruby", 3), ("Lua", 4)]
v = IntVar()
v.set(1)
for lang, num in LANGS:
    b = Radiobutton(root, text=lang, variable=v, value=num, indicatoron=False)
    b.pack(fill=X)
mainloop()
