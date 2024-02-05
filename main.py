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

if __name__ == "__main__":
    game = WarGame()
    player1 = Player("Alice")
    player2 = Player("Bob")

    game.add_observer(player1)
    game.add_observer(player2)

    game.notify_winner("Alice", ["Brasil", "Chile", "Peru"])
