# Khuong Tiet 88812261 and Edwin Alexander Lopez 78243641

import connectfour
from connectfour import ConnectFourGameState

def run_game() :
    '''
    Runs the program
    '''
    game_board = connectfour.new_game_state()
    current_board(game_board)
    handle_command(game_board, ' ')
    
def current_board(game_board: ConnectFourGameState) -> 'TableString':
    '''
    Takes a ConnectFourGameState and returns a string representing the current
    board state
    '''
    board_to_print = _display_board(game_board)
    heading = '{}  {}  {}  {}  {}  {}  {} \n'.format('1','2','3','4','5','6','7')
    print(heading)
    print(board_to_print)


def handle_command(game_board: ConnectFourGameState, AI: str) -> ConnectFourGameState:
    '''
    Prompts the user for input and then implements the input
    '''
    while True:
        print(_current_player(game_board))
        if AI == ' ':
            player_command = input('Please enter a command: ').upper()
        else:
            if player_command == 'DROP':
                game_board = _player_drop(game_board)
                if _check_win(game_board) == True:
                    break
            elif player_command == 'POP':
                game_board = _player_pop(game_board)
                if _check_win(game_board) == True:
                    break
            else:
                print('ERROR INVALID MOVE \nTRY AGAIN')
    return game_board



def _current_player(game_board: ConnectFourGameState) -> str:
    '''
    Takes a ConnectFourGameState and returns a string to determine which player's
    turn it currently is
    '''
    if game_board.turn == 'R':
        current = "It is currently RED's turn"
    elif game_board.turn == 'Y':
        current = "It is currently YELLOW's turn"
    return current


def _display_board(game_board: ConnectFourGameState) -> 'TableString':
    '''
    Takes a ConnectFourGameState and returns a readable board
    '''
    EntireBoard = ''
    for i in range(6):
        RowPrint = ''
        for j in range(connectfour.BOARD_COLUMNS):
                if game_board.board[j][i] == ' ':
                        game_board.board[j][i] = '.'
                row = game_board.board[j][i] + '  '
                RowPrint += row
                if game_board.board[j][i] == '.':
                    game_board.board[j][i] = ' '
        EntireBoard += RowPrint + '\n' + '\n'
    return EntireBoard

def _player_drop(game_board: ConnectFourGameState):
    '''
    Takes a column number and performs a drop in specified column
    '''
    try:
        column = int(input('Please enter a column to drop: '))
        column_num = column - 1
        game_board = connectfour.drop_piece(game_board, column_num)
    except:
        print('ERROR INVALID COLUMN \nTRY AGAIN')
    finally:
        current_board(game_board)
        return game_board

def _player_pop(game_board: ConnectFourGameState):
    '''
    Takes a column number and performs a pop in specified column
    '''
    try:
        column = int(input('Please enter a column to pop: '))
        column_num = column - 1
        game_board = connectfour.pop_piece(game_board, column_num)
    except:
        print('ERROR INVALID COLUMN \nTRY AGAIN')
    finally:
        current_board(game_board)
        return game_board

def _check_win(game_board: ConnectFourGameState):
    '''
    Checks for a winner at the end of a turn
    '''
    if connectfour.winning_player(game_board) != ' ':
        winner = True
        print(_game_over(game_board))
        return winner
    else:
        pass

def _game_over(game_board: ConnectFourGameState):
    '''
    Prints the game over message if there is a winner
    '''
    if game_board.turn == 'Y':
        player = 'Red player'
    elif game_board.turn == 'R':
        player = 'Yellow player'
    end = 'Game over, {} is the winner!'.format(player)
    return end

if __name__ == '__main__':
    run_game()
