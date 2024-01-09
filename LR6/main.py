from LR5.valutes import Vals

def run():
    singletonInstance = Vals()
    singletonInstance2 = Vals()
    print(singletonInstance == singletonInstance2)
