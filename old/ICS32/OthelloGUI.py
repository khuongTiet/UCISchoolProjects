import tkinter
import OthelloModule
import project4

##Create a way for the user to input the starting variables for the game
##Create the grid layout according the the rows and columns inputted
##    Take the number of rows and columns
##    Divide the width and height of the canvas by the number of rows and columns
##    Draw a line at each interval from the top to the bottom or from left to right
##    Each square will have a dimension of width/rows x heigh/columns
##Create a method similar to the spots application where if a click occurs within a square, draw a piece there
##    If mouse click within the coordinates of the square, call the draw piece method within the square
##Create a method that turns flipped pieces into drawn ones

## Create a grid and place in column = 0 the game and column = 1 the score/interface

DEFAULT_FONT = ('Helvetica', 16)


class GameBoard():
    def __init__(self):
        self._board = tkinter.Toplevel()
        self._boardcanvas = tkinter.Canvas(
            master = self._board, width = 600, height = 600,
            background = 'green')
        self._boardcanvas.grid(
            row = 0, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        column_len = (self._boardcanvas.winfo_reqwidth())/GUI.number_of_columns
        rows_len = (self._boardcanvas.winfo_reqheight())/GUI.number_of_rows

        print(column_len)
        print(rows_len)

        for i in range(GUI.number_of_columns):
            self._boardcanvas.create_line(column_len*(i+1), 0, column_len*(i+1), self._boardcanvas.winfo_reqheight())
        for i in range(GUI.number_of_rows):
            self._boardcanvas.create_line(0, rows_len*(i+1),self._boardcanvas.winfo_reqwidth(), rows_len*(i+1))
        

    def show(self):
        pass
        


class GameOptions():
    def __init__(self):
        self._option_window = tkinter.Tk()

        othello_label = tkinter.Label(
            master = self._option_window, text = 'New Game',
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
            master = self._option_window, text = 'First player',
            font = DEFAULT_FONT)

        first_player_label.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.W)

        self._first_player = tkinter.StringVar()
        self._first_player.set(" ")

        black_button = tkinter.Radiobutton(
            master = self._option_window, text = 'Black player', padx = 10,
            variable = self._first_player, value = 'BLACK')

        black_button.grid(
            row = 3, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W)

        white_button = tkinter.Radiobutton(
            master = self._option_window, text = 'White player', padx = 10,
            variable = self._first_player, value = 'WHITE')

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
            variable = self._winning_method, value = 'MOST')

        most_button.grid(
            row = 4, column = 1, padx = 10, pady = 10,
            sticky = tkinter.W)

        least_button = tkinter.Radiobutton(
            master = self._option_window, text = 'Least pieces', padx = 13,
            variable = self._winning_method, value = 'LEAST')

        least_button.grid(
            row = 4, column = 1, padx = 10, pady = 10,
            sticky = tkinter.E)

        start_button = tkinter.Button(
            master = self._option_window, text = 'Start Game',
            font = DEFAULT_FONT, command = self._start_game)

        start_button.grid(
            row = 5, column = 2, padx = 10, pady = 10,
            sticky = tkinter.E)

        

    def start(self) -> None:
        self._option_window.mainloop()

    def _start_game(self) -> None:
        self.number_of_rows = int(self._num_rows_spin.get())
        self.number_of_columns = int(self._num_col_spin.get())
        self.start_player = self._first_player.get()
        self.winning_method = self._winning_method.get()
        print(self.number_of_rows)
        print(self.number_of_columns)
        print(self.start_player)
        print(self.winning_method)
        board = GameBoard()
        board.show()



if __name__ == '__main__':
    game = OthelloModule.OthelloGame()
    GUI = GameOptions()
    GUI.start()

