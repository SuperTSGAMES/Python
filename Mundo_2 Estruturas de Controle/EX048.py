"""
EXERCÍCIO 048: Soma Ímpares Múltiplos de Três

Faça um programa que calcule a soma entre todos os números ímpares que
são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""
import time
import os
print('=' * 43)
print('={:5}Soma Ímpares Múltiplos de Três{:6}='.format('', ''))
print('=' * 43)
soma = 0
cont = 0
for c in range(1 , 500, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'A soma de todos os {cont} valores solicitados é {soma}.')
#os.system('cls') or None
