class CircularQueue:
    def __init__(self,max_size):
        self.max_size=max_size
        self.queue=[None]*max_size
        self.front=-1
        self.rear=-1
        
    def enqueue(self,ele):
        if (self.rear+1)%self.max_size==self.front:
            return "Queue is empty"
        if self.front==-1:
            self.front=0
        self.rear=(self.rear+1)%self.max_size
        
        self.queue[self.rear]=ele
    
    def dequeue(self):
        if self.front==-1:
            return "Queue is empty"
        temp=self.queue[self.front]
        self.queue[self.front]=None
          
        if self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front=(self.front+1)%self.max_size
            
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
        result=[]
        i=self.front
        while True:
            result.append(self.queue[i])
            if i==self.rear:
                break
            i=(i+1)%self.max_size
        return result

ob=CircularQueue(5)
ob.enqueue(10)
ob.enqueue(20)
ob.enqueue(30)
ob.enqueue(40)
print("CircularQueue ",ob.display())
print("Front ",ob.getFront())
print("Rear ",ob.getRear())
print("Deque ",ob.dequeue())
print("CircularQueue after dequeue ",ob.display())