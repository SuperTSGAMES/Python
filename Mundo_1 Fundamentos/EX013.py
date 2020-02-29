"""
EXERCÍCIO 013: Reajuste Salarial

Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
import os
print('='*43)
print('={:6} Calculo "%" Aumento Salario {:6}='.format((''),('')))
print('='*43)
sal = float(input('Valor Salario Atual? R$ '))
porcento = float(input('Quantos "%" de Aumento? '))
novo = sal + (sal * porcento / 100)
print(f'Seu Novo Salario com "{porcento}%" de Aumento é {novo:.2f} R$ ')
os.system('pause')
