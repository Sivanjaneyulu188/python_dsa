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
    
    def insert_at_end(self,val):
        newnode=Node(val)
        if self.head==None:
            self.head=newnode
            return
        
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=newnode
        
    def delete_at_begin(self):
        if self.head is None:
            print("LL is Empty")
            return
        self.head=self.head.next
        
    def delete_at_end(self):
        if self.head is None:
            print("LL is empty")
            return
        if self.head.next is None:
            self.head=None
            
        temp=self.head
        while temp.next!=None:
            prev=temp
            temp=temp.next
            
        prev.next=None
        
    def delete_at_specific(self,pos):
        if pos<1 and self.head is None:
            print("LL is empty")
            return
        
        if pos==1:
            self.head=self.head.next
        
        temp=self.head    
        curr_pos=1
        while temp!=None and curr_pos<pos-1:
            temp=temp.next
            curr_pos+=1
        if temp==None:
            print("position out of range")
            return
        temp.next=temp.next.next
                    

ob=SLL()
ob.insert_at_end(1000)
ob.insert_at_end(2000)
ob.insert_at_end(3000)
ob.insert_at_end(4000)
ob.traversal()
ob.delete_at_begin()
ob.traversal()
ob.delete_at_end()
ob.traversal()
ob.delete_at_specific(200)
ob.traversal()