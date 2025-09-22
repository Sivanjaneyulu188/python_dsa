# stack based on list methods
class Stack:
    def __init__(self):
        self.stack=[]
        
    def push(self,val):
        self.stack.append(val)
        
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def display(self):
        return self.stack
    
obj=Stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
print("Stack: ",obj.display())
print("Top Element",obj.peek())
print("delete element",obj.pop())
print("delete element",obj.pop())
print("Stack: ",obj.display())