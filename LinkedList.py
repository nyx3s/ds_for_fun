# auther: @nyx3s
# Date: 25 Aug 2025
""" 
This is a test code and ites made for fun in booring eveing and my brother asked
me about the linked list so i thuout i forget it so i re implemented in python
for frist time i hope the code help every one happycoding.
"""

class Node:
    def __init__(self,data:int):
        self.next:Node = None
        self.data = data
    def __str__(self):
        return f"{self.data}"

class SingeLinkedList:

    def __init__(self,data):
        self.head:Node = Node(data)

    def addON(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            crr = self.head
            while crr.next != None:
                crr = crr.next

            crr.next = newNode

    def addO1(self,data):
        new = Node(data)
        new.next = self.head
        self.head = new


    def addRecersion(self,data):

        def addRec(crrHead ,data):
            if crrHead == None:
                return Node(data)
            else:
                #print("before the Recersion")
                last = addRec(crrHead.next,data)
                crrHead.next = last
                return crrHead

        self.head = addRec(self.head, data)


    def __str__(self):
        # Inefficient for large string bulding .
        """
        re = ""
        crr = self.head
        while crr != None:
            re += f"{crr.data} => "
            crr = crr.next
        return re + "null"
        """
        l = list()
        crr = self.head
        while crr != None:
            l.append(f"{crr.data} => ")
            crr = crr.next
        l.append("null")

        return "".join(l)

"""Test for the above class Node, SingeLinkedList"""
print("hello world")

l = SingeLinkedList(1)
l.addRecersion(2)
#print(l)
l.addRecersion(3)
l.addRecersion(4)
l.addRecersion(5)
l.addRecersion(6)
l.addRecersion(7)
print(l)
