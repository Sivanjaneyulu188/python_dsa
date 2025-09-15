class Employee:
    def work(self):
        print("Employee works")
class Developer(Employee):
    def code(self):
        print("Developer writes code")
class Tester(Employee):
    def test(self):
        print("Tester tests software")
d = Developer()
t = Tester()
d.work()
d.code()
t.work()
t.test()