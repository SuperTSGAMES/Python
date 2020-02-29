"""
EXERCÍCIO 005: Antecessor e Sucessor

Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
"""
import os
print('='*43)
print('={:2} Antecessor e Sucessor de um numero: {:2}='.format((''),('')))
print('='*43)
n1 = int(input('Digite um Numero: '))
a = n1 - 1
s = n1 + 1
print(f'\nO Antecessor de {n1} é {a} e o Sucessor é {s}')

os.system('pause')
