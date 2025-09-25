class Queue:
    def __init__(self,max_size):
        self.max_size=max_size
        self.queue=[None]*max_size
        self.front=-1
        self.rear=-1
        
    def enqueue(self,ele):
        if self.rear==self.max_size-1:
            return "Queue is empty"
        if self.front==-1:
            self.front=0
        self.rear+=1
        self.queue[self.rear]=ele
    
    def dequeue(self):
        if self.front==-1:
            return "Queue is empty"
        temp=self.queue[self.front]
        self.queue[self.front]=None
        self.front+=1
        if self.front==self.rear:
            self.front=self.rear=-1
        return temp
    
    def getFront(self):
        if self.front==-1:
            return "Queue is empty"
        return self.queue[self.front]
    
    def getRear(self):
        if self.front==-1:
            return "Queue is empty"
        return self.queue[self.rear]
    
    def display(self):
        if self.front==-1:
            return "Queue is empty"
        return self.queue

ob=Queue(5)
ob.enqueue(10)
ob.enqueue(20)
ob.enqueue(30)
ob.enqueue(40)
print("Queue ",ob.display())
print("Front ",ob.getFront())
print("Rear ",ob.getRear())
print("Deque ",ob.dequeue())
print("Queue after dequeue ",ob.display())