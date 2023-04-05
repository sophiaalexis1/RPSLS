class Player:
    def __init__(self, name_passed):
        self.name = name_passed
        self.score = 0
        self.choice = ['Rock','Paper', 'Scissors', 'Lizard', 'Spock']

    def update_score(self, result):
        if result == 'win':
            self.score += 1
        elif result == 'lose':
            self.score -= 0