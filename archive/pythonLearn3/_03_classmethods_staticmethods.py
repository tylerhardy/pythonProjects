"""03 Classmethods and Staticmethods"""
# Differnce between [Regular Methods], [Class Methods], and [Static Methods]
# Regular Instance - takes the instance as the first argument and by convention
# that we call 'self'.

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # Class Method Decorator
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

        

emp_1 = Employee('Tyler','Hardy',41000)
emp_2 = Employee('Test','User',60000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

# People use class methods as alternative constructors which means that you can
# use these class methods in order to provide multiple ways of creating our
# objects.

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

emp_3 = Employee.from_string(emp_str_1)
emp_4 = Employee.from_string(emp_str_2)
emp_5 = Employee.from_string(emp_str_3)

print(emp_3.fullname())
print(emp_4.fullname())
print(emp_5.fullname())


import datetime
my_date = datetime.date(2017, 4, 5)

print(Employee.is_workday(my_date))
