from LR4.fib import *

def getFibFromRaw(raw):
    fb = FibonacciLst(raw)
    for i in fb:
        pass
    return fb.getResult()

def run():
    print(getFibFromRaw([0, 1, 2, 3, 4, 5, 6, 7, 8, 1, 124, 23, 54, 2, 1, 65, 32]))
