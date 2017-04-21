"""17 Dictionaries"""
my_dictionary = {}

my_dictionary["Name"] = "Tyler Hardy"

print(my_dictionary["Name"])


my_second_dictionary = {"name" : "Tyler Hardy", "height" : "6", "weight" : "240"}

print(my_second_dictionary)

for key,value in my_second_dictionary.items():
    print(key)
    print(value)