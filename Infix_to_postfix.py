class InfixtoPostFix:
    def __init__(self):
        self.stack=[]
        self.postfix=""
        
    def push(self,val):
        self.stack.append(val)
        
    def pop(self):
        if not self.stack:
            print("Stack is empty")
            
            return
        return self.stack.pop()
    
    def prece(self,ch):
        if ch=="(":
            return 0
        elif ch=="+" or ch=="-":
            return 1
        elif ch=="*" or ch=="/" or ch=="%":
            return 2
        else:
            return -1
    def convert(self,infix):
        for ch in infix:
            if ch.isalpha() or ch.isdigit():
                self.postfix+=ch
            elif ch=="(":
                self.push(ch)
            elif ch==")":
                while self.stack and self.stack[-1] !="(":
                    self.postfix+=self.pop()
                    
                if self.stack and self.stack[-1]=="(":
                    self.pop()
            else:
                while (self.stack and self.prece(ch)<=self.prece(self.stack[-1])):
                    self.postfix+=self.pop()
                self.push(ch)
        while self.stack:
            self.postfix+=self.pop()
        return self.postfix
    
infix = input("Enter infix expression:")
ob=InfixtoPostFix()
postfix=ob.convert(infix)
print("Postfix expression: ",postfix)