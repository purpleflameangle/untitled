import re


mailre = re.compile(r"(\w+@\w+\.\w+)")

match = []
mails = []

with open('./txt/mailre.txt', 'r+') as f:
    for eachline in f:
        regex = re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b",re.IGNORECASE)
        mails = re.findall(regex, eachline)
        print(mails)
    mails.sort(key=lambda x: len(x))
    print(mails)

with open('./txt/test_new.txt', 'w+') as f1:
    for i in range(len(mails)):
        s = str(mails[i]).replace('[', '').replace(']', '')
        s = s.replace("'", '').replace(',', '') + '\n'
        f1.write(s)

