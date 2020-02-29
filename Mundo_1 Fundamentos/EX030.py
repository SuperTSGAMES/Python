"""
EXERCÍCIO 030: Par ou Ímpar?

Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""
import os

print('='*43)
print('={:14}PAR OU ÍMPAR{:15}='.format((''),('')))
print('='*43)

num = int(input('Digite um Numero Para Saber Se Ele é PAR ou ÍMPAR: '))
n1 = num % 2
if n1 == 0:
    print(f'O Numero {num} Que Voçê Digitou é PAR ')
else:
    print(f'O Numero {num} Que Voçê Digitou é ÍMPAR ')
#os.system('pause')
