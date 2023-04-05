from player import Player
class Human(Player):
    def __init__(self, name_passed) -> None:
        super().__init__(name_passed)
    
    def choose_move(self):
        move = input("\n Choose 0 for Rock. \n Choose 1 for Paper. \n Choose 2 for Scissors. \n Choose 3 for Lizard \n Choose 4 for Spock. \n Choose your move: ")
        return move