class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = 0
        self.score2 = 0
        self.str = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player):
        if player == self.player1:
            self.score1 += 1
        elif player == self.player2:
            self.score2 += 1

    def get_score(self):
        if self.score1 == self.score2:
            return self.tie()
        if self.score1 >= 4 or self.score2 >= 4:
            return self.win_or_advantage()
        else:
            return self.score()

    def tie(self):
        if self.score1 < 4:
            return f"{self.str[self.score1]}-All"
        else:
            return "Deuce"

    def win_or_advantage(self):
        difference = self.score1 - self.score2

        if difference == 1:
            return f"Advantage {self.player1}"
        elif difference == -1:
            return f"Advantage {self.player2}"
        elif difference >= 2:
            return f"Win for {self.player1}"
        else:
            return f"Win for {self.player2}"

    def score(self):
        return f"{self.str[self.score1]}-{self.str[self.score2]}"

