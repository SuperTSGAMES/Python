"""
EXERCÍCIO 015: Conversor de Temperaturas

Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.
"""
import os
print('='*43)
print('={:8} Conversor De Temperatura {:7}='.format((''),('')))
print('='*43)

celsius = float(input('Informe A Temperatura em ºC: '))
far = celsius * 1.8 + 32
print(f'A temperatura de {celsius:.1f}ºC Corresponde a {far:.1f}ºF')

os.system('pause')
