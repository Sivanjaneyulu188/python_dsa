class Person:
    def personal_details(self):
        print("Person details")
class Company:
    def company_details(self):
        print("Company details")
class Employee(Person, Company):
    def employee_details(self):
        print("Employee details")
e = Employee()
e.personal_details()
e.company_details()
e.employee_details()