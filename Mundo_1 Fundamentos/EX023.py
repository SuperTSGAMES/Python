"""
EXERCÍCIO 023: Separando Dígitos de um Número

Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

Ex:
Digite um número: 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1
"""
import os


print('='*43)
print('={:5} Separando Dígitos de um Número{:5}='.format((''),('')))
print('='*43)

num = int(input('Digite um Numero entre "0 e 9999": '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"O numero {num} tem:\n{u} Unidades\n{d} Dezenas\n{c} Centenas\n{m} Milhar")
os.system('pause')
