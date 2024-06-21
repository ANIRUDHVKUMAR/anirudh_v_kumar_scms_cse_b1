"""
stack1 =[]
capacity = 5
stack1.append(10)
stack1.append(20)
stack1.append(30)
stack1.append(40)
print(stack1[-1])
stack1.append(50)
print(stack1)
if(len(stack1)== capacity):
    print("Stack Full")
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()

print(stack1)
if(len(stack1)==0):
    print("Stack Empty")
"""
class Stack:
    def __init__(self, size):
        self.size=size
        self.s=[]
    def push(self,item):
        if(len(self.s) >= self.size):
            print("Stack is Full")
        else:
            self.s.append(item)
            print(self.s)
    def pop(self):
        if(len(self.s) == 0):
            print("Stck is Empty")
        else:
            print(self.s[-1])
            self.s.pop()
            print(self.s)
    def peek(self):
        if(len(self.s) == 0):
            print("Stck is Empty")
        else:
            print(self.s[-1])
    def isEmpty(self):
        if(len(self.s) == 0):
            print("Stck is Empty")
        else:
            print("Stack not Empty")
    def isFull(self):
        if(len(self.s) >= self.size):
            print("Stack is Full")
        else:
            print("Stack not full")
stack1 = Stack(3)
stack1.push(12)
stack1.push(15)
stack1.push(12)
stack1.isFull()
stack1.isEmpty()
stack1.push(76)
stack1.peek()
stack1.pop()
stack1.pop()
stack1.peek()
stack1.pop()
stack1.isFull()
stack1.isEmpty()




    
    
        