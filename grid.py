grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# print(len(grid))
# print(len(grid[0]))
# print(len(grid[0][0]))

for y in range(len(grid)):
    for x in range(len(grid[0])):
        print ('('+str(x) + ', ' + str(y)+')', end = '')
        # print(grid[y][x], end='')
    print()

for y in range(len(grid[0])):
    for x in range(len(grid)):
        print ('('+str(x) + ', ' + str(y)+')', end='')
        # print(grid[x][y], end='')
    print()

