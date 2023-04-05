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
            self.player1_choice = self.human_player1.choose_move()
            self.player2_choice = self.ai1.choose_move()
        elif self.number_of_players == "2":
            self.player1_choice = self.human_player1.choose_move()
            self.player2_choice = self.human_player2.choose_move()

    def determine_winner(self, player1_choice, player2_choice):
        if player1_choice == player2_choice:
            return 'draw'
        elif player1_choice == 'rock':
            if player2_choice == 'paper' or player2_choice == 'spock':
                return 'lose'
            else:
                return 'wiin'
        elif player1_choice == 'paper':
            if player2_choice == 'scissors' or player2_choice == 'lizard':
                return 'lose'
            else:
                return 'win'
        elif player1_choice == 'scissors':
            if player2_choice == 'rock' or player2_choice == 'spock':
                return 'lose'
            else:
                return 'win'
        elif player1_choice == 'lizard':
            if player2_choice == 'rock' or player2_choice == 'scissors':
                return 'lose'
            else:
                return 'win'
        elif player1_choice == 'spock':
            if player2_choice == 'paper' or player2_choice == 'lizard':
                return 'lose'
            else:
                return 'win'
