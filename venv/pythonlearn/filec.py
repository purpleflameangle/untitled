#1.打开文件；2.读取文件每一行；3.识别每行内容；4.识别出小甲鱼和小客户；5.把每行里面根据：号分割左右两个词，分别装入其他定义变量，6。写入文件，把同时写入名称
#import unittest
import os


def file1(f):
    """

    :rtype: object
    """
    f1 = open(f, 'r')
    count = 0
    boy = []
    girl = []
    for each_line in f1:
        if each_line[:6] != "======":
            (role, spoken) = each_line.split(":", 1)
            if role == '小甲鱼':
                boy.append(spoken)
                count += 1
                boy_filename = "boy_" + str(count) + ".txt"
                fboy = open(boy_filename, "w")
                fboy.write(boy[count])
                fboy.close()
            elif role == '小客服':
                girl.append(spoken)
                girl_filename = "girl_"+str(count) + ".txt"
                fgirl = open(girl_filename, 'w')
                fgirl.write(girl[count-1])
                fgirl.close()
    f1.close()
  

#if __name__ == "__main__":
    #unittest.main()
file1('recordxiao.txt')
