from cell import Cell

class Board:
    """
    Crea el tablero de la aplicación
        size: int - Tamaño del tablero.
        grid: list - Tablero del juego.
        free_cells: list - Lista de celdas vacías.
    """

    def __init__(self):
        '''
        Constructor de la aplicación
        '''
        self.size = 4
        self._init_board()

    def _init_board(self):
        '''
        Inicializa el tablero
        '''
        board = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(Cell(i, j))
            board.append(row)
        self.grid = board


    def __str__(self):
        '''
        Representación en cadena del tablero.
        '''
        string = ''
        for row in range(self.size):
            for col in range(self.size):
                string += self.grid[row][col].__str__()
            string += '\n'
        return string
