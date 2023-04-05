from ai import AI
from human import Human
class Game():
    def __init__(self) -> None:
        self.human_player1 = Human('Player 1')
        self.human_player2 = Human('Player 2')
        self.ai1 = AI('Computer 1')
        self.ai2 = AI('Computer 2')

    def run_game(self):
        self.display_welcome()
        self.game_phase()

    def display_welcome(self):
        print("Welcome to Rock Paper Scissors Lizard Spock. \n\n Each match will be best out of three games. \n Use the number keys to enter your selction\n\n Scissors cut Paper \n Paper covers Rock \n Rock crushes Lizard \n Lizard poisons Spock \n Scissors decapitates Lizard \n Lizard eats Paper \n Paper disproves Spock \n Spock vaporizes Rock \n Rock crushes Scissors")

    def game_phase(self):
        self.number_of_players = input("How many players? 1 or 2 ")
        if self.number_of_players == "1":
            self.human_player1.choose_move
            self.ai1.choose_move
        elif self.number_of_players == "2":
            self.human_player1.choose_move
            self.human_player2.choose_move

