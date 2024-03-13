import classes as cl
import funcoes as fn
import commands as cm
import sys

class PilhaEx:
    def __init__(self) -> None:
        self.pilha = []
        self.dados = []
        self.tamanho = 0
    
    def empilhar(self, elemento, parametro):
        self.pilha.append(elemento)
        self.dados.append(parametro)
        self.tamanho += 1

    def desempilhar(self):
        if self.tamanho > 0:
            self.tamanho -= 1
            elemento = self.pilha.pop()
            parametro = self.dados.pop()
            elemento(parametro)
        else:
            return None, None

    def desempilhar_prox(self):
        if self.tamanho >= 2:
            i = self.tamanho - 2
            self.pilha[i](self.dados[i])
            del self.pilha[i]
            del self.dados[i]
            self.tamanho = self.tamanho - 1

def voltar (any): #FUNÇÃO COMUM
    raise cl.end_exception("voltando...")

#FUNÇÕES PARA "verificar_ocorrencias"
def adicionar_ocorrencia(jogador): #verificar_ocorrencias(1)
    nocorrencia = input("Insira a ocorrencia: ")
    jogador.ocorrencias.append(nocorrencia)
    pilha_execucao.desempilhar()
def remover_ocorrencia(jogador): #verificar_ocorrencias(2)
    iocorrencia = input("Insira o número da ocorrencia que deseja remover: ")
    try:
        del jogador.ocorrencias[int(iocorrencia) - 1]
    except:
        fn.error_message("erro ao remover a ocorrencia")
    pilha_execucao.desempilhar()
verificar_ocorrencias_opcoes = [adicionar_ocorrencia, remover_ocorrencia, voltar]

#FUBÇÕES PARA "abrir_jogador"
def verificar_ocorrencias(jogador): #abrir_jogador(1)
    jogador.listar_ocorrencias()
    print("Selecione uma opção:")
    print("1 - Adicionar ocorrencia")
    print("2 - Remover ocorrencia")
    print("3 - Voltar\n")
    escolha = input("Sua opção: ")
    try:
        pilha_execucao.empilhar(verificar_ocorrencias, jogador)
        verificar_ocorrencias_opcoes[int(escolha) - 1](jogador)
    except cl.end_exception as e:
        print(e.mensagem)
        pilha_execucao.desempilhar_prox()
    except:
        fn.error_message("erro ao selecionar ocorrencia")
        pilha_execucao.desempilhar()

#FUNÇÕES PARA "verificar_desempenho"
def adicionar_desempenho(jogador): #verificar_desempenho(1)
    ndesempenho = input("Insira a descrição")
    jogador.desempenho.append(ndesempenho)
    pilha_execucao.desempilhar()
def remover_desempenho(jogador): #verificar_desempenho(2)
    idesempenho = input("Insira o número da descrição que deseja remover: ")
    try:
        del jogador.ocorrencias[int(idesempenho) - 1]
    except:
        fn.error_message("erro ao remover desempenho")
    pilha_execucao.desempilhar()
verificar_desempenho_opcoes = [adicionar_desempenho, remover_desempenho, voltar]

def verificar_desempenho(jogador): #abrir_jogador(2)
    fn.listar(jogador.desempenho)
    print("\n")
    print("Selecione uma opção:")
    print("1 - Adicionar desempenho em um jogo")
    print("2 - Remover desempenho")
    print("3 - Voltar\n")
    escolha = input("Sua opção: ")
    try:
        pilha_execucao.empilhar(verificar_desempenho, jogador)
        verificar_desempenho_opcoes[int(escolha) - 1](jogador)
    except cl.end_exception as e:
        print(e.mensagem)
        pilha_execucao.desempilhar_prox()
    except:
        fn.error_message("erro ao vrificar desempenho")
        pilha_execucao.desempilhar()
