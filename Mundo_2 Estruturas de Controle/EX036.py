"""
EXERCÍCIO 036: Aprovando Empréstimo

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário, ou então o empréstimo será negado.
"""
import os
import random
import time
print('=' * 43)
print('={:9}Aprovaçao de Emprestimo{:9}='.format((''), ('')))
print('=' * 43)

valorcasa = float(input('Qual Valor da Casa A ser Comprada: R$ '))
salario = float(input('Qual seu Salario? R$ '))
anos = int(input('Quantos anos quer Pagar? '))
prestacao = valorcasa / (anos * 12)
minimo = salario * 30 / 100
os.system('cls') or None
print(f'Para pagar uma casa de R$ {valorcasa:.2f} em {anos} anos,')
print(f'A prestação será de R$ {prestacao:.2f}')
if prestacao <= minimo:
    print('\033[32mEmpréstimo pode ser CONCEDIDO!\033[m')
else:
    print('\033[31mEmpréstimo NEGADO!\033[m')
#
os.system('pause')
