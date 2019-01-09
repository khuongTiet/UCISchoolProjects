# Khuong Tiet 88812261 and Edwin Alexander Lopez 78243641

import connectfour
from connectfour import ConnectFourGameState

def run_game() :
    '''
    Runs the program
    '''
    game_board = connectfour.new_game_state()
    current_board(game_board)
    user_prompt(game_board)
    
def current_board(game_board: ConnectFourGameState) -> 'TableString':
    '''
    Takes a ConnectFourGameState and returns a string representing the current
    board state
    '''
    board_to_print = display_board(game_board)
    heading = '{}  {}  {}  {}  {}  {}  {} \n'.format('1','2','3','4','5','6','7')
    print(heading)
    print(board_to_print)

def current_player(game_board: ConnectFourGameState) -> str:
    '''
    Takes a ConnectFourGameState and returns a string to determine which player's
    turn it currently is
    '''
    if game_board.turn == 'R':
        current = "It is currently RED's turn"
    elif game_board.turn == 'Y':
        current = "It is currently YELLOW's turn"
    return current


def display_board(game_board: ConnectFourGameState) -> 'TableString':
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
    
"""
def player_move(game_board: ConnectFourGameState):
    '''
    Takes player command to perform an action
    '''
    while True:
        print(current_player(game_board))
        player_command = input('Please enter a command: ').upper()
        if player_command == 'DROP':
            game_board = _player_drop(game_board)
        elif player_command == 'POP':
            game_board = _player_pop(game_board)
    return game_board
"""

def user_prompt(game_board: ConnectFourGameState):
    '''
    Asks for user input until a winner is decided
    '''
    handle_command(game_board)
    return game_board


def handle_command(game_board: ConnectFourGameState) -> ConnectFourGameState:
    '''
    Prompts the user for input and then implements the input
    '''
    while True:
        print(current_player(game_board))
        player_command = input('Please enter a command: ').upper()
        if player_command == 'DROP':
            game_board = _player_drop(game_board)
        elif player_command == 'POP':
            game_board = _player_pop(game_board)
            check_win(game_board)
    return game_board

def _player_drop(game_board: ConnectFourGameState):
    column = int(input('Please enter a column to drop: '))
    column_num = column - 1
    game_board = connectfour.drop_piece(game_board, column_num)
    current_board(game_board)
    return game_board

def _player_pop(game_board: ConnectFourGameState):
    column = int(input('Please enter a column to pop: '))
    column_num = column - 1
    game_board = connectfour.pop_piece(game_board, column_num)
    current_board(game_board)
    return game_board

def check_win(game_board: ConnectFourGameState):
    if connectfour.winning_player(game_board) == ' ':
        pass
    else:
        return connectfour.winning_player(game_board)



run_game()
