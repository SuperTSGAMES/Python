"""
EXERCÍCIO 007: Média Aritmética

Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""
import os
print('='*43)
print('={:12} Calculo de Média {:11}='.format((''),('')))
print('='*43)
n1 = float(input('Digite a Primeira Nota: '))
n2 = float(input('Digite a Segunda Nota: '))
media = (n1 + n2) / 2
print(f'A Média do Aluno é: {media:.1f}')
os.system('pause')
