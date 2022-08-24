import os


def toFile(filename, mode, data):
    f = open(filename, mode)
    for i in range(5):
        f.write(str(i) + ':' + data + '\r\n')
    f.close()


def writeFile(filename):
    toFile(filename, 'w', 'Hello World')


def appendFile(filename):
    toFile(filename, 'a', 'Hello World')


def readFile(filename):
    if not os.path.exists(filename):
        print('File not found')
        return
    f = open(filename, 'r')
    print(f.read())
    f.close()


# see it in action
myfile = 'hello.txt'
writeFile(myfile)
appendFile(myfile)
readFile(myfile)
