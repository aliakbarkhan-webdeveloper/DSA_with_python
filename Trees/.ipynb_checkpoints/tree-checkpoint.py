class Tree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

t1=Tree(0)
t1.left=Tree(1)
t1.right=Tree(2)
print(t1)
visualize_tree(t1)