""" These special methods allow us to emulate some built-in behaviour within Python
    and it is also how we implement operator overloading
    -- by defining special methods we'll be able to change some of these built-in behaviour and operations
    __these special methods are alwanys surrounded with double underscores(dunder)__ ** __init__ = dunder init """

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

    def __repr__(self):
        return "Employee(\"{}\", \"{}\", {})".format(self.first, self.last, self.pay)
    # Unambiguous Representation of an object
    # and should be used for debugging and logging etc. it is really meant to be seen by other developers

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)
    # Readable Representation of an object
    # meant to be used as a display to the end-user

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)

print(emp_1)
print(repr(emp_1))
print(str(emp_1))
print(emp_1.__repr__())
print(emp_1.__str__())

""" These two special methods allow us to change how our objects are printed and displayed 
    Unless we are writing some more complicated classes these 3 methods __init__(), __repr__() and __str()__ 
    will be the ones that we'll probably use most often """

print(1 + 3)                        # intergers were added
print(int.__add__(1, 3))
print("a" + "b")                    # strings concatenated
print(str.__add__("a", "b"))

print(emp_1 + emp_2)                # print combined salaries (__add__())

print(len("test"))
print("test".__len__())
print(len(emp_1))
print(len(emp_2))


""" https://docs.python.org/3/reference/datamodel.html#special-method-names """
