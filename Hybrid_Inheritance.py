class Person:
    def personal_details(self):
        print("Person details")
class Employee(Person):
    def work(self):
        print("Employee works")
class Trainer(Person):
    def train(self):
        print("Trainer trains employees")
class Manager(Employee, Trainer):
    def manage(self):
        print("Manager manages team")
m = Manager()
m.personal_details()
m.work()
m.train()
m.manage()