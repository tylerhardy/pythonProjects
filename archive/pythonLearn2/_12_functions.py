"""12 Functions"""
## Methods are typically referred to as functions that are attached to objects through classes.

### This function adds to numbers
def my_add_function(first_number, second_number):
    print(first_number + second_number)

def my_multiply_function(first_number, second_number):
    print(first_number * second_number)

def my_smart_function(first_number, second_number, math_operation):
    if math_operation == "add":
        print(first_number + second_number)
    elif math_operation == "multiply":
        print(first_number * second_number)
    else:
        print("Unknown operation")
'''
print("Hello World")

my_add_function(8,2)
my_multiply_function(0,0)
my_smart_function(3,4,"multiply")
'''