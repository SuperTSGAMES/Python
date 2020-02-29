"""
EXERCÍCIO 033: Maior e Menor Valores

Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""
import os
print('='*43)
print('={:11}MAIOR E MENOR VALOR{:11}='.format((''),('')))
print('='*43)

n1 = int(input('Digite um Numero: '))
n2 = int(input('Digite outro Numero: '))
n3 = int(input('Digite mais Numero: '))
#funçao calcular menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O menor valor digitado foi: {menor}')
print(f'O maior valor digitado foi: {maior}')
os.system('pause')
