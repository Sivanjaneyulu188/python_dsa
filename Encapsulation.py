class LogicWhile:
    def __init__(self,name,course):
        self.name=name
        self.__course=course
        self._batch="Morning"
        
    def get_course(self):
        return self.__course
    
    def set_course(self,course):
        if course!="":
            self.__course=course
        else:
            print("Invalid input")
            
ob=LogicWhile("mani","Python")
print(ob.name)
print(ob._batch)
print(ob.get_course())
ob.set_course("Java")
print(ob.get_course())    