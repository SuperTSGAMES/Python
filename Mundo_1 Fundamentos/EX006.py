"""
EXERCÍCIO 006: Dobro, Triplo, Raiz Quadrada

Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""
import os
print('='*43)
print('={:4} Dobro, Triplo, e Raiz Quadrada {:5}='.format((''),('')))
print('='*43)
n1 = int(input('Digite um valor: '))
print('O DOBRO de {} é {}\nO TRIPLO de {} é {}\nA Raiz Quadrada de {} é {:.2f}'.format(n1, (n1*2),n1,(n1*3),n1,(n1**(1/2)) ))
os.system('pause')
