from ai import AI
from human import Human
class Game():
    def __init__(self) -> None:
        self.human_player1 = Human('Player 1')
        self.human_player2 = Human('Player 2')
        self.ai1 = AI('Computer 1')
        self.ai2 = AI('Computer 2')
