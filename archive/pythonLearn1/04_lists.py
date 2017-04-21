## Lists

grocery_list = ['Juice','Tomatoes','Potatoes','Bananas']
print('First Item', grocery_list[0])

grocery_list[0] = "Green Juice"
print('First Item', grocery_list[0])

print(grocery_list[1:3])

other_events = ['Wash Car','Pick Up Kids','Cash Check']

to_do_list = [other_events, grocery_list]
print(to_do_list)

print((to_do_list[1][1]))

grocery_list.append('Onions')
print(to_do_list)

grocery_list.insert(1, "Pickle")
print(to_do_list)

grocery_list.remove("Pickle")
grocery_list.sort()
grocery_list.reverse()

del grocery_list[4]
print(to_do_list)
print(len(to_do_list))
print(max(to_do_list))
print(min(to_do_list))

to_do_list2 = other_events + grocery_list
print(to_do_list2)
print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))