class LogicWhile:
    def __init__(self,course):
        self.course=course
        
    def display(self):
        print("LogicWhile offers:",self.course)
        
class Student:
    def __init__(self,name,course):
        self.name=name
        self.course=course
    
    def display(self):
        print("Student Name:",self.name)
        print("Enrolled coure:",self.course)
        
l=LogicWhile("Python Full Stack")
l.display()
s=Student("Mani","Python Full Stack")
s.display()