"""
EXERCÍCIO 050: Soma dos Pares

Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""
import os
print('=' * 43)
print('={:13}Soma dos Pares{:14}='.format((''), ('')))
print('=' * 43)

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você informou {cont} números PARES e a soma foi {soma}.')
os.system('pause')
