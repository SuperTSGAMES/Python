"""
EXERCÍCIO 025: Procurando uma String Dentro de Outra

Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""
import os


print('='*43)
print('={:10}Procurando uma String{:10}='.format((''),('')))
print('='*43)

nome = str(input('Qual Seu Nome? ')).strip()
print('SILVA' in nome.upper())
os.system('pause')
