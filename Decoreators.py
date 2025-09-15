class LogicWhile:
    def __init__(self,name,course):
        self.name=name
        self.__course=course
        self._batch="Morning"
        
        
    @property   
    def course(self):
        return self.__course
    
    @course.setter
    def course(self,val):
        if val!="":
            self.__course=val
        else:
            print("Invalid input")
            
ob=LogicWhile("mani","Python")
print(ob.name)
print(ob._batch)
print(ob.course)
ob.course="Java"
print(ob.course)