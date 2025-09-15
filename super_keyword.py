class LogicWhile:
    inst = "LogicWhile Training Institute"
    def __init__(self, course):
        self.course = course
    def admission(self):
        print("Admission open for:", self.course)

class Student(LogicWhile):
    def __init__(self, name, course):
        super().__init__(course)   
        self.name = name
    def show_details(self):
        print("Institute:", super().inst)  
        print("Student Name:", self.name)
        print("Course:", self.course)
    def admission(self):
        super().admission()   
        print("Student", self.name, "has taken admission into", self.course)

s = Student("Mani", "Python Full Stack")
s.show_details()
s.admission()