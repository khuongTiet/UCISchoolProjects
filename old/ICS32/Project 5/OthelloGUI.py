import tkinter
import OthelloModule
import random

## TO DO
## Check if there is a winner / loser
## End game if there is a winner / loser
## Add label to display if a move is invalid


DEFAULT_FONT = ('Helvetica', 14)

# More likely to be green
BG_COLOR = ['indianred','royalblue',
            'gold','orchid','pink',
            'darkorange', 'brown']
for colors in range(len(BG_COLOR)):
    BG_COLOR.append('green')



class GameBoard():
    def __init__(self):
        self._board = tkinter.Toplevel()

        self._player = tkinter.StringVar()
        self._player.set(" ")
        
        self._bg_color = random.choice(BG_COLOR)
        self._board_player = tkinter.Label(
            master = self._board, textvariable = self._player,
            font = DEFAULT_FONT)
        self._board_player.grid(
            row = 0, column = 2,
            padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E)
        

        self._move = tkinter.StringVar()
        self._move.set(" ")

        self._move_valid = tkinter.Label(
            master = self._board, textvariable = self._move,
            font = DEFAULT_FONT)
        self._move_valid.grid(
            row = 0, column = 1,
            padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        

        self._score = tkinter.StringVar()
        self._score.set(" ")

        self._board_score = tkinter.Label(
            master = self._board,
            textvariable = self._score,
            font = DEFAULT_FONT)
        self._board_score.grid(
            row = 0, column = 0,
            padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.W)
        
        
        self._board_canvas = tkinter.Canvas(
            master = self._board, width = 700, height = 700,
            background = self._bg_color)
        self._board_canvas.grid(
            row = 1, column = 0, columnspan = 3, padx= 10, pady= 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._board_canvas.bind('<Configure>', self._on_board_resized)
        self._board_canvas.bind('<Button-1>', self._on_square_clicked)

        self._board.rowconfigure(0, weight = 1)
        self._board.rowconfigure(1, weight = 1)
        self._board.columnconfigure(0, weight = 1)
        self._board.columnconfigure(1, weight = 1)
        self._board.columnconfigure(2, weight = 1)


    def show(self):
        self._board.grab_set()
        self._board.wait_window()

    def _on_board_resized(self, event: tkinter.Event) -> None:
        self._redraw_board()

    def _on_square_clicked(self, event: tkinter.Event) -> None:
        self.possible_move = self._board_coordinates(
            event.x, event.y)
        
        self._player_move()
        self._redraw_board()


    def _redraw_board(self) -> None:
        self._board_canvas.delete(tkinter.ALL)

        game.current_score()
        self._player.set('Current Player:   {}'.format(game._current_color))
        self._score.set('Black:  {}      White:  {}'.format(
            game.black_count, game.white_count))

        self.column_len = (
            self._board_canvas.winfo_width() / GUI.number_of_columns)
        self.rows_len = (
            self._board_canvas.winfo_height() / GUI.number_of_rows)

        self._get_pieces()

        for col_num in range(GUI.number_of_columns+1):
            self._board_canvas.create_line(
                self.column_len * col_num, 0,
                self.column_len * col_num, self._board_canvas.winfo_height())

        for row_num in range(GUI.number_of_rows+1):
            self._board_canvas.create_line(
                0, self.rows_len * row_num,
                self._board_canvas.winfo_width(), self.rows_len * row_num)

    def _player_move(self) -> None:
        
        if game.valid_move(self.possible_move) == True:
            game.player_movement(self.possible_move)
            self._move.set(' ')
        else:
            self._move.set('INVALID MOVE TRY AGAIN')

        

    def _get_pieces(self):
        
        for row in range(len(game._board)):
            for column in range(len(game._board[row])):
                if game._board[row][column] == ' x ':
                    self._draw_piece(column, row, 'black')
                    
                elif game._board[row][column] == ' o ':
                    self._draw_piece(column, row, 'white')

    def _draw_piece(self, col: int, row: int, color: str):

        piece_pad = 3

        x1 = self.column_len * row + piece_pad
        y1 = self.rows_len * col + piece_pad
        x2 = self.column_len * (row+1)- piece_pad
        y2 = self.rows_len * (col+1)- piece_pad
        
        self._board_canvas.create_oval(
                        x1,y1,x2,y2, fill = color,
                        outline = self._bg_color, outlinestipple = 'gray75')

    def _board_coordinates(self, x: int, y: int):
        for row in range(len(game._board)):
            for column in range(len(game._board[row])):
                x1 = self.column_len * column
                y1 = self.rows_len * row 
                x2 = self.column_len * (column+1)
                y2 = self.rows_len * (row+1)
                if x > x1 and x < x2:
                    if y > y1 and y < y2:
                        return [row, column]
                
                
class GameOptions():
    def __init__(self):
        self._option_window = tkinter.Tk()

        othello_label = tkinter.Label(
            master = self._option_window, text = 'Othello: New Game > Options',
            font = DEFAULT_FONT)

        othello_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W)

        num_rows_label = tkinter.Label(
            master = self._option_window, text = 'Number of Rows',
            font = DEFAULT_FONT)

        num_rows_label.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        row_layout = tkinter.StringVar()
        row_layout.set("8")

        self._num_rows_spin = tkinter.Spinbox(
            master = self._option_window, from_= 4, to = 16,
            increment = 2, readonlybackground = '#fffffffff',
            state = 'readonly', textvariable = row_layout,
            font = DEFAULT_FONT)

        self._num_rows_spin.grid(
            row = 1, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)

        num_col_label = tkinter.Label(
            master = self._option_window, text = 'Number of Columns',
            font = DEFAULT_FONT)

        num_col_label.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        col_layout = tkinter.StringVar()
        col_layout.set("8")

        self._num_col_spin = tkinter.Spinbox(
            master = self._option_window, from_ = 4, to = 16,
            increment = 2, readonlybackground = '#fffffffff',
            state = 'readonly', textvariable = col_layout,
            font = DEFAULT_FONT)

        self._num_col_spin.grid(
            row = 2, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.E)

        first_player_label = tkinter.Label(
            master = self._option_window, text = 'Starting player',
            font = DEFAULT_FONT)

        first_player_label.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._first_player = tkinter.StringVar()
        self._first_player.set(" ")

        black_button = tkinter.Radiobutton(
            master = self._option_window, text = 'Black player', padx = 10,
            variable = self._first_player, value = 'BLACK',
            font = ('Helvetica', 10))

        black_button.grid(
            row = 3, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W)

        white_button = tkinter.Radiobutton(
            master = self._option_window, text = 'White player', padx = 10,
            variable = self._first_player, value = 'WHITE',
            font = ('Helvetica', 10))

        white_button.grid(
            row = 3, column = 1, padx = 10, pady = 10,
            sticky = tkinter.E)

        winning_label = tkinter.Label(
            master = self._option_window, text = 'Method to win',
            font = DEFAULT_FONT)

        winning_label.grid(
            row = 4, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._winning_method = tkinter.StringVar()
        self._winning_method.set(" ")

        most_button = tkinter.Radiobutton(
            master = self._option_window, text = 'Most pieces', padx = 10,
            variable = self._winning_method, value = 'MOST',
            font = ('Helvetica', 10))

        most_button.grid(
            row = 4, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W)

        least_button = tkinter.Radiobutton(
            master = self._option_window, text = 'Least pieces', padx = 13,
            variable = self._winning_method, value = 'LEAST',
            font = ('Helvetica', 10))

        least_button.grid(
            row = 4, column = 1, padx = 10, pady = 10,
            sticky = tkinter.E)

        self._layout = tkinter.StringVar()
        self._layout.set("YES")

        layout_check = tkinter.Checkbutton(
            master = self._option_window, text = 'Start with upper-left',
            padx = 10, pady = 10, variable = self._layout, font = ('Helvetica', 10),
            onvalue = 'YES', offvalue = 'NO')

        layout_check.grid(
            row = 5, column = 0, padx = 20, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self.startVar = tkinter.StringVar()
        self.startVar.set('Start Game')
        

        start_button = tkinter.Button(
            master = self._option_window, textvariable = self.startVar,
            font = ('Helvetica', 18), command = self._start_check)

        start_button.grid(
            row = 5, column = 1, padx = 10, pady = 10,
            sticky = tkinter.E)

        self._option_window.rowconfigure(0, weight = 1)
        self._option_window.rowconfigure(1, weight = 1)
        self._option_window.rowconfigure(2, weight = 1)
        self._option_window.rowconfigure(3, weight = 1)
        self._option_window.rowconfigure(4, weight = 1)
        self._option_window.rowconfigure(5, weight = 1)
        self._option_window.columnconfigure(0, weight = 1)
        self._option_window.columnconfigure(1, weight = 1)
 



        

    def start(self) -> None:
        self._option_window.mainloop()

    def _start_check(self) -> None:
        if self._first_player.get() != " " and self._winning_method.get() != " ":
            self._start_game()
        else:
            self.startVar.set('Missing inputs!\nTry again')

    def _start_game(self) -> None:
        
        self.number_of_rows = int(self._num_rows_spin.get())
        self.number_of_columns = int(self._num_col_spin.get())
        self.start_player = self._first_player.get()
        self.winning_method = self._winning_method.get()
        self.layout = self._layout.get()
        game.clear_board()
        game.start(self.start_player,
                   self.number_of_rows,
                   self.number_of_columns,
                   self.layout)
        board = GameBoard()
        board.show()

        # Make start game unpressable until start_player and winning_method
        # are both clicked/selected 



if __name__ == '__main__':
    game = OthelloModule.OthelloGame()
    GUI = GameOptions()
    GUI.start()

