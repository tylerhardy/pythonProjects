# Memoization
#
# Memoization is an optimization technique used primarily to speed up computer
# programs by storing the results of expensive function calls and returning the
# cached result when the same inputs occuer again.

import time

ef_cache = {}

def expensive_func(num):
    if num in ef_cache:
        return ef_cache[num]
    
    print("Computing {}...".format(num))
    time.sleep(1)
    result = num*num
    ef_cache[num] = num * num
    return result

result = expensive_func(4)
print(result)

result = expensive_func(10)
print(result)

result = expensive_func(4)
print(result)

result = expensive_func(10)
print(result)