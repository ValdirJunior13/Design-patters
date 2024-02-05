# Importando a biblioteca para testes unitários
import unittest
from main import JogoDeGuerra, Jogador

# Teste unitário
class TestObserverPattern(unittest.TestCase):
    def test_observer_pattern(self):
        jogo = JogoDeGuerra()
        jogador1 = Jogador('Jogador 1')
        jogador2 = Jogador('Jogador 2')

        jogo.anexar(jogador1)
        jogo.anexar(jogador2)

        jogo.notificar('Jogador 1')

if __name__ == "__main__":
    unittest.main()
