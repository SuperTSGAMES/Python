"""
EXERCÍCIO 011: Pintando Parede

Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2 m².
"""
import os
print('='*43)
print('={:12} Calculo de Area {:12}='.format((''),('')))
print('='*43)
larg = float(input('Qual Largura da parede? '))
alt = float(input('Qual altura da parede? '))
area = larg * alt
l = area / 2
print(f'A Area Total a ser Pintada Mede {area:.2f}m², sera Nescessario {l:.2f} litros de tinta')
os.system('pause')
