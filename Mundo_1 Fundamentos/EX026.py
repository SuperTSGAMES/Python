"""
EXERCÍCIO 026: Primeira e Última Ocorrência de uma String

Faça um programa que leia uma frase pelo teclado e mostre:

> Quantas vezes aparece a letra "A".
> Em que posição ela aparece a primeira vez.
> Em que posição ela aparece a última vez.
"""
import os


print('='*43)
print('={:7}Primeira e Última Ocorrência{:6}='.format((''),('')))
print('='*43)
frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece "{frase.count("A")}" vezes na frase.')
print(f'A primeira letra A apareceu na posição "{frase.find("A") + 1}".')
print(f'A última letra A apareceu na posição {frase.rfind("A") + 1}.')
os.system('pause')
