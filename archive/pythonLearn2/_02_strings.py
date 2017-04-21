# 02 Strings

my_variable = "<html><head><title>Look at this</title></head><body><h1>Hello World!</h1><a href='http://www.hipstercode.com'>Click Me!</a></body></html>"

my_second_variable = "This is some more stuff"

# String concatenation
my_combined_variable = my_variable + ". " + my_second_variable + "!"

print(my_combined_variable)

# Variable Rules
'''
Convention is to have an underscore between words
Cannot start with numbers (1234)
Can start with an underscore (_)
There are reserved words:: http://infohost.nmt.edu/tcc/help/pubs/python27/web/names.html
'''

#my_html_file = open("/projects/python/python_lern2/my_html_file.html","w")
my_html_file = open("/Users/tylerhardy/Projects/python/python_learn2/my_html_file.html","w")

my_html_file.write(my_variable)