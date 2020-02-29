"""
EXERCÍCIO 027: Primeiro e Último Nome de uma Pessoa

Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.

Ex: Ana Maria de Souza
Primeiro = Ana
Último = Souza
"""
import os

print('='*43)
print('={:10}Primeiro e Último Nome{:9}='.format((''),('')))
print('='*43)
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print(f'Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}.')
print(f'Seu último nome é {nome[len(nome) - 1]}.')
os.system('pause')
