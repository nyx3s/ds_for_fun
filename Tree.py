class BtreeNode:
    def __init__(self,data):
        self.data = data
        self.left: BtreeNode = None
        self.right: BtreeNode = None

    def __str__(self):
        left = self.left.data if self.left else "None"
        right = self.right.data if self.right else "None"
        return f"({left}) <= ({self.data}) => ({right})"


class BST:
    def __init__(self, root_data):
        self.root = BtreeNode(root_data)

    def show(self, how="pre"):

        def PreOrder(crr):
            if crr == None:
                return
            print(crr)
            PreOrder(crr.left)
            PreOrder(crr.right)

        if how == "pre":
            PreOrder(self.root)
        elif how == "post":
            print("Not implemented")
        elif how == "in":
            print("Not implemented")
        else:
            print("Please select from the 3 method in/pre/post types of orders.")



    def add(self, data):

        def add_Rec(crr: BtreeNode, data:int):
            if crr == None:
                return BtreeNode(data)
            elif data > crr.data:
                crr.right = add_Rec(crr.right, data)
            elif data < crr.data:
                crr.left = add_Rec(crr.left, data)
            return crr


        return add_Rec(self.root, data)

def test():
    """simple test before the implemntion of the func tests."""
    print("Hello from test")
    b = BST(11)
    b.add(5)
    b.add(12)
    b.add(1)
    b.add(6)
    b.show()

""" main test of the tow clases above"""
test()

