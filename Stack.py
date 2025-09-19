from LinkedList import *

class stackList:

    def __init__(self):
        self.top = -1
        self.data = list()

    def __str__(self):
        return f" {self.data} <= top "
    
    def isEmpty(self):
        return self.top == -1

    def push(self, value):
        # only insert in zero index
        self.top += 1
        self.data.append(value)
        return True

    def pop(self):

        assert not self.isEmpty() , "stackList object is Empty"

        value = self.data[-1]
        self.top -= 1
        self.data = self.data[:-1]
        return value

class stackLinked(stackList):

    def __init__(self):

def test():

    s = stackList()

    s.push(1)
    s.push(2)
    s.push(3)

    print(s)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.isEmpty())
    #print(s.pop())
    print(s)

# start
test()
