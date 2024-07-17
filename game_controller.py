import random
from cell import Cell
import os

class GameController:
    '''
    Clase que controla el flujo del juego.
    '''
    def __init__(self, game):
        '''
        Inicializa el juego.
        '''
        self.game = game

    def play(self):
        '''
        Inicia la partida
        '''
        self.fill_random()
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')

            print(f'You used {self.game.counter} moves')

            if self._has_won():
                print('You won!')
                break

            if not self._can_move_any_dir(self.game.board.grid):
                print('Game Over')
                break

            print(self.game.board)

            move = input('move (awsd): ')
            if self.move(move):
                self.game.increment_counter()

            if move == 'q':
                break


    def fill_random(self):
        '''
        Llena una casilla aleatoria del tablero si quedan casillas vacías
        '''
        empty_cells = []

        for i in range(self.game.board.size):
            for j in range(self.game.board.size):
                if not self.game.board.grid[i][j].alive:
                    empty_cells.append((i, j))

        if empty_cells:
            row, col = random.choice(empty_cells)
            self.game.board.grid[row][col] = Cell(row, col)
            self.game.board.grid[row][col].spawn()
            
    def move(self, direction) -> bool:
        '''
        Mueve las celdas en la dirección indicada.
            direction: str - Dirección en la que se moverán las celdas.
                        
                        w: arriba
                        s: abajo
                        a: izquierda
                        d: derecha
        '''
        grid = self.game.board.grid
        if not self._can_move(grid, direction):
            return False

        if direction == 'w':
            self.move_up(grid)
        elif direction == 's':
            self.move_down(grid)
        elif direction == 'a':
            self.move_left(grid)
        elif direction == 'd':
            self.move_right(grid)
        else:
            return False
        
        self.fill_random()
        return True

    def move_up(self, grid):
        '''
        Mueve todas las celdas hacia arriba.
        '''
        for row in range(1, self.game.board.size):
            for col in range(self.game.board.size):
                if not grid[row][col].alive:
                    continue
                current_row = row
                while current_row > 0:
                    if not grid[current_row - 1][col].alive:
                        grid[current_row - 1][col] = grid[current_row][col]
                        grid[current_row][col] = Cell(current_row, col)
                        current_row -= 1
                    elif grid[current_row - 1][col].value == grid[current_row][col].value:
                        grid[current_row - 1][col].grow()
                        grid[current_row][col] = Cell(current_row, col)
                        current_row -= 1
                    else:
                        break
  
    def move_down(self, grid):
        '''
        Mueve todas las celdas hacia abajo.
        '''
        for row in range(self.game.board.size - 2, -1, -1):
            for col in range(self.game.board.size):
                if not grid[row][col].alive:
                    continue
                current_row = row
                while current_row < self.game.board.size - 1:
                    if not grid[current_row + 1][col].alive:
                        grid[current_row + 1][col] = grid[current_row][col]
                        grid[current_row][col] = Cell(current_row, col)
                        current_row += 1
                    elif grid[current_row + 1][col].value == grid[current_row][col].value:
                        grid[current_row + 1][col].grow()
                        grid[current_row][col] = Cell(current_row, col)
                        current_row += 1
                    else:
                        break

    def move_left(self, grid):
        '''
        Mueve todas las celdas hacia la izquierda.
        '''
        for row in range(self.game.board.size):
            for col in range(1, self.game.board.size):
                if not grid[row][col].alive:
                    continue
                current_col = col
                while current_col > 0:
                    if not grid[row][current_col - 1].alive:
                        grid[row][current_col - 1] = grid[row][current_col]
                        grid[row][current_col] = Cell(row, current_col)
                        current_col -= 1
                    elif grid[row ][current_col - 1].value == grid[row][current_col].value:
                        grid[row][current_col - 1].grow()
                        grid[row][current_col] = Cell(row, current_col)
                        current_col -= 1
                    else:
                        break
            

    def move_right(self, grid):
        '''
        Mueve todas las celdas hacia la derecha.
        '''
        for row in range(self.game.board.size):
            for col in range(self.game.board.size - 2, -1, -1):
                if not grid[row][col].alive:
                    continue
                current_col = col
                while current_col < self.game.board.size - 1:
                    if not grid[row][current_col + 1].alive:
                        grid[row][current_col + 1] = grid[row][current_col]
                        grid[row][current_col] = Cell(row, current_col)
                        current_col += 1
                    elif grid[row][current_col + 1].value == grid[row][current_col].value:
                        grid[row][current_col + 1].grow()
                        grid[row][current_col] = Cell(row, current_col)
                        current_col += 1
                    else:
                        break
                
    def _can_move(self, grid, move) -> bool:
        '''
        Verifica si se puede realizar un movimiento.
        '''

        for row in range(self.game.board.size):
            for col in range(self.game.board.size):
                match move:
                    case 'w':
                        if (
                            row > 0 
                            and grid[row][col].is_movable(grid[row - 1][col])
                            ):
                            return True
                    case 's':
                        if (
                            row < self.game.board.size - 1 
                            and grid[row][col].is_movable(grid[row + 1][col])
                            ):
                            return True
            
                    case 'a':
                        if (
                            col > 0 
                            and grid[row][col].is_movable(grid[row][col - 1])
                            ):
                            return True
              
                    case 'd':
                        if (
                            col < self.game.board.size - 1 
                            and grid[row][col].is_movable(grid[row][col + 1])
                            ):
                            return True
        return False
                    
    def _can_move_any_dir(self, grid) -> bool:
        '''
        Verifica si hay algún movimiento posible, independientemente de la dirección
        '''
        return any(self._can_move(grid, move) for move in ('w', 's', 'a', 'd'))
    
    
    def _has_won(self) -> bool:
        '''
        Verifica si el jugador ha ganado.
        '''
        for row in range(self.game.board.size):
            for col in range(self.game.board.size):
                if self.game.board.grid[row][col].value == 2048:
                    return True
        return False   