from game import Game
from game_controller import GameController

if __name__ == '__main__':
    controller = GameController(Game())
    controller.play()