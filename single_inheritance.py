class Employee:
    def work(self):
        print("Employee works")
class Manager(Employee):
    def manage(self):
        print("Manager manages team")
m = Manager()
m.work()
m.manage()