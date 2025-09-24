class Postfix:
    def __init__(self,exp):
        self.exp=exp
    
    def evalution(self):
        self.stack=[]
        for i in self.exp:
            if i not in "+-*/":
                self.stack.append(int(i))
            else:
                b=self.stack.pop()
                a=self.stack.pop()
                if i=='+':
                    self.stack.append(a+b)
                elif i=='-':
                    self.stack.append(a-b)
                elif i=='*':
                    self.stack.append(a*b)
                else:
                    self.stack.append(a//b)
        return self.stack.pop()
ex=input()
ob=Postfix(ex)
res=ob.evalution()
print(res)