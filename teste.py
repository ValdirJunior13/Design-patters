import unittest
from unittest.mock import patch
from io import StringIO
import time
from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(self, winner: str, countries_won: List[str]):
        pass

class Player(Observer):
    def __init__(self, name: str):
        self.name = name
        self.countries_won = []

    def update(self, winner: str, countries_won: List[str]):
        if winner == self.name:
            print(f"{self.name} venceu a batalha e conquistou os países: {', '.join(countries_won)}")
            print(f"{self.name} perdeu a batalha.")
        else:
            print(f"{self.name} perdeu a batalha para {winner}.")
            print(f"{winner} conquistou os países: {', '.join(countries_won)}")

class WarGame:
    def __init__(self):
        self.observers: List[Observer] = []
        self.countries = ["Brasil", "Argentina", "Chile", "Peru", "Colômbia"]

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def notify_winner(self, winner: str, countries_won: List[str]):
        for country in countries_won:
            time.sleep(1)
            print(f"{winner} conquistou o país: {country}")

        for observer in self.observers:
            observer.update(winner, countries_won)

class TestWarGame(unittest.TestCase):
    def setUp(self):
        self.game = WarGame()
        self.player1 = Player("Alice")
        self.player2 = Player("Bob")
        self.game.add_observer(self.player1)
        self.game.add_observer(self.player2)

    @patch("sys.stdout", new_callable=StringIO)
    def assert_stdout(self, expected_output, mock_stdout):
        self.game.notify_winner("Alice", ["Brasil", "Chile", "Peru"])
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_notify_winner(self):
        expected_output = "Alice conquistou o país: Brasil\nAlice conquistou o país: Chile\nAlice conquistou o país: Peru\nBob perdeu a batalha para Alice.\nAlice venceu a batalha e conquistou os países: Brasil, Chile, Peru\nBob perdeu a batalha.\n"
        self.assert_stdout(expected_output)

if __name__ == "__main__":
    unittest.main()
