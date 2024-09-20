class BST:
    def __init__(self,val,parent=None):
        # super.__init__(val)
        self.val=val
        self.left=None
        self.right=None
        self.parent=parent

    def insert(self,val):
        if val<self.val:   #handeling smaller and insertion in left
            if self.left is None:
                new_node=BST(val,parent=self)
                self.left=new_node
            else: self.left.insert(val)
        else:  #handeling greater val case
            if self.right is None:
                self.right=BST(val,parent=self)
            else: self.right.insert(val)
    
    def search(self,data):
        print("search")


    #helping Constructors for deletion process

    #to find root of tree
    def find_root(self):
        temp=self
        while temp.parent is not None:
            temp=temp.parent
        return temp
    
    def find_min(self):
        min_node=self
        if self.left is not None:
            min_node=self.left.find_min()
        return min_node
    
    #constructor to delete self reference and attach its child to its Parent
    def set_for_parent(self,new_ref):
        if self.parent is None: return

        if self.parent.right==self:
            self.parent.right=new_ref
        if self.parent.left ==self:
            self.parent.left=new_ref
        
     #constructor to set child Node at its place, so its reference can be removed permanently
    def replace_with_node(self,node):
        #connect new node to parent at proper location
        self.set_for_parent(node)
        #set node's parent correctly
        node.parent=self.parent
        #disconnect from parent
        self.parent=None
        #find root again and return it
        return self.find_root()

    def delete(self,val):

        #condition 1: if only parent node and value also matches then return None/delete node
        if self.parent is None and self.right is None and self.left is None and self.val==val:
            return None

        #Condition 2: we are having one leaf Node

        if self.val==val:
            if self.left is None and self.right is None:   # checking if we are leaf Node or Not.
                self.set_for_parent(None)
                return self.find_root()

            #checking if we have only right Node
            if self.left is None:
                return self.replace_with_node(self.right)
            #checking if we have only left Node
            if self.right is None:
                return self.replace_with_node(self.left)

            #condition when we have two nodes, find successor/child and change it with self
            successor=self.right.find_min()
            #copy successor value
            self.val=successor.val

            return self.right.delete(successor.val)
        #if the value that we want to delete is its children then find it
        if val<self.val:
            if self.left is not None:
                return self.left.delete(val)
            else:
                return self.find_root() #--> Nothing to delete, node not found
        else: # if value is greater then we will travel on right side
            if self.right is not None:
                return self.right.delete(val)
            else:
                return self.find_root()



l=[1,2,3,4,5,7,8,9,10]
t=BST(6)
for i in l:
    t.insert(i)

print(t.val)
print(t.left.right.val)
