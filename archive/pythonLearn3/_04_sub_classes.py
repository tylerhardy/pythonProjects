"""04 Sub Classes"""
# Inheritance allows us to inherit attributes and methods from a parent class 
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


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        #Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Tyler','Hardy',41000, 'python')
dev_2 = Developer('Test','User',60000, 'java')
mgr_1 = Manager('Sue','Smith',90000, [dev_1])

# When we instantiated our developers it first looked in our developer class
# for our __init__ method. Since the Developer class has no __init__ method it
# will then walk up this chain of inheritance until it finds what it is looking
# for.  This chain is called: Method Resolution Order

'''
print(help(Developer))
'''

print(dev_1.email)
print(dev_1.prog_lang)
print(dev_2.email)
print(dev_2.prog_lang)

mgr_1.add_employee(dev_2)


print(mgr_1.email)
print(mgr_1.print_emps())

mgr_1.remove_employee(dev_1)
print(mgr_1.print_emps())

# isinstance() and issubclass()
# isinstance() will tell us if an object is an instance of a class.
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))
# issubclass() will tell us if a class is a subclass of another.
print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))


