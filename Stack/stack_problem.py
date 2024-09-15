#Bracket Matching
from jedi.plugins.django import mapping


#Stack
class Stack:
    def __init__(self):
        self.list=[]

    def push(self, item):
        self.list.append(item)
        print(self.list)

    def pop(self):
        if self.list.__len__()==0:
            return None
        return self.list.pop()
    def peek(self):
        if self.list.__len__()==0:
            return None
        return self.list[-1]
    def isEmpty(self):
        if self.list.__len__()==0:
            return True
        return  False



#Solution 1
def valid_paranthesis(string):
    open_brackets="({["
    close_brackets=")}]"
    map=dict(zip(open_brackets,close_brackets))

    s=Stack()
    for c in string:
        #case 1
        if c not in map.values() and c not in map.keys():
            continue
        #case 2
        #check for starting brackets
        if c in map:
            s.push(map[c]) #looking for corresponding closing brackets

        #case 3
        #has to close brackets if we get
        elif s.isEmpty() or c!=s.pop():
            return False
    return s.isEmpty()





valid_paranthesis("(a+b)*{a+c-[a+b])")
# print(a)