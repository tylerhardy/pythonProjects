"""02 Class Variables"""
class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

print(Employee.num_of_emps)

emp_1 = Employee('Tyler','Hardy',41000)
emp_2 = Employee('Test','User',60000)

# Class Variables are variables that are shared among all instance of a class
# so while instance variables can be unique for each instance like our names,
# email, and pay class variables should be the same for each instance.

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_2.pay)
Employee.apply_raise(emp_2)
print(emp_2.pay)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# When we try to access an attribute on an instance it will first check if the
# instance contains that attribute.  If it does not contain that attribute it
# will check the class or any class that it inherits from if it contains that
# attribute.

# Print out the namespace of emp_1 This shows all the instance variables that
# the instance emp_1 contains.
print(emp_1.__dict__)

# Print out the namespace of Employee This shows all the class variables that
# the class Employee contains.
print(Employee.__dict__)

Employee.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_1.raise_amount = 1.03

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.__dict__)
print(emp_2.__dict__)

print(Employee.num_of_emps)