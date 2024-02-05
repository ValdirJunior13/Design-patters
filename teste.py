import unittest
from time import sleep
from src import WarII,jogador
class TestClass(unittest.TestCase):

    def inserindojoagoresnoJogo(self):
        jogo = WarII(True, [])
        player1 = jogador('Jogador 1', jogo)
        self.assertEqual(len(jogo.jogadores),1, "teste falhou")
    
    def enviandoNotificacao(self):
        jogo = WarII(True, [])
        player1 = jogador('Jogador 1', jogo)
        player1.notify_subscribers()
        self.assertEqual(player1.notify_subscribers(), jogo.state, "teste falhou")

    def test_estado_inicial_do_jogo(self):
        jogo = WarII(True, [])
        self.assertTrue(jogo.state, "O jogo não está no estado inicial esperado.")

    def test_remover_jogador_do_jogo(self):
        jogo = WarII(True, [])
        player1 = jogador('Jogador 1', jogo)
        jogo.adicionar_jogador(player1)  # Adicionando jogador ao jogo
        jogo.remover_jogador(player1)  # Removendo jogador do jogo
        self.assertEqual(len(jogo.jogadores), 0, "A remoção do jogador do jogo falhou.")




if __name__ == "__main__":
    unittest.main()