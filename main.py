class Player:
    def __init__(self, name):
        self.name = name
        self.countries_won = []

class WarGame:
    def __init__(self):
        self.observers = []

    def add_observer(self, player):
        self.observers.append(player)

    def notify_winner(self, winner_name, countries_won):
        for player in self.observers:
            if player.name == winner_name:
                player.countries_won.extend(countries_won)
                for country in countries_won:
                    print(f"{winner_name} conquistou o país: {country}")
                print(f"{winner_name} venceu a batalha e conquistou os países: {', '.join(countries_won)}")
            else:
                print(f"{player.name} perdeu a batalha para {winner_name}.")
