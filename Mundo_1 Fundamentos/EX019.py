"""
EXERCÍCIO 019: Sorteando um Item na Lista

Um professor quer sortear um dos seus quatros alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""
import os
import random

print('='*43)
print('={:16} Sorteio {:16}='.format((''),('')))
print('='*43)

al1 = input('Nome do 1º Aluno: ')
al2 = input('Nome do 2º Aluno: ')
al3 = input('Nome do 3º Aluno: ')
al4 = input('Nome do 4º Aluno: ')
alunos = [al1,al2,al3,al4]
sorteio = random.choice(alunos)
print(f'O Ganhador do Sorteio Foi: {sorteio}')
os.system('pause')
