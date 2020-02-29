"""
EXERCÍCIO 024: Verificando as Primeiras Letras de um Texto

Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
"""
import os


print('='*43)
print('={:5}Verificando as Primeiras Letras{:5}='.format((''),('')))
print('='*43)
nome = str(input('Qual Nome da Sua Cidade? ')).strip()
print(nome[:5].upper() == 'SANTO')
os.system('pause')
