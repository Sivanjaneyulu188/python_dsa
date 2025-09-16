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
        
def show(entity):
    entity.display()
    entity.course("Python")
    
l=LogicWhile()
s=Student()
show(l)
show(s)

# 832 826 4226