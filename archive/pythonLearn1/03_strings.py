# Strings

quote = "\"Always remember to escape your characters\""
print(quote)

multi_line_quote = ''' Just
like everyone else'''

print(multi_line_quote)

new_string = quote + multi_line_quote
print(new_string)

print("%s %s %s" % ('I like to quote', quote, multi_line_quote))
print('\n' * 5)
print("I don't like ", end="")
print("newlines")