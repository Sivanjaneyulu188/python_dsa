class LogicWhile:
           
    def display(self):
        print("Welcome to LogicWhile:")
        
    def course(self,course_name):
        print(course_name,"is good for future")
        
class Student(LogicWhile):
    
    def display(self):
        print("Welcome student to logicwhile")
        
    def course(self, course_name):
        print(course_name,"is good for seniors")
l=LogicWhile()
l.display()
l.course("Java")

s=Student()
s.display()
s.course("Java")
