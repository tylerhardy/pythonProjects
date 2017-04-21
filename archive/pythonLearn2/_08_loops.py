# 08 For Loops

my_string = "This is a string."

for char in my_string:
    print(char)

print(my_string[5])

for whatever_you_want in my_string:
    if whatever_you_want == "g":
        print("It's a G")

fruits = ["Banana", "Apple", "Pear"]
for f in fruits:
    print("I like to eat "+f)

for f in fruits:
    if f == "Banana":
        print("I like Bananas!")
        break