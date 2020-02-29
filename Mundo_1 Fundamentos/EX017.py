"""
EXERCÍCIO 017: Catetos e Hipotenusa

Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
"""
import os
import math

print('='*43)
print('={:10} Calcular HIPOTENUSA {:10}='.format((''),('')))
print('='*43)

ctop = float(input('Qual a Medida do Cateto Oposto? '))
ctadj = float(input("Qual a Medida do Cateto Adjacente? "))
hip = math.hypot(ctop, ctadj)
print(f'O Comprimento da HIPOTENUSA é: {hip:.2f}')
os.system('pause')
