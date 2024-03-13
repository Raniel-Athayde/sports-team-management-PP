import pickle
import os
import platform
from traceback import print_tb
from classes import *

def limpar_terminal():
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def listar(lista):
    for i, elemento in enumerate(lista, start = 1):
        print(f"    {i} - {elemento.nome}")
    print()

def remover(lista, item):
    print("Qual " + item + " você deseja remover?")
    i_item = input("Escreva o numero do " + item +":" )
    try:
        del lista[int(i_item) - 1]
    except:
        print("Opção invalida")
        input("Pressione ENTER para continuar")

def novo_time(lista_times):
    jogadores = []
    prox_jogos = []
    nome = input("Digite o nome do time: ")
    ntime = Time(nome, jogadores, prox_jogos, 0, 0, 0)
    lista_times.append(ntime)

def salvar_times(lista_times):
    with open('dados_times.pkl', 'wb') as file:
        pickle.dump(lista_times, file)

def carregar_times():
    try:
        with open('dados_times.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []
    
def input_error_message():  
    print("Opção invalida")
    input("Pressione ENTER para continuar")

def error_message(mensagem):
    print(mensagem)
    input("Pressione ENTER para continuar")