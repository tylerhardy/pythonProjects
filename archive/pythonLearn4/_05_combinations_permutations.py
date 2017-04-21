# Combinations and Permutations
#
# Combination is all the different ways in which you can group something where
# the order does not matter.
# Permutations are all the different ways in which you can group some values
# where the order does matter.
'''
import itertools

my_list = [1,2,3]

combinations = itertools.combinations(my_list, 2)
for c in combinations:
    print("c:",c)

permutations = itertools.permutations(my_list, 3)
for p in permutations:
    print("p:",p)
'''

import itertools

my_list = [1,2,3,4,5,6]

combinations = itertools.combinations(my_list, 3)
permutations = itertools.permutations(my_list, 3)

print([result for result in combinations if sum(result) == 10])

word = 'sample'
my_letters = 'plmeas'

combinations = itertools.combinations(my_letters, 6)
permutations = itertools.permutations(my_letters, 6)

for p in permutations:
    print(p)
    if ''.join(p) == word:
        print('Match')
        break
    else:
        print('Not Match')

