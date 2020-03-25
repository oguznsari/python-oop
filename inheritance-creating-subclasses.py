""" Inheritance allows us to inherit attributes and methods from a parent class
    This is useful because we can create subclasses and get all the functionality of our parent class
    and then we can overwrite or add completely new functionality without affecting the parent class in any way """

class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):                              # specifying what classes we want to inherit from
    raise_amount = 1.10                                 # doesn't effects the Employee parent class

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)                          # let Employee class handle these attributes
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):         # Why we just didn't pass in an empty list as default argument instead on None
        super().__init__(first, last, pay)                          # We never want to pass mutable datatypes like a list or a dictionary as default arguments
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())

# dev1 = Employee("Corey", "Schafer", 50000)
# dev2 = Employee("Test", "User", 60000)
                                                                    # chain of inheritence - method resolution order
dev1 = Developer("Corey", "Schafer", 50000, "Python")               # Developer is empty(no __init__() method) so it gets from Employee class
dev2 = Developer("Test", "User", 60000, "Java")                     # Developer - Employee - builtins.object
                                                                    # every class in Python inherits from this base object
print(dev1.email)
print(dev1.prog_lang)

# print(help(Developer))

print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)

mgr_1 = Manager("Sue", "Smith", 90000, [dev1])
print(mgr_1.email)
mgr_1.add_emp(dev2)
mgr_1.remove_emp(dev1)
mgr_1.print_emps()

print(isinstance(mgr_1, Manager))                               # Even though Developer and Manageer both inherits from Employee
print(isinstance(mgr_1, Employee))                              # they aren't part of each other's inheritance
print(isinstance(mgr_1, Developer))

print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))


""" Using inheritence is extremely useful as our prohects grow in size and makes everything much easier to maintain """