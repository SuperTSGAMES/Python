"""
EXERCÍCIO 047: Contagem de Pares

Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""
import time
import os
print('=' * 43)
print('={:12}Contagem de Pares{:12}='.format('', ''))
print('=' * 43)
for par in range(2, 51, 2):
    print(par)
print('FIM')
#os.system('cls') or None
