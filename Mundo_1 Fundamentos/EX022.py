"""
EXERCÍCIO 022: Analisador de Textos

Crie um programa que leia o nome completo de uma pessoa e mostre:

> O nome com todas as letras maiúsculas e minúsculas.
> Quantas letras ao todo (sem considerar espaços).
> Quantas letras tem o primeiro nome.
"""
import os


print('='*43)
print('={:12} Analizando Texto{:12}='.format((''),('')))
print('='*43)

nome = str(input('Qual Seu Nome? ')).strip()
separa = nome.split()
print(f'Seu Nome em Maiusculo é: "{nome.upper()}"')
print(f'Seu Nome em Minusculo é: "{nome.lower()}"')
print('Seu Nome Tem "{}" Letras'.format(len(nome) - nome.count(' ')))
print(f'Seu Primeiro Nome é "{separa[0]}" e Tem "{nome.find(" ")}"')

os.system('pause')
