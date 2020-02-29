"""
DESAFIO 042: Analisando Triângulos v2.0

Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""
import os
import random
import time
print('='*44)
print('={:8}Analisando Triângulos v2.0{:8}='.format((''),('')))
print('='*44)
r1 = float(input('Digite o Comprimento da 1º RETA: '))
r2 = float(input('Digite o Comprimento da 2º RETA: '))
r3 = float(input('Digite o Comprimento da 3º RETA: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 == r3:
        print('Os segmentos acima podem formar um triângulo EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('Os segmentos acima podem formar um triângulo ISÓSCELES!')
    else:
        print('Os segmentos acima podem formar um triângulo ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
os.system('pause')
