from time import sleep
import random

class Subject:
    def __init__(self):
        self.observers = []

    def add_subscriber(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_subscriber(self, observer):
        self.observers.remove(observer)

    def notify_subscribers(self, message):
        for observer in self.observers:
            observer.update(message)


class Player:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def notify_subscribers(self):
        self.subject.add_subscriber(self)

    def update(self, message):
        print(f"{self.name} received the message: {message}")

    def ready(self):
        print(f"{self.name} is ready for the game!")


class WarGame(Subject):
    def __init__(self, game_started, players):
        super().__init__()
        self.game_started = game_started
        self.players = players

    def start_game(self):
        self.game_started = True
        self.notify_subscribers("The game has started!")

    def end_game(self, winner):
        self.game_started = False
        self.notify_subscribers(f"The game has ended! Player {winner.name} won!")


if __name__ == '__main__':
    # Game instance #
    war_game = WarGame(False, [])

    # Player instances #
    player1 = Player('Player 1', war_game)
    player2 = Player('Player 2', war_game)
    player3 = Player('Player 3', war_game)

    # Players notify the game that they are ready #
    player1.notify_subscribers()
    player2.notify_subscribers()
    player3.notify_subscribers()

    # Game notifies players that the game has started #
    war_game.add_subscriber(player1)
    war_game.add_subscriber(player2)
    war_game.add_subscriber(player3)
    war_game.start_game()

    # Simulating game progress with a sleep
    print('Game in progress...')
    print('...')
    sleep(3)

    # Game notifies players that the game has ended #
    winner = None
    random_number = random.randint(1, 3)
    print(f'Random number: {random_number}')

    if random_number == 1:
        winner = player1
    elif random_number == 2:
        winner = player2
    else:
        winner = player3

    war_game.end_game(winner)
