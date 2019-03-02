from easygui import *
import os
import sys

#msgbox("Hi girl")
'''
message 
author: hermes
'''

msg = "请问你的选择"
title = "选择"
choice = ["谈恋爱", "编程", "think", "书"]
choices = choicebox(msg, title, choice)
msgbox("你的选择：" + str(choices), "结果")

if ccbox(msg, title):
    pass #df
else:
    sys.exit(0)