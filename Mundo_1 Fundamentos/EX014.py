"""
EXERCÍCIO 014: Calculando Descontos e juros

Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com "5%" de desconto.
"""
import os
print('='*43)
print('={:6} Calculo "%" Desconto A Vista {:5}='.format((''),('')))
print('={:5} Calculo "%" Aumento Parcelado {:5}='.format((''),('')))
print('='*43)

prod = float(input('Qual Valor do Produto? R$ '))
des = float(input('Valor do Desconto "%" ? '))
aumento = float(input('Valor dos Juros "%" Para Parcelado ? '))
parcela = int(input('Em Quantas Parcela Deseja Fazer? '))
totaldes = prod - (prod * des / 100)
totalaumento = prod + (prod * aumento / 100)
valparcela = totalaumento / parcela

print(f'O Valor do Produto é R$ {prod:.2f} Com "{des:.0f}%" de Desconto Fica R$ {totaldes:.2f}')
print(f'O Produto Tem "{aumento:.0f}%" de Juros se Parcelado, e O valor Total Fica R${totalaumento:.2f} ')
print(f'O Produto Sera Parcelado em {parcela}x O valor das Parcelas Ficara R$ {valparcela:.2f} ')

os.system('pause')
