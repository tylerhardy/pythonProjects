"""15 sub classes"""

class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def print_name(self):
        '''Print Name'''
        print(self.name)

    def print_height(self):
        '''Print Height'''
        print(self.height)

    def print_weight(self):
        '''Print Weight'''
        print(self.weight)

class Employee(Person):
    employee_id = ""
    def __init__(self, name, height, weight, employee_id):
        #super(Employee, self).__init__(name, height, weight)
        Person.__init__(self, name, height, weight)
        self.employee_id = employee_id

    def print_employee_id(self):
        print(self.employee_id)

employee_tyler = Employee("Tyler Hardy", "6 ft", "240 lbs","0001")

print(employee_tyler)
employee_tyler.print_name()
employee_tyler.print_employee_id()
employee_tyler.print_height()
employee_tyler.print_weight()