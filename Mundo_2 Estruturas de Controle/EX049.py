"""
EXERCÍCIO 049: Tabuada v2.0

Refaça o EXERCÍCIO 009, mostrando a tabuada de um número que
o usuário escolher, só que agora utilizando um laço for.
"""
import os
print('=' * 43)
print('={:15}Tabuada v2.0{:14}='.format('', ''))
print('=' * 43)
num = int(input('Digite um Numero: '))
for c in range(0, 11):
    res = num * c
    print(f'{num} X {c:2} = {res}')
#os.system('cls') or None
