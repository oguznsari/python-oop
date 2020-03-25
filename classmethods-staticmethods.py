""" When working with classes Regular methods automatically pass the instance as the 1st argument (self)
                              Class methods automatically pass the class as the 1st argument (cls)
                              Static methods don't pass anything automatically """

class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1                       # incremenst 1 for each employee instance

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):                              # common conventions "self" for instance variable "cls" for class variable
        self.pay = int(self.pay + self.pay * self.raise_amount)

    @classmethod                # adding decorator for class method     # altering the functionality of our method to where
    def set_raise_amount(cls, amount):                                  # we recieve class as 1st argument instead of the instance
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)                    # need to return so that it can be recieved

    @staticmethod                   # static method decorator
    def is_workday(day):            # static methods doesn't take class or instance as the 1st argument
        if day.weekday() == 5 or day.weekday() == 6:          # saturday and sunday
            return False
        return True
# use static method if you don't access class or instance anywhere within the function

emp1 = Employee("Corey", "Schafer", 50000)
emp2 = Employee("Test", "User", 60000)

Employee.set_raise_amount(1.05)                 # we are working with class instead of the instance
# Employee.raise_amount = 1.05                  # does same job

# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

# first, last, pay = emp_str_1.split("-")
# new_emp_1 = Employee(first, last, pay)
# print(new_emp_1.email)
# print(new_emp_1.pay)

""" Can use class methods as alternative constructors;
    Means that we can use these class methods in order to provide multiple ways of creating our objects """

""" We can create an alternative constructor that allows them to pass into a string and we can create Employee """

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)

""" static method """
    #  simple function that takes a date and return whether or not that was a workday

import datetime
my_date1 = datetime.date(2016, 7, 10)        # sunday
my_date2 = datetime.date(2016, 7, 11)        # monday
print(Employee.is_workday(my_date1))
print(Employee.is_workday(my_date2))
