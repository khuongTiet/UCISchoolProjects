# Khuong Tiet 88812261 Project 4 Lab Section 8

from OthelloModule import OthelloGame

##
##  Main functions
##

##
##Things to finish:
##    Check if move is valid
##        Vertically
##        Horizontally
##        Diagonally
##    Flip pieces
##    Switch players
##    Implement winning methods
##    Check for winner
##    


def input_var(input_spec: str, var: str):
    '''
    Takes a string that specifies the user for input and a variable
    that affects what the function will do on the input
    '''
    
    while True:
        query = str(input('Please enter {} '.format(input_spec)))
        if var == 'str':
            try:
                query = str(query)
                if query.upper() == 'WHITE' or query.upper() == 'BLACK':
                    query = query.upper()
                    break
                else:
                    print('ERROR "{}" IS AN INVALID INPUT'.format(query))
            except ValueError:
                print('ERROR INVALID INPUT')
        elif var == 'int':
            try:
                query = int(query)
                if _integer_check(int(query)) == True:
                    break
                else:
                    print('ERROR "{}" MUST BE EVEN AND BETWEEN 4 AND 16'.format(query))
            except ValueError:
                print('ERROR INVALD INPUT')
    return query
            

def print_board(game: OthelloGame):
    display = ''
    for number in range(len(game._board)):
        letter = ' {}  '.format(game.x_axis[number])
        display += letter
    counter = 1
    for rows in game._board:
        row = ''
        for columns in rows:
            row += columns + ' '
        display += '\n' + row + str(counter) + '\n'
        counter += 1
    game.display_score()
    print(display)
    

def player_move():
    '''
    Takes an input from the user and converts it into a format for the Othello
    game to use for movement
    '''
    
    move = input('Please enter a move in the format: LetterNumber,\nex. A1 ')
    column = move[0].upper()
    row = move[1:]
    return [column,row]




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
    print(rows)
    columns = input_var('how many columns there will be: ', 'int')
    print(columns)
    first_player = input_var('which player will go first: ', 'str').upper()
    print(first_player + ' is the first player!')
    print()
    game = OthelloGame()
    game.current_player(first_player)
    game.start(first_player,rows,columns)
    print_board(game)

    
    
