class Employee:
    # Class variables are shared among all instances of a class
    # Instance variables are used for data that is unique to each instance (name, email, pay)


    raise_amount = 1.04
    num_of_emps = 0                             # increment for every instance

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1               # counting number of employees
                                                # using Employee instead of self (same of every instance)

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)           # or Employee.raise_amount but instance raise_amount is better to have
                                                               # because that will give us the ability to change that amount
                                                               # for a single instance if we really wanted to (i.e: emp1 or emp2)

emp1 = Employee("Corey", "Schafer", 50000)
emp2 = Employee("Test", "User", 60000)

print(emp1.fullname())
print(Employee.fullname(emp1))
print(Employee.fullname(emp2))
print(emp1.email)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

# emp1.raise_amount = 1.05              # changes the raise_amount only for emp1(instance)
Employee.raise_amount = 1.05            # changes the raise_amount for the class and all of the instances

print(Employee.raise_amount)
print(emp1.raise_amount)                # they are accesses classes' attributes
print(emp2.raise_amount)

print(emp1.__dict__)                    # accessing the namespace !!! no raise_amount
print(Employee.__dict__)                # class does contain raise_amount attribute

print(Employee.num_of_emps)             # 2 because of emp1 and emp2

# When we try to access an attribute on an instance
# it will 1st checks if the instance contains that attribute
# and if it doesn't then it will see if the class or any class that it inherits from contains that attribute