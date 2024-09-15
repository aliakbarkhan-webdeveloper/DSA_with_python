class Node:
    def __init__(self, data=None):
        self.val = data
        self.next = None
        self.prev = None


class Doublylinkedlist:
    def __init__(self):
        self.head = None

    #counstructor for Push
    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            print("case 1")
            self.head = new_node
            return
        print("case 2")
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last

    #constructor for pop the data
    def pop(self):
        # Case 1: List is empty
        if self.head is None:
            print("list is empty")
            return None
        # Case 2:  only one Node
        if self.head.next is None:
            val = self.head.val
            self.head = None
            return val
        # Case 3: More than one nodes
        temp=self.head
        while temp.next.next is not None:
            temp = temp.next
        val=temp.next.val
       #temp.next.prev = None # we do not to do it manually bcz when we do next null then their will not be any method to go that node so it will destroyed automatically
        temp.next=None
        return val


    #constructore for insertion if Node
    def insert(self, idx, val):
        new_node = Node(val)
        # insertion at 0th index
        if idx == 0:
            print("insertion done in case 1")
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
            return

        # when we want to insert in the middle
        temp = self.head
        prev = None
        counter = 0
        while temp is not None and counter < idx:
            prev = temp
            temp = temp.next
            counter += 1
            print(counter)
        counter=counter+2
        if idx==counter:
            print("insertion done in case 0000")
            return None
        print("return not working")
        prev.next = new_node
        new_node.prev = prev
        new_node.next = temp
        if temp is not None:
            temp.prev = new_node
        print("insertion done in case 2")


    #length
    def findLength(self):
        print("length of list")



    #remove element of an index
    def remove(self, val):
        print("remove Node")


    #constructor for print list that invoke
    def __str__(self):
        ret_str = '['
        temp = self.head
        while temp is not None:
            ret_str += str(temp.val) + ', '
            temp = temp.next

        ret_str = ret_str.rstrip(', ')
        ret_str += "]"
        return ret_str



a=Doublylinkedlist()
a.push(5)
a.push(7)
a.insert(0,700)
a.insert(1,900)
a.insert(4,10000)

print(a)
