# -*- coding: utf-8 -*-
import tkinter as tk


# 创建一个主窗口，用于容纳整个gui程序
root = tk.Tk()
# 设置主窗口对象的标题栏
root.title("this is gui")
# 添加一个Label组件，Label组件是gui程序中最常用的组件之一
# Label组件可以显示文本、图标或者图片
# 在这里我们让它显示制定文档
Label = tk.Label(root, text="这个是label")
# 然后我们调用Label组件的pack（）方法，用于自动调节组件自身的尺寸
Label.pack()
# 注意，这时候窗体还是不会显示的
# 除非执行下面这条代码
Label.mainloop()


root = tk.Tk()
root.title("hello world")
label = tk.Label(root, text="this is label:hell world")
label.pack()
label.mainloop()


class App:
    def __init__(self, root):
        frame = tk.Frame(root)
        frame.pack()
        self.hi_there = tk.Button(frame, text="hello world", fg='blue', command=self.say_hi())
        self.hi_there.pack(side=tk.LEFT)

    def say_hi(self):
        print("hello world")


root = tk.Tk()
app = App(root)
root.mainloop()