def editar_jogador(jogador): #abrir_jogador(3)
    mudar_nome = cm.OverwriteCommand(jogador.nome, "", "nome")
    novo_nome = mudar_nome.execute()
    jogador.novo_nome(novo_nome)
    mudar_posicao = cm.OverwriteCommand(jogador.posicao, "", "posição")
    nova_posicao = mudar_posicao.execute()
    jogador.mudar_posicao(nova_posicao)
    pilha_execucao.desempilhar()

abrir_jogador_opcoes = [verificar_ocorrencias, verificar_desempenho, editar_jogador, 
                        voltar]

def abrir_jogador(jogador): #vizualizar_jogador(0)
    fn.limpar_terminal()
    print("Nome: " + jogador.nome)
    print("Estado: " + jogador.estado + " a jogar")
    print("Posição: " + jogador.posicao)
    print("Selecione uma opção: ")
    print("1 - Verificar ocorrencias")
    print("2 - verificar desempenho")
    print("3 - Editar Jogador")
    print("4 - voltar\n")
    escolha = input("sua opção: ")
    try:
        pilha_execucao.empilhar(abrir_jogador, jogador)
        abrir_jogador_opcoes[int(escolha) - 1](jogador)
    except cl.end_exception as e:
        print(e.mensagem)
        pilha_execucao.desempilhar_prox()
    except:
        fn.error_message("erro ao escolher opção")

#FUNÇÕES PARA "abrir_time"
def novo_jogador(time): #abrir_time(1)
    time.novo_jogador()
    pilha_execucao.desempilhar()
def vizualizar_jogador(time): #abrir_time(2)
    ijogador = input("Insira o numero do(a) jogador(a): ")
    try:
        abrir_jogador(time.jogadores[int(ijogador) - 1])
    except:
        fn.error_message("Erro ao selecionar o jogador")
        pilha_execucao.desempilhar()
def remover_jogador(time): #abrir_time(3)
    fn.remover(time.jogadores, "jogador(a)") #melhorar isso daqui
    pilha_execucao.desempilhar()

#Funções para "vizualizar_jogos"
def adicionar_jogo(time): #vizualizar_jogos(1)
    evento = input("Insira aqui o nome do evento: ")
    time.prox_jogos.append(evento)
    pilha_execucao.desempilhar()
def concluir_jogo(time): #vizualizar_jogos(2)
    ievento = input("Escolha o evento que deseja concluir: ")
    sucesso = False
    try:
        del time.prox_jogos[int(ievento) - 1]
        sucesso = True
    except:
        fn.error_message("erro ao concluir o evento")
    if sucesso == True:
        print("Qual foi o resultado do jogo?")
        print("1 - Vitória")
        print("2 - Derrota")
        print("3 - Empate")
        print("4 - Irrelevante\n")
        resultado = input("Resultado: ")

        if resultado == "1":
            time.vict += 1

        elif resultado == "2":
            time.derr += 1
                    
        elif resultado == "3":
            time.em += 1
    pilha_execucao.desempilhar()
vizualizar_jogos_opcoes = [adicionar_jogo, concluir_jogo, voltar]

def vizualizar_jogos(time): #abrir_time(4)
    fn.limpar_terminal()
    print("Time: " + time.nome)
    print("Seus jogos:\n")
    time.prox_jogos.listar()
    print("O que deseja fazer?")
    print("1 - Adicionar jogo")
    print("2 - Concluir jogo")
    print("3 - Voltar")
    escolha = input("Sua opão: ")
    try:
        pilha_execucao.empilhar(vizualizar_jogos, time)
        vizualizar_jogos_opcoes[int(escolha) - 1](time)
    except cl.end_exception as e:
        print(e.mensagem)
        pilha_execucao.desempilhar_prox()
    except:
        fn.error_message("erro em vizualizar jogos")
        pilha_execucao.desempilhar()
def vizualizar_resultados(time): #abrir_time(5)
    print("n° de vitorias: " + str(time.vict)) 
    print("n° de derrotas: " + str(time.derr))
    print("n° de empates: " + str(time.em))
    total = time.vict + time.derr + time.em
    try:
        porcetagem = (time.vict / total) * 100
    except ZeroDivisionError:
        porcetagem = 0
    print("resultado: " + str(time.vict) +"/" + str(total) + "(" +  str(porcetagem) + "%)\n")
    input("precione enter para continuar")
    pilha_execucao.desempilhar()        
