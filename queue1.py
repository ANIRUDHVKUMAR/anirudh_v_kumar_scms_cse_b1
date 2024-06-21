class Queue:
    def __init__(self,size):
        self.size=size
        self.q=[]
    def enqueue(self,item):
        if(len(self.q) >= self.size):
            print("Queue is Full")
        else:
            self.q.append(item)
            print(self.q)
    def dequeue(self):
        if(len(self.q) == 0):
            print("Queue is Empty")
        else:
            print(self.q[0])
            self.q.pop(0)
            print(self.q)
    def front(self):
        if(len(self.q) == 0):
            print("Queue is Empty")
        else:
            print(self.q[0])
    def rear(self):
        if(len(self.q) == 0):
            print("Queue is Empty")
        else:
            print(self.q[-1])
    def isEmpty(self):
        if(len(self.q) == 0):
            print("Queue is Empty")
        else:
            print("Queue not Empty")
    def isFull(self):
        if(len(self.q) >= self.size):
            print("Queue is Full")
        else:
            print("Queue not full")
q1 = Queue(3)
q1.enqueue(8)
q1.front()
q1.rear()
q1.enqueue(18)
q1.enqueue(82)
q1.front()
q1.rear()
q1.isEmpty()
q1.isFull()
q1.enqueue(98)
q1.dequeue()
q1.front()
q1.rear()
q1.dequeue()
q1.dequeue()
q1.isEmpty()
q1.isFull()
q1.enqueue(23)
            