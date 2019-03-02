def splitefile(f):
    count = 0
    girl = []
    boy = []
    fil = open(f, 'r')
    for eachline in fil:
        if eachline[:6] != "======":
            (role, spoken) = eachline.split(':', 1)
            if role == '小甲鱼':
                boy.append(spoken)
            elif role == '小客户':
                girl.append(spoken)
        else:
            save_file(boy, girl, count)
            boy = []
            girl = []
            count += 1
    #save_file(boy, girl, count)
    fil.close()


def save_file(boy, girl, count):
    boy_fname = "boy_"+str(count)+'.txt'
    girl_fname = "girl_"+str(count)+'.txt'
    bf = open(boy_fname, 'w')
    bf.writelines(boy)
    gf = open(girl_fname, 'w')
    gf.writelines(girl)
    bf.close()
    gf.close()


splitefile("recordxiao.txt")

