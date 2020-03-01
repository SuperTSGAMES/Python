"""
DESAFIO 045: Pedra, Papel e Tesoura

Crie um programa que faça o computador jogar Jokenpô com você.
"""
import os
from random import choice
import time
placarpc = 0
placarp1 = 0

cores = dict(vermelho='\033[31m', verde='\033[32m', limpa='\033[m')
x = 0
while x == 0:# Checa se o nome é VALIDO ENQUANTO for Invalido executa ate Ser valido
    print('=' * 42)
    print('={:9}Pedra, Papel e Tesoura{:9}='.format('', ''))
    print('=' * 42)
    player = str(input('\nOLÁ Qual é o Seu Nome? ')).strip().upper()
    player.isnumeric()
    os.system('cls') or None
    if player != '' and player.isnumeric() == False:
        x = 1
    else:
        print('Nome INVALIDO Tente Novamente!\n')
        x = 0
while x == 1:#Quando Nome for Valido INICIA o JOGO
    print('=' * 42)
    print('={:9}Pedra, Papel e Tesoura{:9}='.format('', ''))
    print('={:13}PLACAR DO JOGO{:13}='.format('', ''))
    print('={:7}JOGADOR : {} | COMPUTADOR:{} {:6}='.format('', placarp1, placarpc, ''))
    print('=' * 42)
    opcoes = ['PAPEL', 'PEDRA', 'TESOURA']
    pc = choice(opcoes)
    #Pede para o jogador Escolher uma opçao
    jogador = str(input(f'BEM VINDO ao Jogo {player}\nEscolha entre "PEDRA, PAPEL ou TESOURA" para JOGAR: ')).upper().strip()
    if jogador == 'PEDRA' or jogador == 'PAPEL' or jogador == 'TESOURA':
        print('PROCESSANDO...')
        time.sleep(2)
        print(f'Voce Jogou {jogador} e o Computador Jogou {pc}: ', end='')
        if jogador == pc:
            print(f'{player} Nós EMPATAMOS')
            x = int(input("\nDeseja JOGAR Novamente?\nTecle: 1 para Sim ou 2 para Não: "))
            if x != 1:
                print("SAINDO...")
                time.sleep(5)
            os.system('cls') or None
        elif jogador == 'PAPEL' and pc == 'PEDRA' or jogador == 'TESOURA' and pc == 'PAPEL' or jogador == 'PEDRA' and pc == 'TESOURA':
            print('Parabéns {} {}VOÇÊ GANHOU{}!'.format(player, cores['verde'], cores['limpa']))
            placarp1 += 1
            x = int(input("\nDeseja JOGAR Novamente?\nTecle: 1 para Sim ou 2 para Não: "))
            if x != 1:
                print("SAINDO...")
                time.sleep(5)
            os.system('cls') or None
        elif jogador == 'PEDRA' and pc == 'PAPEL' or jogador == 'PAPEL' and pc == 'TESOURA' or jogador == 'TESOURA' and pc == 'PEDRA':
            print('Sinto Muito {} {}VOÇÊ PERDEU{}!'.format(player, cores['vermelho'], cores['limpa']))
            placarpc += 1
            x = int(input("\nDeseja JOGAR Novamente?\nTecle: 1 para Sim ou 2 para Não: "))
            if x != 1:
                print("SAINDO...")
                time.sleep(5)
            os.system('cls') or None
    else:#Executa se opçao escolhida Pelo Jogador for INVALIDA
        print('Opção INVALIDA')
        x = int(input("\nDeseja JOGAR Novamente?\nTecle: 1 para Sim ou 2 para Não: "))
        if x != 1:
            print("SAINDO...")
            time.sleep(5)
    os.system('cls') or None
else:
    x = 0
