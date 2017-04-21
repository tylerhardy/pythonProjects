my_list = ['apples','bananas','tofu','cats']
print(my_list)

def listToString(my_list):
    if len(my_list) == 0:
       return 
    elif len(my_list) == 1:
        return my_list[0]
    else:
        return (', '.join(my_list[0:-1])) + ' and ' + str(my_list[-1])
        # return (str(my_list[0:(len(my_list)) -1])) + ' and ' + str(my_list[-1])
if listToString(my_list) == None:
    print('List is empty!')
else:
    print(listToString(my_list))

def toString(arr):
    s = ''
    for i in range(len(arr)):
        if i > 0:
            if i == len(arr) - 1:
                # last one
                s = s + ' and '
            else:
                # second, third, ...
                s = s + ', '
        s = s + arr[i]
    return s
print(toString(my_list))