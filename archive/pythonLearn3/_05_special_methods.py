"""05 Special (Magic/Dunder) Methods"""
# 
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        # An unambiguous representation of the object and should be used for
        # debugging and logging.  Meant to only be seen by other developers.
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        # A more readable representation of an object and is meant to be used
        # as a display to the end user.
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())
    

emp_1 = Employee('Tyler','Hardy',41000)
emp_2 = Employee('Test','User',60000)

print(emp_1)

# Typical syntax
print(repr(emp_1))
print(str(emp_1))
# Verbose syntax
print(emp_1.__repr__())
print(emp_1.__str__())

print(1+2)

print(int.__add__(1,2))
print(str.__add__('a','b'))

print(emp_1 + emp_2)


print(len('test'))
print('test'.__len__())

print(len(emp_1))
