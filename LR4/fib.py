from itertools import islice

def genListWhileLower(n):
    a = [0, 1]
    while a[-1] + a[-2] <= n:
        a.append(a[-1] + a[-2])
    return a

class FibonacciLst:
    def __init__(self, rawArray):
        self.rawArray = rawArray
        self.index = 0
        self.a = genListWhileLower(max(rawArray))
        self.result = []

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.rawArray):
            curVal = self.rawArray[self.index]
            if curVal in self.a:
                self.result.append(curVal)
            self.index += 1
        raise StopIteration

    def getResult(self):
        return self.result


def getWithItertool(iterable):
    fibValues = {0, 1}
    a, b = 0, 1

    n = max(iterable)
    while a + b < n:
        fibValues.add(b)
        a, b = b, a + b

    ans = []
    for val in islice(iterable, None):
        if val in fibValues:
            ans.append(val)

    return ans
