class jogadores:
    def __init__(self, nomes, alturas, forças, velocidades, habilidades, pontarias, tecnicas):
        # Definimos o valor inicial dos atributo "carta1J" e "carta1C" como "None", que significa que o objeto jogador/computador ainda não tem uma carta selecionada.
        self.carta1J = None
        self.carta1C = None
        # Definimos o valor inicial dos atributos "pontosJ/C" como 0, indicando que ambos os jogadores não tem pontos iniciais.
        self.pontosJ = 0
        self.pontosC = 0
        #  Aqui armazenamos as informações que serão utilizadas durante o jogo para fazer as comparações entre as cartas dos jogadores.
        self.nomes = nomes
        self.alturas = alturas
        self.forças = forças
        self.velocidades = velocidades
        self.habilidades = habilidades
        self.pontarias = pontarias
        self.tecnicas = tecnicas
    #A função "mostrar" é responsável por exibir as informações sobre um objeto da classe "jogadores". Quando essa função é chamada para um objeto, ele imprime na tela os valores dos seus atributos, como nome, altura, força, velocidade, etc.
    def mostrar(self,):
        print("")
        print("NOME: ", self.nomes, "\n altura: ", self.alturas)
        print("VELOCIDADES: ", self.velocidades)
        print("HABILIDADE: ", self.habilidades)
        print("FORÇA: ", self.forças)
        print("PONTARIA: ", self.pontarias)
        print("TÉCNICA: ", self.tecnicas)
