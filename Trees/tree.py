

class Tree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

    def pot(self):
        print(self.val)
        if self.left:
            self.left.pot()
        if self.right:
            self.right.pot()

    def preOr(self):
        if self.left:
            self.left.pot()
        if self.right:
            self.right.pot()
            print(self.val)

    def ino(self):
        if self.left:
            self.left.pot()
        print(self.val)
        if self.right:
            self.right.pot()
    def bfs(self):
        to_visit=[self]
        while to_visit:
            current=to_visit.pop(0)
            print(current.val)
            if current.left:
                to_visit.append(current.left)
            if current.right:
                to_visit.append(current.right)
            



tree=Tree(0)
tree.left=Tree(1)
tree.right=Tree(2)
tree.left.left=Tree(3)
tree.left.right=Tree(4)
tree.right.left=Tree(5)
tree.right.right=Tree(6)

tree.bfs()