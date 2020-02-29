"""
EXERCÍCIO 020: Sorteando uma Ordem na Lista

O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
import os
import random

print('='*43)
print('={:12} Sorteio em Lista{:12}='.format((''),('')))
print('='*43)

al1 = input('Nome do 1º Aluno: ')
al2 = input('Nome do 2º Aluno: ')
al3 = input('Nome do 3º Aluno: ')
al4 = input('Nome do 4º Aluno: ')
alunos = [al1,al2,al3,al4]
random.shuffle(alunos)
print(f'A Ordem dos Ganhadores é: {alunos}')

os.system('pause')
