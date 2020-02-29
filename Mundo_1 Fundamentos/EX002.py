"""
EXERCÍCIO 003: Somando Dois Números

Crie um programa que leia dois números e mostre a soma entre eles.
"""
import os
print('='*42)
print('={:11} Soma de Numeros! {:11}='.format((''),('')))
print('='*42)

n1 = int(input('Digite Um Numero Inteiro: '))
n2 = int(input('\nDigite Outro Numero Inteiro: '))
s = n1 + n2
print(f'\nA Soma entre {n1} + {n2} é = {s}\n')

print(f'Exercicio SOMA de Numeros Reais (float)\n\n')

n3 = float(input('Digite uma Nota: '))
n4 = float(input('\nDigite outra Nota: '))
res = (n3 + n4) / 2
print(f"\nA media das notas é: {res:.2f}\n")
os.system('pause')
