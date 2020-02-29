"""
DESAFIO 040: Aquele Clássico da Média

Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:

- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
"""
import os
import random
import time
print('=' * 43)
print('={:14}Média de Nota{:14}='.format((''), ('')))
print('=' * 43)
nota1 = float(input('Digite a Primeira Nota: '))
nota2 = float(input('Digite a Segunda Nota: '))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print(f'A Média do aluno é {media:.1f}: Aluno APROVADO')
elif media >= 5 and media <= 6.9:
    print(f'A Média do aluno é {media:.1f}: Aluno em RECUPERAÇÃO')
else:
    print(f'A Média do aluno é {media:.1f}: Aluno REPROVADO')
#os.system('pause')
