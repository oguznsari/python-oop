# Python Object-Oriented Programming

# Logically grouping data&functions(attributes&methods) in a way that is easy to reuse and also easy to build upon when needed


class Employee:        # a class is basically a blueprint for creating instances
     # each method in a class automatically takes the instance as the 1st argument(self)
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)              # Each of these going to be their own unique instances of the Employee class

# print(emp_1)
# print(emp_2)                    # can see that both of these are Employee objects and unique

# emp_1.first = "Corey"
# emp_1.last = "Schafer"
# emp_1.email = "Corey.Schafer@company.com"
# emp_1.pay = 50000
#
# emp_2.first = "Test"
# emp_2.last = "User"
# emp_2.email = "Test.User@company.com"
# emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

# print("{} {}".format(emp_1.first, emp_1.last))
print(emp_1.fullname())                         # emp_1 passes as the 1st argument automatically
print(emp_2.fullname())                         # emp_2 passes as the 2nd argument automatically

print(Employee.fullname(emp_1))                 # manually passing the instances (while running from a class)
print(Employee.fullname(emp_2))                 # manually passing the instances (while running from a class)