class Stack:
    def __init__(self,max_size):
        self.max_size=max_size
        self.stack=[None]*self.max_size
        self.top=-1
        
    def push(self,val):
        if self.top==self.max_size-1:
            print("Stack is Full")
        else:
            self.top+=1
            self.stack[self.top]=val
            
    def pop(self):
        if self.top==-1:
            print("Stack is empty")
        else:
            temp=self.stack[self.top]
            self.stack[self.top]=None
            self.top-=1
            return temp
        
    def peek(self):
        if self.top==-1:
            print("Stack is empty")
        else:
            return self.stack[self.top]
        
    def display(self):
        if self.top==-1:
            print("Stack is empty")
        else:
            return self.stack
        
obj=Stack(5)
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.push(50)
print("Stack: ",obj.display())
print("Top Element",obj.peek())
print("delete element",obj.pop())
print("delete element",obj.pop())
print("Stack: ",obj.display())