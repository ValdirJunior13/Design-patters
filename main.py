# Definindo a interface do sujeito
class JogoDeGuerra:
    def __init__(self):
        self.jogadores = []

    def anexar(self, jogador):
        self.jogadores.append(jogador)

    def notificar(self, vencedor):
        for jogador in self.jogadores:
            jogador.atualizar(vencedor)

# Definindo a classe do observador
class Jogador:
    def __init__(self, nome):
        self.nome = nome

    def atualizar(self, vencedor):
        if self.nome == vencedor:
            print(f'{self.nome} ganhou a batalha!')
        else:
            print(f'{self.nome} perdeu para {vencedor}.')
