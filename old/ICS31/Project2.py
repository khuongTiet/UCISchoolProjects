#Khuong Tiet 88812261 and Edwin Alexander Lopez 78243641

import connectfour
def run_it() :
    game_board = connectfour.new_game_state()
    current_board = display_board(game_board)
    print(current_board)
 

def display_board(C4GS: 'namedtuple') -> 'TableString':
    EntireBoard = ''
    for i in range(6):
        RowPrint = ''
        for j in range(connectfour.BOARD_COLUMNS):
                if C4GS.board[j][i] == ' ':
                        C4GS.board[j][i] = '.'
                row = C4GS.board[j][i] + ' '
                RowPrint += row
                if C4GS.board[j][i] == '.':
                    C4GS.board[j][i] = ' '
        EntireBoard += RowPrint + '\n'
    return EntireBoard
    


def player_move(game_board: 'Connect Four Game State'):
    player_command = input('Please enter a command: ')
    column_num = int(input('Please enter a column to drop: '))
    if player_command.upper() == 'DROP':
        game_board = connectfour.drop_piece(game_board, column_num-1)
    elif player_command.upper() == 'POP':
        game_board = connectfour.drop_piece(game_board, column_num-1)
    return game_board


'''
def player_move(C4GS: 'namedtuple') -> [[str]]:
    while True:
            player_command = input('Please enter a command: ')
            column_num = int(input('Please enter a column to drop: '))
            if player_command.upper() == 'DROP':
                C4GS = connectfour.drop_piece(C4GS, column_num-1)
                break
            elif player_command.upper() == 'POP':
                C4GS = connectfour.pop_piece(C4GS, column_num-1)
                break
            else:
                print('ERROR: Invalid command/column. Please try again.')
            print(C4GS)
            return

'''
