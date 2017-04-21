## File IO
# Use "ab+" to Read and Append to File (it also opens or creates the file)

import os

test_file = open("test.txt","wb")

print(test_file.mode)

print(test_file.name)

test_file.write(bytes("Write me to the file\n", 'UTF-8'))

test_file.close()

test_file = open("test.txt", "r+")
text_in_file = test_file.read()
print(text_in_file)
test_file.close()

os.remove("test.txt")