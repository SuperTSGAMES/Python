"""
EXERCÍCIO 035: Analisando Triângulo v1.0

Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
"""
import os
print('='*42)
print('={:10}Analisando Triangulo{:10}='.format((''),('')))
print('='*42)

r1 = float(input('Digite o Comprimento da 1º RETA: '))
r2 = float(input('Digite o Comprimento da 2º RETA: '))
r3 = float(input('Digite o Comprimento da 3º RETA: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print('Os segmentos acima PODEM FORMAR triângulo!')
else:
  print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
os.system('pause')
