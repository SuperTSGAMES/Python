"""
DESAFIO 041: Classificando Atletas

A Confederação Nacional de Natação precisa de um programa que leia o ano
de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER
"""
import os
import random
import time
from datetime import date
print('=' * 43)
print('={:10}Classificando Atletas{:10}='.format((''), ('')))
print('=' * 43)
nasc = int(input('Qual ano de Nascimento do Atleta? '))
atual = date.today().year
ano = atual - nasc
if ano <= 9:
    print(f'O Atleta Nasceu em {nasc}\nE tem {ano} Anos de Idade esta Classificado Como ATLETA MIRIM')
elif ano <= 14:
    print(f'O Atleta Nasceu em {nasc}\nE tem {ano} Anos de Idade esta Classificado Como ATLETA INFANTIL')
elif ano <= 19:
    print(f'O Atleta Nasceu em {nasc}\nE tem {ano} Anos de Idade esta Classificado Como ATLETA JUNIOR')
elif ano <= 25:
    print(f'O Atleta Nasceu em {nasc}\nE tem {ano} Anos de Idade esta Classificado Como ATLETA SÊNIOR')
else:
    print(f'O Atleta Nasceu em {nasc}\nE tem {ano} Anos de Idade esta Classificado Como ATLETA MASTER')
#os.system('pause')
