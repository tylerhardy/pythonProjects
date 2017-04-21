import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
char_count = {}

for i in message:
    char_count.setdefault(i, 0)
    char_count[i] = char_count[i] + 1

pprint.pprint(char_count)
# print(pprint.pformat(char_count))