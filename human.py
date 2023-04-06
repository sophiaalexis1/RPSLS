from player import Player
class Human(Player):
    def __init__(self, name_passed) -> None:
        super().__init__(name_passed)
    
    def choose_move(self):
        print("\n Choose 0 for Rock. \n Choose 1 for Paper. \n Choose 2 for Scissors. \n Choose 3 for Lizard \n Choose 4 for Spock. \n")
        move = int(input('Choose your move: '))
        player_choice = self.choice[move]
        print(f"Player choose {player_choice}")
        return player_choice
       