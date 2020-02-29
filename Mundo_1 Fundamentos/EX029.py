"""
EXERCÍCIO 029: Radar Eletrônico

Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma
mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.
"""
import os
print('='*43)
print('={:12}Radar Eletrônico{:13}='.format((''),('')))
print('='*43)
vel = float(input('Qual Velocidade do Carro? KM/h '))
if vel <= 80:
    print(f'Parabéns! Sua Velocidade foi de {vel:.0f}KM/h\nVoce Dirige Dentro Dos Limites de Velocidade Da Rodovia')
else:
    multa = (vel - 80) * 7
    print(f'Voçê Foi MULTADO Você deve pagar um multa de R$ {multa:.2f}!')
print('Tenha um bom dia! Dirija com segurança!')

os.system('pause')
