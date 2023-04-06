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
        self.play_again()
        

    def display_welcome(self):
        print("Welcome to Rock Paper Scissors Lizard Spock. \n\n Each match will be best out of three games. \n Use the number keys to enter your selction\n\n Scissors cut Paper \n Paper covers Rock \n Rock crushes Lizard \n Lizard poisons Spock \n Scissors decapitates Lizard \n Lizard eats Paper \n Paper disproves Spock \n Spock vaporizes Rock \n Rock crushes Scissors\n")

    def game_phase(self):
        self.number_of_players = input("How many players? 1 or 2 ")
        if self.number_of_players == "1":
            self.one_player_game()
        elif self.number_of_players == "2":
            self.two_player_game()
    
    def play_again(self): 
        self.play_again = input("Would you like to play again? Y or N ")
        if self.play_again == 'Y':
            self.player1.score = 0
            self.player2.score = 0
            self.run_game()
        else:
            print("Thanks for playing!")

    def one_player_game(self):
        self.player1 = self.human_player1
        self.player2 = self.ai1
        while self.player1.score < 2 and self.player2.score < 2:
            self.player1_choice = self.human_player1.choose_move()
            self.player2_choice = self.ai1.choose_move()
            self.result = self.determine_winner(self.player1_choice,self.player2_choice)
            if self.player1.score == 2:
                print(f"/n{self.player1.name} wins the game!")
            elif self.player2.score == 2:
                print(f"/n{self.player2.name} winse the game!")

    def two_player_game(self):
        self.player1 = self.human_player1
        self.player2 = self.human_player2
        while self.player1.score < 2 and self.player2.score < 2:
            self.player1_choice = self.human_player1.choose_move()
            self.player2_choice = self.human_player2.choose_move()
            self.result = self.determine_winner(self.player1_choice,self.player2_choice)
            if self.player1.score == 2:
                print(f"/n{self.player1.name} wins the game!")
            elif self.player2.score == 2:
                print(f"/n{self.player2.name} winse the game!")

    def determine_winner(self, player1_choice, player2_choice):
        if player1_choice == player2_choice:
            print("The round is a draw!")
            self.player1.update_score('lose')
            self.player2.update_score('lose')
            return 'draw'
        elif player1_choice == 'Rock':
            if player2_choice == 'Paper' or player2_choice == 'Spock':
                print(f"{self.player2.name} wins the round!")
                self.player2.update_score('win')
                return 'lose'
            else:
                print(f"{self.player1.name} wins the round!")
                self.player1.update_score('win')
                return 'win'
        elif player1_choice == 'Paper':
            if player2_choice == 'Scissors' or player2_choice == 'Lizard':
                print(f"{self.player2.name} wins the round!")
                self.player2.update_score('win')
                return 'lose'
            else:
                print(f"{self.player1.name} wins the round!")
                self.player1.update_score('win')
                return 'win'
        elif player1_choice == 'Scissors':
            if player2_choice == 'Rock' or player2_choice == 'Spock':
                print(f"{self.player2.name} wins the round!")
                self.player2.update_score('win')
                return 'lose'
            else:
                print(f"{self.player1.name} wins the round!")
                self.player1.update_score('win')
                return 'win'
        elif player1_choice == 'Lizard':
            if player2_choice == 'Rock' or player2_choice == 'Scissors':
                print(f"{self.player2.name} wins the round!")
                self.player2.update_score('win')
                return 'lose'
            else:
                print(f"{self.player1.name} wins the round!")
                self.player1.update_score('win')
                return 'win'
        elif player1_choice == 'Spock':
            if player2_choice == 'Paper' or player2_choice == 'Lizard':
                print(f"{self.player2.name} wins the round!")
                self.player2.update_score('win')
                return 'lose'
            else:
                print(f"{self.player1.name} wins the round!")
                self.player1.update_score('win')
                return 'win'
        
