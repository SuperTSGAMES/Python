"""
EXERCÍCIO 016: Quebrando um Número

Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

Ex:
Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
"""

"""
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}!'.format(num, trunc(num)))
"""
import math
import os

print('='*44)
print('={:12} Quebra de Numero {:12}='.format((''),('')))
print('='*44)

n1 = float(input('Digite Um Numero REAL: '))
print(f'Você Digitou o Numero {n1}, E a Porção Inteira desse Numero é {int(n1)}')
os.system('pause')
