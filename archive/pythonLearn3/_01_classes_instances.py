"""01 Classes and Instances"""
# They allow us to logically group our data and functions in a way that is easy
# to reuse and build upon if need be.
#
# Data and functions that are associated with a specific class we call those
# attributes and methods.
#

class Employee:

    # The __init__ is like a constructor
    # When the method is created within a class they receive the instance as
    # the first argument automatically and by convention we should call the
    # instance 'self'.

    # the initialize method
    def __init__(self, first, last, pay):
        # Within the __init__ method we are going to set all theese instance
        # variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        # When 'Self' is the instance it is meant that when we set
        # [self.first = first] it is going to be the same thing as expicitely
        # assigning the variable manually below
        #
        # The __init__ method takes the instance which we call self and the
        # first name, last name, and pay as arguments.  When we create our
        # employee down below the instance is passed automatically so we
        # leave off 'Self', we only need to provide the names and the pay.

    # The fullname method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

# The difference between a 'Class' and an 'Instance of a Class'
# The 'Class' is a blueprint for creating instances. Each unique employee
# that we create using the employee class will be an instance of that class

emp_1 = Employee('Tyler','Hardy','41000')
emp_2 = Employee('Test','User','60000')

# print(emp_1)
# print(emp_2)

# Instance Variables vs Class Variables
# Instance Variables contain data that is unique to each instance
# Example below in manually inputing instance variables

''' Manually assigning variables
emp_1.first = 'Tyler'
emp_1.last = 'Hardy'
emp_1.email = 'tylerhardy@weber.edu'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'McTesterson'
emp_2.email = 'testmctesterson@gmail.com'
emp_2.pay = 60000
'''

print(emp_1.email)
print(emp_2.email)

#print('{} {}'.format(emp_1.first, emp_1.last))
#print(emp_1.fullname())

# Methods require the parenthesis '()' while attributes do not require
# parenthesis
#
# One common mistake when creating methods is forgetting the self argument for
# for the instance.  It may look like there are no arguments being passed in
# the method fullname() but the instance (emp_1 or emp_2) is getting passed automatically.
# So we have to expect that instance argument in our method

# print(class.method(instance))
print(Employee.fullname(emp_1))
# print(instance.method())
print(emp_2.fullname())
