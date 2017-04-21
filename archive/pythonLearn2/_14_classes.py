"""14 Classes"""
## Classes are a set of blueprints (Instructions)

class Person:
    '''
    def assign_name(self):
        self.name = "Tyler Hardy"
    '''

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

tyler = Person("Tyler Hardy", "6 ft", "240 lbs")

#tyler.assign_name()
tyler.print_name()
tyler.print_height()
tyler.print_weight()

# Constructor class method the inet