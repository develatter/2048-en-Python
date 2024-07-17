class Cell:
    def __init__(self, x, y):
        '''
        Inicializa una celda.
            x: int - Coordenada x de la celda.
            y: int - Coordenada y de la celda.
        '''
        self.x = x
        self.y = y
        self.value = 0
        self.alive = False

    def grow(self):
        '''
        Hace crecer el valor de la celda.
        '''
        if self.alive and self.value < 2048:
            self.value *= 2
    
    def spawn(self):
        '''
        Hace que la celda vuelva a estar viva.
        '''
        if not self.alive:
            self.value = 2
            self.alive = True

    def get_coords(self) -> tuple:
        '''
        Obtiene las coordenadas de la celda.
            return: tuple - Coordenadas de la celda.
        '''
        return self.x, self.y
    
    def is_movable(self, target) -> bool:
        '''
        Verifica si la celda es movible.
            target: Cell - Celda objetivo.
            return: bool - True si la celda es movible, False
        '''
        return (
            self.alive 
            and (not target.alive 
                 or (target.alive and self.value == target.value))
            )

    def __str__(self) -> str:
        '''
        Representación en cadena de la celda.
            return: str - Representación en cadena de la celda.
        '''
        shown = self.value if self.alive else ' '
        return str(f'[{shown:^5}]')
    
    def __repr__(self) -> str:
        '''
        Representación en cadena de la celda.
            return: str - Representación en cadena de la celda.
        '''
        return str(self.value)