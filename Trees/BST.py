

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
            

class BST:
    def __init__(self,val,parent=None):
        super.__init__(val)
        self.parent=parent
    
    def insert(self,val): 
        if val<self.val:#handeling smaller and insertion in left
            if self.left==None:
                new_node=BST(val,parent=self)
                self.left=new_node
            else: self.inser(val)
        else:  #handeling greater val case
            if self.right is None:
                self.right=BST(val,parent=self)
            else: self.right.insert(val)
    
    def search(self,data):
        print("search")
    def delete(self,data):
        print("delete")


tree=Tree(0)
tree.left=Tree(1)
tree.right=Tree(2)
tree.left.left=Tree(3)
tree.left.right=Tree(4)
tree.right.left=Tree(5)
tree.right.right=Tree(6)