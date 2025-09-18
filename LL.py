class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    
    def traversal(self):
        if self.head==None:
            print("LL is Empty")
        temp=self.head
        while temp!=None:
            print(temp.data,end="-->")
            temp=temp.next 
        print("NULL")
    def insert_begin(self,val):
        newnode=Node(val)    
        if self.head==None:
            self.head=newnode 
        else:
            newnode.next=self.head
            self.head=newnode    
    
    def insert_at_end(self,val):
        newnode=Node(val)
        if self.head==None:
            self.head=newnode
        
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=newnode
        
    def insert_at_postion(self,val,pos):
        newnode=Node(val)
        temp=self.head
        current_pos=1
        if pos<1:
            print("Invalid position")
            return
        if pos==1:
            newnode.next=self.head
            self.head=newnode
            return
        while temp!=None and current_pos<pos-1:
            temp=temp.next
            current_pos+=1
            
        if temp==None:
            print("Position is out of range")
            return
        newnode.next=temp.next
        temp.next=newnode
        
    def delete_at_begin(self):
        if self.head==None:
            print("List is Empty")
        else:    
            temp=self.head
            self.head=temp.next
        
        
    def delete_at_end(self):
        temp=self.head
        prev=None
        if self.head==None:
            print("List is empty")
            
        if temp.next==None:
            temp=None
            
        while temp.next!=None:
            prev=temp
            temp=temp.next
        prev.next=None
            
        
    
l=SLL()
l.insert_begin(10)
l.insert_begin(20)
l.insert_begin(30)
l.insert_begin(40)
l.insert_at_end(50)
l.insert_at_postion(60,3)
l.traversal()
l.delete_at_begin()
l.traversal()
l.delete_at_end()
l.traversal()