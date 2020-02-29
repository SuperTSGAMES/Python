"""
EXERCÍCIO 031: Custo da Viagem

Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.
"""

import os
print('='*43)
print('={:13}Custo de Viagem{:13}='.format((''),('')))
print('='*43)
dist = float(input('Qual é a distância da sua viagem? Km '))
if dist <= 200:
    preco = dist * 0.50
    print(f'Você está prestes a fazer uma viagem de {dist:.1f} Km, Voçê Vai Pagar R$ {preco:.2f} Na Passagem')
else:
    preco = dist * 0.45
    print(f'Você está prestes a fazer uma viagem de {dist:.1f} Km, Voçê Vai Pagar R$ {preco:.2f} Na Passagem')
print('TENHA UMA BOA VIAGEM!')
os.system('pause')
