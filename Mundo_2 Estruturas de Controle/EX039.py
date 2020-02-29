"""
EXERCÍCIO 039: Alistamento Militar

Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar, ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
import os
import random
import time
from datetime import date

print('='*43)
print('={:11}Alistamento Militar{:11}='.format((''),('')))
print('='*43)
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print(f'Você ainda não tem 18 anos. Ainda faltam {saldo} anos para o alistamento.')
    print(f'Seu alistamento será em {ano}.')
else:
    saldo = idade - 18
    ano = atual - saldo
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    print(f'Seu alistamento foi em {ano}.')
#os.system('pause')
