

            
class OthelloGame:
    
    def __init__(self):
        self._board = []
        self.empty = ' . '
        self.white = ' o '
        self.black = ' x '
        self.x_axis = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
  
    def current_player(self, player: str):
        '''
        Sets the current player and the opposite of the current player
        '''
        if player == 'WHITE':
            self._current = self.white
            self._opposite = self.black
        elif player == 'BLACK':
            self._current = self.black
            self._opposite = self.white

    def start(self, player: str, rows: int, columns: int):
        self.current_player(player)
        
        for column in range(columns):
            self._board.append([])
        for column in range(len(self._board)):
            for row in range(rows):
                self._board[column].append(self.empty)
                
        mid_board = int(len(self._board)/2) - 1
        center = self._board[mid_board:mid_board+2]
        for i in range(len(center)):
            for j in range(len(center)):
                center[i][int(len(center[i])/2 -1)+i] = self._current
                center[i][int(len(center[i])/2)-i] = self._opposite

    def check_player(self, player: str):
        '''
        Checks the input player against the current player
        '''
        return player == self._currentPlayer

    def player_movement(self, move: list):
        self.column = self.x_axis.index(move[0])
        self.row = int(move[-1])
        print(self.column)
        print(self.row)

    def display_score(self):
        self.black_count = 0
        self.white_count = 0
        for rows in self._board:
            for columns in rows:
                if columns == self.black:
                    self.black_count += 1
                elif columns == self.white:
                    self.white_count += 1
        print('Score\nBlack: {}    White: {}\n'.format(self.black_count, self.white_count))

            



        # for i in self._board[x][0:self.row]
        #   if i == self._current:
        #       for j in self._board[index(i):self.row]
        #       if j != self._current:
        #           j = self._current
        #
        # for i in self._board[x][self.row:-1]
        #   if i == self._current:
        #       for j in self._board[self.row:index(i)]
        #       if j != self._current:
        #           j = self._current
        # NOTE: j = self._current won't change it, it has to be in the format of self._board[x][y] == self._current
        

# for i in self._board:
#   if i[self.column]

    
        
    
    def valid_move(self):
        move = self._board[self.row][self.column]
        if self._board[self.row+1][self.column] == self._opposite:
            if self._board[self.row+2][self.column] == self._current:
                self.board[self.row+1][self.column] = self._current
            elif self._board[self.row+2][self.column] == self._opposite:
                if self._board[self.row+3][self.column] == self._current:
                    self.board[self.row+2][self.column] = self._current
    ## ^^ This is how you will check each direction, recursion or some sort of counter work be nice
    ## Due to it using (row+int) so often and will later use (column+int) as well


##        self._board[self.row+1][self.column]    =  South
##        self._board[self.row-1][self.column]    =  North
##        self._board[self.row][self.column+1]    =  East
##        self._board[self.row][self.column-1]    =  West
##        self._board[self.row+1][self.column+1]  =  SouthEast
##        self._board[self.row+1][self.column-1]  =  SouthWest
##        self._board[self.row-1][self.column+1]  =  NorthEast
##        self._board[self.row-1][self.column-1]  =  NorthWest


