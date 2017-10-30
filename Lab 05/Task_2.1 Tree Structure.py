class Tree():
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
        
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

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
root.left.left.left = Tree(6)
root.left.right.left = Tree(7)
root.left.right.right = Tree(8)

print('Pre Order')
root.PreOrder(root)
print('In Order')
root.InOrder(root)
print('Post Order')
root.PostOrder(root)