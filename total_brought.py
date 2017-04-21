all_guests = {'Alice': {'apples': 5, 'pretzels': 12},
                'Bob': {'ham sandwiches': 3, 'apples': 2},
                'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(dictionary, string):
    number_brought = 0
    for k, v in dictionary.items():
        number_brought = number_brought + (v.get(string, 0))
    return number_brought

print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(all_guests, 'apples')))
print(' - Cups           ' + str(totalBrought(all_guests, 'cups')))
print(' - Cakes          ' + str(totalBrought(all_guests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(all_guests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(all_guests, 'apple pies')))