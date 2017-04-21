# String Interpolation
#
# The process of evaluating a string literal containing one or more
# placeholders, yielding a result in which the placeholders are replaced with
# their corresponding values.

# String Concatenation
name = 'Tyler'
age = 31

greeting = 'My name is ' + name + ' and I am ' + str(age) + ' years old'
print(greeting)

# String Interpolation
name = 'Tyler'
age = 31

greeting = 'My name is {} and I am {} years old'.format(name, age)
print(greeting)

greeting = 'I am {age} years old and my name is {name}'.format(name=name, age=age)
print(greeting)

greeting = 'I am {1} years old and my name is {0}'.format(name, age)
print(greeting)

