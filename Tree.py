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
    
    def search(self,value):

        def search_rec(crr, value):
            if crr == None:
                return False
            elif value > crr.data:
                return search_rec(crr.right, value)
            elif value < crr.data:
                return search_rec(crr.left, value)
            return True

        return search_rec(self.root, value) 

    def delete(self, value):

        def delete_rec(crr, value):
            return 

        return delete(self.root, value)

    def min(self):

        def min_h(crr):
            if crr.left == None:
                return crr
            return min_h(crr.left)
        
        return min_h(self.root)

    def height(self):

        def height_h(crr):
            if crr == None:
                return -1
            return 1 + max(height_h(crr.left),height_h(crr.right))

        return height_h(self.root)

def test():
    """simple test before the implemntion of the func tests."""
    print("Hello from test")
    b = BST(11)
    b.add(5)
    b.add(12)
    b.add(1)
    b.add(6)
    b.add(13)
    b.show()
    # search test
    """ 
    print(b.search(1))
    print(b.search(6))
    print(b.search(33))
    b.add(13)
    print(b.search(13))
    b.show()
    """
    # min test
    #print("min Node is : ",b.min())
    print(b.height())

""" main test of the tow clases above"""
test()

