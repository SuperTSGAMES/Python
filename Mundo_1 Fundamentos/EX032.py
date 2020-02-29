"""
EXERCÍCIO 032: Ano Bissexto

Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
"""
import os
from datetime import date
print('='*43)
print('={:14}ANO BISSEXTO?{:14}='.format((''),('')))
print('='*43)

ano = int(input('Digite Um Ano Para Saber Se ele É BISSEXTO ou Digite 0 para o ano Atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O Ano de {ano} é BISSEXTO')
else:
    print(f'O Ano de {ano} NÃO é BISSEXTO')
os.system('pause')
