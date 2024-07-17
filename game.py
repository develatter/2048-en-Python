from board import Board

class Game:
    '''
    Clase que representa una partida
        board: Board - Tablero del juego.
        counter: int - Contador de movimientos.
    '''
    def __init__(self):
        '''
        Inicializa el juego.
        '''
        self.board = Board()
        self.counter = 0
    
    def increment_counter(self):
        '''
        Incrementa el contador de movimientos.
        '''
        self.counter += 1

 