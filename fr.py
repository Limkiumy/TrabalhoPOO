from Classe import jogadores

from random import random

# A função "Rodada1" vai ser responsável por executar uma rodada do jogo, que é recebido como parâmetro uma escolha feita pelo jogador.
def Rodada1(self, caracescolhido):

    # Tornamos as variáveis "pontosJ" e "pontosC" variáveis globais. Elas vão ser usadas para armazenar os pontos de cada jogador na rodada. Como elas são globais, podem ser acessadas e modificadas por qualquer método dentro da classe Jogadores.
    global pontosJ, pontosC

    if caracescolhido == self.velocidades:
        if self.carta1J.velocidades > self.carta1C.velocidades:
            print("")
            print("A carta escolhida pelo computador foi: ")
            self.carta1C.mostrar()
            self.alana.mostrar()
            return self.velocidades
            print("Você ganhou a rodada número 1!")
            pontosJ += 3
        else:
            print("")
            print("A carta escolhida pelo computador foi: ")
            self.carta1C.mostrar()
            self.alana.mostrar()
            print("Você perdeu a rodada número 1")
            pontosC += 3
    elif caracescolhido == self.habilidades:
        if self.carta1J.habilidades > self.carta1C.habilidades:
            print("")
            print("A carta escolhida pelo computador foi: ")
            self.carta1C.mostrar()
            self.alana.mostrar()
            print("Você ganhou a rodada número 1!")
            pontosJ += 3
        else:
            print("")
            print("A carta escolhida pelo computador foi: ")
            self.carta1C.mostrar()
            self.alana.mostrar()
            print("Você perdeu a perdeu número 1")
            pontosC += 3
    elif caracescolhido == self.forças:
        if self.carta1J.forças > self.carta1C.forças:
            print("")
            print("A carta escolhida pelo computador foi: ")
            self.carta1C.mostrar()
            self.alana.mostrar()
            print("Você ganhou a rodada número 1!")
            pontosJ += 3
        else:
            print("")
            print("A carta escolhida pelo computador foi: ")
            self.carta1C.mostrar()
            self.alana.mostrar()
            print("Você perdeu a rodada número 1")
            pontosC += 3
    elif caracescolhido == self.pontarias:
        if self.carta1J.pontarias > self.carta1C.pontarias:
            print("")
            print("A carta escolhida pelo computador foi: ")
            self.carta1C.mostrar()
            self.alana.mostrar()
            print("Você ganhou a rodada número 1!")
            pontosJ += 3
        else:
            print("")
            print("A carta escolhida pelo computador foi: ")
            self.carta1C.mostrar()
            self.alana.mostrar()
            print("Você perdeu a rodada número 1")
            pontosC += 3
    elif caracescolhido == self.tecnicas:
        if self.carta1J.tecnicas > self.carta1C.tecnicas:
            print("")
            print("A carta escolhida pelo computador foi: ")
            self.carta1C.mostrar()
            self.alana.mostrar()
            print("Você ganhou a rodada número 1!")
            pontosJ += 3
        else:
            print("")
            print("A carta escolhida pelo computador foi: ")
            self.carta1C.mostrar()
            self.alana.mostrar()
            print("Você perdeu a rodada número 1")
            pontosC += 3
def compararRodada1(self, escolha_jogador, rodadas_ganhas_jogador, rodadas_ganhas_computador):
 escolhas_disponiveis = [self.velocidades, self.habilidades, self.forças, self.pontarias, self.tecnicas]
 escolha_computador = random.choice(escolhas_disponiveis)
 print("O computador escolheu: ", escolha_computador)
 if escolha_computador == self.velocidades:
  print("Velocidade: ")
 elif escolha_computador == self.habilidades:
  print("Habilidade: ")
 elif escolha_computador == self.forças:
  print("Força: ")
 elif escolha_computador == self.pontarias:
  print("Pontaria: ")
 elif escolha_computador == self.tecnicas:
  print("Técnica: ")
 if escolha_jogador == escolha_computador:
  print("Empate na rodada 1!")
 elif escolha_jogador == self.velocidades and escolha_computador == self.habilidades:
  print("Você ganhou a rodada 1!")
  rodadas_ganhas_jogador += 1
 elif escolha_jogador == self.habilidades and escolha_computador == self.forças:
  print("Você ganhou a rodada 1!")
  rodadas_ganhas_jogador += 1
 elif escolha_jogador == self.forças and escolha_computador == self.pontarias:
  print("Você ganhou a rodada 1!")
  rodadas_ganhas_jogador += 1
 elif escolha_jogador == self.pontarias and escolha_computador == self.tecnicas:
  print("Você ganhou a rodada 1!")
  rodadas_ganhas_jogador += 1
 elif escolha_jogador == self.tecnicas and escolha_computador == self.velocidades:
  print("Você ganhou a rodada 1!")
  rodadas_ganhas_jogador += 1
 else:
  print("Você perdeu a rodada 1!")
  rodadas_ganhas_computador += 1