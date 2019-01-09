

class OthelloBoundaryError:
    pass

        
class OthelloGame:
    
    def __init__(self):
        self._board = []
        self.empty = ' . '
        self.white = ' o '
        self.black = ' x '
        self.alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.directions = [0,1,-1]
        self.game_over = False
        self.black_count = 0
        self.white_count = 0

    def clear_board(self):
        self._board = []
        self._current = ''
        self._opposite = ''
        self.black_count = 0
        self.white_count = 0

  
    def current_player(self, player: str):
        '''
        Sets the current player and the opposite of the current player
        '''
        if player == 'WHITE':
            self._current = self.white
            self._current_color = player
            self._opposite = self.black
            self._opposite_color = 'BLACK'
        elif player == 'BLACK':
            self._current = self.black
            self._current_color = player
            self._opposite = self.white
            self._opposite_color = 'WHITE'

    def start(self, player: str, rows: int, columns: int, layout: str):
        self.current_player(player)
        for column in range(columns):
            self._board.append([])
        for column in range(len(self._board)):
            for row in range(rows):
                self._board[column].append(self.empty)

        self.starting_pieces(layout)


    def starting_pieces(self, start: str):
        upper_left = ''
        upper_right = ''
        if start == 'YES':
            upper_left = self._current
            upper_right = self._opposite
        else:
            upper_left = self._opposite
            upper_right = self._current
        mid_board = int(len(self._board)/2) - 1
        center = self._board[mid_board:mid_board+2]
        for i in range(len(center)):
            for j in range(len(center)):
                center[i][int(len(center[i])/2 -1)+i] = upper_left
                center[i][int(len(center[i])/2)-i] = upper_right

    def check_player(self, player: str):
        '''
        Checks the input player against the current player
        '''
        return player == self._currentPlayer


    def current_score(self):
        black = 0
        white = 0
        for rows in self._board:
            for columns in rows:
                if columns == self.black:
                    black += 1
                    self.black_count = black
                elif columns == self.white:
                    white += 1
                    self.white_count = white



    def game_mode(self, mode: str):
        self.game_win = mode
        if self.game_win == 'MOST':
            if self.black_count > self.white_count:
                return self.black
            else:
                return self.white
        elif self.game_win == 'LEAST':
            if self.black_count < self.white_count:
                return self.black
            else:
                return self.white
            

    def is_game_over(self) -> bool:
        if self.black_count == 0 or self.white_count == 0:
            self.game_over = True
        AllPieces = len(self._board[0]) * len(self._board)
        pieces = self.black_count + self.white_count
        if AllPieces == pieces:
            self.game_over = True
        else:
            pass

    def game_is_over(self):
        if self.game_win == self._current:
            return self._current_color + ' is the winner!'
        else:
            return self._opposite_color + ' is the winner!'

    def playable_piece(self, row: int, col: int):
        try:
            if self._board[row][col] == self.empty:
                return col >= 0 and row >= 0 and col <= len(self._board) and row <= len(self._board)
        except:
            return OthelloBoundaryError

    def check_cell(self, row: int, col: int):
        return self._board[row][col]

    def moveable(self) -> bool:
        moves_available = 0
        for rows in range(len(self._board)):
            for col in range(len(self._board[rows])):
                if self.valid_move([col, rows]) == True:
                    moves_available += 1
        return moves_available >= 1


    def valid_move(self, move: list):
        '''
        Checks if a move is valid and returns a list of pieces to be flipped
        '''
        self.flippable_pieces = []
        Valid = False
        if self.playable_piece(move[-1],move[0]) == True:
            for i in self.directions:
                for j in self.directions:
                    row = move[-1] + i
                    col = move[0] + j
                    try:
                        if self._board[row][col] == self._opposite:
                            row += i
                            col += j
                            if not self._board[row][col] == self.empty:
                                while self._board[row][col] == self._opposite:
                                    row += i
                                    col += j
                                    if self._board[row][col] == self._current:
                                        break
                                if self._board[row][col] == self._current:
                                    row -= i
                                    col -= j
                                    while self._board[row][col] == self._opposite:
                                        self.flippable_pieces.append([row,col])
                                        row -= i
                                        col -= j
                                        if self._board[row][col] == self._board[move[-1]][move[0]]:
                                            Valid = True
                                            break
                    except IndexError:
                        pass
        return Valid
                

    
    def flip_pieces(self):
        for flipped in self.flippable_pieces:
            self._board[flipped[0]][flipped[-1]] = self._current
        

    def player_movement(self, move: list):
        
        self._board[move[-1]][move[0]] = self._current
        self.flip_pieces()
        self.is_game_over()
        self.current_score()
        if self.game_over == True:
            self.game_is_over()
        else:
            if self._current == self.white:
                self.current_player('BLACK')
            else:
                self.current_player('WHITE')


        
