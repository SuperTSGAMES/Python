"""
EXERCÍCIO 034: Aumentos Múltiplos

Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para inferiores ou iguais, o aumento é de 15%.
"""
import os
print('='*42)
print('={:11}Aumentos Múltiplos{:11}='.format((''),('')))
print('='*42)

salario = float(input('Qual o Salário do Funcionário? R$'))
#aumento = float(input('Quantos "%" Deseja dar de Aumento? '))

if salario >= 1250.00:
    novosalario = salario + (salario * 10 / 100)
    print(f'O Salario do Funcionario Que era {salario:.2f}R$\nPassa a ser {novosalario:.2f} R$ com "10%" De Aumento' )
else:
    novosalario = salario + (salario * 15 / 100)
    print(f'O Salario do Funcionario Que era {salario:.2f}R$\nPassa a ser {novosalario:.2f} R$ com "15%" De Aumento')
os.system('pause')
