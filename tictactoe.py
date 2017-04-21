the_board = {'top_left': ' ', 'top_middle': ' ', 'top_right':' ',
'mid_left':' ','mid_middle':' ','mid_right':' ',
'low_left':' ','low_middle':' ','low_right':' '}

def print_board(board):
    print(board['top_left'] + '|' + board['top_middle'] + '|' + board['top_right'])
    print('-+-+-')
    print(board['mid_left'] + '|' + board['mid_middle'] + '|' + board['mid_right'])
    print('-+-+-')
    print(board['low_left'] + '|' + board['low_middle'] + '|' + board['low_right'])

turn = 'X'
for i in range(9):
    print(i)
    print_board(the_board)
    print('Turn for ' + turn + '. Move on which space?')    
    while True:
        while True:
            move = input()
            # check = the_board.get(move, 0)
            # if check == 0:
            if move not in the_board.keys():
                print('Invalid Selection, please try again.')
                continue
            else:
                break
        if (the_board[move] == 'X') or (the_board[move] == 'O'):
            print('That space is already taken, please try again.')
            continue
        else:
            break
    the_board[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
print_board(the_board)