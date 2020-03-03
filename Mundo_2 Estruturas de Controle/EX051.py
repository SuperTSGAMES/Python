"""
EXERCÍCIO 051: Progressão Aritmética

Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""
import os
print('=' * 43)
print('={:10}Progressão Aritmética{:10}='.format((''), ('')))
print('=' * 43)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f'{c}', end=' → ')
print('ACABOU')
os.system('pause')
