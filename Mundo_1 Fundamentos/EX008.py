"""
EXERCÍCIO 008: Conversor de Medidas

Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""
import os
print('='*44)
print('={:10} CONVERSOR DE MEDIDAS {:10}='.format('', ''))
print('='*44)
n1 = float(input('\nQuantos Metros Quer converter? '))
cm = n1 * 100
mm = n1 * 1000
km = n1 / 1000
print(f'{n1} metros Tem  {cm:.0f} cm\n{n1} metros Tem {mm:.0f} mm\n{n1} metros tem {km:.2f} Km')
os.system('pause')
