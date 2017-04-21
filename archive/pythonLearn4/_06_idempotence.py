# Idempotence
# 
# The property of certain operations in mathematics and computer science, that
# can be applied multiple times without changing the result beyond the initial
# application.

# f(f(x)) = f(x)

# f(x)
# add_ten(num)

def add_ten(num):
    return num + 10

# f(f(x)) = f(x)

print(add_ten(10))
print(add_ten(add_ten(10)))

# print abs(-10)
# abs(-10) == 10
# abs(10) == 10
# abs(10) == 10
