"""
EXERCÍCIO 038: Comparando Números

Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é maior.
- O segundo valor é maior.
- Não existe valor maior, os dois são iguais.
"""
import os
import random
import time
print('=' * 43)
print('={:12}Comparando Numeros{:11}='.format((''), ('')))
print('=' * 43)

n1 = int(input('Digite o 1º numero Inteiro: '))
n2 = int(input('Digite o 2º Numero Inteiro: '))
if n1 > n2:
    print(f'O Primeiro Numero é Maior')
elif n1 < n2:
    print(f'O Segundo Numero é Maior')
else:
    print('Não Existe Numero Maior nem Menor os Dois Numeros Sao Iguais')
#os.system('pause')