def editar_nome_time(time): #abrir_time(6)
    change_name = cm.OverwriteCommand(time.nome, "", "nome")
    novo_nome = change_name.execute()
    time.novo_nome(novo_nome)
    pilha_execucao.desempilhar()
abrir_time_opcoes = [novo_jogador, vizualizar_jogador, remover_jogador, 
                     vizualizar_jogos, vizualizar_resultados, editar_nome_time, voltar]

def abrir_time(time): #escolher_time(0)
    fn.limpar_terminal()
    print("Time: " + time.nome)
    print()
    print("   Jogadores:")
    time.listar_jogadores()
    print("Selecione a opção:")
    print("1 - Adicionar Jogador(a)")
    print("2 - Vizualizar jogador(a)")
    print("3 - Remover jogador(a)")
    print("4 - vizualizar jogos")
    print("5 - vizualizar resultados")
    print("6 - Editar nome")
    print("7 - voltar\n")
    escolha = input("Sua opção: ")
    try:
        pilha_execucao.empilhar(abrir_time, time)
        abrir_time_opcoes[int(escolha) - 1](time)
    except cl.end_exception as e:
        fn.error_message(e.mensagem)
        pilha_execucao.desempilhar_prox()
    except:
        fn.error_message("erro ao selecionar a opção (dentro da função abrir time)")
        pilha_execucao.desempilhar()

#FUNÇÕES PARA "Verificar_times"
def escolher_time(lista): #verificar_time(1)
    print("Qual time deseja vizualizar?")
    escolha3 = input("Escreva o número do time: ")
    try:
        abrir_time(lista[int(escolha3) - 1])
    except:
        fn.input_error_message("erro ao escolher time")
        pilha_execucao.desempilhar()
def remover_time(lista): # verificar_time(2)
    fn.remover(lista, "time")
    pilha_execucao.desempilhar()

Verificar_times_opcoes = [escolher_time, remover_time, voltar]

#FUNÇÕES PARA "inicio"
def olhar_times(lista): #inicio(1)
    
    fn.limpar_terminal()
    print("Seus times salvos são:\n")
    fn.listar(lista)
    print("Secione a opção:\n")
    print("1 - Vizualizar time")
    print("2 - Remover time")
    print("3 - Voltar\n")
    escolha = input("Sua opção: ")
    try:
        pilha_execucao.empilhar(olhar_times, lista)
        Verificar_times_opcoes[int(escolha)-1](lista)
    except cl.end_exception as e:
        print(e.mensagem)
        input("pressione enter")
        fn.salvar_times(lista)
        pilha_execucao.desempilhar_prox()
    except:
        fn.error_message("Opção inválida")
        pilha_execucao.desempilhar()

def adicionar_time(lista): #inicio(2)
    fn.novo_time(lista)
    fn.salvar_times(lista)
    pilha_execucao.desempilhar()
def encerrar(lista): #inicio(3)
    fn.salvar_times(lista)
    raise cl.end_exception("encerrando...")
inicio_opcoes = [olhar_times, adicionar_time, encerrar]

def inicio(lista):
    fn.limpar_terminal()
    print("\nBem-vindo ao STM\n")
    print("Selecione a opção:")
    print("1 - Verificar times")
    print("2 - Adicionar time")
    print("3 - Salvar e encerrar\n")

    escolha = input("Sua opção: ")

    try:
        pilha_execucao.empilhar(inicio, lista)
        inicio_opcoes[int(escolha)-1](listat)
    except cl.end_exception as e:
        fn.salvar_times(lista)
        fn.error_message(e.mensagem)
        sys.exit()
    except:
        fn.error_message("Opção inválida")
        pilha_execucao.desempilhar()

pilha_execucao = PilhaEx()

if __name__ == "__main__":
    listat = fn.carregar_times()
    inicio(listat)


