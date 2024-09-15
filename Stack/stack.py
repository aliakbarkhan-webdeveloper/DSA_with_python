class Stack:
    def __init__(self):
        self.list=[]

    def push(self, item):
        self.list.append(item)
        print(self.list)

    def pop(self):
        if self.list.__len__()==0:
            print("Stack is empty")
            return
        return self.list.pop()
    def peek(self):
        if self.list.__len__()==0:
            print("Stack is empty")
            return
        return self.list[-1]
    def isEmpty(self):
        if self.list.__len__()==0:
            print("Stack is empty")
            return True
        return  False

s=Stack()
s.push(5)
s.push(78)
s.push(5678)
print(s.isEmpty())