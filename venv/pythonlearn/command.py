import os


def commando(cmdone):
    with open(cmdone, 'w+') as f:
        f.write('dfs fds')
        f.read()
        print(f.readline())
        print(os.getcwd(), os.listdir(), os.mkdir("test1"), os.makedirs(r".\a\b"), os.remove('commandone.txt'))
        print(os.rename('test1', 'test2'), os.rename('test2', 'test1'), os.rmdir('test1'))


commando('commandone.txt')
