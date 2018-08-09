class Tree():
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

    def Insert(self, value):
        if self.data == None:
            self.data = Tree(value)
            return
        elif value < self.data:
            if self.left == None:
                self.left = Tree(value)
                return
            else:
                if self.left != None:
                    self.Insert(self,value)
        elif value > self.data:
            if self.right == None:
                self.right = Tree(value)
                return
            else:
                if self.right != None:
                    self.Insert(self, value)

        
    def PreOrder(self, root):
        if root:
            print(root.data)
            self.PreOrder(root.left)
            self.PreOrder(root.right)
    def PreOrderList(self, root, list):
        if root:
            list.append(root.data)
            self.PreOrder(root.left, list)
            self.PreOrder(root.right, list)
        else:
            return list
    def InOrder(self, root):
        if root:
            self.InOrder(root.left)
            print(root.data)
            self.InOrder(root.right)
            
    def PostOrder(self, root):
        if root:
            self.PostOrder(root.left)
            self.PostOrder(root.right)
            print(root.data)

root = Tree(5)
root.Insert(2)
root.Insert(6)
root.Insert(7)
##root.Insert(1)
##root.Insert(3)
##root.Insert(5)
##root.Insert(4)

print('Pre Order')
root.PreOrder(root)
print('In Order')
root.InOrder(root)
print('Post Order')
root.PostOrder(root)
