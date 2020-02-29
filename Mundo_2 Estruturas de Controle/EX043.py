"""
EXERCÍCIO 043: Índice de Massa Corporal

Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""

import os
import time
print('=' * 43)
print('={:15}Calculo IMC{:15}='.format((''), ('')))
print('=' * 43)
peso = float(input('Qual Seu Peso? kg '))
altura = float(input('Qual sua Altura? (m) '))
imc = peso / (altura * altura)
if imc < 18.5:
    print(f'Seu IMC é de {imc:.1f} Voçê esta ABAIXO DO PESO!')
elif imc >= 18.5 and imc < 25:
    print(f'Seu IMC é de {imc:.1f} Voçê esta com PESO IDEAL!')
elif imc >= 25 and imc < 30:
    print(f'Seu IMC é de {imc:.1f} Voçê esta com SOBREPESO!')
elif imc >=30 and imc < 40:
    print(f'Seu IMC é de {imc:.1f} Voçê esta OBESO!')
else:
    print(f'Seu IMC é de {imc:.1f} Voçê esta com OBESIDADE MORBIDA!')
#os.system('pause')
