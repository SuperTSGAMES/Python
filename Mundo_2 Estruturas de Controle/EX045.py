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

def jokempo(opcoes):
    if opcoes == 'PEDRA':
        print("""
        MMMMMMMMMMMMMMMMMMMMM0;   'kMWo. .,kMMMMMMMMMMMMMM
        MMMMMMMMMMMMMM0o::cdc lk0Oo.'.,dOko.'NMMMMMMMMMMMM
        MMMMMMMMMMMMN..xKX0c dMMMMMO ,MMMMMO xMMMMMMMMMMMM
        MMMMMMMMMWKOl OMMMMW cMMMMMK dMMWKOc kMMMMMMMMMMMM
        MMMMMMMX;.;l; :MMMMM'.MMMMMx ll'.;lo:.:NMMMMMMMMMM
        MMMMMMM,.WMMM: KMMMMl XOl;'.'ckNMMMMMN,.KMMMMMMMMM
        MMMMMMM. XMMMW.,MMMMO l cXMMMMMMMMMX;0W; KMMMMMMMM
        MMMMMMN  'WMMMO xMMMW ;'.OWMMMMMMWk.'NMW,.XMMMMMMM
        MMMMMM0 c.'NMMM, OMMK  '   .'''.. :OMMMMN.,MMMMMMM
        MMMMMMO kNc.;lc.,;,,,oK: ;xNMMMWx;.';KMMMd 0MMMMMM
        MMMMMMk OMMWKO0NMMMMWc lNMMMMMMMMMMWNMMMMd OMMMMMM
        MMMMMMk OMMMMMMMMMMX..XMMMMMMMMMMMMMMMMM0 ;MMMMMMM
        MMMMMM0 xMMMMMMMMMX.,WMMMMMMMMMMMMMMMMX:.dMMMMMMMM
        MMMMMMX lMMMMMMMMMNxWMMMMMMMMMMMMMMM0;.oNMMMMMMMMM
        MMMMMMMo 0MMMMMMMMMMMMMMMMMMMMMK:.cKMMMMMMMMMMMMMM
        MMMMMMMW..NMMMMMMMMMMMMMMMMMMMc oWMMMMMMMMMMMMMMMM
        MMMMMMMMN..XMMMMMMMMMMMMMMMMMX lMMMMMMMMMMMMMMMMMM
        MMMMMMMMMN lMMMMMMMMMMMMMMMMMO xMMMMMMMMMMMMMMMMMM
        MMMMMMMMMX oMMMMMMMMMMMMMMMMMX oMMMMMMMMMMMMMMMMMM
        MMMMMMMMM0 dMMMMMMMMMMMMMMMMMW ;MMMMMMMMMMMMMMMMMM
        MMMMMMMMMO cOOOOOOOOOOOOOOOOOO..MMMMMMMMMMMMMMMMMM""")
    elif opcoes == 'PAPEL':
        print("""
        MMMMMMMMMMMMMMMMMMMMWc.  ;XMMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMXKKWMMMMMM; oOd..WMMMMMMMMMMMMMMMMMMMMMM
        MMMMMMMMO..;'.oWMMMX cMMMd kMMMMMKl;;c0MMMMMMMMMMM
        MMMMMMMM; OMMO lMMMX lMMMk dMMMMx ,kd  XMMMMMMMMMM
        MMWWMMMMN..WMMN.'WMX lMMMx kMMK..WMMO ,MMMMMMMMMMM
        x....dWMMd dMMMd xMX lMMMd OMW' OMMW' 0MMMMMMMMMMM
         ,MWx..KMW..XMMW,.WX lMMMo 0Mo lMMMx cMMMMMMMMMMMM
        : kMMK..0Md :MMM0 oX lMMMl KX 'WMMM' XMMMMMMMMMMMM
        W; dMMN, dN. 0MMM; k lMMMc 0, KMMMk lMMMMMMMMMMMMM
        MWc cWMWl cx 'WMMO . lMMM: ; oMMMN..NMMMMMMMMMMMMM
        MMMx ,XMMO.'. xMMM:  lMMM;  'WMMMl oMMMMMMMMMMMMMM
        MMMMO..KMMK.  .WMMNk0NMMMNXXWMMMX .NMMMMMNOddd0NMM
        MMMMMK..0MMN:;dWMMMMMMMMMMMMMMMMl oMMMM0, 'coc'.:K
        MMMMMMX' kMMMMMMMMMMMMMMMMMMMMMMd cMMNl cXMMMWx..d
        MMMMMMMk cMMMMMMMMMMMMMMMMMMMMMMX .;..,OMMMNd.'xWM
        MMMMMMMo dMMMMMMMMMMMMMMMMMMMM0c..ckNMMMMXc.,OMMMM
        MMMMMMMd oMMMMMMMMMMMMMMMMMM0' :0MMMMMMWl ,KMMMMMM
        MMMMMMMK .WMMMMMMMMMMMMMMMMN;cXMMMMMMMK..xWMMMMMMM
        MMMMMMMMMd lMMMMMMMMMMMMMMMMMMMMWx, cXMMMMMMMMMMMM
        MMMMMMMMMMc lWMMMMMMMMMMMMMMMMXo..lXMMMMMMMMMMMMMM
        MMMMMMMMMMWd..OMMMMMMMMMMMMMO,.,kWMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMNo lMMMMMMMMMMMM,.NMMMMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMM.'MMMMMMMMMMMM,.MMMMMMMMMMMMMMMMMMMM""")
    else:
        print("""
        MMMMMMMMMMMMMMMMMMMWxllkMMMMMMMMMMWMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMN.lKK,,MMMMMMW;':,,XMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMM,;MMM,,MMMMW.oMMX 0MMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMx WMMO KMMMx WMMl.MMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMW xMMM.:MMM.cMMM.oMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMM;,MMMO XM0 XMM0 XMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMK',ll.oMMMO x 0MMM dMMMMMMMMMMMMMM
        MMMMMMMMMMMMMx;;.;MMMo.MMMMk:OMMM0 XMMMMMMMMMMMMMM
        MMMMMMMMMMMMo.NMo.MMMo.;;;;cdOXMMx MMMMMMMMMMMMMMM
        MMMMMMMMMMMMl.MMW.dMM':MMMMXOdc;,' MMMMMMMMMMMMMMM
        MMMMMMMMMMMMK OMMO KMX.:XMMMMMMMMO OMMMMMMMMMMMMMM
        MMMMMMMMMMMMW  KMMo.XMMx ';ldWMMMMc.MMMMMMMMMMMMMM
        MMMMMMMMMMMMM.'.c00, ;;,ol.o 0MMMMN OMMMMMMMMMMMMM
        MMMMMMMMMMMMM:'MOdokNMMM,'NModMMMMM.oMMMMMMMMMMMMM
        MMMMMMMMMMMMMX OMMMMMMMK.WMMMMMMMMO XMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMO.lNMMMMMMMMMMMMWo.kMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMWx,,lkKXNNNKOo;'dWMMMMMMMMMMMMMMMM
        MMMMMMMMMMMMMMMMMMMWKxolcccldOWMMMMMMMMMMMMMMMMMMM""")

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
        print('\n{:22}{} Jogou {} '.format(' ', player, jogador))
        jokempo(jogador)
        print('\n{:22}O Computador Jogou {} '.format(' ', pc))
        jokempo(pc)
        if jogador == pc:
            print('\n{:22}{} Nós EMPATAMOS'.format(' ', player))
            x = int(input("\nDeseja JOGAR Novamente?\nTecle: 1 para Sim ou 2 para Não: "))
            if x != 1:
                print("SAINDO...")
                time.sleep(5)
            os.system('cls') or None
        elif jogador == 'PAPEL' and pc == 'PEDRA' or jogador == 'TESOURA' and pc == 'PAPEL' or jogador == 'PEDRA' and pc == 'TESOURA':
            print('\n{:22}Parabéns {} {}VOÇÊ GANHOU{}!'.format(' ', player, cores['verde'], cores['limpa']))
            placarp1 += 1
            x = int(input("\nDeseja JOGAR Novamente?\nTecle: 1 para Sim ou 2 para Não: "))
            if x != 1:
                print("SAINDO...")
                time.sleep(5)
            os.system('cls') or None
        elif jogador == 'PEDRA' and pc == 'PAPEL' or jogador == 'PAPEL' and pc == 'TESOURA' or jogador == 'TESOURA' and pc == 'PEDRA':
            print('\n{:22}Sinto Muito {} {}VOÇÊ PERDEU{}!'.format(' ', player, cores['vermelho'], cores['limpa']))
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
