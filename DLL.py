class Node:
    def __init__(self,val):
        self.data=val
        self.prev=None
        self.next=None
class Dll:
    def __init__(self):
        self.head=None
        
    def forward(self):
        if self.head is None:
            print("DLL is Empty")
            return
        temp=self.head
        while temp:
            print(temp.data,end="<-->")
            temp=temp.next
        print("Null \n")
        
    def backward(self):
        if self.head is None:
            print("DLL is Empty")
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        
        while temp:
            print(temp.data,end="<-->")
            temp=temp.prev
        print("Null \n")
    
    def insert_at_begin(self,val):
        newnode=Node(val)
        if self.head==None:
            self.head=newnode
            return
        
        newnode.next=self.head            
        self.head.prev=newnode
        self.head=newnode     
    
    def insert_at_end(self,val):
        newnode=Node(val)
        if self.head is None:
            self.head=newnode
        
        temp=self.head
        while temp.next:
            temp=temp.next
        newnode.prev=temp    
        temp.next=newnode        
        
    def delete_at_begin(self):
        if self.head is None:
            print("LL is empty")
            return
        if self.head.next is None:
            self.head=None
            return
        
        self.head=self.head.next
        self.head.prev=None
        
    def delete_at_end(self):
        if self.head is None:
            print("LL is Empty")
            return
        if self.head.next is None:
            self.head=None
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.prev.next=None
        
    def insert_at_position(self,pos,val):
        newnode=Node(val)
        if pos<1 and self.head is None:
            print("DLL is Empty")
            return
        if pos==1:
            newnode.next=self.head
            self.head=newnode
            return
        
        
    
obj=Dll()
obj.insert_at_begin(10)
obj.insert_at_begin(20)
obj.insert_at_begin(30)
obj.insert_at_begin(40)
obj.forward()
# obj.backward()
obj.insert_at_end(50)
obj.forward()
# obj.backward()
obj.delete_at_begin()
obj.forward()
obj.delete_at_end()
obj.forward()