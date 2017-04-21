# Closures

# A closure is a record storing a function together with
# an environment: a mapping associating each free variable of the function
# with the value or storage location to which the name was bound when the
# closure was created.  A closure, unlike a plain function, allows the
# function to access those captured variables through the closure's
# reference to them, even when the function is invoked outside their
# scope.

# First-Class Functions: Allow us to treat functions like anyother object.
# For example we can pass functions as an argument to another function, 
# we can return functions, and we can assign functions to variables.
'''
def outer_func():
    message = 'Hi'

    def inner_func():
        print(message)
    
    # return inner_func()
    return inner_func

outer_func()

my_func = outer_func()
print(my_func)
print(my_func.__name__)

my_func()
my_func()
my_func()
my_func()
'''

# In simple terms: Closure - an inner function that remembers and has access to
# variables in the local scope in which it was created even after the outer
# function has finished executing.

def outer_func(msg):
    message = msg

    def inner_func():
        print(message)
    
    # return inner_func()
    return inner_func

hi_func = outer_func('Hi')
hello_func = outer_func('Hello')

hi_func()
hello_func()

# Note: A closure closes over the free variables from their environment, and
# in this case 'message' would be that free variable

import logging
logging.basicConfig(filename='example.log', level=logging.INFO)

# Outer function called 'logger' which takes in a function as its parameter
def logger(func):
    # Inner function called 'log_func' takes in any number of arguments
    # (*args - pass in any number of arguments)
    def log_func(*args):
        # Within the inner function we are loggin that we are running the
        # function that we passed in and it also prints out the arguments
        # that we used with that function
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        # We execute the function with the arguments then print that to the
        # console
        print(func(*args))
    # We are returning this inner log function
    return log_func

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3,3)
add_logger(4,5)

sub_logger(10,5)
sub_logger(20,10)