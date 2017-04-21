# Mutable/Inmutable
#
# An immutable object is an object whose state cannot be modified after it is
# created.  This is in contrast to a mutable object, which can be modified
# after it is created.

# a = 'tyler'
# print(a)
# print('Address of [a] is: {}'.format(id(a)))

# a = 'hardy'
# print(a)
# print('Address of [a] is: {}'.format(id(a)))

# a = 'tyler'
# print(a)
# print('Address of [a] is: {}'.format(id(a)))

# a[0] = 'T'
# print(a)
# print('Address of [a] is: {}'.format(id(a)))

# a = [1,2,3,4,5]
# print(a)
# print('Address of [a] is: {}'.format(id(a)))

# a[0] = 6
# print(a)
# print('Address of [a] is: {}'.format(id(a)))

employees = ['Tyler','John','Rick','Steve','Carl','Adam']
output = '<ul>\n'
for employee in employees:
    output += '\t<li>{}</li>\n'.format(employee)
    print('Address of output is {}'.format(id(output)))

output += '</ul>'
print(output)
print('\n')
