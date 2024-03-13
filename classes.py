

class Jogador:
    def __init__(self, nome, estado, ocorrencias, desempenho, posicao):
        self.nome = nome
        self.estado = estado
        self.ocorrencias = ocorrencias
        self.desempenho = desempenho
        self.posicao = posicao

    def novo_nome(self, nome):
        self.nome = nome

    def mudar_posicao(self, posicao):
        self.posicao = posicao

    def mudar_estado(self):
        if self.estado == "Disponivél":
            self.estado = "Indisponivél"
        else:
            self.estado = "Disponivél"

    def listar_ocorrencias(self):
        for i, elemento in enumerate(self.ocorrencias, start = 1):
            print(f"    {i} - {elemento}")
        print()

class jogo:
    def __init__(self, nome, descricao, data):
        self.nome = nome
        self.descricao = descricao
        self.data = data
        

class Time:
    def __init__(self, nome, jogadores, prox_jogos, vict, derr, em):
        self.nome = nome
        self.jogadores = jogadores
        self.prox_jogos = prox_jogos
        self.vict = vict
        self.derr = derr
        self.em = em

    def novo_nome(self, nome):
        self.nome = nome

    def novo_jogador(self):
        nome = input("\nNome do jogador: ")
        ocorrencias = []
        desempenho = []
        estado = "Apto"
        njogador = Jogador(nome, estado, ocorrencias, desempenho, "indefinida")
        self.jogadores.append(njogador)

    def listar_jogadores(self):
        for i, elemento in enumerate(self.jogadores, start = 1):
            print(f"    {i} - {elemento.nome} - {elemento.estado}")
        print()


    def listar_prox_jogos(self):
        for i, elemento in enumerate(self.prox_jogos, start = 1):
            print(f"    {i} - {elemento}")
        print()

class end_exception(Exception):
    def __init__(self, mensagem):
        self.mensagem = mensagem
        


