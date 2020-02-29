"""
EXERCÍCIO 018: Seno, Cosseno e Tangente

Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""
import os
import math

print('='*43)
print('={:8} Calculo SEN, COS e TANG {:8}='.format((''),('')))
print('='*43)

ang = float(input('Digite o Valor Do Angulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print(f'O Seno de {ang} é: {sen:.2f}\nO Cosseno de {ang} é: {cos:.2f}\nA Tangente de {ang} é: {tang:.2f}')

os.system('pause')
