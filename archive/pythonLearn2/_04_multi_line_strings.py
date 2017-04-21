# 04 Multi-line Strings

animal = "cat"

my_variable = '''
    <html>
        <head>
            <title>Look at this</title>
        </head>
        <body>
            <h1>Hello World!</h1>
            <a href='http://www.hipstercode.com'>Click Me!</a>
        </body>
    </html>
'''

print("%s ran over the hill" % animal)

my_html_file = open("/Users/tylerhardy/Projects/python/python_learn2/my_html_file2.html","w")

my_html_file.write(my_variable)

my_html_file.close()

print(my_variable)