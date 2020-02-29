"""
EXERCÍCIO 009: Tabuada

Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
"""
import os
print('='*43)
print('={:16} Tabuada {:16}='.format((''),('')))
print('='*43)
n1 = int(input('Digite um Numero Para Calcular Sua Tabuada: '))
print('{} X {:2} = {}'.format(n1, 1, n1*1))
print('{} X {:2} = {}'.format(n1, 2, n1*2))
print('{} X {:2} = {}'.format(n1, 3, n1*3))
print('{} X {:2} = {}'.format(n1, 4, n1*4))
print('{} X {:2} = {}'.format(n1, 5, n1*5))
print('{} X {:2} = {}'.format(n1, 6, n1*6))
print('{} X {:2} = {}'.format(n1, 7, n1*7))
print('{} X {:2} = {}'.format(n1, 8, n1*8))
print('{} X {:2} = {}'.format(n1, 9, n1*9))
print('{} X {:2} = {}'.format(n1, 10, n1*10))
os.system('pause')
