class Person:
    def personal_details(self):
        print("Person details")
class Employee(Person):
    def work(self):
        print("Employee works")
class Manager(Employee):
    def manage(self):
        print("Manager manages team")
m = Manager()
m.personal_details()
m.work()
m.manage()