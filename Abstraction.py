from abc import ABC,abstractmethod

class College(ABC):
    def dispaly():
        print("CIET")
        
    @abstractmethod
    def branch(self):
        pass
class Cse(College):
    def branch(self):
        print("CSE Stdents")  
        
class Ece(College):
    def branch(self):
        print("ECE Students")
        
class IT(College):
    def branch(self):
        print("IT Students")
        
c=Cse()
e=Ece()
i=IT()

c.branch()
e.branch()
i.branch()