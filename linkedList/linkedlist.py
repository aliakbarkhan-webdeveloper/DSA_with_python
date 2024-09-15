class Node:
     def __init__(self,data=None):
        self.val=data
        self.next=None

class linkedlist:
                 def __init__(self):
                    self.head=None

                 def push(self,val):
                    new_node=Node(val)

                    if self.head is None:
                        print("case 1")
                        self.head=new_node
                        return

                    print("case 2")
                    last=self.head
                    while last.next is not None:
                        last=last.next

                    last.next=new_node

                 def pop(self):
                     #Case 1: List is empty
                     if self.head is None:
                         print("list is empty")
                     #Case 2:  only one Node
                     if self.head.next is None:
                         val=self.head.val
                         self.head=None
                         return val
                     #Case 3: More than one nodes
                     temp=self.head
                     prev=None
                     while temp.next is not None:
                         prev=temp
                         temp=temp.next
                     val=temp.val
                     prev.next=None
                     return val

                 #insertion of node
                 def insert(self,idx,val):
                    new_node=Node(val)
                    #insertion at 0th index
                    if idx==0:
                        print("insertion done in case 1")
                        new_node.next=self.head
                        self.head=new_node
                        return

                    #when we want to insert in the middle
                    temp=self.head
                    prev=None
                    counter=0
                    while temp is not None and counter<idx:
                        prev=temp
                        temp=temp.next
                        counter+=1
                        print(counter)
                    prev.next=new_node
                    new_node.next=temp
                    print("insretion done in case 2")

                 #constructor for delete any node
                 def delete(self,val):
                     temp=self.head

                     if temp is None:
                         print("list is empty")
                         return
                     #when we have  only single node in list
                     if temp is not None and temp.val==val:
                         self.head=temp.next
                         temp=None
                         return
                     #when more than one nodes
                     prev = None
                     while temp is not None and temp.val!=val:
                         prev=temp
                         temp=temp.next

                     #removing the node
                     if temp is None:
                        print("list is empty")
                        return
                     prev.next=temp.next
                     temp=None


                 #constructor for finding index
                 def findIdxValue(self,idx):
                    if idx<0:
                        print("index should be greater than 0")
                        return
                    temp=self.head
                    counter=0
                    while counter<idx:
                        if temp.next is None:
                            print("only '",counter," 'indexes are available ")
                            return
                        temp=temp.next
                        counter=counter+1
                    print("final case")
                    return temp.val

                 #constructor for finding length
                 def listLength(self):
                    temp=self.head
                    counter=1
                    if temp is None:
                        print("list is empty")
                        return 0
                    while temp.next is not None:
                        temp=temp.next
                        counter=counter+1
                    print("the length of list is",counter)
                    return counter

                 #Constructor for print Linkedlist list
                 def __str__(self):
                    ret_str='['
                    temp=self.head
                    while temp is not None:
                        ret_str += str(temp.val) + ', '
                        temp=temp.next

                    ret_str=ret_str.rstrip(', ')
                    ret_str+="]"
                    return ret_str





a = linkedlist()
a.push(6)
a.push(10)
a.push(5)
a.push(0)
print(a)

a.insert(3,100)
a.insert(0,5000)

print(a.findIdxValue(50))
a.push(987)
a.listLength()