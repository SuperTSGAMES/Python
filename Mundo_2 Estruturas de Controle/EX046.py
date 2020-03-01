"""
EXERCÍCIO 046: Contagem Regressiva

Faça um programa que mostre na tela uma contagem regressiva para o estouro de
fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""
import time
import os
import emoji
print('=' * 43)
print('={:14}Bomba Relógio{:14}='.format('', ''))
print('=' * 43)
for cont in range(10, 0-1, -1):
    print(cont)
    time.sleep(1)
print(emoji.emojize('BOOOOMMMM :boom:', use_aliases=True))
#os.system('cls') or None
