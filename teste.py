import unittest
from main import Player, WarGame

class TestWarGame(unittest.TestCase):
    def setUp(self):
        self.game = WarGame()
        self.player1 = Player("Alice")
        self.player2 = Player("Bob")

        self.game.add_observer(self.player1)
        self.game.add_observer(self.player2)

    def test_notify_winner(self):
        self.game.notify_winner("Alice", ["Brasil", "Chile", "Peru"])
        self.assertTrue(self.player1.countries_won or self.player2.countries_won)

    def test_winner_has_at_least_three_countries(self):
        self.game.notify_winner("Alice", ["Brasil", "Chile", "Peru"])
        if self.player1.countries_won:
            self.assertTrue(len(self.player1.countries_won) >= 3)
        else:
            self.assertTrue(len(self.player2.countries_won) >= 3)

    def test_loser_has_two_or_less_countries(self):
        self.game.notify_winner("Alice", ["Brasil", "Chile", "Peru"])
        if self.player1.countries_won:
            self.assertTrue(len(self.player2.countries_won) <= 2)
        else:
            self.assertTrue(len(self.player1.countries_won) <= 2)

if __name__ == "__main__":
    unittest.main()
