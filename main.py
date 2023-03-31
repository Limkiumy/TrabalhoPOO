#Importamos a classe jogadores e o módulo random para embaralhar as cartas.
from Classe import jogadores
import random

# Aqui estão os objetos e atributos da classe "jogadores".
dudalisboa = jogadores("Duda Lisboa", 1.8, 6, 5, 10, 6, 7)
emanuelrego = jogadores("Emanuel Rego", 1.9, 7, 6, 9, 8, 10)
anapatricia = jogadores("Ana Patrícia", 1.94, 5, 7, 6, 5, 6)
agatha = jogadores("Ágatha", 1.82, 4, 8, 3, 4, 5)
alana = jogadores("Alana", 1.63, 9, 4, 5, 7, 4)
andressa = jogadores("Andressa Calvacanti", 1.75, 8, 9, 7, 3, 3)

# Uma lista contendo três objetos da classe jogadores.
listcartas = [alana, agatha, andressa]

# Aqui embaralhamos a "listcartas".
random.shuffle(listcartas)

carta1J = listcartas[0]

carta1J.Rodada1(int(input("Qual categoria você irá escolher para ser comparada?\n(Digite f para:força; Digite v para:velocidade; Digite h para:habilidade; Digite t para:técnica; Digite p para:pontaria.")))

# Aqui chamamos a função "mostrar" dentro do objeto "carta1J".
carta1J.mostrar()

# Variáveis que vão ser usadas para armazenar os pontos do jogador e do computador durante o jogo.
pontosJ = 0
pontosC = 0

# RodadasGanhasJ = 0
# RodadasGanhasC = 0

# CartaDoisJ = listcartas[1]
# CartaTresJ = listcartas[2]



