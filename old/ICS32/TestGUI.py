class OthelloGUI():
    def __init__(self):
        self._root_window = tkinter.Tk()

##        self._maincanvas = tkinter.Canvas(
##            master = self._root_window, width = 600, height = 600,
##            background = '#32CD32')
##        self._maincanvas.grid(
##            row = 0, column = 0, padx = 10, pady = 10,
##            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._inputcanvas = tkinter.Canvas(
            master = self._root_window, width = 300, height = 300,
            background = '#32CD32')
        self._inputcanvas.grid(
            row = 0, column = 0, padx = 5, pady = 5,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

        options = GameOptions()
        options.show()



        
    def user_input(self):
        def inputted():
            self.num_of_rows = int(e1.get())
            self.num_of_columns = int(e2.get())
            self.first_player = e3.get()
            self.method = e4.get()
            print(self._inputcanvas.find_all())
            self.create_board()
            print('Rows: {}\nColumns: {}\nStarting: {}\nWinning Method: {}'.format(e1.get(),e2.get(),e3.get(),e4.get()))
        self._inputcanvas.rowconfigure(0, weight = 1)
        self._inputcanvas.columnconfigure(0, weight = 1)

        header = self._inputcanvas.create_text(
            149, 30, text = 'OTHELLO', font = ('Helvetica', 30))

        e1 = tkinter.Entry(
            master = self._inputcanvas)
        e2 = tkinter.Entry(
            master = self._inputcanvas)
        e3 = tkinter.Entry(
            master = self._inputcanvas)
        e4 = tkinter.Entry(
            master = self._inputcanvas)

        self._rows = tkinter.Label(
            master = self._inputcanvas, text = 'Please enter the number of rows', background = '#99CCFF')
        self._columns = tkinter.Label(
            master = self._inputcanvas, text = 'Please enter the number of columns', background = '#99CCFF')
        self._player = tkinter.Label(
            master = self._inputcanvas, text = 'Please enter which player will go first', background = '#99CCFF')
        self._winning = tkinter.Label(
            master = self._inputcanvas, text = 'Please enter the winning method', background = '#99CCFF')

        self._inputcanvas.create_window(149,70, window = self._rows)
        self._inputcanvas.create_window(149,90, window = e1)
        self._inputcanvas.create_window(149,120, window = self._columns)
        self._inputcanvas.create_window(149,140, window = e2)
        self._inputcanvas.create_window(149,170, window = self._player)
        self._inputcanvas.create_window(149,190, window = e3)
        self._inputcanvas.create_window(149,220, window = self._winning)
        self._inputcanvas.create_window(149,240, window = e4)
        

        press = tkinter.Button(
            master = self._inputcanvas, text = 'Start Game',
            command = self._options)

        self._inputcanvas.create_window(149,270, window = press)

    def create_board(self):
        self._maincanvas = tkinter.Canvas(
            master = self._root_window, width = 600, height = 600,
            background = '#32CD32')
        self._maincanvas.grid(
            row = 0, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        column_len = (self._maincanvas.winfo_reqwidth())/self.num_of_columns
        rows_len = (self._maincanvas.winfo_reqheight())/self.num_of_rows
        print(self._maincanvas.winfo_reqwidth())
        print(self._maincanvas.winfo_reqheight())

        for i in range(self.num_of_columns):
            self._maincanvas.create_line(column_len*(i+1), 0, column_len*(i+1), self._maincanvas.winfo_reqheight(), fill = 'black')
        for i in range(self.num_of_rows):
            self._maincanvas.create_line(0, rows_len*(i+1),self._maincanvas.winfo_reqwidth(), rows_len*(i+1))

        # A Square would be (0,0),      (column_len * (i + 1), 0,),     (0, rows_len * (i + 1)),        (column_len * (i + 1), rows_len * (i + 1)
        #                   top left,   top right,                      bottom left,                    bottom right
        # Say a piece is in board[2][4]
        # That means you would do column_len * (4 + 1) and rows_len * ( 2 + 1)
