from player import Player
import random
class AI(Player):
    def __init__(self, name_passed) -> None:
        super().__init__(name_passed)
    
    def choose_move(self):
        move = random.choice(self.choice)
        print(f"Ai has picked {move}.")
        return move