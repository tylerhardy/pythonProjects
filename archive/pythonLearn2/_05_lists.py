# 05 Lists

another_list = [4,3,4,5,6,7,3,948]
my_list = ["Apple","Pear","Orange", 1, another_list]
my_list.append("Banana")
my_fruit = my_list[2]
my_list.insert(1, "Shrimp")


print(my_list.pop())
print(my_list)

my_list.remove("Shrimp")

print(len(my_list))
print(my_fruit)

print(my_list)

my_list.extend(["Kiwi","Strawberry","Grape"])

print(my_list)

new_list = my_list[1:4]

print(new_list)
