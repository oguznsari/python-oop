""" Property Decorators - Getters, Setters and Deleters
    @property allows us to access attributes without putting getters and setters everywhere
    but if we need that funtionality then it is easy to add in with the property decorator
    and if we do this correctly then people using our class won't even need to change any of their code
    because they'll still be able to access those attributes in a same way they did before """

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + "." + last + "@company.com"

    @property                                   # in order to reach to email as an attribute but not as a method ()
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None


emp_1 = Employee("John", "Smith")

emp_1.first = "Jim"                             # updates first and fullname but not the email
print(emp_1.first)
# print(emp_1.email)
# print(emp_1.email())                            # while using as a method(regular)
print(emp_1.email)
print(emp_1.fullname)

emp_1.fullname = "Corey Schafer"                  # need to configure setter

print(emp_1.first)

print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
print(emp_1.fullname)