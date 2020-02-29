"""
EXERCÍCIO 012: Calculando Descontos

Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com "5%" de desconto.
"""
import os
print('='*43)
print('={:8} Calculo de "%" Desconto {:8}='.format((''),('')))
print('='*43)
val = float(input('Qual valor do Produto? '))
por = float(input('Qual a Porcentagem de Desconto? '))
des = val - (val * por / 100)
print(f'O preço de produto é R$ {val:.2f} com "{por}%" de desconto fica R$ {des:.2f}')
os.system('pause')
