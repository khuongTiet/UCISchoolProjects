# Khuong Tiet 88812261 Project 4 Lab Section 8

import OthelloModule

##
##  Main functions
##


##    Implement winning methods
##    Check for winner



def input_var(input_spec: str, var: str):
    '''
    Takes a string that specifies the user for input an a variable
    that affects what the function will do on the input
    '''

    ERROR = 'ERROR, {} IS AN INVALID INPUT'
    
    while True:
        query = str(input('Please enter {} '.format(input_spec)))
        if var == 'str':
            try:
                query = str(query)
                if query.upper() == 'WHITE' or query.upper() == 'BLACK':
                    query = query.upper()
                    break
                elif query.upper() == 'MOST' or query.upper() == 'LEAST':
                    query = query.upper()
                    break
                elif query.upper() == 'YES' or query.upper() == 'NO':
                    query = query.upper()
                    break
                else:
                    print('ERROR "{}" IS AN INVALID INPUT'.format(query))
            except ValueError:
                print(ERROR.format(query))
        elif var == 'int':
            try:
                query = int(query)
                if _integer_check(int(query)) == True:
                    break
                else:
                    print('ERROR "{}" MUST BE EVEN AND BETWEEN 4 AND 16'.format(query))
            except ValueError:
                print(ERROR.format(query))

    return query
            

def print_board(game: OthelloModule.OthelloGame):
    display = ''
    for number in range(len(game._board[0])):
        letter = ' {}  '.format(game.alpha[number])
        display += letter
    counter = 1
    for rows in game._board:
        row = ''
        for columns in rows:
            row += columns + ' '
        display += '\n' + row + str(counter) + '\n'
        counter += 1
    game.current_score()

    print(display)
    

def player_move():
    '''
    Takes an input from the user and converts it into a format for the Othello
    game to use for movement
    '''

    while True:
        move = input('Please enter a move in the format: LetterNumber(ex. A1,F3)\n')
        if len(move) > 1 or len(move) <= 3:
            column = move[0].upper()
            row = move[1:]
            column_move = game.alpha.index(column)
            row_move = int(row[-1])-1
            return [column_move,column+row,row_move]


def program(game: OthelloModule.OthelloGame):
        while game.game_over != True:
            if game.moveable() == True:
                print('IT IS {}\'S TURN'.format(game._current_color))
                move = player_move()
                if game.valid_move(move) == True:
                    game.player_movement(move)
                    print_board(game)
                else:
                    print('ERROR {} IS AN INVALID MOVE'.format(move[1]))
                    print_board(game)
        print('Game over!:'.format(game.game_is_over()))

        



##
##  Private Functions
##

def _integer_check(check: int) -> bool:
    '''
    Checks if an integer is even as well as between 4 and 16
    '''
    if check%2 == 0:
        return check >= 4 and check <= 16
    else:
        return False



if __name__ == '__main__':
    rows = input_var('how many rows there will be: ','int')
    columns = input_var('how many columns there will be: ', 'int')
    first_player = input_var('which player will go first (BLACK/WHITE): ', 'str').upper()
    winning = input_var('how the game will be won (MOST/LEAST): ', 'str').upper()
    layout = input_var(' if you would like to start upper-left: (YES/NO): ', 'str').upper()
    print()
    game = OthelloModule.OthelloGame()
    game.start(first_player,rows,columns, layout)
    print_board(game)
    game.game_mode(winning)
    program(game)


    
    
